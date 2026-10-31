#!/usr/bin/env python3
"""Builds the JS Jewelry site pages into public/.

Edit content here, then run:  python3 src/build.py
Shared header, mobile menu, banner and footer are defined once below.
"""
import os

ROOT = os.path.join(os.path.dirname(__file__), "..", "public")
SITE = "https://jsjewelry.online"
PHONE_TEL = "+17472898808"
PHONE = "(747) 289-8808"
EMAIL = "jmoon1167@gmail.com"
IG = "https://www.instagram.com/jsjewelryoc/"
OG_DEFAULT = "/media/holiday-opener-poster.jpg"

NAV = [
    ("/holiday/", "Holiday Set"),
    ("/engagement/", "Engagement"),
    ("/shop/", "Ready to Ship"),
    ("/custom/", "Custom"),
    ("/about/", "About"),
]


def img(name, alt, w, h, cls="", lazy=True):
    c = f' class="{cls}"' if cls else ""
    l = ' loading="lazy" decoding="async"' if lazy else ""
    return f'<img{c}{l} src="/img/{name}" width="{w}" height="{h}" alt="{alt}">'


def head(title, desc, path, og=OG_DEFAULT):
    url = SITE + path
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{url}">
<meta name="theme-color" content="#000000">
<link rel="icon" type="image/png" href="/favicon.png">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<meta property="og:type" content="website">
<meta property="og:site_name" content="JS Jewelry">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE}{og}">
<meta name="twitter:card" content="summary_large_image">
<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"JewelryStore","name":"JS Jewelry","url":"{SITE}/","image":"{SITE}{OG_DEFAULT}","logo":"{SITE}/icon-512.png","telephone":"+1-747-289-8808","email":"{EMAIL}","address":{{"@type":"PostalAddress","streetAddress":"9200 Bolsa Ave, Asian Garden Mall","addressLocality":"Westminster","addressRegion":"CA","postalCode":"92683","addressCountry":"US"}},"sameAs":["{IG}"],"priceRange":"$$"}}
</script>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;1,300&family=Jost:wght@300;400&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/css/site.css">
</head>
<body>
"""


def header(active):
    def cur(href):
        return ' aria-current="page"' if href == active else ""
    links = "\n".join(
        f'      <li><a class="link{" on" if href == active else ""}" href="{href}"{cur(href)}>{label}</a></li>'
        for href, label in NAV
    )
    mlinks = "\n".join(f'    <a href="{href}"{cur(href)}>{label}</a>' for href, label in NAV)
    return f"""<a class="holiday-bar" href="/holiday/"><b>Holiday Engagement Set</b> · 3 rings, one price: $2,800 · <span class="go">See the offer →</span></a>

<header>
  <div class="wrap nav">
    <a class="brand" href="/" aria-label="JS Jewelry home">
      <img class="brand-mark" src="/img/logo-mark.png" width="320" height="243" alt="">
      <span class="brand-word">Jewelry</span>
    </a>
    <ul>
{links}
    </ul>
    <div class="nav-r">
      <a class="link" href="/about/#visit">Visit</a>
      <button class="menu-btn" type="button" aria-expanded="false" aria-controls="mnav" aria-label="Open menu"><span></span><span></span></button>
    </div>
  </div>
  <nav class="mnav" id="mnav" hidden>
    <a href="/">Home</a>
{mlinks}
    <div class="mnav-foot">
      <a class="btn" href="/about/#consult">Book a consultation</a>
      <a href="tel:{PHONE_TEL}">{PHONE}</a>
    </div>
  </nav>
</header>

<main>
"""


FOOTER = f"""</main>

<footer>
  <div class="wrap">
    <div class="foot">
      <div>
        <img class="logo-full" loading="lazy" src="/img/logo-full.png" width="640" height="573" alt="JS Jewelry">
        <p style="color:#96928A;font-size:14px;max-width:34ch;margin-top:20px">Custom fine jewelry and diamond setting, made in Orange County, California. Shipping anywhere in the U.S. and worldwide.</p>
        <ul style="margin-top:22px">
          <li><a href="tel:{PHONE_TEL}">{PHONE}</a></li>
          <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
          <li><a href="{IG}" target="_blank" rel="noopener">@jsjewelryoc</a></li>
        </ul>
      </div>
      <div>
        <h4 class="mark">Work</h4>
        <ul>
          <li><a href="/holiday/">Holiday Engagement Set</a></li>
          <li><a href="/engagement/">Engagement &amp; bands</a></li>
          <li><a href="/shop/">Ready to ship</a></li>
          <li><a href="/custom/">Custom work</a></li>
        </ul>
      </div>
      <div>
        <h4 class="mark">Info</h4>
        <ul>
          <li><a href="/about/#story">Our story</a></li>
          <li><a href="/custom/#commission">How commissions work</a></li>
          <li><a href="/about/#consult">Book a consultation</a></li>
          <li><a href="/about/#shipping">Shipping</a></li>
          <li><a href="/about/#visit">Visit the store</a></li>
        </ul>
      </div>
    </div>
    <div class="foot-btm">
      <span class="mark">© 2026 JS Jewelry</span>
      <span class="mark">jsjewelry.online</span>
    </div>
  </div>
</footer>

<script src="/js/site.js" defer></script>
</body>
</html>
"""

# ---------------------------------------------------------------- sections

RINGS_SVG = """<svg viewBox="0 0 520 360" role="img" aria-label="Three interlocking gold rings">
            <defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#8A6421"/><stop offset=".35" stop-color="#D9B45F"/><stop offset=".55" stop-color="#F7E7BE"/><stop offset=".8" stop-color="#C99A3E"/><stop offset="1" stop-color="#8A6421"/></linearGradient></defs>
            <g fill="none" stroke="url(#g)"><ellipse cx="170" cy="215" rx="108" ry="108" stroke-width="7"/><ellipse cx="290" cy="215" rx="100" ry="100" stroke-width="3"/><ellipse cx="380" cy="215" rx="92" ry="92" stroke-width="12"/><path d="M150 112 L170 84 L190 112" stroke-width="3"/></g>
            <g transform="translate(170 70)"><polygon points="0,-30 22,-12 0,22 -22,-12" fill="none" stroke="url(#g)" stroke-width="2"/></g>
          </svg>"""


def opener(caption=True):
    cap = '<p class="illus mark">Rings shown for illustration</p>' if caption else ""
    return f"""<div class="set-art">
        <video class="opener" autoplay muted loop playsinline preload="auto" poster="/media/holiday-opener-poster.jpg" aria-label="Three gold rings turning in the light: oval halo engagement ring, matching pavé band, and men's band">
          <source src="/media/holiday-opener.mp4" type="video/mp4">
        </video>
        <div class="opener-fallback" hidden>{RINGS_SVG}</div>
        {cap}
      </div>"""


SPECS = """<ul>
          <li><span class="mark">Her ring</span><span>2&nbsp;ct lab-grown diamond center, D color, VVS clarity. Solitaire, halo, 3/4 eternity, or any combination.</span></li>
          <li><span class="mark">Her band</span><span>Matching wedding band, up to 2&nbsp;mm.</span></li>
          <li><span class="mark">His band</span><span>5&nbsp;mm men's wedding band.</span></li>
          <li><span class="mark">Metal</span><span>14K gold in yellow, white, or rose.</span></li>
        </ul>
        <p class="fine">Same price for any style or combination. Want a bigger center stone? Add $300 per carat, prorated.</p>"""


def holiday_block(full, h="h2"):
    if full:
        body = SPECS + f"""
        <div class="cta" style="margin-top:34px">
          <a class="btn" href="#consult">Book your consultation</a>
          <a class="btn-plain" href="tel:{PHONE_TEL}">Call or text {PHONE}</a>
        </div>"""
    else:
        body = f"""<p class="fine" style="margin-top:22px;max-width:44ch">Engagement ring with a 2&nbsp;ct lab-grown center, her matching band and his band, in 14K gold of your choice. Any style, same price.</p>
        <div class="cta" style="margin-top:30px">
          <a class="btn" href="/holiday/">See the set</a>
          <a class="btn-plain" href="/holiday/#consult">Book a consultation</a>
        </div>"""
    return f"""
  <section id="holiday" class="band snow-wrap">
    <div class="snow" aria-hidden="true"></div>
    <div class="wrap set">
      {opener()}
      <div>
        <span class="mark">Holiday 2026 · Limited offer</span>
        <{h} class="h2" style="margin-top:16px">The Holiday <em>Engagement Set</em></{h}>
        <div class="price-big gold-text">$2,800</div>
        <p class="tag">Three rings. One price. Any style.</p>
        {body}
      </div>
    </div>
  </section>
"""


def page_head(eyebrow, title_html, lede):
    return f"""
  <section class="phead">
    <div class="wrap">
      <div class="eyebrow"><span class="bar"></span><span class="mark">{eyebrow}</span></div>
      <h1>{title_html}</h1>
      <p class="lede">{lede}</p>
    </div>
  </section>
"""


def piece(name, alt, title, marks, price=None, note=None, href=None, w=760, h=950, ask=False):
    tag = "a" if href else "div"
    hr = f' href="{href}"' if href else ""
    hall = '<span class="dot"></span>'.join(f'<span class="mark">{m}</span>' for m in marks)
    stock = '<div class="stock"><span class="pip"></span><span class="mark">In stock</span></div>' if price else ""
    pr = f'<div class="price">{price}</div>' if price else ""
    nt = f'<p class="note">{note}</p>' if note else ""
    ak = ""
    if ask:
        from urllib.parse import quote
        ak = f'<a class="btn-plain ask" href="/about/?interest=shop&amp;piece={quote(title)}#consult">Ask about this piece</a>'
    return f"""        <{tag} class="piece"{hr}>
          <div class="shot">{img(name, alt, w, h)}</div>
          {stock}
          <h3>{title}</h3>
          <div class="hallmark">{hall}</div>
          {pr}{nt}{ak}
        </{tag}>"""


SHOP_ITEMS = [
    ("skull-ring.jpg", "Sterling silver skull ring with scrollwork shoulders", "Carved skull ring", ["Sterling silver", "Hand carved", "Oxidized finish"], "$250"),
    ("cross-huggies.jpg", "Gold huggie hoop earrings with lab diamond cross drops", "Cross huggie earrings", ["14K gold", "Lab diamonds", "Huggie hoop"], "$500"),
    ("four-marquise-pendant.jpg", "Pendant of four marquise lab diamonds on a fine chain", "Four-marquise pendant", ["14K gold", "Lab diamonds", "Four marquise"], "$700"),
    ("oval-eternity-band.jpg", "Eternity band set all the way around with oval lab diamonds", "Oval eternity band", ["14K gold", "Lab diamonds", "Oval cut"], "$1,500"),
    ("emerald-halo-ring.jpg", "Emerald-cut lab diamond with a halo and pavé shoulders", "Emerald halo engagement ring", ["14K gold", "Lab diamonds", "Halo setting"], "$2,000"),
    ("tennis-bracelet.jpg", "Gold tennis bracelet set with round lab diamonds", "Diamond tennis bracelet", ["14K gold", "Lab diamonds", "Box clasp"], "$3,500"),
]

MTO = [
    ("oval-marquise-ring.jpg", "Oval-cut diamond with marquise and round accent stones", "Oval with marquise accents", ["Oval cut", "Marquise accents", "Pavé band"], "Marquise and round accents cut to sit flush against the center stone."),
    ("radiant-baguette-ring.jpg", "Radiant-cut diamond on a baguette eternity band", "Radiant on a baguette band", ["Radiant cut", "Baguette eternity", "White gold"], "Baguettes all the way around, not just the shoulders."),
    ("emerald-solitaire.jpg", "Emerald-cut diamond solitaire in a yellow gold setting", "Emerald solitaire", ["Emerald cut", "Yellow gold", "Cathedral set"], "Cathedral shoulders lift the stone clear of the band."),
]

STEPS = """
  <section id="commission">
    <div class="wrap">
      <div class="sec-head"><h2>How a commission <em>works</em></h2></div>
      <div class="hair"></div>
      <div class="steps">
        <div class="step">
          <div class="num gold-text">01</div>
          <h3>Tell us what you're picturing</h3>
          <p>A screenshot, a sketch, a stone you already own, or a heirloom you want reset. Rough is fine. Most people start with rough.</p>
        </div>
        <div class="step">
          <div class="num gold-text">02</div>
          <h3>We quote the stone and the setting</h3>
          <p>You see the diamond specs and the metal cost separately, so you know exactly what you're paying for before anything is cast.</p>
        </div>
        <div class="step">
          <div class="num gold-text">03</div>
          <h3>Set, finished, and photographed</h3>
          <p>Four to six weeks for most pieces. You get the shots of your piece before it ships. They're yours to keep.</p>
        </div>
      </div>
      <div class="cta" style="margin-top:48px"><a class="btn" href="/about/?interest=custom#consult">Start your commission</a></div>
    </div>
  </section>
"""

DIAMONDS = """
  <section class="band">
    <div class="wrap story">
      <div>
        <span class="mark">How we choose diamonds</span>
        <h2 style="margin-top:16px">Fire and <em>brilliance</em>, every stone</h2>
      </div>
      <div class="story-body">
        <p>We choose every diamond for the balance of fire and brilliance, because cut and proportion matter as much as color and clarity. That goes for the center stone and for the smallest accent in the band.</p>
        <p>Lab-grown or natural? Both are real diamonds. We walk you through the difference honestly and let you choose what is right for you. No pressure either way.</p>
      </div>
    </div>
  </section>
"""

STORY = """
  <section id="story">
    <div class="wrap story">
      <div>
        <span class="mark">Our story</span>
        <h2 style="margin-top:16px">Fifteen years at <em>the bench</em></h2>
      </div>
      <div class="story-body">
        <p>JS Jewelry is a small custom studio inside Asian Garden Mall in Westminster. We have spent fifteen years designing and making fine jewelry, and every piece still starts the same way: a conversation about what it should mean to the person wearing it.</p>
        <p>We choose every diamond for the balance of fire and brilliance, because cut and proportion matter as much as color and clarity. That goes for the center stone and for the smallest accent in the band. It is the difference you see from across the room.</p>
        <p>Lab-grown or natural? Both are real diamonds. We walk you through the difference honestly and let you choose what is right for you. No pressure either way.</p>
        <div class="pillars">
          <div><span class="num gold-text">15</span><span class="mark">Years designing</span></div>
          <div><span class="num gold-text">1:1</span><span class="mark">One-on-one design</span></div>
          <div><span class="num gold-text">OC</span><span class="mark">Designed in Orange County</span></div>
        </div>
      </div>
    </div>
  </section>
"""

PHOTOS = f"""
  <section class="band">
    <div class="wrap sign">
      <div>
        <div class="eyebrow"><span class="bar"></span><span class="mark">Why our photos look like this</span></div>
        <h2>We shoot our work <em>ourselves.</em></h2>
        <p>The finished pieces on this site were photographed by us, not pulled from a catalog. Same stones, same setting, same finish that left the bench.</p>
        <p>It's also how we hand a piece over. Before it ships you get a full set of images, lit the way the stone actually behaves.</p>
        <div class="cta"><a class="btn" href="#consult">Talk to us about a piece</a></div>
      </div>
      {img("emerald-ring-box.jpg", "Emerald-cut diamond ring in a presentation box", 820, 820)}
    </div>
  </section>
"""


def consult(preselect="", heading="Tell us about <em>your piece</em>", band=True):
    opts = [
        ("holiday", "Holiday Engagement Set ($2,800)"),
        ("engagement", "Custom engagement ring"),
        ("bands", "Wedding bands"),
        ("shop", "A ready-to-ship piece"),
        ("custom", "Pendant, chain or other custom piece"),
        ("repair", "Reset or repair"),
        ("other", "Something else"),
    ]
    o = "\n".join(
        f'            <option value="{label}" data-key="{key}"{" selected" if key == preselect else ""}>{label}</option>'
        for key, label in opts
    )
    b = ' class="band"' if band else ""
    return f"""
  <section id="consult"{b}>
    <div class="wrap consult">
      <div>
        <span class="mark">Book a consultation</span>
        <h2 style="margin-top:16px">{heading}</h2>
        <p class="consult-lede">Send a few details and we will reach out to set up a time, in the store or over the phone. Prefer to talk now? Call or text <a href="tel:{PHONE_TEL}">{PHONE}</a>.</p>
      </div>
      <form class="cform" action="https://formsubmit.co/{EMAIL}" method="POST">
        <input type="hidden" name="_subject" value="New consultation request · jsjewelry.online">
        <input type="hidden" name="_template" value="table">
        <input type="hidden" name="Page" value="">
        <div class="row2">
          <label><span class="mark">Name</span><input name="Name" required autocomplete="name"></label>
          <label><span class="mark">Phone</span><input name="Phone" type="tel" autocomplete="tel"></label>
        </div>
        <label><span class="mark">Email</span><input name="email" type="email" required autocomplete="email"></label>
        <label><span class="mark">Interested in</span>
          <select name="Interested in">
{o}
          </select>
        </label>
        <label><span class="mark">Tell us more</span><textarea name="Message" rows="4" placeholder="Style ideas, budget, timeline, ring size if you know it"></textarea></label>
        <button class="btn" type="submit">Send request</button>
        <p class="cform-msg" role="status" aria-live="polite"></p>
      </form>
    </div>
  </section>
"""


VISIT = f"""
  <section id="visit">
    <div class="wrap">
      <div class="sec-head"><h2>Come see <em>the bench</em></h2></div>
      <div class="hair"></div>
      <div class="contact-grid">
        <div>
          <span class="mark">Call or text</span>
          <a href="tel:{PHONE_TEL}">{PHONE}</a>
        </div>
        <div>
          <span class="mark">Email</span>
          <a href="mailto:{EMAIL}">{EMAIL}</a>
        </div>
        <div>
          <span class="mark">Instagram</span>
          <a href="{IG}" target="_blank" rel="noopener">@jsjewelryoc</a>
        </div>
        <div>
          <span class="mark">Visit the store</span>
          <address>Asian Garden Mall<br>9200 Bolsa Ave<br>Westminster, CA 92683</address>
          <a class="map" href="https://maps.google.com/?q=Asian+Garden+Mall+9200+Bolsa+Ave+Westminster+CA+92683" target="_blank" rel="noopener">Get directions</a>
        </div>
      </div>
    </div>
  </section>
"""


SHIPPING = """
  <section id="shipping" class="ship">
    <div class="wrap">
      <div class="ship-grid">
        <div>
          <span class="mark">Shipping</span>
          <h2 style="margin-top:14px">Delivered <em>anywhere</em></h2>
        </div>
        <div class="ship-item">
          <span class="mark">Across the U.S.</span>
          <p>We ship anywhere in the United States, typically by next-day air, as soon as your piece is in stock or finished.</p>
        </div>
        <div class="ship-item">
          <span class="mark">Worldwide</span>
          <p>We ship internationally too. Ask us for timing and rates to your country.</p>
        </div>
      </div>
    </div>
  </section>
"""


def cta_band(title_html, text, href, label):
    return f"""
  <section class="band cta-band">
    <div class="wrap">
      <h2>{title_html}</h2>
      <p>{text}</p>
      <div class="cta" style="justify-content:center"><a class="btn" href="{href}">{label}</a><a class="btn-plain" href="tel:{PHONE_TEL}">Call or text {PHONE}</a></div>
    </div>
  </section>
"""


# ---------------------------------------------------------------- pages

def home():
    tiles = [
        ("/engagement/", "emerald-solitaire.jpg", "Emerald-cut diamond solitaire in a yellow gold setting", "Engagement &amp; bands", "Solitaires, halos, eternity bands and matching sets."),
        ("/shop/", "cross-huggies.jpg", "Gold huggie hoop earrings with lab diamond cross drops", "Ready to ship", "Finished pieces in the case today, priced and ready."),
        ("/custom/", "figure-pendant.jpg", "Solid gold figure pendant with pavé diamond detail", "Custom work", "Pendants, rosaries and one-of-one pieces built to order."),
    ]
    t = "\n".join(
        f"""        <a class="piece tile" href="{href}">
          <div class="shot">{img(n, alt, 760 if 'figure' not in n else 900, 950 if 'figure' not in n else 1200)}</div>
          <h3>{title} <span class="arrow">→</span></h3>
          <p class="note">{note}</p>
        </a>"""
        for href, n, alt, title, note in tiles
    )
    body = holiday_block(full=False) + f"""
  <div class="wrap">
    <div class="hero">
      <div class="rise">
        <div class="eyebrow"><span class="bar"></span><span class="mark">Custom fine jewelry · Orange County</span></div>
        <h1>Finished pieces,<br>and pieces that<br><em>don't exist yet.</em></h1>
        <p class="lede">A small case of work that's ready to ship, and a bench that builds the rest to order. Every stone chosen for fire and brilliance.</p>
        <div class="cta">
          <a class="btn" href="/shop/">Shop ready to ship</a>
          <a class="btn-plain" href="/custom/">Start a commission</a>
        </div>
      </div>
      <div class="shot hero-shot rise d">
        {img("cushion-hidden-halo.jpg", "Cushion-cut diamond ring with a hidden halo and pavé band", 1000, 1250, lazy=False)}
      </div>
    </div>
  </div>

  <section class="band">
    <div class="wrap">
      <div class="sec-head"><h2>Find <em>your piece</em></h2></div>
      <div class="hair"></div>
      <div class="grid3">
{t}
      </div>
    </div>
  </section>

  <section>
    <div class="wrap story">
      <div>
        <span class="mark">Our story</span>
        <h2 style="margin-top:16px">Fifteen years at <em>the bench</em></h2>
      </div>
      <div class="story-body">
        <p>A small custom studio inside Asian Garden Mall in Westminster. Every piece starts with a conversation about what it should mean to the person wearing it, and every diamond is chosen for the balance of fire and brilliance, down to the smallest accent.</p>
        <div class="cta"><a class="btn-plain" href="/about/">Read our story</a></div>
      </div>
    </div>
  </section>
""" + VISIT.replace('<section id="visit">', '<section id="visit" class="band">')
    return (head("JS Jewelry · Custom fine jewelry, Orange County",
                 "Custom engagement rings, wedding bands and fine jewelry at Asian Garden Mall in Westminster, CA. Holiday Engagement Set: three rings for $2,800.", "/")
            + header("/") + body + FOOTER)


def holiday():
    steps = """
  <section>
    <div class="wrap">
      <div class="sec-head"><h2>Make it <em>yours</em></h2></div>
      <div class="hair"></div>
      <div class="steps">
        <div class="step"><div class="num gold-text">01</div><h3>Pick your style</h3><p>Solitaire, halo, 3/4 eternity, or any combination. The price stays $2,800 whichever you choose.</p></div>
        <div class="step"><div class="num gold-text">02</div><h3>Pick your gold</h3><p>14K yellow, white, or rose gold, matched across all three rings.</p></div>
        <div class="step"><div class="num gold-text">03</div><h3>Size your center</h3><p>A 2&nbsp;ct lab-grown center, D color, VVS clarity. Want more? Add $300 per carat, prorated.</p></div>
      </div>
    </div>
  </section>
"""
    body = holiday_block(full=True, h="h1") + steps + SHIPPING + DIAMONDS + consult("holiday", "Design your <em>set</em>", band=False)
    return (head("Holiday Engagement Set · 3 rings for $2,800 · JS Jewelry",
                 "Engagement ring with a 2 ct lab-grown center (D, VVS), her matching band and his 5 mm band in 14K gold. Any style, one price: $2,800.", "/holiday/")
            + header("/holiday/") + body + FOOTER)


def engagement():
    items = "\n".join([
        piece("emerald-halo-ring.jpg", SHOP_ITEMS[4][1], "Emerald halo engagement ring", ["14K gold", "Lab diamonds", "Halo setting"], price="$2,000", ask=True),
        piece("oval-eternity-band.jpg", SHOP_ITEMS[3][1], "Oval eternity band", ["14K gold", "Lab diamonds", "Oval cut"], price="$1,500", ask=True),
        piece("cushion-hidden-halo.jpg", "Cushion-cut diamond ring with a hidden halo and pavé band", "Cushion with hidden halo", ["Cushion cut", "Hidden halo", "Pavé band"], note="A halo tucked under the stone, so it only shows from the side.", w=1000, h=1250),
    ] + [piece(n, a, t, m, note=nt) for n, a, t, m, nt in MTO])
    callout = """
  <section class="band">
    <div class="wrap callout">
      <div>
        <span class="mark">Holiday 2026</span>
        <h2 style="margin-top:12px">Ring and both bands, <span class="gold-text">$2,800</span></h2>
        <p class="fine" style="margin-top:12px">2&nbsp;ct lab-grown center, D color, VVS clarity, any style, 14K gold of your choice.</p>
      </div>
      <a class="btn" href="/holiday/">See the Holiday Set</a>
    </div>
  </section>
"""
    body = (page_head("Engagement rings &amp; wedding bands", "Rings made for <em>one person.</em>",
                      "Solitaires, halos, hidden halos and eternity bands in 14K gold, with every diamond chosen for fire and brilliance. Start from a piece below, or from an idea of your own.")
            + callout + f"""
  <section>
    <div class="wrap">
      <div class="sec-head"><h2>Rings we've <em>made</em></h2><span class="mark">In stock pieces are priced</span></div>
      <div class="hair"></div>
      <div class="grid3">
{items}
      </div>
    </div>
  </section>
""" + SHIPPING + DIAMONDS + cta_band("Start with a <em>conversation</em>", "Bring a screenshot, a sketch, or just a feeling. We'll quote the stone and the setting separately so you know exactly what you're paying for.", "/about/?interest=engagement#consult", "Book a consultation"))
    return (head("Engagement Rings &amp; Wedding Bands · JS Jewelry, Orange County",
                 "Custom engagement rings and wedding bands in 14K gold, designed in Orange County. Solitaires, halos, hidden halos and eternity bands. Lab-grown or natural.", "/engagement/")
            + header("/engagement/") + body + FOOTER)


def shop():
    items = "\n".join(piece(n, a, t, m, price=p, ask=True) for n, a, t, m, p in SHOP_ITEMS)
    body = (page_head("Ready to ship · In hand today", "Finished, and <em>ready.</em>",
                      f"Pieces in the case right now. To buy one, tap “Ask about this piece,” call or text {PHONE}, or come see it at the store. In-stock pieces ship next-day air anywhere in the U.S.")
            + f"""
  <section style="padding-top:24px">
    <div class="wrap">
      <div class="hair"></div>
      <div class="grid3">
{items}
      </div>
    </div>
  </section>
""" + SHIPPING + cta_band("Want something <em>like it?</em>", "Any piece here can be the starting point for a custom version: a different stone, metal, or size.", "/custom/", "See custom work"))
    return (head("Ready to Ship · Fine Jewelry in Stock · JS Jewelry",
                 "Finished 14K gold and lab diamond jewelry in stock at JS Jewelry, Westminster: earrings, pendants, eternity bands, engagement rings and tennis bracelets.", "/shop/")
            + header("/shop/") + body + FOOTER)


def custom():
    items = "\n".join(piece(n, a, t, m, note=nt, href="/about/?interest=custom#consult") for n, a, t, m, nt in MTO)
    body = (page_head("Custom work · Made to order", "Pieces that <em>don't exist yet.</em>",
                      "Engagement rings, pendants, rosaries and one-of-one pieces, modeled and built to order from your idea.")
            + f"""
  <section style="padding-top:24px">
    <div class="wrap">
      <div class="sec-head"><h2>Made <em>to order</em></h2></div>
      <div class="hair"></div>
      <div class="grid3">
{items}
      </div>
      <div class="sec-head" id="beyond-rings" style="margin-top:88px"><h2>Not everything is a <em>ring</em></h2></div>
      <div class="hair"></div>
      <div class="two">
        <a class="piece" href="/about/?interest=custom#consult">
          <div class="shot">{img("figure-pendant.jpg", "Solid gold figure pendant with pavé diamond detail", 900, 1200)}</div>
          <div class="cap"><h3>Figure pendant, solid gold</h3><p>Modeled, cast, and hand set from a customer's reference.</p></div>
        </a>
        <a class="piece" href="/about/?interest=custom#consult">
          <div class="shot">{img("diamond-rosary.jpg", "Gold rosary with pavé diamond beads, medallion and cross", 900, 1200)}</div>
          <div class="cap"><h3>Diamond rosary</h3><p>Alternating polished and pavé beads, enamel medallion, fully set cross.</p></div>
        </a>
      </div>
    </div>
  </section>
""" + STEPS.replace('<section id="commission">', '<section id="commission" class="band">') + SHIPPING)
    return (head("Custom Jewelry · Made to Order in Orange County · JS Jewelry",
                 "Custom engagement rings, pendants, rosaries and one-of-one fine jewelry, designed with you and built to order. Asian Garden Mall, Westminster, CA.", "/custom/")
            + header("/custom/") + body + FOOTER)


def about():
    body = STORY.replace('<section id="story">', '<section id="story" style="padding-top:88px">').replace('<h2 style="margin-top:16px">', '<h1 class="h2" style="margin-top:16px">', 1).replace("the bench</em></h2>", "the bench</em></h1>", 1) + PHOTOS + consult() + SHIPPING + VISIT
    return (head("About JS Jewelry · Visit Us at Asian Garden Mall, Westminster",
                 "Fifteen years designing fine jewelry. Visit JS Jewelry at Asian Garden Mall, 9200 Bolsa Ave, Westminster, CA, or book a consultation.", "/about/")
            + header("/about/") + body + FOOTER)


def notfound():
    body = page_head("Page not found", "This piece <em>isn't here.</em>",
                     "The page you were looking for has moved. Try one of these instead.") + """
  <section style="padding-top:0">
    <div class="wrap"><div class="cta"><a class="btn" href="/">Back to home</a><a class="btn-plain" href="/holiday/">Holiday Engagement Set</a><a class="btn-plain" href="/shop/">Ready to ship</a></div></div>
  </section>
"""
    return head("Page not found · JS Jewelry", "JS Jewelry, custom fine jewelry in Orange County.", "/404") + header("") + body + FOOTER


PAGES = {
    "404.html": notfound,
    "index.html": home,
    "holiday/index.html": holiday,
    "engagement/index.html": engagement,
    "shop/index.html": shop,
    "custom/index.html": custom,
    "about/index.html": about,
}

if __name__ == "__main__":
    for path, fn in PAGES.items():
        out = os.path.join(ROOT, path)
        os.makedirs(os.path.dirname(out), exist_ok=True)
        with open(out, "w") as f:
            f.write(fn())
        print("built", path)
