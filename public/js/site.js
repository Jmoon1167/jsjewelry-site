(function(){
  // Mobile menu
  var btn=document.querySelector('.menu-btn'),nav=document.getElementById('mnav');
  if(btn&&nav){
    btn.addEventListener('click',function(){var open=btn.getAttribute('aria-expanded')==='true';
      btn.setAttribute('aria-expanded',String(!open));btn.setAttribute('aria-label',open?'Open menu':'Close menu');nav.hidden=open;});
    nav.addEventListener('click',function(e){if(e.target.tagName==='A'){btn.setAttribute('aria-expanded','false');nav.hidden=true;}});
  }

  // Gold snowfall
  var box=document.querySelector('.snow');
  if(box&&!(window.matchMedia&&matchMedia('(prefers-reduced-motion: reduce)').matches)){
    var n=window.innerWidth<700?18:34;
    for(var i=0;i<n;i++){var f=document.createElement('span');f.className='flake';
      var sz=(Math.random()*4+2).toFixed(1);f.style.width=f.style.height=sz+'px';
      f.style.left=(Math.random()*100).toFixed(2)+'%';f.style.opacity=(Math.random()*.5+.25).toFixed(2);
      f.style.setProperty('--drift',((Math.random()*80)-40).toFixed(0)+'px');
      f.style.animationDuration=(Math.random()*10+12).toFixed(1)+'s';f.style.animationDelay=(-Math.random()*20).toFixed(1)+'s';
      box.appendChild(f);}
  }

  // Opener video fallback
  var v=document.querySelector('.opener'),fb=document.querySelector('.opener-fallback');
  if(v&&fb){var useFb=function(){v.style.display='none';fb.hidden=false;};
    var src=v.querySelector('source');if(src)src.addEventListener('error',useFb);
    var p=v.play&&v.play();if(p&&p.catch)p.catch(function(){});}

  // Consultation forms
  var params=new URLSearchParams(location.search);
  var fallback='Please call or text <a href="tel:+17472898808" style="color:inherit">(747) 289-8808</a>.';
  Array.prototype.forEach.call(document.querySelectorAll('.cform'),function(f){
    var msg=f.querySelector('.cform-msg'),b=f.querySelector('button'),sel=f.querySelector('select'),ta=f.querySelector('textarea'),pg=f.querySelector('input[name="Page"]');
    if(pg)pg.value=location.pathname;
    var key=params.get('interest');
    if(key&&sel){Array.prototype.forEach.call(sel.options,function(o){if(o.getAttribute('data-key')===key)o.selected=true;});}
    var piece=params.get('piece');if(piece&&ta&&!ta.value)ta.value="I'm interested in the "+piece+". ";
    function show(cls,html){msg.className='cform-msg'+(cls?' '+cls:'');msg.innerHTML=html;msg.scrollIntoView({block:'nearest',behavior:'smooth'});}
    if(!window.fetch)return;
    f.addEventListener('submit',function(e){e.preventDefault();
      b.disabled=true;b.textContent='Sending...';show('','Sending your request...');
      fetch('https://formsubmit.co/ajax/jmoon1167@gmail.com',{method:'POST',headers:{'Accept':'application/json'},body:new FormData(f)})
      .then(function(r){return r.json().catch(function(){return {};}).then(function(d){return {ok:r.ok,d:d};});})
      .then(function(res){if(res.ok&&String(res.d.success)!=='false'){f.reset();if(pg)pg.value=location.pathname;show('ok','Thank you. We received your request and will reach out soon.');}
        else{show('err','That did not go through. '+fallback);}})
      .catch(function(){show('err','That did not go through. '+fallback);})
      .then(function(){b.disabled=false;b.textContent='Send request';});});
  });
})();
