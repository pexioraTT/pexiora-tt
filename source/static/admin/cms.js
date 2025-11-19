// Prévisualisation personnalisée DecapCMS
CMS.registerPreviewTemplate("pages", PagePreview);

// Ajout des styles Bulma et custom pour la prévisualisation
CMS.registerPreviewStyle(
  "https://cdn.jsdelivr.net/npm/bulma@1.0.4/css/bulma.min.css"
);
CMS.registerPreviewStyle("/style.css");

function PagePreview(props) {
  const title = props.entry.getIn(["data", "title"]);
  const description = props.entry.getIn(["data", "description"]);
  const body = props.entry.getIn(["data", "body"]);

  return `
        <div style="max-width: 800px; margin: 0 auto; padding: 20px; font-family: system-ui;">
            <header style="margin-bottom: 2rem;">
                <h1 style="color: #2563eb; margin-bottom: 0.5rem;">${title}</h1>
                ${description ? `<p style="color: #6b7280; font-size: 1.1rem;">${description}</p>` : ""}
            </header>
            <div style="line-height: 1.6;">
                ${body ? marked.parse(body) : ""}
            </div>
        </div>
    `;
}
