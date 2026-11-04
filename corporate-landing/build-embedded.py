"""Builds two self-contained files where every image is embedded (base64), so they show images anywhere:
  index.html                      local preview (CF7 form replaced by a stub that imitates its events)
  divi-snippet-with-images.html   paste into a Divi Fullwidth Code module; keeps the real [contact-form-7 id="1438"] shortcode
divi-snippet.html stays the lightweight version that expects the images to be uploaded to the Media Library."""
import base64, pathlib, re
d = pathlib.Path(__file__).parent
snip = (d / 'divi-snippet.html').read_text()

def embed(text):
    def r(m):
        f = d / 'assets' / m.group(1)
        data = base64.b64encode(f.read_bytes()).decode()
        mime = 'image/webp' if f.suffix == '.webp' else 'image/jpeg'
        return 'data:%s;base64,%s' % (mime, data)
    return re.sub(r"assets/([A-Za-z0-9_\-\.]+)", r, text)

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
emb = embed(snip)
(d / 'divi-snippet-with-images.html').write_text(emb)
page = ('<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
        '<title>Corporate Travel Agent in Nairobi | Spice Travel (preview)</title><style>body{margin:0}</style></head><body>'
        + emb.replace('[contact-form-7 id="1438"]', form) + stub + '</body></html>')
(d / 'index.html').write_text(page)
print('divi-snippet-with-images.html', len(emb)//1024, 'KB; index.html', len(page)//1024, 'KB')
