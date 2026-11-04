"""Builds index.html (local preview) from divi-snippet.html.
Replaces the CF7 shortcode with the real markup of form 1438 plus a tiny stub that imitates
Contact Form 7's events, so the step form can be tested without WordPress.
Open index.html?stub=invalid to simulate a validation error."""
import pathlib
d = pathlib.Path(__file__).parent
snip = (d / 'divi-snippet.html').read_text()
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
/* PREVIEW ONLY: imitates CF7 events */
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
        '<title>Corporate Travel Agent in Nairobi | Spice Travel (preview)</title><style>body{margin:0}</style></head><body>'
        + snip.replace('[contact-form-7 id="1438"]', form) + stub + '</body></html>')
(d / 'index.html').write_text(page)
print('ok', len(page))
