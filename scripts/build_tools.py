#!/usr/bin/env python3
"""Builds every page in scripts/pages/*.py into tools/<slug>/index.html,
plus tools/index.html and sitemap.xml.

Add a page: copy an existing file in scripts/pages/, change PAGE, run
    python3 scripts/build_tools.py
"""
import glob, html, importlib.util, json, os, datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = "https://glossaiskin.github.io"
APP = "https://apps.apple.com/us/app/gloss-ai-skin-analysis/id6792349354"

def load_pages():
    pages = []
    for path in sorted(glob.glob(os.path.join(ROOT, "scripts", "pages", "*.py"))):
        spec = importlib.util.spec_from_file_location(os.path.basename(path)[:-3], path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        pages.append(mod.PAGE)
    pages.sort(key=lambda p: p.get("order", 99))
    return pages

def faq_jsonld(faqs):
    return json.dumps({
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [{"@type": "Question", "name": q,
                        "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faqs],
    }, ensure_ascii=False, indent=1)

def app_jsonld(p):
    return json.dumps({
        "@context": "https://schema.org",
        "@type": "WebApplication",
        "name": p["h1"],
        "url": f"{SITE}/tools/{p['slug']}/",
        "applicationCategory": "UtilitiesApplication",
        "operatingSystem": "Any",
        "browserRequirements": "Requires JavaScript",
        "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"},
        "publisher": {"@type": "Organization", "name": "Gloss", "url": SITE},
    }, ensure_ascii=False, indent=1)

def cta(p):
    c = p.get("cta", {})
    return f"""
  <div class="cta">
    <div>
      <h2>{c.get('title', 'Get the real number from your actual skin')}</h2>
      <p>{c.get('body', 'Gloss scans your skin from a selfie and scores hydration, clarity, texture and radiance out of 100, then builds a routine around what it sees. Free on iPhone.')}</p>
      <p class="fine">Cosmetic tracking only, not medical advice. Your scan photo is analyzed and discarded, never stored.</p>
    </div>
    <a class="btn" href="{APP}" rel="noopener">Download Gloss</a>
  </div>"""

def related(p, pages):
    others = [o for o in pages if o["slug"] != p["slug"]][:4]
    cards = "".join(
        f'<a class="card" href="../{o["slug"]}/"><span class="kind">{html.escape(o["kind"])}</span>'
        f'<h3>{html.escape(o["card_title"])}</h3><p>{html.escape(o["card_blurb"])}</p></a>' for o in others)
    return f'<h2>More free skin tools</h2><div class="grid">{cards}</div>'

def render(p, pages):
    faqs_html = "".join(f"<details><summary>{html.escape(q)}</summary><p>{a}</p></details>" for q, a in p["faqs"])
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>{html.escape(p['title'])}</title>
  <meta name="description" content="{html.escape(p['description'])}" />
  <link rel="canonical" href="{SITE}/tools/{p['slug']}/" />
  <link rel="icon" href="../../assets/logo.svg" type="image/svg+xml" />
  <link rel="stylesheet" href="../../assets/gloss.css" />
  <meta property="og:type" content="website" />
  <meta property="og:title" content="{html.escape(p['h1'])}" />
  <meta property="og:description" content="{html.escape(p['description'])}" />
  <meta property="og:url" content="{SITE}/tools/{p['slug']}/" />
  <meta property="og:image" content="{SITE}/assets/logo.svg" />
  <meta name="apple-itunes-app" content="app-id=6792349354" />
  <script type="application/ld+json">{faq_jsonld(p['faqs'])}</script>
  <script type="application/ld+json">{app_jsonld(p)}</script>
</head>
<body data-root="../../">
<main class="wrap">
  <div class="breadcrumb"><a href="../../">Gloss</a> › <a href="../">Free tools</a> › {html.escape(p['card_title'])}</div>
  <h1>{p['h1']}</h1>
  <p class="intro">{p['intro']}</p>

  <div class="tool" id="tool">
{p['tool_html']}
  </div>

  <p class="small">This tool runs entirely in your browser. Nothing you enter is sent anywhere.</p>
{cta(p)}
{p['article_html']}

  <h2>Common questions</h2>
  <div class="faq">{faqs_html}</div>

  <p class="notice">Gloss and the tools on this site are for cosmetic and general information only. They do not diagnose or treat any condition. If something on your skin is new, changing, painful or worrying, see a dermatologist or doctor.</p>

  {related(p, pages)}
</main>
<script src="../../assets/site.js"></script>
<script>
{p['tool_js']}
</script>
</body>
</html>
"""

def render_index(pages):
    cards = "".join(
        f'<a class="card" href="./{o["slug"]}/"><span class="kind">{html.escape(o["kind"])}</span>'
        f'<h3>{html.escape(o["card_title"])}</h3><p>{html.escape(o["card_blurb"])}</p></a>' for o in pages)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Free skin tools: skin type quiz, routine builder, sunscreen calculator and more | Gloss</title>
  <meta name="description" content="Free browser tools from Gloss: find your skin type, put your routine in the right order, check if two ingredients mix, work out how much sunscreen you need, and more." />
  <link rel="canonical" href="{SITE}/tools/" />
  <link rel="icon" href="../assets/logo.svg" type="image/svg+xml" />
  <link rel="stylesheet" href="../assets/gloss.css" />
  <meta property="og:title" content="Free skin tools from Gloss" />
  <meta property="og:description" content="Quizzes, calculators and checkers for the skincare questions people ask most." />
  <meta property="og:url" content="{SITE}/tools/" />
  <meta name="apple-itunes-app" content="app-id=6792349354" />
</head>
<body data-root="../">
<main class="wrap wide">
  <div class="breadcrumb"><a href="../">Gloss</a> › Free tools</div>
  <h1>Free skin tools</h1>
  <p class="intro">Each of these answers one question people type into Google. They run in your browser, nothing is uploaded, and no sign-up is needed. When you want a real read on your own skin instead of a self-estimate, the Gloss app does that from a selfie.</p>
  <div class="grid">{cards}</div>
  <div class="cta">
    <div>
      <h2>Ready for the real scan?</h2>
      <p>Gloss scores hydration, clarity, texture and radiance from a selfie and tracks them over time. Free on iPhone.</p>
    </div>
    <a class="btn" href="{APP}" rel="noopener">Download Gloss</a>
  </div>
</main>
<script src="../assets/site.js"></script>
</body>
</html>
"""

def render_sitemap(pages):
    today = datetime.date.today().isoformat()
    urls = [f"{SITE}/", f"{SITE}/tools/", f"{SITE}/support.html", f"{SITE}/privacy-policy.html", f"{SITE}/terms.html"]
    urls += [f"{SITE}/tools/{p['slug']}/" for p in pages]
    body = "".join(f"  <url><loc>{u}</loc><lastmod>{today}</lastmod></url>\n" for u in urls)
    return f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{body}</urlset>\n'

def main():
    pages = load_pages()
    for p in pages:
        out_dir = os.path.join(ROOT, "tools", p["slug"])
        os.makedirs(out_dir, exist_ok=True)
        with open(os.path.join(out_dir, "index.html"), "w") as f:
            f.write(render(p, pages))
        print("built", p["slug"])
    with open(os.path.join(ROOT, "tools", "index.html"), "w") as f:
        f.write(render_index(pages))
    with open(os.path.join(ROOT, "sitemap.xml"), "w") as f:
        f.write(render_sitemap(pages))
    print("built tools/index.html and sitemap.xml")

if __name__ == "__main__":
    main()
