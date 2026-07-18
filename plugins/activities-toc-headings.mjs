const ACTIVITY_TITLE_RE = /^activity\s+\d+/i;
const HEADING_CLASS = "activity-toc-heading";

const extractText = (node) => {
  if (!node) return "";
  if (typeof node.value === "string") return node.value;
  if (!Array.isArray(node.children)) return "";
  return node.children.map(extractText).join("");
};

const normalizeText = (text) => text.replace(/\s+/g, " ").trim();

const slugify = (text) =>
  text
    .toLowerCase()
    .replace(/[^a-z0-9]+/g, "-")
    .replace(/(^-|-$)/g, "");

const collectIdentifiers = (node, set) => {
  if (!node) return;
  if (typeof node.identifier === "string" && node.identifier) {
    set.add(node.identifier);
  }
  if (typeof node.html_id === "string" && node.html_id) {
    set.add(node.html_id);
  }
  if (Array.isArray(node.children)) {
    node.children.forEach((child) => collectIdentifiers(child, set));
  }
};

const ensureUniqueId = (base, used) => {
  let candidate = base;
  let i = 2;
  while (used.has(candidate)) {
    candidate = `${base}-${i}`;
    i += 1;
  }
  used.add(candidate);
  return candidate;
};

const hasActivityHeadingMarker = (node) =>
  node?.type === "heading" &&
  (node?.data?.activityTocHeading ||
    (Array.isArray(node?.data?.hProperties?.className) &&
      node.data.hProperties.className.includes(HEADING_CLASS)));

const isActivityAdmonition = (node) => {
  if (!node || node.type !== "admonition") return false;
  if (node.kind !== "tip") return false;
  const titleNode = node.children?.find((child) => child.type === "admonitionTitle");
  if (!titleNode) return false;
  const titleText = normalizeText(extractText(titleNode));
  return ACTIVITY_TITLE_RE.test(titleText);
};

const getActivityTitle = (node) => {
  const titleNode = node.children?.find((child) => child.type === "admonitionTitle");
  const titleText = normalizeText(extractText(titleNode));
  return titleText;
};

const makeHeading = (titleText, identifier) => ({
  type: "heading",
  depth: 3,
  children: [{ type: "text", value: titleText }],
  identifier,
  label: titleText,
  html_id: identifier,
  enumerated: false,
  data: {
    activityTocHeading: true,
    hProperties: {
      className: [HEADING_CLASS],
      "aria-hidden": "true",
    },
  },
});

const insertActivityHeadings = (node, usedIdentifiers, inAdmonition = false) => {
  if (!node || !Array.isArray(node.children)) return;
  for (let i = 0; i < node.children.length; i += 1) {
    const child = node.children[i];
    const childInAdmonition = inAdmonition || child?.type === "admonition";

    if (!inAdmonition && isActivityAdmonition(child)) {
      const previous = node.children[i - 1];
      if (!hasActivityHeadingMarker(previous)) {
        const titleText = getActivityTitle(child);
        const base = slugify(titleText) || "activity";
        const id = ensureUniqueId(base.startsWith("activity") ? base : `activity-${base}`, usedIdentifiers);
        node.children.splice(i, 0, makeHeading(titleText, id));
        i += 1;
      }
    }

    insertActivityHeadings(child, usedIdentifiers, childInAdmonition);
  }
};

const plugin = () => (mdast) => {
  const usedIdentifiers = new Set();
  collectIdentifiers(mdast, usedIdentifiers);
  insertActivityHeadings(mdast, usedIdentifiers, false);
};

export default {
  name: "activities-toc-headings",
  transforms: [
    {
      name: "activities-toc-headings",
      stage: "document",
      plugin,
    },
  ],
};
