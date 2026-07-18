(() => {
  const BANNER_TEXT =
    "For best results, open these notes in light mode in Google Chrome.";
  const BANNER_ID = "lightmode-banner";
  const VISITED_KEY = "lightmode-banner-visited";
  const DISMISSED_KEY = "lightmode-banner-dismissed";

  const storageAvailable = () => {
    try {
      const testKey = "__banner_test__";
      window.localStorage.setItem(testKey, "1");
      window.localStorage.removeItem(testKey);
      return true;
    } catch (error) {
      return false;
    }
  };

  const readStorage = (key) => {
    try {
      return window.localStorage.getItem(key);
    } catch (error) {
      return null;
    }
  };

  const writeStorage = (key, value) => {
    try {
      window.localStorage.setItem(key, value);
    } catch (error) {
      return;
    }
  };

  const dismissBanner = (banner) => {
    banner.remove();
    document.body.classList.remove("lightmode-banner-active");
  };

  const showBanner = () => {
    if (document.getElementById(BANNER_ID)) return;

    const banner = document.createElement("div");
    banner.id = BANNER_ID;
    banner.className = "lightmode-banner";
    banner.textContent = BANNER_TEXT;

    const shouldShowClose = readStorage(VISITED_KEY) === "true";
    if (shouldShowClose) {
      const closeButton = document.createElement("button");
      closeButton.type = "button";
      closeButton.className = "lightmode-banner__close";
      closeButton.setAttribute("aria-label", "Dismiss banner");
      closeButton.textContent = "x";
      closeButton.addEventListener("click", () => {
        writeStorage(DISMISSED_KEY, "true");
        dismissBanner(banner);
      });
      banner.appendChild(closeButton);
    }

    document.body.classList.add("lightmode-banner-active");
    document.body.prepend(banner);
    writeStorage(VISITED_KEY, "true");
  };

  const init = () => {
    if (!document.body) return;
    if (!storageAvailable()) {
      showBanner();
      return;
    }

    if (readStorage(DISMISSED_KEY) === "true") return;
    showBanner();
  };

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
