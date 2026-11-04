"""Builds the BEST landing page (corporate first + flights + holiday packages) from template.html.
  divi-snippet.html               lightweight (upload images, replace "assets/"); optional AI images auto-appear if uploaded
  divi-snippet-with-images.html   images embedded (base64): paste straight into Divi
  index.html                      local preview with CF7 stub. Try index.html?s=agent / ?s=flights / ?s=packages / ?s=corporate
Base CSS is reused from ../corporate-landing/divi-snippet.html so all pages share one design."""
import base64, pathlib, re
d = pathlib.Path(__file__).parent
corp = (d.parent / 'corporate-landing' / 'divi-snippet.html').read_text()
css = re.search(r'<style>\n(.*?)\n</style>', corp, re.S).group(1)
css = re.sub(r"url\('assets/[^']+'\)", 'none', css)

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

# ---------------- SEO: meta + JSON-LD schema ----------------
import json, html as _h
URL = 'https://spicetravel.co.ke/best-travel-agent-nairobi/'
TITLE = 'Best Corporate Travel Agent in Nairobi | Spice Travel'
DESC = 'IATA-certified corporate travel agent in Nairobi. Corporate travel management, flight booking and holiday packages. Free quote and call back today.'
OGIMG = 'https://spicetravel.co.ke/wp-content/uploads/2026/11/hero-tented-suite.webp'
assert len(TITLE) <= 60, len(TITLE)
assert 120 <= len(DESC) <= 160, len(DESC)

def strip(t):
    t = re.sub(r'<[^>]+>', '', t)
    return _h.unescape(t).replace('\u00a0', ' ').strip()
faq = []
for m in re.finditer(r'<details><summary>(.*?)</summary><p>(.*?)</p></details>', tpl, re.S):
    faq.append({'@type': 'Question', 'name': strip(m.group(1)), 'acceptedAnswer': {'@type': 'Answer', 'text': strip(m.group(2))}})
ORG = 'https://spicetravel.co.ke/#organization'
def svc(name, desc, ident):
    return {'@type': 'Service', '@id': URL + '#' + ident, 'name': name, 'description': desc, 'serviceType': name,
            'provider': {'@id': ORG}, 'areaServed': {'@type': 'City', 'name': 'Nairobi'}}
graph = [
  {'@type': 'WebPage', '@id': URL + '#webpage', 'url': URL, 'name': TITLE, 'description': DESC, 'inLanguage': 'en-KE',
   'isPartOf': {'@id': 'https://spicetravel.co.ke/#website'}, 'about': {'@id': ORG},
   'breadcrumb': {'@id': URL + '#breadcrumb'}, 'primaryImageOfPage': {'@type': 'ImageObject', 'url': OGIMG}},
  {'@type': 'BreadcrumbList', '@id': URL + '#breadcrumb', 'itemListElement': [
      {'@type': 'ListItem', 'position': 1, 'name': 'Home', 'item': 'https://spicetravel.co.ke/'},
      {'@type': 'ListItem', 'position': 2, 'name': 'Corporate Travel Agent in Nairobi', 'item': URL}]},
  {'@type': ['TravelAgency', 'LocalBusiness'], '@id': ORG, 'name': 'Spice Travel Ltd', 'url': 'https://spicetravel.co.ke/',
   'logo': 'https://spicetravel.co.ke/wp-content/uploads/2026/03/Spice-Travel-Monochrome-Logo-1.png',
   'image': OGIMG, 'telephone': '+254740633759', 'email': 'sales@spicetravel.co.ke',
   'description': 'IATA-certified travel agency in Nairobi since 1994: corporate travel management, flight booking, holiday packages, safaris and visa assistance.',
   'foundingDate': '1994',
   'address': {'@type': 'PostalAddress', 'streetAddress': 'The Westwood, Vale Close, Off Ring Road, Parklands, 2nd Floor, Unit D',
               'addressLocality': 'Westlands, Nairobi', 'addressCountry': 'KE'},
   'areaServed': [{'@type': 'City', 'name': 'Nairobi'}, {'@type': 'Country', 'name': 'Kenya'}],
   'openingHoursSpecification': [
       {'@type': 'OpeningHoursSpecification', 'dayOfWeek': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'], 'opens': '08:30', 'closes': '17:30'},
       {'@type': 'OpeningHoursSpecification', 'dayOfWeek': 'Saturday', 'opens': '08:30', 'closes': '13:00'}],
   'sameAs': ['https://web.facebook.com/spicetravellt', 'https://www.instagram.com/spicetravel254/', 'https://www.youtube.com/@SpiceTravelLtd']},
  svc('Corporate travel management', 'Business flights, hotels, conference travel, team retreats and itemised invoicing for companies, NGOs and event teams in Nairobi.', 'corporate'),
  svc('Flight booking', 'Domestic and international flight tickets on any airline for individuals, families and corporate travellers.', 'flights'),
  svc('Holiday and safari packages', 'Kenya safari, beach and international holiday packages from Nairobi, including flights, hotels, transfers and visa help.', 'packages'),
  {'@type': 'FAQPage', '@id': URL + '#faq', 'mainEntity': faq},
]
schema_json = json.dumps({'@context': 'https://schema.org', '@graph': graph}, ensure_ascii=True, indent=1)
assert '&' not in schema_json
schema_tag = '<script type="application/ld+json">\n' + schema_json + '\n</script>'

head_block = (
 '<title>%s</title>\n'
 '<meta name="description" content="%s">\n'
 '<link rel="canonical" href="%s">\n'
 '<meta name="robots" content="noindex, follow">\n'
 '<meta property="og:type" content="website">\n'
 '<meta property="og:locale" content="en_KE">\n'
 '<meta property="og:site_name" content="Spice Travel Ltd">\n'
 '<meta property="og:title" content="%s">\n'
 '<meta property="og:description" content="%s">\n'
 '<meta property="og:url" content="%s">\n'
 '<meta property="og:image" content="%s">\n'
 '<meta name="twitter:card" content="summary_large_image">\n'
 '<meta name="twitter:title" content="%s">\n'
 '<meta name="twitter:description" content="%s">\n'
 '<meta name="twitter:image" content="%s">\n'
) % (TITLE, DESC, URL, TITLE, DESC, URL, OGIMG, TITLE, DESC, OGIMG)
(d / 'seo-head.html').write_text('<!-- Paste into the page head only if you do not use Yoast for these fields (WPCode: page-specific "Site Wide Header"). With Yoast, fill the same values in the Yoast box instead. -->\n' + head_block)
(d / 'schema.jsonld').write_text(schema_json + '\n')

snip = (tpl.replace('@@CSS@@', css).replace('@@SCHEMA@@', schema_tag)
           .replace('@@CATEGORIES@@', '\n'.join(category(c) for c in CATS))
           .replace('@@RETREATCARDS@@', '\n'.join(card(CARDS[k], True) for k in RETREAT)))
(d / 'divi-snippet.html').write_text(snip)

def embed(text):
    # every <img> gets its own inline data URI: no script and no CSS url() is needed for images to show
    def opt(m):
        tag = m.group(0)
        name = re.search(r'src="assets/([^"]+)"', tag).group(1)
        return tag if (d / 'assets' / name).exists() else ''
    text = re.sub(r'<img [^>]*data-opt[^>]*>', opt, text)
    text = text.replace(' onerror="this.remove()"', '')
    def r(m):
        f = d / 'assets' / m.group(1)
        return 'data:image/webp;base64,' + base64.b64encode(f.read_bytes()).decode()
    return re.sub(r"assets/([A-Za-z0-9_\-\.]+)", r, text)
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
        '<title>' + TITLE + '</title><meta name="description" content="' + DESC + '"><meta name="robots" content="noindex, follow"><style>body{margin:0}</style></head><body>'
        + emb.replace('[contact-form-7 id="1438"]', form) + stub + '</body></html>')
(d / 'index.html').write_text(page)
for tag in ('style', 'script'):
    for m in re.finditer(r'<%s[^>]*>(.*?)</%s>' % (tag, tag), snip, re.S):
        assert '&' not in m.group(1), (tag, re.findall(r'.{20}&.{20}', m.group(1))[:3])
print('built', len(snip)//1024, 'KB light;', len(emb)//1024, 'KB embedded')
