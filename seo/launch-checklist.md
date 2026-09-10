# Launch checklist

Things only you can do, in order.

1. **Merge the PR.** GitHub Pages serves from `main`, so the pages go live a minute or two after merge at https://glossaiskin.github.io/tools/.

2. **Update the App Store privacy policy URL.** The homepage used to be a copy of the privacy policy. It is now a real homepage. If App Store Connect points the Privacy Policy URL at `https://glossaiskin.github.io/`, change it to `https://glossaiskin.github.io/privacy-policy.html`. Same check for the Support URL, which should be `https://glossaiskin.github.io/support.html`. Do this before the next app submission.

3. **Google Search Console.** search.google.com/search-console, add property `https://glossaiskin.github.io/`, verify with the HTML tag method, and paste the tag into the `<head>` of `index.html`. Then Sitemaps, submit `sitemap.xml`. This is where the ranking numbers for the follow-up reel come from (Performance, filter by page).

4. **Keyword Planner.** Paste `seo/keywords.md` list in and note the volumes next to each page. Anything with volume that is not covered gets a page.

5. **Request indexing** for each of the 9 tool URLs in Search Console's URL inspection. It speeds up the first crawl from weeks to days.

6. **Analytics (optional).** The site has none. If you want to see clicks through to the App Store, add a lightweight tracker to `assets/site.js` and fire an event on `[data-app-link]` and `.cta .btn` clicks. Update the privacy policy's GitHub row if you add one.

7. **Retake the App Store screenshots link.** Every CTA on the site points to https://apps.apple.com/us/app/gloss-ai-skin-analysis/id6792349354. If you add an App Store campaign token later, change the `APP` constant in `assets/site.js` and `scripts/build_tools.py` and rebuild.
