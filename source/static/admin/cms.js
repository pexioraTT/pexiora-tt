if (window.CMS) {
  const h = window.h || (window.React && window.React.createElement);

  // Ajout des styles Bulma et custom pour la prévisualisation
  CMS.registerPreviewStyle(
    "https://cdn.jsdelivr.net/npm/bulma@1.0.4/css/bulma.min.css"
  );
  CMS.registerPreviewStyle("/style.css");

  // Preview type "page" (pages et actualités)
  const renderPageLikePreview = ({ entry, widgetFor }) => {
    if (!h) return null;
    const data = entry.get("data");
    const title = data && data.get("title");
    const description = data && data.get("description");
    const extraImage = data && data.getIn(["extra", "image"]);
    const extraImageDescription =
      data && data.getIn(["extra", "image_description"]);

    return h(
      "div",
      {
        className: "box",
        style: { maxWidth: "800px", margin: "0 auto", padding: "2rem" },
      },
      h(
        "header",
        { className: "mb-5" },
        title
          ? h(
              "h1",
              {
                className: "title is-2",
                style: { color: "var(--color-primary)" },
              },
              title
            )
          : null,
        description
          ? h(
              "p",
              {
                className: "subtitle is-5",
                style: { color: "var(--color-accent-light)" },
              },
              description
            )
          : null
      ),
      h(
        "div",
        { className: "content", style: { lineHeight: "1.6" } },
        extraImage
          ? h("img", {
              alt: extraImageDescription || "",
              src: extraImage.startsWith("/") ? extraImage : `/${extraImage}`,
              style: { maxWidth: "100%", marginBottom: "1rem" },
            })
          : null,
        widgetFor("body")
      )
    );
  };

  CMS.registerPreviewTemplate("pages", renderPageLikePreview);
  CMS.registerPreviewTemplate("actualites", renderPageLikePreview);

  // Preview spécifique pour sponsors
  CMS.registerPreviewTemplate("sponsors", ({ entry, widgetFor }) => {
    const data = entry.get("data");
    const title = data && data.get("title");
    const description = data && data.get("description");
    const extra = data && data.get("extra");
    const logo = extra && extra.get("image");
    const site = extra && extra.get("site");

    return h(
      "div",
      {
        className: "box",
        style: {
          maxWidth: "600px",
          margin: "0 auto",
          padding: "2rem",
          textAlign: "center",
        },
      },
      logo
        ? h("img", {
            src: logo && logo.startsWith("/") ? logo : `/${logo}`,
            alt: `Logo ${title || ""}`.trim(),
            style: {
              maxWidth: "160px",
              marginBottom: "1rem",
              borderRadius: "1rem",
              boxShadow: "0 2px 8px var(--color-primary-dark)",
            },
          })
        : null,
      title
        ? h(
            "h2",
            {
              className: "title is-3",
              style: { color: "var(--color-primary)" },
            },
            title
          )
        : null,
      site
        ? h(
            "p",
            {},
            h(
              "a",
              {
                href: site,
                target: "_blank",
                className: "button is-link is-light",
                style: { marginBottom: "1rem" },
              },
              "Site web"
            )
          )
        : null,
      description
        ? h(
            "p",
            {
              className: "subtitle is-6",
              style: { color: "var(--color-accent-light)" },
            },
            description
          )
        : null,
      h(
        "div",
        {
          className: "content",
          style: { lineHeight: "1.6", marginTop: "1rem" },
        },
        widgetFor("body")
      )
    );
  });
}
