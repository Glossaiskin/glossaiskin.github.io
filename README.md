# glossaiskin.github.io

Website for Gloss, the AI skin analysis app for iPhone. Static HTML on GitHub Pages.

## Layout

- `index.html` homepage
- `tools/` one folder per free tool page, each targeting one search query
- `tools/index.html` list of all tools
- `support.html`, `privacy-policy.html`, `terms.html` App Store required pages
- `assets/gloss.css` shared styles, `assets/site.js` shared header and footer, `assets/logo.svg`
- `scripts/build_tools.py` generates the tool pages, `tools/index.html` and `sitemap.xml`
- `scripts/pages/*.py` one file per tool page: metadata, tool HTML, tool JS, article, FAQs
- `seo/keywords.md` the query each page targets and the paste list for Keyword Planner
- `seo/launch-checklist.md` what to do after merging

## Adding a tool page

1. Copy any file in `scripts/pages/`, give it the next number, and edit `PAGE`.
2. `python3 scripts/build_tools.py`
3. Open the new page locally (`python3 -m http.server`) and click through the tool.
4. Add a card for it in `index.html` under "Free skin tools" if you want it on the homepage.
5. Commit the generated `tools/<slug>/index.html` along with the source.
