"""Builds the BEST landing page (corporate first + flights + holiday packages) from template.html.
  divi-snippet.html               lightweight (upload images, replace "assets/"); optional AI images auto-appear if uploaded
  divi-snippet-with-images.html   images embedded (base64): paste straight into Divi
  index.html                      local preview with CF7 stub. Try index.html?s=agent / ?s=flights / ?s=packages / ?s=corporate
Base CSS is reused from ../corporate-landing/divi-snippet.html so all pages share one design."""
import base64, pathlib, re
d = pathlib.Path(__file__).parent
corp = (d.parent / 'corporate-landing' / 'divi-snippet.html').read_text()
css = re.search(r'<style>\n(.*?)\n</style>', corp, re.S).group(1)

ICON_SAFARI = '<svg viewBox="0 0 24 24"><path d="M3 20L12 4l9 16z"/><path d="M12 4v16M9 20l3-5 3 5"/></svg>'
ICON_STAR = '<svg viewBox="0 0 24 24"><path d="M12 3l2.600 5.600 6 .8-4.400 4.200 1.100 6L12 16.800 6.700 19.600l1.100-6L3.400 9.400l6-.8z"/></svg>'
ICON_SUN = '<svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="4"/><path d="M12 2v3M12 19v3M2 12h3M19 12h3M5 5l2 2M17 17l2 2M19 5l-2 2M7 17l-2 2"/></svg>'
ICON_GLOBE = '<svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c3 3 3 15 0 18M12 3c-3 3-3 15 0 18"/></svg>'
ICON_MSG = '<svg viewBox="0 0 24 24"><path d="M4 5h16v11H9l-5 4z"/></svg>'

# every card: title, one location line, exactly two short bullets, one price
CARDS = {
 'taita':    dict(img='taita-hills', alt='Pool and gardens at Taita Hills Safari Resort', title='Taita Hills Safari Resort', dur='3 days, 2 nights &middot; Taita Hills', bl=['SGR 1st class travel','Pool, gardens and game viewing'], price='KES 40,950', unit='per person sharing', pkg='Taita Hills Safari Resort'),
 'soroi':    dict(img='soroi-amboseli', alt='Infinity pool and deck at a safari lodge in Amboseli', title='Soroi Amboseli', dur='Full board &middot; Amboseli', bl=['Meals, drinks, wifi and minibar','Park fees and game drives extra'], price='KES 33,500', unit='from, per person sharing', pkg='Soroi Amboseli'),
 'kitirua':  dict(img='kitirua-lodge', alt='Thatched lodge lounge with woven lamps at Kitirua Plains Lodge', title='Kitirua Plains Lodge', dur='Amboseli National Park', bl=['Authentic Maasai cultural experiences','Cultural visits and storytelling'], price='USD 350', unit='per person sharing', pkg='Kitirua Plains Lodge, Amboseli'),
 'loisaba':  dict(img='loisaba-lodo-springs', alt='Tented suite with valley views at Loisaba Lodo Springs', title='Loisaba Lodo Springs', dur='3 days, 2 nights &middot; Laikipia', bl=['All meals included','Self-drive, conservancy fees extra'], price='KES 99,000', unit='per person sharing', pkg='Loisaba Lodo Springs'),
 'elsas':    dict(img='elsas-kopje-meru', alt="Sunset dinner deck at Elsa's Kopje, Meru", title="Elsa's Kopje, Meru", dur='3 days, 2 nights &middot; Meru', bl=['All meals included','Self-drive, conservancy fees extra'], price='KES 106,000', unit='per person sharing', pkg="Elsa's Kopje, Meru"),
 'suyian':   dict(img='suyian-lodge', alt='Suyian Lodge terraces and fire pit at sunset in Laikipia', title='Suyian Lodge', dur='Private conservancy &middot; Laikipia', bl=['Luxury safari away from the crowds','Self-drive'], price='USD 1,300', unit='per person sharing', pkg='Suyian Lodge, Laikipia'),
 'jw':       dict(img='jw-rhino-camp', alt='Safari camp pool and tented lounge at Mount Kenya Rhino Reserve', title='JW Marriott Rhino Reserve', dur='Mount Kenya &middot; Full board', bl=['Luxury tented suite','Self-drive, residents\' rate'], price='KES 68,000', unit='per person sharing', pkg='JW Marriott Mount Kenya Rhino Reserve Safari Camp'),
 'ritz':     dict(img='ritz-mara', alt='Pool deck at sunset beside the Mara river at The Ritz-Carlton Masai Mara', title='The Ritz-Carlton, Masai Mara', dur='5-star camp &middot; Maasai Mara', bl=['Stay 3 nights, pay for 2','Self-drive or flying package'], price='USD 1,950', unit='self-drive, per person sharing', pkg='The Ritz-Carlton, Masai Mara'),
 'sarova':   dict(img='sarova-whitesands', alt='Pool at Sarova Whitesands Beach Resort, Mombasa', title='Sarova Whitesands', dur='3 days, 2 nights &middot; Mombasa', bl=['Half board and airport transfers','Return tickets to Mombasa'], price='KES 50,600', unit='per person sharing', pkg='Sarova Whitesands, Mombasa'),
 'zanzibar': dict(img='zanzibar', alt='Resort pool and palm trees in Zanzibar', title='Zanzibar, Lux* Marijani', dur='5 days, 4 nights &middot; Zanzibar', bl=['All inclusive stay','Return flights and transfers'], price='USD 2,535', unit='from, per person', pkg='Zanzibar, Lux* Marijani (5 days 4 nights)'),
 'mauritius':dict(img='mauritius', alt='Mauritius mountains, palms and pool', title='Mauritius', dur='4 nights &middot; 4-star hotel', bl=['Flights, transfers, dinner and breakfast','North and south island tours'], price=None, unit="Ask for today's rate", pkg='Mauritius tour'),
 'seychelles':dict(img='seychelles', alt='Seychelles island resorts and beaches', title='Seychelles', dur='5 nights, 6 days &middot; Seychelles', bl=['Island resorts and white beaches','Stay and flights on request'], price=None, unit="Ask for today's rate", pkg='Seychelles (5 nights 6 days)'),
 'dubai':    dict(img='dubai', alt='Burj Al Arab in Dubai at sunset', title='Christmas in Dubai', dur='5 nights &middot; 4-star hotel', bl=['Burj Khalifa, dhow dinner, desert safari','Visa processing included'], price='USD 1,539', unit='per person, double sharing', pkg='Christmas in Dubai (5 nights)'),
 'turkey':   dict(img='turkey', alt='Istanbul rooftops and old town in northern Turkey', title='Northern Turkey', dur='8 days, 7 nights &middot; Turkey', bl=['4 to 5 star resorts, daily meals','Flights and transfers included'], price='USD 895', unit='from, per person', pkg='Northern Turkey (8 days 7 nights)'),
}
CATS = [
 dict(icon=ICON_SAFARI, title='Safari Getaways', tag="Short escapes into Kenya's wild", chip='From KES 33,500', items=['taita','soroi','kitirua'], cta=True),
 dict(icon=ICON_STAR, title='Luxury Safari Lodges', tag='Private conservancies and five-star camps', chip='From KES 68,000', items=['loisaba','elsas','suyian','jw','ritz'], cta=False),
 dict(icon=ICON_SUN, title='Beach and Island Escapes', tag='Mombasa, Zanzibar, Mauritius and Seychelles', chip='From KES 50,600', items=['sarova','zanzibar','mauritius','seychelles'], cta=False),
 dict(icon=ICON_GLOBE, title='International City Breaks', tag='Dubai and Turkey, with visa help', chip='From USD 895', items=['dubai','turkey'], cta=True),
]
RETREAT = ['taita', 'sarova', 'loisaba', 'elsas']

def card(c, retreat=False):
    badge = ('<span class="pb">%s</span>' % c['price']) if c['price'] else '<span class="pb">Ask rate</span>'
    ph = ('<div class="ph"><img data-no-lazy="1" data-skip-lazy="" class="skip-lazy" src="assets/%s.webp" alt="%s" width="800" height="600">%s</div>'
          % (c['img'], c['alt'], badge))
    bl = ''.join('<li>%s</li>' % b for b in c['bl'])
    if c['price']:
        pr = '<div class="pr">From<b>%s</b>%s</div>' % (c['price'], c['unit'])
    else:
        pr = '<div class="pr"><b class="ask">%s</b>Final price in your quote</div>' % c['unit']
    need = ' data-need="corporate"' if retreat else ''
    lab = 'Get a group quote' if retreat else 'Get a quote'
    return ('      <article class="pc">%s<div class="bd"><h3>%s</h3><div class="dur">%s</div><ul>%s</ul>%s'
            '<button type="button" class="btn btn-ol sl-pick"%s data-pkg="%s">%s</button></div></article>'
            % (ph, c['title'], c['dur'], bl, pr, need, c['pkg'], lab))

def cta_card():
    return ('      <article class="pc cta"><span class="ic2">%s</span><h3>Not sure which one?</h3>'
            '<p>Tell us your dates and budget. We suggest the best fit.</p>'
            '<button type="button" class="btn btn-am sl-need" data-need="packages">Request a call back</button></article>' % ICON_MSG)

def category(cat):
    cards = [card(CARDS[k]) for k in cat['items']]
    if cat['cta']:
        cards.append(cta_card())
    return ('  <div class="cb"><div class="cb-h"><span class="cb-ic">%s</span><div class="cb-t"><h3>%s</h3><p>%s</p></div>'
            '<span class="cb-chip">%s</span><div class="cb-nav"><button type="button" class="cb-prev" aria-label="Previous">&lsaquo;</button><button type="button" class="cb-next" aria-label="Next">&rsaquo;</button></div></div>'
            '<div class="cb-row">\n%s\n    </div></div>' % (cat['icon'], cat['title'], cat['tag'], cat['chip'], '\n'.join(cards)))

tpl = (d / 'template.html').read_text()
# drop the unused decorative group in the team illustration
tpl = re.sub(r'\n\s*<g class="pf" fill="#ffffff" opacity="\.85"><path d="M610 120[^\n]*</g>', '', tpl)
snip = (tpl.replace('@@CSS@@', css)
           .replace('@@CATEGORIES@@', '\n'.join(category(c) for c in CATS))
           .replace('@@RETREATCARDS@@', '\n'.join(card(CARDS[k], True) for k in RETREAT)))
(d / 'divi-snippet.html').write_text(snip)

def embed(text):
    # optional images: keep (embedded) if the file exists, otherwise drop the tag
    def opt(m):
        tag = m.group(0)
        name = re.search(r'src="assets/([^"]+)"', tag).group(1)
        return tag if (d / 'assets' / name).exists() else ''
    text = re.sub(r'<img [^>]*data-opt[^>]*>', opt, text)
    text = text.replace(' onerror="this.remove()"', '')
    # CSS background urls would embed a second copy: blank them, a small script reuses the hero image instead
    text = re.sub(r"url\('assets/[^']+'\)", 'none', text)
    seen = set()
    PH = 'data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEAAAAALAAAAAABAAEAAAIBRAA7'
    def img(m):
        tag = m.group(0)
        mm = re.search(r'src="assets/([^"]+)"', tag)
        if not mm:
            return tag
        name = mm.group(1)
        key = name.rsplit('.', 1)[0]
        if name in seen:
            return tag.replace(mm.group(0), 'data-ik="%s" src="%s"' % (key, PH))
        seen.add(name)
        data = 'data:image/webp;base64,' + base64.b64encode((d / 'assets' / name).read_bytes()).decode()
        return tag.replace(mm.group(0), 'data-ik="%s" src="%s"' % (key, data))
    text = re.sub(r'<img [^>]*>', img, text)
    reuse = ('<script>\n(function () {\n'
             '  var m = {};\n'
             '  var all = document.querySelectorAll("img[data-ik]");\n'
             '  for (var i = 0; i < all.length; i++) { if (all[i].src.length > 300) { m[all[i].getAttribute("data-ik")] = all[i].src; } }\n'
             '  for (var j = 0; j < all.length; j++) { var k = all[j].getAttribute("data-ik"); if (all[j].src.length < 300) { if (m[k]) { all[j].src = m[k]; } } }\n'
             '  var c = document.querySelector(".sl .cine");\n'
             '  if (c) { if (m["sunrise-balloons"]) { c.style.backgroundImage = "url(" + m["sunrise-balloons"] + ")"; } }\n'
             '})();\n</script>')
    return text + '\n' + reuse
emb = embed(snip)
(d / 'divi-snippet-with-images.html').write_text(emb)

form = '''<div class="wpcf7 no-js" id="wpcf7-f1438-p1096-o1" lang="en-US" dir="ltr" data-wpcf7-id="1438">
<form action="/#wpcf7-f1438-p1096-o1" method="post" class="wpcf7-form init" novalidate="novalidate">
<input type="hidden" name="_wpcf7" value="1438" />
<p><input type="text" name="Name" class="wpcf7-form-control wpcf7-text" value=""></p>
<p><input type="email" name="Email" class="wpcf7-form-control wpcf7-email" value=""></p>
<p><input type="tel" name="Phone" class="wpcf7-form-control wpcf7-tel" value=""></p>
<p><select name="Service" class="wpcf7-form-control wpcf7-select"><option value="">---</option><option value="Flight Booking">Flight Booking</option><option value="Safari &amp; Wildlife Tour">Safari &amp; Wildlife Tour</option><option value="Holiday Package">Holiday Package</option><option value="Visa Assistance">Visa Assistance</option><option value="Hotel Reservation">Hotel Reservation</option><option value="Group Travel">Group Travel</option><option value="Other">Other</option></select></p>
<p><textarea name="Message" class="wpcf7-form-control wpcf7-textarea"></textarea></p>
<p><input class="wpcf7-form-control wpcf7-submit" type="submit" value="Send Message"></p>
</form></div>'''
stub = '''<script>
/* PREVIEW ONLY: imitates CF7 events. Open index.html?stub=invalid to simulate a validation error. */
document.addEventListener('submit', function (e) {
  var f = e.target;
  if (!f.closest || !f.closest('.sl-cf7')) { return; }
  e.preventDefault();
  window.__lastCF7 = Object.fromEntries(new FormData(f).entries());
  var box = f.closest('.wpcf7');
  var invalid = location.search.indexOf('stub=invalid') > -1;
  setTimeout(function () {
    if (invalid) {
      box.dispatchEvent(new CustomEvent('wpcf7invalid', { bubbles: true, detail: { apiResponse: { invalid_fields: [{ field: 'Email', message: 'Invalid' }] } } }));
    } else {
      box.dispatchEvent(new CustomEvent('wpcf7mailsent', { bubbles: true, detail: { contactFormId: 1438 } }));
    }
  }, 200);
});
</script>'''
page = ('<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
        '<title>Best Corporate Travel Management in Nairobi | Spice Travel (preview)</title><style>body{margin:0}</style></head><body>'
        + emb.replace('[contact-form-7 id="1438"]', form) + stub + '</body></html>')
(d / 'index.html').write_text(page)
for tag in ('style', 'script'):
    for m in re.finditer(r'<%s[^>]*>(.*?)</%s>' % (tag, tag), snip, re.S):
        assert '&' not in m.group(1), (tag, re.findall(r'.{20}&.{20}', m.group(1))[:3])
print('built', len(snip)//1024, 'KB light;', len(emb)//1024, 'KB embedded')
