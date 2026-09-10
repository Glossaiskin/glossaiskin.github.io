# Gloss keyword targets

Each page below targets one search intent. The "Primary" query is the one the
page title and H1 are written for. "Also ranks for" lists the phrasings the page
answers in its body and FAQ so it can pick them up as well.

I could not run these through Google Keyword Planner from this environment
(it needs a signed-in Google Ads account). The paste list at the bottom is
ready for it. Steps:

1. ads.google.com, Tools, Planning, Keyword Planner, "Discover new keywords".
2. Paste the list, set location to your target countries (US first), language English.
3. Sort by "Avg. monthly searches". Keep the low-competition ones.
4. Any query with volume that no page below covers gets its own page.
   Copy a file in `scripts/pages/`, change the content, run `python3 scripts/build_tools.py`.

## Live pages

| Page | Primary query | Also ranks for |
|---|---|---|
| /tools/skin-type-quiz/ | what is my skin type quiz | skin type quiz, how to know my skin type, skin type test, what skin type do I have, combination skin quiz |
| /tools/rate-my-skin/ | rate my skin | skin score, skin rating app, app that rates your skin, skin analysis online free, skin health score |
| /tools/skincare-routine-order/ | skincare routine order | what order to apply skincare, order of skincare products, does moisturizer go before serum, when to apply sunscreen in routine, skincare steps in order |
| /tools/dry-vs-dehydrated-skin/ | dry vs dehydrated skin | is my skin dry or dehydrated, dehydrated skin signs, can oily skin be dehydrated, dehydrated skin quiz |
| /tools/sunscreen-amount-calculator/ | how much sunscreen for face | how much sunscreen to use, two finger rule sunscreen, sunscreen amount calculator, how long should sunscreen bottle last |
| /tools/can-i-mix-skincare-ingredients/ | can I use retinol and vitamin c together | skincare ingredient checker, what not to mix with retinol, niacinamide and vitamin c together, can I use AHA and BHA together, salicylic acid and retinol |
| /tools/skincare-results-timeline/ | how long does it take for skincare to work | how long does retinol take to work, how long does vitamin c take to work, how long to see results from skincare, when to give up on a skincare product |
| /tools/purging-or-breakout/ | purging vs breakout | is my skin purging, skin purging or breakout quiz, how long does skin purging last, does niacinamide cause purging |
| /tools/how-often-to-exfoliate/ | how often should I exfoliate | how often to exfoliate face, can I exfoliate every day, over exfoliated skin signs, how often to use salicylic acid |

## Next pages to build (once volume confirms)

- what causes dull skin / how to get glowing skin (radiance angle)
- how to reduce redness on face (clarity angle)
- skin barrier damaged quiz / how to repair skin barrier
- morning vs night skincare routine
- how to take a good skin photo for tracking (low volume, high intent, matches the app)
- skincare routine for oily skin / dry skin / combination skin (one page per type, links from quiz results)
- does drinking water help skin
- best time to apply retinol
- how to track skincare progress (very close to the app's core use case)

## Paste list for Keyword Planner

```
what is my skin type
skin type quiz
skin type test
how to know my skin type
what skin type do I have
combination skin quiz
rate my skin
skin score
skin rating app
app that rates your skin
skin analysis app
free skin analysis
ai skin analysis
skin analysis online
skin health score
skincare routine order
what order to apply skincare
order of skincare products
skincare steps in order
does moisturizer go before serum
does sunscreen go before or after moisturizer
when to apply eye cream
dry vs dehydrated skin
is my skin dry or dehydrated
dehydrated skin signs
can oily skin be dehydrated
how to fix dehydrated skin
how much sunscreen for face
how much sunscreen to use
two finger rule sunscreen
sunscreen amount
how long should a bottle of sunscreen last
can I use retinol and vitamin c together
can I use niacinamide with vitamin c
can I use salicylic acid and retinol together
what not to mix with retinol
can I use aha and bha together
skincare ingredients not to mix
skincare ingredient checker
benzoyl peroxide and retinol
how long does it take for skincare to work
how long does retinol take to work
how long does vitamin c take to work
how long does niacinamide take to work
how long to see results from skincare
skin purging vs breakout
is my skin purging
how long does skin purging last
does niacinamide cause purging
retinol purge
how often should I exfoliate
how often to exfoliate face
can I exfoliate every day
over exfoliated skin
how often to use salicylic acid
how often to use glycolic acid
how to get glowing skin
why is my skin dull
how to reduce redness on face
skin barrier damaged
how to repair skin barrier
how to track skincare progress
skincare progress photos
```
