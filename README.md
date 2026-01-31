# Personal Website (Jekyll + GitHub Pages)

## Getting started

1) Install dependencies:

```bash
bundle install
```

Recommended Ruby version: `3.3.4` (see `.ruby-version`).

2) Run locally:

```bash
bundle exec jekyll serve --baseurl=""
```

3) Build locally:

```bash
bundle exec jekyll build
```

## Content overview

- Home page: `index.md`.
- Blog index: `blog/index.md`.
- Blog posts: `_posts/*.md` (date in filename).
- Portfolio: `portfolio.md`.
- CV/publications: `cv.md` and `publications.md`, backed by `_data/cv.yml` and `_data/publications.yml`.
- Assets: `assets/` (images, CSS, etc).
- Favicon: `assets/favicon.svg` plus root `favicon.ico` fallback for browsers that request `/favicon.ico`.

## CV and publications

- Edit CV data in `_data/cv.yml`.
- Edit publications data in `_data/publications.yml`.
- The pages `cv.md` and `publications.md` render directly from those YAML files (Markdown fields use `*_md` keys).

## Regenerating TeX/PDFs locally

Render TeX from YAML:

```bash
python3 scripts/render_tex.py
```

Build PDFs (requires `latexmk`):

```bash
scripts/build_pdf.sh
```

This also runs the above Python script under the hood.

Note that GitHub Pages will not run TeX during the build, so `.github/workflows/build-pdfs.yml` handles PDF generation for deployment.

## GitHub Pages constraints

GitHub Pages builds with a restricted set of supported plugins. This site uses the `github-pages` gem (which includes `jekyll-feed` and `jekyll-seo-tag`) to stay compatible. Avoid adding unsupported plugins or custom build steps to the default Pages build.

If you update dependencies, keep `github-pages` aligned with the GitHub Pages build environment (the lockfile currently pins `github-pages` 232 / Jekyll 3.10.0).

## Blog feed

The RSS/Atom feed is provided by `jekyll-feed` and available at `/feed.xml` once the site is built.

## License

Code (templates, styles, scripts, and configuration) is licensed under the MIT License in `LICENSE`.
Reserved personal content (CV, portfolio, and related data/assets) is all rights reserved per
`LICENSE-CONTENT`. Blog posts and associated blog assets are licensed under CC BY-SA 4.0 per
`LICENSE-CONTENT`. Third-party materials remain under their original licenses and attribution terms.
