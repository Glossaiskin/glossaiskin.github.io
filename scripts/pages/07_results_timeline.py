PAGE = dict(
    order=7,
    slug="skincare-results-timeline",
    kind="Timeline",
    card_title="How long until skincare works",
    card_blurb="Realistic timelines per ingredient, with the dates to check back on.",
    title="How Long Does It Take for Skincare to Work? Results Timeline by Ingredient",
    description="Pick the product or ingredient you started and your start date. Get a realistic timeline for first results, full results, and the exact dates to take a comparison photo.",
    h1="How long does skincare take to work? Get your timeline",
    intro="Most products get abandoned in week two, right before they would have started working. Pick what you started and when, and get the dates when a change should be visible, so you can judge it fairly.",
    cta=dict(
        title="Take the comparison photos with a score attached",
        body="Gloss scans your skin daily and stores hydration, clarity, texture and radiance scores, so on each check-in date you compare numbers, not memories. Start the timeline the day you start the product.",
    ),
    tool_html="""
    <div class="cols">
      <div class="q"><label class="qlabel" for="ing">What did you start?</label><select id="ing"></select></div>
      <div class="q"><label class="qlabel" for="date">When did you start?</label><input type="text" id="date" placeholder="YYYY-MM-DD" inputmode="numeric"></div>
    </div>
    <div class="q"><label class="qlabel" for="goal">Main goal</label>
      <select id="goal">
        <option value="acne">Fewer breakouts</option><option value="marks">Fade dark marks</option><option value="texture">Smoother texture</option><option value="lines">Fine lines</option><option value="hydration">Hydration and plumpness</option><option value="glow">Brightness and glow</option><option value="redness">Less redness</option>
      </select></div>
    <div class="actions"><button class="btn" id="go">Show my timeline</button></div>
    <div class="result" id="res"></div>
""",
    tool_js=r"""
(function(){
  var T = {
    retinol:{n:'Retinol / retinoid', adj:[14,28], first:[42,56], full:[84,180], note:'Weeks 1 to 4 can bring dryness, flaking and sometimes more breakouts (purging). This is expected. Texture improves first, then tone, then fine lines last.'},
    vitc:{n:'Vitamin C serum', adj:[0,7], first:[21,42], full:[84,120], note:'Brightness is usually the first thing people notice. Dark marks take longer.'},
    niacinamide:{n:'Niacinamide', adj:[0,7], first:[14,28], full:[56,84], note:'Oil control and redness respond first. Pore appearance and marks take the full course.'},
    bha:{n:'Salicylic acid (BHA)', adj:[7,21], first:[14,28], full:[56,84], note:'Blackheads and congestion clear first. Inflamed spots follow. A short purge in weeks 1 to 3 is common.'},
    aha:{n:'Glycolic or lactic acid (AHA)', adj:[7,14], first:[14,28], full:[56,84], note:'Skin feels smoother within a few uses. Even tone and marks take the longer course.'},
    azelaic:{n:'Azelaic acid', adj:[7,14], first:[28,42], full:[84,120], note:'Slow but steady. Redness eases first, then marks. Itching in the first week is common and passes.'},
    bp:{n:'Benzoyl peroxide', adj:[7,14], first:[14,28], full:[56,84], note:'Works quickly on inflamed spots. Dryness in the first two weeks is the usual reason people stop. Use less, not none.'},
    ha:{n:'Hyaluronic acid / hydrating serum', adj:[0,0], first:[1,3], full:[14,28], note:'Plumpness is immediate but temporary. The lasting gain comes from consistent use and sealing it with moisturizer.'},
    ceramide:{n:'Barrier repair moisturizer', adj:[0,0], first:[3,7], full:[14,28], note:'Tightness and stinging ease in days. Full barrier recovery after over-exfoliation takes two to four weeks.'},
    spf:{n:'Daily sunscreen', adj:[0,0], first:[28,56], full:[180,365], note:'Nothing visible at first, since sunscreen prevents rather than treats. Over months, fewer new marks and more even tone. Over years, it is the difference.'},
    tranex:{n:'Tranexamic acid', adj:[0,7], first:[28,56], full:[84,120], note:'Pigmentation only. Pairs well with vitamin C and SPF, which are needed to keep results.'},
    peptides:{n:'Peptide serum', adj:[0,0], first:[28,56], full:[84,120], note:'Subtle. Firmness and fine lines. Do not expect a dramatic before and after.'},
    prescription:{n:'Prescription retinoid (tretinoin, adapalene)', adj:[14,42], first:[56,84], full:[120,180], note:'The adjustment period is longer and harsher than retinol. Dermatologists judge results at 12 weeks, not before.'}
  };
  var GOAL = { acne:'breakouts', marks:'dark marks', texture:'texture', lines:'fine lines', hydration:'hydration', glow:'glow', redness:'redness' };
  var SLOW = { marks:1.3, lines:1.5 }; // pigment and lines take longer than the base timeline
  var sel=document.getElementById('ing'); Object.keys(T).forEach(function(k){ sel.add(new Option(T[k].n,k)); });
  var d=document.getElementById('date'); d.value = new Date().toISOString().slice(0,10);
  function addDays(base, n){ var x=new Date(base); x.setDate(x.getDate()+n); return x; }
  function fmt(x){ return x.toLocaleDateString(undefined,{month:'short',day:'numeric',year:'numeric'}); }
  document.getElementById('go').addEventListener('click', function(){
    var t=T[sel.value], g=document.getElementById('goal').value, mult=SLOW[g]||1;
    var base=new Date(d.value+'T12:00:00'); if(isNaN(base)) base=new Date();
    var today=new Date(); var day=Math.floor((today-base)/86400000);
    var f0=Math.round(t.first[0]*mult), f1=Math.round(t.first[1]*mult), u0=Math.round(t.full[0]*mult), u1=Math.round(t.full[1]*mult);
    var out='<span class="tag">'+t.n+' for '+GOAL[g]+'</span>';
    if (day>=0) out+='<div class="big">Day '+day+'</div>';
    out+='<ol class="steps">';
    if (t.adj[1]>0) out+='<li><div><strong>Adjustment: days '+t.adj[0]+' to '+t.adj[1]+'</strong> ('+fmt(addDays(base,t.adj[0]))+' to '+fmt(addDays(base,t.adj[1]))+')<span class="why">Dryness, tingling or a purge can happen here. Do not judge the product yet.</span></div></li>';
    out+='<li><div><strong>First visible change: days '+f0+' to '+f1+'</strong> ('+fmt(addDays(base,f0))+' to '+fmt(addDays(base,f1))+')<span class="why">Take your first comparison photo on '+fmt(addDays(base,f1))+'. Same light, same time of day, no makeup.</span></div></li>';
    out+='<li><div><strong>Full result: days '+u0+' to '+u1+'</strong> ('+fmt(addDays(base,u0))+' to '+fmt(addDays(base,u1))+')<span class="why">Decision point is '+fmt(addDays(base,u0))+'. If nothing has moved by then, it is fair to stop.</span></div></li></ol>';
    out+='<p>'+t.note+'</p>';
    if (day>=0 && day<f0) out+='<p><strong>Where you are:</strong> too early to judge. Keep going unless you have burning, swelling or a rash, which are reasons to stop regardless of timeline.</p>';
    else if (day>=f0 && day<u0) out+='<p><strong>Where you are:</strong> the window where early change should be visible. Compare a photo from day 0 with today rather than relying on memory.</p>';
    else if (day>=u0) out+='<p><strong>Where you are:</strong> past the point where results should show. If your skin is no better, this product is not doing it for you. If it is better, this is your new baseline.</p>';
    out+='<p class="small">Timelines are typical ranges from clinical studies and dermatology guidance for consistent use at the recommended frequency. Skipping days resets the clock more than people expect.</p>';
    out+='<p><a class="btn" href="https://apps.apple.com/us/app/gloss-ai-skin-analysis/id6792349354" rel="noopener">Track this in Gloss with daily scores</a></p>';
    var r=document.getElementById('res'); r.innerHTML=out; r.classList.add('show'); r.scrollIntoView({behavior:'smooth',block:'start'});
  });
})();
""",
    article_html="""
  <h2>Typical timelines at a glance</h2>
  <div class="table-wrap"><table>
    <tr><th>Ingredient</th><th>First change</th><th>Full result</th></tr>
    <tr><td>Hydrating serum</td><td>1 to 3 days</td><td>2 to 4 weeks</td></tr>
    <tr><td>Barrier moisturizer</td><td>3 to 7 days</td><td>2 to 4 weeks</td></tr>
    <tr><td>Niacinamide</td><td>2 to 4 weeks</td><td>8 to 12 weeks</td></tr>
    <tr><td>Salicylic acid</td><td>2 to 4 weeks</td><td>8 to 12 weeks</td></tr>
    <tr><td>Vitamin C</td><td>3 to 6 weeks</td><td>12 to 16 weeks</td></tr>
    <tr><td>Azelaic acid</td><td>4 to 6 weeks</td><td>12 to 16 weeks</td></tr>
    <tr><td>Retinol</td><td>6 to 8 weeks</td><td>12 to 24 weeks</td></tr>
    <tr><td>Prescription retinoid</td><td>8 to 12 weeks</td><td>4 to 6 months</td></tr>
    <tr><td>Daily sunscreen</td><td>1 to 2 months</td><td>Ongoing, years</td></tr>
  </table></div>

  <h2>Why it takes this long</h2>
  <p>Skin renews itself roughly every 28 days in your twenties and slower after that, up to 45 days or more by your forties. Anything that works by changing how new skin cells form (retinoids, acids, niacinamide, vitamin C) needs at least one full cycle before the new skin is on the surface, and two or three cycles before the change is obvious. Hydration is the exception because it changes the skin you already have.</p>

  <h2>How to judge fairly</h2>
  <ul>
    <li>Photograph day 0 in daylight, no makeup, same spot, same distance. Repeat on the check-in dates.</li>
    <li>Change one thing at a time. If you add three products, you cannot attribute the result to any of them.</li>
    <li>Use it at the frequency it is meant for. Twice a week retinol judged at week 6 has had 12 applications. That is not enough.</li>
    <li>Separate "worse" from "adjusting". Dryness, mild flaking and a few extra spots in the first weeks of an active are adjustment. Burning, swelling and hives are reactions. Stop for the second, not the first.</li>
  </ul>

  <h2>When to give up on a product</h2>
  <p>At the start of the "full result" window, if your comparison photos show nothing. For most actives that is 12 weeks. For hydration products it is one month. Giving up earlier means you paid for the adjustment period and left before the payoff. Giving up later means you are hoping, not measuring.</p>
""",
    faqs=[
        ("How long does it take for retinol to work?", "Six to eight weeks for the first visible change in texture, and 12 to 24 weeks for the full result on tone and fine lines. The first two to four weeks usually bring dryness or a purge, which is not a sign it is failing."),
        ("How long does vitamin C take to work on the skin?", "Three to six weeks for brightness, and 12 to 16 weeks for dark marks to fade noticeably. It needs daily use and sunscreen on top to hold the result."),
        ("How long does it take for a skincare routine to show results?", "Hydration changes in days. Breakouts and texture take four to eight weeks. Pigmentation and fine lines take three to six months. Judge each product at the end of its own window, not the shortest one."),
        ("How long should I try a skincare product before giving up?", "Twelve weeks for actives like retinol, acids, vitamin C and niacinamide. Four weeks for moisturizers and hydrating serums. Stop sooner only for burning, swelling or a rash."),
        ("Why does my skin get worse before it gets better?", "Retinoids and exfoliating acids speed up cell turnover, which pushes clogged pores to the surface faster than usual for the first few weeks. This purge settles by week four to six. New breakouts in areas you never get them, or lasting past eight weeks, are a reaction rather than a purge."),
    ],
)
