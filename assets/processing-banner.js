(() => {
  const BANNER_TEXT =
    "Note: This section is under active development and may be revised as the course evolves.";
  const BANNER_ID = "processing-banner";

  const showBanner = () => {
    if (document.getElementById(BANNER_ID)) return;
    const banner = document.createElement("div");
    banner.id = BANNER_ID;
    banner.className = "processing-banner";
    banner.textContent = BANNER_TEXT;
    document.body.classList.add("processing-banner-active");
    document.body.prepend(banner);
  };

  const getSlugFromPath = () => {
    const path = window.location.pathname || "";
    const trimmed = path.replace(/^\/+|\/+$/g, "");
    if (!trimmed) return "index";
    return trimmed.replace(/\//g, ".");
  };

  const fetchJSON = async (url) => {
    try {
      const response = await fetch(url);
      if (!response.ok) return null;
      return await response.json();
    } catch (error) {
      return null;
    }
  };

  const getIpynbUrl = (data) => {
    const exports = data && data.frontmatter && data.frontmatter.exports;
    if (!Array.isArray(exports)) return null;
    const ipynbExport = exports.find((e) => e && e.format === "ipynb" && e.url);
    return ipynbExport ? ipynbExport.url : null;
  };

  const parseProcessingFromNotebook = (notebook) => {
    const cell = notebook && notebook.cells && notebook.cells[0];
    if (!cell || cell.cell_type !== "markdown") return false;
    const source = Array.isArray(cell.source)
      ? cell.source.join("")
      : cell.source || "";
    const match = source.match(/^---\s*\n([\s\S]*?)\n---/);
    if (!match) return false;
    return /(^|\n)\s*processing\s*:\s*true\s*(\n|$)/.test(match[1]);
  };

  const init = async () => {
    if (!document.body) return;

    const slug = getSlugFromPath();
    if (slug === "index") return;

    // Fetch MyST's content JSON to get the ipynb export URL
    const contentUrl = `/${slug}.json`;
    const data = await fetchJSON(contentUrl);
    if (!data) return;

    // Get the notebook URL from exports
    const ipynbUrl = getIpynbUrl(data);
    if (!ipynbUrl) return;

    // Fetch the notebook and parse frontmatter for processing flag
    const notebook = await fetchJSON(ipynbUrl);
    if (notebook && parseProcessingFromNotebook(notebook)) {
      showBanner();
    }
  };

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
