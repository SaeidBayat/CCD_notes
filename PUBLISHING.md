# Publishing the course notes

This project builds and publishes automatically with GitHub Actions and GitHub Pages. The workflow builds the HTML site and includes the committed `exports/notes.pdf`; it does not regenerate the PDF in GitHub Actions.

## First publication

1. Authenticate GitHub CLI and create the repository:

   ```bash
   gh auth login -h github.com
   gh repo create control-co-design-notes --public --source=. --remote=origin --push
   ```

2. On GitHub, open **Settings → Pages**. Under **Build and deployment**, select **GitHub Actions** as the source if it is not already selected.
3. Open the **Actions** tab and wait for “Deploy MyST course to GitHub Pages” to finish.

The site will normally appear at:

```text
https://YOUR-USERNAME.github.io/control-co-design-notes/
```

## Publishing later changes

```bash
git add .
git commit -m "Update course notes"
git push
```

Each push to `main` rebuilds and republishes the website.

## Local preview

```bash
npm ci
npx myst start
```

The generated `_build/` directory is intentionally excluded from Git because GitHub Actions rebuilds it.

## Custom domain

Configure a custom domain in **GitHub → Settings → Pages** only after the standard GitHub Pages URL works. Then add the domain GitHub specifies to the repository; do not reuse the former `notes.eecs245.org` setting.
