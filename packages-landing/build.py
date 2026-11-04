"""Builds the packages landing page files from template.html.
  divi-snippet.html               lightweight, expects images uploaded to Media Library (replace "assets/")
  divi-snippet-with-images.html   images embedded (base64), paste straight into a Divi Fullwidth Code module
  index.html                      local preview (CF7 form replaced by a stub), images embedded
Base CSS is reused from ../corporate-landing/divi-snippet.html so both pages share one design."""
import base64, pathlib, re
d = pathlib.Path(__file__).parent
corp = (d.parent / 'corporate-landing' / 'divi-snippet.html').read_text()
css = re.search(r'<style>\n(.*?)\n</style>', corp, re.S).group(1)

ICON_TENT = '<svg viewBox="0 0 24 24"><path d="M3 20L12 4l9 16z"/><path d="M12 4v16M9 20l3-5 3 5"/></svg>'
ICON_STAR = '<svg viewBox="0 0 24 24"><path d="M12 3l2.600 5.600 6 .8-4.400 4.200 1.100 6L12 16.800 6.700 19.600l1.100-6L3.400 9.400l6-.8z"/></svg>'
ICON_LEAF = '<svg viewBox="0 0 24 24"><path d="M5 19c0-8 5-14 15-14 0 10-6 15-14 15"/><path d="M5 19c3-5 6-8 10-10"/></svg>'

# cat: space separated tabs (kenya / beach / intl); img None => gradient header with icon
CARDS = [
 dict(cat='kenya', img='taita-hills', alt='Pool and gardens at Taita Hills Safari Resort', badge='Safari', title='Taita Hills Safari Resort', dur='3 days, 2 nights &middot; Taita Hills Sanctuary', bl=['SGR 1st class travel','Pool, gardens and game viewing'], price='KES 40,950', unit='per person sharing', pkg='Taita Hills Safari Resort'),
 dict(cat='kenya', img=None, icon=ICON_TENT, region='Amboseli', badge='Safari', title='Soroi Amboseli', dur='Full board, Amboseli', bl=['Meals, soft drinks, local beers, selected spirits and house wines','Wifi and minibar'], ex='Excludes park fees, transport, game drives and excursions.', price='KES 33,500', unit='from, per person sharing', pkg='Soroi Amboseli'),
 dict(cat='kenya', img=None, icon=ICON_LEAF, region='Amboseli', badge='Safari', title='Kitirua Plains Lodge', dur='Amboseli National Park', bl=['Maasai cultural experiences','Cultural visits and storytelling'], price='USD 350', unit='per person sharing', pkg='Kitirua Plains Lodge, Amboseli'),
 dict(cat='kenya', img='loisaba-lodo-springs', alt='Tented suite with valley views at Loisaba Lodo Springs', badge='Luxury', title='Loisaba Lodo Springs', dur='3 days, 2 nights &middot; Laikipia', bl=['All meals included','Self-drive, conservancy fees extra'], price='KES 99,000', unit='per person sharing', pkg='Loisaba Lodo Springs'),
 dict(cat='kenya', img='elsas-kopje-meru', alt="Sunset dinner deck at Elsa's Kopje, Meru", badge='Luxury', title="Elsa's Kopje, Meru", dur='3 days, 2 nights &middot; Meru National Park', bl=['All meals included','Self-drive, conservancy fees extra'], price='KES 106,000', unit='per person sharing', pkg="Elsa's Kopje, Meru"),
 dict(cat='kenya', img=None, icon=ICON_STAR, region='Mount Kenya', badge='Luxury', title='JW Marriott Mount Kenya Rhino Reserve Safari Camp', dur='Full board, self-drive', bl=['Luxury tented suite','Rhino reserve setting'], price='KES 68,000', unit='per person sharing', pkg='JW Marriott Mount Kenya Rhino Reserve Safari Camp'),
 dict(cat='kenya', img=None, icon=ICON_STAR, region='Laikipia', badge='Luxury', title='Suyian Lodge, Laikipia', dur='Private conservancy', bl=['Self-drive','Luxury conservancy safari experience'], price='USD 1,300', unit='per person sharing', pkg='Suyian Lodge, Laikipia'),
 dict(cat='kenya', img=None, icon=ICON_STAR, region='Maasai Mara', badge='Luxury', title='The Ritz-Carlton, Masai Mara', dur='5-star safari camp', bl=['Self-drive: USD 1,950','Flying package: USD 2,450'], price='USD 1,950', unit='self-drive, per person sharing', pkg='The Ritz-Carlton, Masai Mara'),
 dict(cat='beach', img='sarova-whitesands', alt='Pool at Sarova Whitesands Beach Resort, Mombasa', badge='Beach', title='Sarova Whitesands, Mombasa', dur='3 days, 2 nights &middot; Half board', bl=['Return tickets to Mombasa','Airport transfers (sharing)'], price='KES 50,600', unit='per person sharing', pkg='Sarova Whitesands, Mombasa'),
 dict(cat='intl', img='dubai', alt='Burj Al Arab in Dubai at sunset', badge='Dubai', title='Christmas in Dubai', dur='5 nights &middot; 4-star hotel', bl=['Daily breakfast, return airport transfers','Burj Khalifa, dhow cruise dinner, desert safari','Visa processing included'], price='USD 1,539', unit='per person, double sharing', pkg='Christmas in Dubai (5 nights)'),
 dict(cat='beach intl', img='zanzibar', alt='Resort pool and palm trees in Zanzibar', badge='Zanzibar', title='Zanzibar, Lux* Marijani', dur='5 days, 4 nights', bl=['Return flights and airport transfers','All inclusive'], price='USD 2,535', unit='from, per person', pkg='Zanzibar, Lux* Marijani (5 days 4 nights)'),
 dict(cat='intl', img='turkey', alt='Istanbul rooftops and old town in northern Turkey', badge='Turkey', title='Northern Turkey', dur='8 days, 7 nights', bl=['4 to 5 star resorts','Daily meals, flights and transfers'], price='USD 895', unit='from, per person', pkg='Northern Turkey (8 days 7 nights)'),
 dict(cat='beach intl', img='mauritius', alt='Mauritius mountains, palms and pool', badge='Mauritius', title='Mauritius', dur='4 nights &middot; 4-star hotel', bl=['Airport transfers and return flights','Daily dinner and breakfast','North tour, south tour and Ile aux Cerfs'], price=None, unit='Ask for today\'s rate', pkg='Mauritius tour'),
 dict(cat='beach intl', img='seychelles', alt='Seychelles island resorts and beaches', badge='Seychelles', title='Seychelles', dur='5 nights, 6 days', bl=['Island resorts and beaches','Love-at-first-sight escape'], price=None, unit='Ask for today\'s rate', pkg='Seychelles (5 nights 6 days)'),
]

def card(c):
    if c['img']:
        ph = '<div class="ph"><img src="assets/%s.webp" alt="%s" loading="lazy" width="900" height="675"><span class="cat">%s</span></div>' % (c['img'], c['alt'], c['badge'])
    else:
        ph = '<div class="ph np">%s<span class="l">%s</span><span class="cat">%s</span></div>' % (c['icon'], c['region'], c['badge'])
    bl = ''.join('<li>%s</li>' % b for b in c['bl'])
    ex = '<p class="ex">%s</p>' % c['ex'] if c.get('ex') else ''
    if c['price']:
        pr = '<div class="pr">From<b>%s</b>%s</div>' % (c['price'], c['unit'])
    else:
        pr = '<div class="pr"><b class="ask">%s</b>Final price in your quote</div>' % c['unit']
    return ('    <article class="pc" data-cat="%s">%s<div class="bd"><h3>%s</h3><div class="dur">%s</div><ul>%s</ul>%s%s'
            '<button type="button" class="btn btn-ol sl-pick" data-pkg="%s">Get a quote</button></div></article>'
            % (c['cat'], ph, c['title'], c['dur'], bl, ex, pr, c['pkg']))

tpl = (d / 'template.html').read_text()
snip = tpl.replace('@@CSS@@', css).replace('@@CARDS@@', '\n'.join(card(c) for c in CARDS))
(d / 'divi-snippet.html').write_text(snip)

def embed(text):
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
        '<title>Holiday Packages from Nairobi | Spice Travel (preview)</title><style>body{margin:0}</style></head><body>'
        + emb.replace('[contact-form-7 id="1438"]', form) + stub + '</body></html>')
(d / 'index.html').write_text(page)
for tag in ('style', 'script'):
    for m in re.finditer(r'<%s[^>]*>(.*?)</%s>' % (tag, tag), snip, re.S):
        n = len(re.findall('&', m.group(1)))
        assert n == 0, (tag, n)
print('built', len(snip)//1024, 'KB light;', len(emb)//1024, 'KB embedded')
