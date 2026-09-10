PAGE = dict(
    order=6,
    slug="can-i-mix-skincare-ingredients",
    kind="Checker",
    card_title="Can I mix these ingredients?",
    card_blurb="Retinol with vitamin C? Niacinamide with acids? Pick two and check.",
    title="Can I Mix These Skincare Ingredients? Free Compatibility Checker (Retinol, Vitamin C, Niacinamide, Acids)",
    description="Pick any two skincare ingredients and find out if you can layer them, use them on the same day at different times, or keep them on separate nights. Covers retinol, vitamin C, niacinamide, AHAs, BHA, benzoyl peroxide, azelaic acid and more.",
    h1="Can I mix these skincare ingredients? Check any two",
    intro="Choose two ingredients. You get a plain verdict (layer them, split AM and PM, alternate nights, or avoid), the reason, and how to schedule them.",
    cta=dict(
        title="Added a new active? Measure what it does.",
        body="The only way to know if a new ingredient is helping is to watch your skin over weeks, not days. Gloss scores clarity, texture, hydration and radiance daily so you can see the before and after instead of guessing.",
    ),
    tool_html="""
    <div class="cols">
      <div class="q"><label class="qlabel" for="a">Ingredient one</label><select id="a"></select></div>
      <div class="q"><label class="qlabel" for="b">Ingredient two</label><select id="b"></select></div>
    </div>
    <div class="actions"><button class="btn" id="go">Check</button></div>
    <div class="result" id="res"></div>
""",
    tool_js=r"""
(function(){
  var ING = {
    retinol:'Retinol / retinoids', vitc:'Vitamin C (L-ascorbic acid)', niacinamide:'Niacinamide', aha:'AHA (glycolic, lactic)', bha:'BHA (salicylic acid)',
    bp:'Benzoyl peroxide', azelaic:'Azelaic acid', ha:'Hyaluronic acid', peptides:'Peptides', ceramides:'Ceramides', spf:'Sunscreen', copper:'Copper peptides', tranex:'Tranexamic acid', bakuchiol:'Bakuchiol'
  };
  // verdicts: L = layer freely, S = same day, split AM/PM, A = alternate nights, X = avoid together
  var R = {
    'retinol|vitc':['S','Both are effective, but layering them raises irritation and the low pH of vitamin C is not ideal under retinol. Vitamin C in the morning under SPF, retinol at night.'],
    'retinol|aha':['A','Two exfoliating processes at once. Alternate nights: acid on two nights, retinol on two or three others, at least one night with neither.'],
    'retinol|bha':['A','Same as with AHAs. Salicylic acid on some nights, retinol on others. If you have very oily, resilient skin you can eventually do BHA in the morning and retinol at night.'],
    'retinol|bp':['S','Benzoyl peroxide oxidises most forms of retinol on contact. Benzoyl peroxide in the morning or as a wash, retinol at night. Adapalene is the exception and can be layered with BP.'],
    'retinol|niacinamide':['L','A good pair. Niacinamide reduces the irritation and dryness retinol causes. Apply niacinamide first, retinol on top, or mix into moisturizer.'],
    'retinol|azelaic':['L','Fine together and often prescribed together. If your skin is sensitive, azelaic in the morning and retinol at night is gentler.'],
    'retinol|ha':['L','Ideal. Hyaluronic acid on damp skin first, then retinol, then moisturizer. The extra hydration offsets retinol dryness.'],
    'retinol|peptides':['L','No conflict. Peptides first, retinol after, or peptides in the morning.'],
    'retinol|ceramides':['L','Ceramides repair the barrier retinol stresses. Use a ceramide moisturizer over your retinol every night.'],
    'retinol|spf':['S','Not a conflict, a requirement. Retinol at night, sunscreen every morning. Retinoids make skin more sun-sensitive.'],
    'retinol|copper':['A','Copper peptides may be destabilised by retinoids and both are potent. Alternate nights or copper peptides in the morning.'],
    'retinol|tranex':['L','No known conflict. Both help with dark marks. Tranexamic first, then retinol.'],
    'retinol|bakuchiol':['L','Bakuchiol is often marketed as a retinol alternative, but the two can be used together and bakuchiol may reduce retinol irritation. Not much point doubling up though.'],
    'vitc|niacinamide':['L','The old warning about them cancelling out came from a 1960s study at high heat. In modern formulas they are fine together. Vitamin C first, niacinamide after.'],
    'vitc|aha':['S','Both are low pH. Layering them is a common cause of stinging and redness. Vitamin C in the morning, acids at night.'],
    'vitc|bha':['S','Same as with AHAs. Vitamin C in the morning, salicylic acid at night.'],
    'vitc|bp':['X','Benzoyl peroxide oxidises L-ascorbic acid immediately. Do not layer. Vitamin C in the morning, benzoyl peroxide at night, or use a stable vitamin C derivative instead.'],
    'vitc|azelaic':['L','Fine together. Vitamin C first, azelaic acid after. Both help pigmentation.'],
    'vitc|ha':['L','Ideal. Vitamin C first, hyaluronic acid over it, then moisturizer and SPF.'],
    'vitc|peptides':['S','L-ascorbic acid is very acidic and some peptides break down at low pH. Vitamin C in the morning, peptides at night, or keep 20 minutes between them.'],
    'vitc|ceramides':['L','No conflict. Vitamin C, then a ceramide moisturizer.'],
    'vitc|spf':['L','One of the best pairs in skincare. Vitamin C under sunscreen boosts the protection against UV-generated free radicals.'],
    'vitc|copper':['X','Copper ions oxidise ascorbic acid. Keep them at opposite ends of the day.'],
    'vitc|tranex':['L','Fine together, and a strong combination for dark marks. Vitamin C first.'],
    'vitc|bakuchiol':['L','No conflict. Bakuchiol works day or night.'],
    'niacinamide|aha':['L','Fine for most people. Acid first on dry skin, wait a minute, then niacinamide. Rarely, layering causes flushing; if so, split them.'],
    'niacinamide|bha':['L','A common and effective pair for oily, congested skin. BHA first, then niacinamide.'],
    'niacinamide|bp':['L','No conflict. Niacinamide can calm the dryness benzoyl peroxide causes.'],
    'niacinamide|azelaic':['L','Excellent together for redness and marks. Either order.'],
    'niacinamide|ha':['L','Both hydrating, no conflict, often in the same bottle.'],
    'niacinamide|peptides':['L','No conflict.'],
    'niacinamide|ceramides':['L','No conflict. Both support the barrier.'],
    'niacinamide|spf':['L','No conflict. Niacinamide under SPF is a standard morning routine.'],
    'niacinamide|copper':['L','No conflict.'],
    'niacinamide|tranex':['L','No conflict and a good pigmentation pair.'],
    'niacinamide|bakuchiol':['L','No conflict.'],
    'aha|bha':['A','Both exfoliate. Using separate products on the same night over-exfoliates most skin. Alternate nights, or use a single product that combines them at a sensible strength.'],
    'aha|bp':['A','Both are drying and irritating. Alternate nights, or benzoyl peroxide as a morning wash and AHA at night.'],
    'aha|azelaic':['S','Usually fine, but sensitive skin can sting. Azelaic in the morning, AHA at night.'],
    'aha|ha':['L','Acid first, then hyaluronic acid on top to rehydrate.'],
    'aha|peptides':['S','Low pH can degrade some peptides. Peptides in the morning, acid at night.'],
    'aha|ceramides':['L','Acid first, then a ceramide moisturizer to repair.'],
    'aha|spf':['S','AHAs increase sun sensitivity for up to a week after use. Acid at night, sunscreen every morning without exception.'],
    'aha|copper':['A','Low pH may destabilise copper peptides. Alternate.'],
    'aha|tranex':['L','Fine together.'],
    'aha|bakuchiol':['L','Fine together, bakuchiol is not an exfoliant.'],
    'bha|bp':['A','Both drying, both for acne. Alternate nights, or BP wash in the morning and BHA at night. Watch for peeling.'],
    'bha|azelaic':['L','Good acne pair. BHA first, azelaic after. Split them if you get stinging.'],
    'bha|ha':['L','BHA first, hydrate on top.'],
    'bha|peptides':['S','Peptides in the morning, BHA at night.'],
    'bha|ceramides':['L','BHA then ceramide moisturizer.'],
    'bha|spf':['L','No conflict, but exfoliants raise sun sensitivity, so SPF every morning.'],
    'bha|copper':['A','Alternate nights.'],
    'bha|tranex':['L','Fine together.'],
    'bha|bakuchiol':['L','Fine together.'],
    'bp|azelaic':['L','Both used for acne and rosacea, fine together. Start slowly, both can dry.'],
    'bp|ha':['L','No conflict. Hydrate after BP.'],
    'bp|peptides':['S','Benzoyl peroxide is an oxidiser. Peptides at the other end of the day.'],
    'bp|ceramides':['L','No conflict. Ceramides offset the dryness.'],
    'bp|spf':['L','No conflict. BP can bleach fabric, not skin, so let it dry before dressing.'],
    'bp|copper':['X','Oxidiser plus a metal peptide. Keep separate.'],
    'bp|tranex':['L','No known conflict.'],
    'bp|bakuchiol':['L','No known conflict.'],
    'azelaic|ha':['L','No conflict.'],'azelaic|peptides':['L','No conflict.'],'azelaic|ceramides':['L','No conflict.'],'azelaic|spf':['L','No conflict, azelaic is fine in the morning.'],'azelaic|copper':['L','No conflict.'],'azelaic|tranex':['L','Good pigmentation pair.'],'azelaic|bakuchiol':['L','No conflict.'],
    'ha|peptides':['L','No conflict.'],'ha|ceramides':['L','No conflict, textbook hydration pairing.'],'ha|spf':['L','No conflict.'],'ha|copper':['L','No conflict.'],'ha|tranex':['L','No conflict.'],'ha|bakuchiol':['L','No conflict.'],
    'peptides|ceramides':['L','No conflict.'],'peptides|spf':['L','No conflict.'],'peptides|copper':['L','No conflict, copper peptides are peptides.'],'peptides|tranex':['L','No conflict.'],'peptides|bakuchiol':['L','No conflict.'],
    'ceramides|spf':['L','No conflict.'],'ceramides|copper':['L','No conflict.'],'ceramides|tranex':['L','No conflict.'],'ceramides|bakuchiol':['L','No conflict.'],
    'spf|copper':['L','No conflict.'],'spf|tranex':['L','No conflict.'],'spf|bakuchiol':['L','No conflict.'],
    'copper|tranex':['L','No known conflict.'],'copper|bakuchiol':['L','No known conflict.'],
    'tranex|bakuchiol':['L','No known conflict.']
  };
  var V = { L:['ok','Yes, layer them'], S:['warn','Same day, different times'], A:['warn','Alternate nights'], X:['no','Keep them apart'] };
  var a=document.getElementById('a'), b=document.getElementById('b');
  Object.keys(ING).forEach(function(k){ a.add(new Option(ING[k],k)); b.add(new Option(ING[k],k)); });
  a.value='retinol'; b.value='vitc';
  document.getElementById('go').addEventListener('click', function(){
    var x=a.value, y=b.value, out='';
    if (x===y){ out='<p>Pick two different ingredients.</p>'; }
    else {
      var rec = R[x+'|'+y] || R[y+'|'+x];
      var v = V[rec[0]];
      out = '<span class="tag '+v[0]+'">'+v[1]+'</span><h3>'+ING[x]+' + '+ING[y]+'</h3><p>'+rec[1]+'</p>';
      if (rec[0]==='A') out += '<p><strong>Example week:</strong> Mon '+ING[x]+', Tue '+ING[y]+', Wed rest, Thu '+ING[x]+', Fri '+ING[y]+', Sat rest, Sun '+ING[x]+'.</p>';
      out += '<p class="small">Whenever you add a second active, give the first one four weeks alone first. If two things go wrong at once you cannot tell which one did it.</p>';
    }
    out += '<p><a class="btn" href="https://apps.apple.com/us/app/gloss-ai-skin-analysis/id6792349354" rel="noopener">Track what this combo does in Gloss</a></p>';
    var r=document.getElementById('res'); r.innerHTML=out; r.classList.add('show'); r.scrollIntoView({behavior:'smooth',block:'start'});
  });
})();
""",
    article_html="""
  <h2>The combinations people ask about most</h2>
  <div class="table-wrap"><table>
    <tr><th>Pair</th><th>Verdict</th><th>How</th></tr>
    <tr><td>Retinol + vitamin C</td><td>Same day, split</td><td>Vitamin C morning, retinol night</td></tr>
    <tr><td>Retinol + AHA or BHA</td><td>Alternate nights</td><td>Acids two nights, retinol three, one night off</td></tr>
    <tr><td>Retinol + niacinamide</td><td>Layer</td><td>Niacinamide first, retinol on top</td></tr>
    <tr><td>Retinol + benzoyl peroxide</td><td>Split</td><td>BP morning, retinol night (adapalene is the exception)</td></tr>
    <tr><td>Vitamin C + niacinamide</td><td>Layer</td><td>The "they cancel out" myth is from a 1960s heat study</td></tr>
    <tr><td>Vitamin C + acids</td><td>Split</td><td>Vitamin C morning, acids night</td></tr>
    <tr><td>Vitamin C + benzoyl peroxide</td><td>Avoid together</td><td>BP oxidises ascorbic acid on contact</td></tr>
    <tr><td>AHA + BHA</td><td>Alternate</td><td>Or a single combined product at a sensible strength</td></tr>
    <tr><td>Niacinamide + anything</td><td>Layer</td><td>The most compatible active there is</td></tr>
  </table></div>

  <h2>Three rules that cover most of it</h2>
  <ol>
    <li><strong>One exfoliating process per night.</strong> Retinoids, AHAs, BHAs and benzoyl peroxide all increase cell turnover or dry the skin. Stack two and you get a damaged barrier, not double results.</li>
    <li><strong>Low pH and high pH do not layer well.</strong> L-ascorbic acid and exfoliating acids work at a low pH. Layering them with each other stings, and layering them with peptides can degrade the peptides. Split by time of day.</li>
    <li><strong>Oxidisers break things.</strong> Benzoyl peroxide destroys L-ascorbic acid and most retinol on contact. Keep them at opposite ends of the day.</li>
  </ol>

  <h2>How to introduce a new active</h2>
  <p>One at a time, two or three nights a week, for four weeks before adding anything else. Take a bare-faced photo in the same light before you start. If your skin is worse at four weeks, stop it. If it is better, keep it and add the next one. This sounds slow. It is faster than the usual cycle of adding four things, reacting, stopping everything and starting over.</p>
""",
    faqs=[
        ("Can I use retinol and vitamin C together?", "Yes, but not at the same time. Vitamin C in the morning under sunscreen and retinol at night. Layering them raises irritation without adding benefit."),
        ("Can I use niacinamide with vitamin C?", "Yes. The belief that they cancel each other comes from a 1960s study done at high temperatures with unstable forms. Modern formulas layer fine. Apply vitamin C first."),
        ("Can I use salicylic acid and retinol together?", "Alternate nights rather than layering. Both increase turnover and using them on the same night over-exfoliates most skin. Resilient oily skin can eventually move salicylic acid to the morning."),
        ("What should you not mix with retinol?", "Do not layer retinol with AHAs, BHAs or benzoyl peroxide on the same night. Vitamin C is fine on the other end of the day. Niacinamide, hyaluronic acid and ceramides all pair well with it."),
        ("Can I use AHA and BHA together?", "Not as separate products on the same night. Pick one per night, or use a single product formulated with both at a moderate strength."),
        ("What can I mix with benzoyl peroxide?", "Niacinamide, hyaluronic acid, ceramides, azelaic acid and adapalene. Keep it away from L-ascorbic acid vitamin C and most retinol, which it oxidises."),
    ],
)
