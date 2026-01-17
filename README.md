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

## GitHub Pages constraints

GitHub Pages builds with a restricted set of supported plugins. This site uses the `github-pages` gem (which includes `jekyll-feed`) to stay compatible. Avoid adding unsupported plugins or custom build steps to the default Pages build.

If you update dependencies, keep `github-pages` aligned with the GitHub Pages build environment (the lockfile currently pins `github-pages` 232 / Jekyll 3.10.0).

## Blog feed

The RSS/Atom feed is provided by `jekyll-feed` and available at `/feed.xml` once the site is built.

## Future: TeX to PDF workflow

GitHub Pages cannot run TeX during its build. Two viable options:

- Option A: build PDFs locally and commit the generated files to the repository.
- Option B (recommended): use a GitHub Actions workflow to compile TeX and deploy Pages artifacts.

Replace placeholder content in `index.md`, `_config.yml`, and the `_data/` files.
