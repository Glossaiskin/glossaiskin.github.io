PAGE = dict(
    order=1,
    slug="skin-type-quiz",
    kind="Quiz",
    card_title="What is my skin type?",
    card_blurb="Eight questions. Oily, dry, combination, normal or sensitive, with a routine to match.",
    title="What Is My Skin Type? Free 8-Question Skin Type Quiz (Oily, Dry, Combination, Normal)",
    description="Find your skin type in 2 minutes. This free quiz tells you if your skin is oily, dry, combination, normal or sensitive, explains why, and gives you a simple routine for it.",
    h1="What is my skin type? Take the 2-minute quiz",
    intro="Answer eight questions about how your skin behaves on a normal day. You get your type, the reason behind it, and a starter routine. No email, no sign-up.",
    cta=dict(
        title="Your type is the starting point. Your scores are the rest.",
        body="Two people with oily skin can have completely different hydration and texture. Gloss scans your face and scores hydration, clarity, texture and radiance so the routine fits you, not your category.",
    ),
    tool_html="""
    <form id="quiz" onsubmit="return false">
      <div class="q"><span class="qlabel">1. An hour after washing your face with nothing on it, how does it feel?</span>
        <div class="opts">
          <label class="opt"><input type="radio" name="q1" value="D2S1" required> Tight, maybe a bit itchy or flaky</label>
          <label class="opt"><input type="radio" name="q1" value="N1"> Comfortable, I forget about it</label>
          <label class="opt"><input type="radio" name="q1" value="O2"> Already a little shiny</label>
          <label class="opt"><input type="radio" name="q1" value="C2"> Shiny on the forehead and nose, tight on the cheeks</label>
        </div></div>
      <div class="q"><span class="qlabel">2. By mid-afternoon, where is the shine?</span>
        <div class="opts">
          <label class="opt"><input type="radio" name="q2" value="D2" required> Nowhere. If anything I look dull</label>
          <label class="opt"><input type="radio" name="q2" value="N1"> Maybe a little on the nose</label>
          <label class="opt"><input type="radio" name="q2" value="C2"> Forehead, nose and chin. Cheeks are fine</label>
          <label class="opt"><input type="radio" name="q2" value="O2"> Everywhere</label>
        </div></div>
      <div class="q"><span class="qlabel">3. How visible are your pores?</span>
        <div class="opts">
          <label class="opt"><input type="radio" name="q3" value="D1" required> Barely, I have to look for them</label>
          <label class="opt"><input type="radio" name="q3" value="N1"> Small, mostly around the nose</label>
          <label class="opt"><input type="radio" name="q3" value="C1"> Noticeable in the T-zone only</label>
          <label class="opt"><input type="radio" name="q3" value="O2"> Noticeable across most of my face</label>
        </div></div>
      <div class="q"><span class="qlabel">4. How does your skin react to new products?</span>
        <div class="opts">
          <label class="opt"><input type="radio" name="q4" value="S2" required> Often stings, goes red or bumpy</label>
          <label class="opt"><input type="radio" name="q4" value="S1"> Sometimes, with strong actives or fragrance</label>
          <label class="opt"><input type="radio" name="q4" value="N1"> Rarely, I can use most things</label>
        </div></div>
      <div class="q"><span class="qlabel">5. How often do you get breakouts?</span>
        <div class="opts">
          <label class="opt"><input type="radio" name="q5" value="D1" required> Almost never</label>
          <label class="opt"><input type="radio" name="q5" value="N1"> Occasionally, around my period or stress</label>
          <label class="opt"><input type="radio" name="q5" value="C1"> Mostly on forehead, nose or chin</label>
          <label class="opt"><input type="radio" name="q5" value="O2"> Regularly, in more than one area</label>
        </div></div>
      <div class="q"><span class="qlabel">6. Flaking or rough patches?</span>
        <div class="opts">
          <label class="opt"><input type="radio" name="q6" value="D2" required> Yes, regularly, especially in winter</label>
          <label class="opt"><input type="radio" name="q6" value="C1"> Only on my cheeks or around the nose</label>
          <label class="opt"><input type="radio" name="q6" value="N1"> Rarely</label>
          <label class="opt"><input type="radio" name="q6" value="O1"> Never</label>
        </div></div>
      <div class="q"><span class="qlabel">7. If you wear foundation or SPF, what happens by evening?</span>
        <div class="opts">
          <label class="opt"><input type="radio" name="q7" value="D2" required> It clings to dry patches and looks cakey</label>
          <label class="opt"><input type="radio" name="q7" value="N1"> It mostly stays put</label>
          <label class="opt"><input type="radio" name="q7" value="C2"> It slides off my nose and forehead, fine elsewhere</label>
          <label class="opt"><input type="radio" name="q7" value="O2"> It slides off everywhere</label>
        </div></div>
      <div class="q"><span class="qlabel">8. Does your face flush or go red easily (heat, wind, spicy food, exercise)?</span>
        <div class="opts">
          <label class="opt"><input type="radio" name="q8" value="S2" required> Yes, very easily and it lingers</label>
          <label class="opt"><input type="radio" name="q8" value="S1"> A bit, but it fades fast</label>
          <label class="opt"><input type="radio" name="q8" value="N1"> Not really</label>
        </div></div>
      <div class="actions"><button class="btn" id="go">Show my skin type</button><span class="small" id="err"></span></div>
    </form>
    <div class="result" id="res"></div>
""",
    tool_js=r"""
(function(){
  var TYPES = {
    oily: {name:'Oily', why:'Your answers point to oil production across the whole face: shine that comes back within hours, visible pores in more than one zone, and makeup that slides. Oily skin is not "dirty" skin and it is not a reason to strip it. Over-cleansing makes it produce more.',
      am:['Gel or foaming cleanser','Niacinamide serum (2 to 5%)','Light gel moisturizer','Fluid or gel SPF 30+'],
      pm:['Gel cleanser (double cleanse if you wore SPF or makeup)','Salicylic acid 2% (start 2 to 3 nights a week) or a retinoid on alternate nights','Light moisturizer'],
      tip:'Do not skip moisturizer. Dehydrated oily skin is the most common reason an oily routine stops working.'},
    dry: {name:'Dry', why:'Tightness after cleansing, flaking, small pores and makeup that clings to patches all point to skin that does not make enough oil. The goal is to add lipids and stop stripping the ones you have.',
      am:['Cream or milk cleanser, or just rinse with water','Hyaluronic acid or glycerin serum on damp skin','Rich cream with ceramides','Cream SPF 30+'],
      pm:['Cream or oil cleanser','Hydrating serum','Rich moisturizer, plus a few drops of face oil on top if still tight','A gentle retinoid only 1 to 2 nights a week once the barrier feels calm'],
      tip:'Apply moisturizer within a minute of cleansing while skin is still damp. It traps far more water than applying to dry skin.'},
    combination: {name:'Combination', why:'Your T-zone (forehead, nose, chin) behaves oily and your cheeks behave normal to dry. This is the most common type, and the mistake most people make is treating the whole face like the oily part.',
      am:['Gentle gel cleanser','Niacinamide serum (helps both zones)','Light moisturizer on the T-zone, a richer one on the cheeks','SPF 30+, fluid texture'],
      pm:['Gentle cleanser','Salicylic acid on the T-zone only, 2 to 3 nights a week','Moisturizer, heavier on cheeks'],
      tip:'Zone your routine. It is fine to use two moisturizers, or one moisturizer applied thin in the centre and thick at the sides.'},
    normal: {name:'Normal', why:'Balanced oil, few reactions, small pores, rare flaking. Your job is maintenance and prevention: protect it from sun, keep the barrier happy, and add actives slowly if you want them.',
      am:['Gentle cleanser','Antioxidant serum (vitamin C) if you like','Moisturizer','SPF 30+ every day'],
      pm:['Gentle cleanser','A retinoid 2 to 3 nights a week if you want anti-aging or texture benefits','Moisturizer'],
      tip:'The biggest gain available to normal skin is daily sunscreen. Everything else is optional.'},
    sensitive: {name:'Sensitive', why:'Stinging with new products, easy flushing and redness that lingers mean your skin barrier reacts more than most. Sensitivity sits on top of another type (you can be sensitive and oily, or sensitive and dry), so the second line of your result shows the base type.',
      am:['Cream cleanser or water only','Barrier serum (ceramides, panthenol, centella)','Fragrance-free moisturizer','Mineral SPF 30+ (zinc oxide) tends to sting less'],
      pm:['Cream cleanser','Moisturizer','Introduce one new product at a time and patch test behind the ear for 3 nights first'],
      tip:'Fewer products, fragrance-free, and no more than one active. Most sensitive skin calms down when you remove things, not when you add them.'}
  };
  var form = document.getElementById('quiz');
  document.getElementById('go').addEventListener('click', function(){
    var s = {O:0,D:0,C:0,N:0,S:0}, answered = 0;
    for (var i=1;i<=8;i++){
      var el = form.querySelector('input[name=q'+i+']:checked');
      if(!el) continue; answered++;
      el.value.match(/[ODCNS]\d/g).forEach(function(tok){ s[tok[0]] += +tok[1]; });
    }
    if (answered < 8){ document.getElementById('err').textContent = 'Answer all 8 questions first.'; return; }
    document.getElementById('err').textContent = '';
    var base = ['O','D','C','N'].sort(function(a,b){ return s[b]-s[a]; });
    // Combination if C leads, or if O and D are both strong.
    var key = {O:'oily',D:'dry',C:'combination',N:'normal'}[base[0]];
    if (s.O >= 4 && s.D >= 4 && key !== 'combination') key = 'combination';
    var sens = s.S >= 3;
    var t = TYPES[key], out = '';
    if (sens){
      var sT = TYPES.sensitive;
      out += '<span class="tag">Your result</span><div class="big">Sensitive ' + t.name.toLowerCase() + '</div>';
      out += '<p>' + sT.why + '</p><p><strong>Base type: ' + t.name + '.</strong> ' + t.why + '</p>';
      out += '<div class="cols"><div><h4>Morning</h4><ol>' + sT.am.map(function(x){return '<li>'+x+'</li>'}).join('') + '</ol></div>';
      out += '<div><h4>Evening</h4><ol>' + sT.pm.map(function(x){return '<li>'+x+'</li>'}).join('') + '</ol></div></div>';
      out += '<p><strong>One thing to do this week:</strong> ' + sT.tip + '</p>';
    } else {
      out += '<span class="tag">Your result</span><div class="big">' + t.name + '</div><p>' + t.why + '</p>';
      out += '<div class="cols"><div><h4>Morning</h4><ol>' + t.am.map(function(x){return '<li>'+x+'</li>'}).join('') + '</ol></div>';
      out += '<div><h4>Evening</h4><ol>' + t.pm.map(function(x){return '<li>'+x+'</li>'}).join('') + '</ol></div></div>';
      out += '<p><strong>One thing to do this week:</strong> ' + t.tip + '</p>';
    }
    var total = s.O+s.D+s.C+s.N || 1;
    out += '<p class="small">Signal strength: oily ' + s.O + ', dry ' + s.D + ', combination ' + s.C + ', normal ' + s.N + ', sensitivity ' + s.S + '. Skin type shifts with season, hormones and climate, so retake this in a few months.</p>';
    out += '<p><a class="btn" href="https://apps.apple.com/us/app/gloss-ai-skin-analysis/id6792349354" rel="noopener">Scan my skin in Gloss for the real scores</a></p>';
    var r = document.getElementById('res'); r.innerHTML = out; r.classList.add('show'); r.scrollIntoView({behavior:'smooth', block:'start'});
  });
})();
""",
    article_html="""
  <h2>The five skin types, in one line each</h2>
  <ul>
    <li><strong>Oily:</strong> shine returns within a couple of hours of cleansing, pores are visible across the face, breakouts are common.</li>
    <li><strong>Dry:</strong> tight after washing, flaky in places, pores are small, makeup clings to patches.</li>
    <li><strong>Combination:</strong> oily forehead, nose and chin with normal or dry cheeks. The most common type.</li>
    <li><strong>Normal:</strong> not much shine, not much flaking, few reactions. Rare, and mostly about maintenance.</li>
    <li><strong>Sensitive:</strong> stings, flushes or goes bumpy with new products. Sits on top of one of the other four.</li>
  </ul>

  <h2>The bare-face test if you want to double-check</h2>
  <p>Wash your face with a gentle cleanser, pat dry, and apply nothing. Wait an hour, then look in a mirror in daylight. Shine everywhere means oily. Tight and dull means dry. Shine only down the centre means combination. Nothing much means normal. Do this on a normal day at home, not after a workout or a flight.</p>

  <h2>Skin type versus skin condition</h2>
  <p>Your type is mostly genetic and describes how much oil your skin makes. A condition is temporary and can happen to any type: dehydration, a damaged barrier, acne, sun damage. Oily skin can be dehydrated. Dry skin can break out. The quiz finds your type. Whether your skin is currently hydrated, clear, smooth and bright is a separate question, and it changes week to week. That is what a scan measures.</p>

  <h2>Why one quiz result is not the whole picture</h2>
  <p>Any quiz, including this one, relies on how you describe your own skin, and most people describe it the same way for years even as it changes. Seasons, hormones, stress, new medications and moving city all shift it. A quick way to catch that drift is to track a few numbers over time rather than re-diagnosing from memory. The Gloss app scores hydration, clarity, texture and radiance from a daily selfie, so you see the change instead of guessing.</p>
""",
    faqs=[
        ("How do I know my skin type at home?", "Cleanse, apply nothing, wait an hour and look in daylight. Shine all over is oily, tightness and dullness is dry, shine only in the T-zone is combination, and no strong signal either way is normal. Stinging or flushing from products on top of any of those means sensitive."),
        ("Can my skin type change?", "Yes. Oil production drops with age, changes with hormones and medication, and responds to climate. Many people move from oily in their teens to combination in their thirties. Retake the quiz when the season changes or when your usual routine stops feeling right."),
        ("What is the most common skin type?", "Combination. Most faces produce more oil in the forehead, nose and chin than on the cheeks, because that is where sebaceous glands are densest."),
        ("Is dehydrated skin the same as dry skin?", "No. Dry skin lacks oil and is a type. Dehydrated skin lacks water and is a temporary condition that can affect oily skin too. If you are oily but also tight and dull, you are likely dehydrated, not dry. Try the dry versus dehydrated quiz on this site."),
        ("What routine should I use for combination skin?", "A gentle gel cleanser, niacinamide, a light moisturizer in the T-zone and a richer one on the cheeks, and SPF in the morning. In the evening, use salicylic acid on the oily zones only, two or three nights a week."),
    ],
)
