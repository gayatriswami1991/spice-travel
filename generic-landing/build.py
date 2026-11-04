"""Builds the generic landing page (flights + packages + corporate) from template.html.
  divi-snippet.html               lightweight (upload images, replace "assets/")
  divi-snippet-with-images.html   images embedded, paste straight into Divi
  index.html                      local preview (CF7 stub). Try index.html?s=corporate / ?s=flights / ?s=packages
Base CSS is reused from ../corporate-landing/divi-snippet.html so all pages share one design."""
import base64, pathlib, re
d = pathlib.Path(__file__).parent
corp = (d.parent / 'corporate-landing' / 'divi-snippet.html').read_text()
css = re.search(r'<style>\n(.*?)\n</style>', corp, re.S).group(1)

CARDS = [
 dict(img='taita-hills', alt='Pool and gardens at Taita Hills Safari Resort', badge='Safari', title='Taita Hills Safari Resort', dur='3 days, 2 nights &middot; Taita Hills Sanctuary', bl=['SGR 1st class travel','Pool, gardens and game viewing'], price='KES 40,950', unit='per person sharing', pkg='Taita Hills Safari Resort'),
 dict(img='sarova-whitesands', alt='Pool at Sarova Whitesands Beach Resort, Mombasa', badge='Beach', title='Sarova Whitesands, Mombasa', dur='3 days, 2 nights &middot; Half board', bl=['Return tickets to Mombasa','Airport transfers (sharing)'], price='KES 50,600', unit='per person sharing', pkg='Sarova Whitesands, Mombasa'),
 dict(img='loisaba-lodo-springs', alt='Tented suite with valley views at Loisaba Lodo Springs', badge='Luxury', title='Loisaba Lodo Springs', dur='3 days, 2 nights &middot; Laikipia', bl=['All meals included','Self-drive, conservancy fees extra'], price='KES 99,000', unit='per person sharing', pkg='Loisaba Lodo Springs'),
 dict(img='dubai', alt='Burj Al Arab in Dubai at sunset', badge='Dubai', title='Christmas in Dubai', dur='5 nights &middot; 4-star hotel', bl=['Daily breakfast, return airport transfers','Burj Khalifa, dhow cruise dinner, desert safari','Visa processing included'], price='USD 1,539', unit='per person, double sharing', pkg='Christmas in Dubai (5 nights)'),
]
def card(c):
    bl = ''.join('<li>%s</li>' % b for b in c['bl'])
    return ('      <article class="pc"><div class="ph"><img src="assets/%s.webp" alt="%s" loading="lazy" width="900" height="675"><span class="cat">%s</span></div>'
            '<div class="bd"><h3>%s</h3><div class="dur">%s</div><ul>%s</ul><div class="pr">From<b>%s</b>%s</div>'
            '<button type="button" class="btn btn-ol sl-pick" data-pkg="%s">Get a quote</button></div></article>'
            % (c['img'], c['alt'], c['badge'], c['title'], c['dur'], bl, c['price'], c['unit'], c['pkg']))

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
        '<title>Travel Agent in Nairobi | Spice Travel (preview)</title><style>body{margin:0}</style></head><body>'
        + emb.replace('[contact-form-7 id="1438"]', form) + stub + '</body></html>')
(d / 'index.html').write_text(page)
for tag in ('style', 'script'):
    for m in re.finditer(r'<%s[^>]*>(.*?)</%s>' % (tag, tag), snip, re.S):
        assert '&' not in m.group(1), tag
print('built', len(snip)//1024, 'KB light;', len(emb)//1024, 'KB embedded')
