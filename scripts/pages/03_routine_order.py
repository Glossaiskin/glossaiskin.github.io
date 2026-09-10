PAGE = dict(
    order=3,
    slug="skincare-routine-order",
    kind="Builder",
    card_title="Skincare routine order",
    card_blurb="Tick the products you own and get the correct AM and PM order.",
    title="Skincare Routine Order: What Order to Apply Skincare Products (Free Builder)",
    description="Tick the products you actually own and get the correct order to apply them, morning and night, with a note on which ones should not go on the same night.",
    h1="What order should I apply my skincare? Build your routine",
    intro="Select what you have. The builder puts it in the right order for morning and evening, drops anything that does not belong at that time of day, and warns you about combinations that clash.",
    cta=dict(
        title="Now find out if the routine is doing anything",
        body="Order is the easy part. Knowing whether the routine is improving your skin takes measurement. Gloss scores hydration, clarity, texture and radiance from a daily selfie so you can see which change actually moved the needle.",
    ),
    tool_html="""
    <p class="qlabel">Which of these do you use?</p>
    <div class="chips" id="chips">
      <label class="chip"><input type="checkbox" value="oilcleanser"> Oil or balm cleanser</label>
      <label class="chip"><input type="checkbox" value="cleanser" checked> Cleanser</label>
      <label class="chip"><input type="checkbox" value="toner"> Toner</label>
      <label class="chip"><input type="checkbox" value="essence"> Essence</label>
      <label class="chip"><input type="checkbox" value="vitc"> Vitamin C serum</label>
      <label class="chip"><input type="checkbox" value="ha"> Hyaluronic acid serum</label>
      <label class="chip"><input type="checkbox" value="niacinamide"> Niacinamide serum</label>
      <label class="chip"><input type="checkbox" value="aha"> AHA (glycolic, lactic, mandelic)</label>
      <label class="chip"><input type="checkbox" value="bha"> BHA (salicylic acid)</label>
      <label class="chip"><input type="checkbox" value="retinoid"> Retinol or retinoid</label>
      <label class="chip"><input type="checkbox" value="azelaic"> Azelaic acid</label>
      <label class="chip"><input type="checkbox" value="benzoyl"> Benzoyl peroxide</label>
      <label class="chip"><input type="checkbox" value="peptide"> Peptide serum</label>
      <label class="chip"><input type="checkbox" value="spot"> Spot treatment</label>
      <label class="chip"><input type="checkbox" value="eye"> Eye cream</label>
      <label class="chip"><input type="checkbox" value="moisturizer" checked> Moisturizer</label>
      <label class="chip"><input type="checkbox" value="oil"> Face oil</label>
      <label class="chip"><input type="checkbox" value="spf" checked> Sunscreen</label>
      <label class="chip"><input type="checkbox" value="sleepmask"> Sleeping mask</label>
    </div>
    <div class="actions"><button class="btn" id="go">Put it in order</button></div>
    <div class="result" id="res"></div>
""",
    tool_js=r"""
(function(){
  // order: position in the routine. am/pm: when it belongs. why: one-line reason.
  var P = {
    oilcleanser:{n:'Oil or balm cleanser',o:1,am:false,pm:true,why:'First at night to dissolve SPF, makeup and sebum. Not needed in the morning.'},
    cleanser:{n:'Cleanser',o:2,am:true,pm:true,why:'Clean base so everything after it can absorb.'},
    toner:{n:'Toner',o:3,am:true,pm:true,why:'Thinnest liquid goes first. Skip it if it stings.'},
    essence:{n:'Essence',o:4,am:true,pm:true,why:'Watery hydration layer before serums.'},
    bha:{n:'BHA (salicylic acid)',o:5,am:false,pm:true,why:'Low pH exfoliant goes on clean skin before other serums. Night only, 2 to 3 times a week.'},
    aha:{n:'AHA',o:5,am:false,pm:true,why:'Same slot as BHA. Do not use AHA and BHA on the same night unless it is one combined product.'},
    vitc:{n:'Vitamin C serum',o:6,am:true,pm:false,why:'Antioxidant that works best under sunscreen in the morning.'},
    azelaic:{n:'Azelaic acid',o:7,am:true,pm:true,why:'Gentle enough for either time. Goes after thinner serums.'},
    niacinamide:{n:'Niacinamide serum',o:8,am:true,pm:true,why:'Plays well with almost everything. Serum slot.'},
    ha:{n:'Hyaluronic acid serum',o:8,am:true,pm:true,why:'Apply to slightly damp skin and follow with moisturizer to seal it.'},
    peptide:{n:'Peptide serum',o:9,am:true,pm:true,why:'Serum slot. Keep it away from strong acids on the same application.'},
    retinoid:{n:'Retinol or retinoid',o:10,am:false,pm:true,why:'Night only, on dry skin, after serums and before moisturizer. Start 2 nights a week.'},
    benzoyl:{n:'Benzoyl peroxide',o:10,am:true,pm:true,why:'Treatment slot. Do not layer with retinol on the same night, it deactivates most forms.'},
    spot:{n:'Spot treatment',o:11,am:true,pm:true,why:'Dab on the spot only, after serums so it is not diluted.'},
    eye:{n:'Eye cream',o:12,am:true,pm:true,why:'Before moisturizer so the moisturizer does not block it.'},
    moisturizer:{n:'Moisturizer',o:13,am:true,pm:true,why:'Seals everything below it.'},
    oil:{n:'Face oil',o:14,am:false,pm:true,why:'Oil sits on top of cream, never under it. Night is better so it does not disturb SPF.'},
    sleepmask:{n:'Sleeping mask',o:15,am:false,pm:true,why:'Last step at night, replaces or goes over moisturizer.'},
    spf:{n:'Sunscreen',o:16,am:true,pm:false,why:'Always last in the morning, before makeup. Two finger lengths for the face and neck.'}
  };
  document.getElementById('go').addEventListener('click', function(){
    var sel = Array.prototype.map.call(document.querySelectorAll('#chips input:checked'), function(i){return i.value});
    if (!sel.length){ return; }
    var items = sel.map(function(k){return P[k]}).sort(function(a,b){return a.o-b.o});
    function list(when){
      var l = items.filter(function(p){return p[when]});
      if (!l.length) return '<p class="small">Nothing selected for this time of day.</p>';
      return '<ol class="steps">'+l.map(function(p){return '<li><div><strong>'+p.n+'</strong><span class="why">'+p.why+'</span></div></li>'}).join('')+'</ol>';
    }
    var warns = [];
    var has = function(k){return sel.indexOf(k)>-1};
    if (has('retinoid') && (has('aha')||has('bha'))) warns.push('Retinoid plus an acid: alternate nights. Acids Monday and Thursday, retinoid the other nights, one night off.');
    if (has('retinoid') && has('benzoyl')) warns.push('Retinoid plus benzoyl peroxide: benzoyl in the morning, retinoid at night. Not on the same application.');
    if (has('vitc') && (has('aha')||has('bha'))) warns.push('Vitamin C plus acids: vitamin C in the morning, acids at night. Layering both at once is a common cause of stinging.');
    if (has('aha') && has('bha')) warns.push('AHA plus BHA: pick one per night unless the product combines them. Using both separately on the same night over-exfoliates.');
    if (has('oil') && !has('moisturizer')) warns.push('Face oil without moisturizer: oil seals but does not hydrate. Add a moisturizer under it.');
    if (!has('spf')) warns.push('No sunscreen selected. It is the single step with the most evidence behind it. Add it in the morning, last.');
    if (!has('moisturizer')) warns.push('No moisturizer. Even oily skin needs one, especially with any active in the routine.');
    var out = '<span class="tag">Your order</span><div class="cols"><div><h3>Morning</h3>'+list('am')+'</div><div><h3>Evening</h3>'+list('pm')+'</div></div>';
    if (warns.length) out += '<h4>Things to watch</h4><ul>'+warns.map(function(w){return '<li>'+w+'</li>'}).join('')+'</ul>';
    out += '<p class="small">Rule of thumb behind this order: thinnest to thickest, water-based before oil-based, treatments on clean skin, sunscreen last. Wait about a minute between layers so each one sets.</p>';
    out += '<p><a class="btn" href="https://apps.apple.com/us/app/gloss-ai-skin-analysis/id6792349354" rel="noopener">Track whether this routine works in Gloss</a></p>';
    var r = document.getElementById('res'); r.innerHTML = out; r.classList.add('show'); r.scrollIntoView({behavior:'smooth', block:'start'});
  });
})();
""",
    article_html="""
  <h2>The rule that decides the order</h2>
  <p>Thinnest to thickest. Water-based products go on before oil-based ones, because oil blocks water from getting through but water does not block oil. Treatments with an active ingredient go on clean skin so they reach it undiluted. Sunscreen goes last in the morning because it needs to form an even film on the surface.</p>

  <h2>The standard morning order</h2>
  <ol>
    <li>Cleanser (or a rinse with water if your skin is dry)</li>
    <li>Toner or essence, if you use one</li>
    <li>Vitamin C or another antioxidant serum</li>
    <li>Other serums, thinnest first (hyaluronic acid, niacinamide)</li>
    <li>Eye cream</li>
    <li>Moisturizer</li>
    <li>Sunscreen, two finger lengths</li>
  </ol>

  <h2>The standard evening order</h2>
  <ol>
    <li>Oil or balm cleanser if you wore SPF or makeup</li>
    <li>Water-based cleanser</li>
    <li>Exfoliating acid on the nights you use it</li>
    <li>Hydrating serums</li>
    <li>Retinoid on the nights you use it, on dry skin</li>
    <li>Eye cream</li>
    <li>Moisturizer</li>
    <li>Face oil or sleeping mask, if you use one</li>
  </ol>

  <h2>How long to wait between steps</h2>
  <p>About a minute. Enough for the previous layer to stop feeling wet. The one exception is retinoids on sensitive skin, where waiting 20 minutes after cleansing (or applying moisturizer first, then retinoid on top) reduces irritation. Sunscreen needs no wait time to "activate" but does need to be applied on a dry face so it spreads evenly.</p>

  <h2>Do you actually need all of these?</h2>
  <p>No. Cleanser, moisturizer and sunscreen do most of the work. Add one active for your main concern. Every extra step is a place for irritation to come from and one more thing to forget. A three-step routine done every day beats a nine-step routine done twice a week.</p>
""",
    faqs=[
        ("What order should I apply skincare?", "Cleanser, toner, serums from thinnest to thickest, eye cream, moisturizer, then sunscreen in the morning or face oil at night. Treatments like acids and retinoids go on clean skin before the hydrating layers."),
        ("Does moisturizer go before or after serum?", "After. Serums are thin and water-based, so they need to reach the skin first. Moisturizer seals them in."),
        ("Does sunscreen go before or after moisturizer?", "After moisturizer, as the last step before makeup. Wait a minute for moisturizer to set so the sunscreen spreads evenly."),
        ("Can I use vitamin C and retinol together?", "Not in the same application. Vitamin C in the morning under sunscreen, retinol at night. Using both is fine as long as they are on different ends of the day."),
        ("When do I apply eye cream?", "Before moisturizer. If you apply moisturizer first it forms a film that keeps the eye cream from absorbing."),
    ],
)
