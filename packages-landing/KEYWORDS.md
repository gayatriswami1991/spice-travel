# Google Ads keywords for the Holiday Packages page

Page: `https://spicetravel.co.ke/holiday-packages-from-nairobi/` (set noindex in Yoast)
Campaign: `Search | Holiday Packages | Kenya | Leads` (separate from the corporate and flights campaigns)
Match types: phrase and exact only. Locations: Kenya (Nairobi first), presence only. Language: English.

## Ad groups

| Ad group | Keywords |
| --- | --- |
| Holiday packages Nairobi | holiday packages from nairobi, holiday packages nairobi, holiday packages kenya, travel packages from nairobi, tour packages from nairobi, vacation packages from nairobi, affordable holiday packages kenya, cheap holiday packages kenya |
| December and year-end | december holiday packages kenya, christmas holiday packages kenya, new year holiday packages kenya, december holidays from nairobi |
| Kenya safari | kenya safari packages, safari packages from nairobi, affordable safari packages kenya, maasai mara safari packages, maasai mara packages, amboseli safari packages, amboseli safari holidays, laikipia safari packages |
| Luxury safari | luxury safari packages kenya, luxury safari lodges kenya, luxury maasai mara safari, maasai mara flying safari, maasai mara fly in packages, balloon safari maasai mara |
| Mara special offers | maasai mara special offers, maasai mara pay 2 stay 3, mara safari offers 2026, maasai mara flying package |
| Beach (coast) | mombasa holiday packages, mombasa beach holidays, mombasa hotel packages, watamu holiday packages, watamu hotel offers, beach holiday packages kenya |
| Zanzibar | zanzibar holiday packages from nairobi, zanzibar packages from kenya, zanzibar all inclusive packages |
| Dubai | dubai holiday packages from nairobi, dubai packages from kenya, dubai tour packages nairobi, christmas in dubai from nairobi |
| Mauritius, Seychelles, Turkey | mauritius holiday packages from kenya, seychelles holiday packages from kenya, turkey holiday packages from nairobi, istanbul packages from nairobi |
| Brand | spice travel, spice travel kenya, spice travel nairobi, spice travel ltd |

Start with these 5 first (most intent, easiest to prove): Holiday packages Nairobi, Kenya safari, Mara special offers, Beach (coast), Dubai.

## Negative keywords (campaign level)

jobs, job, career, careers, salary, internship, course, training, how to become, become a travel agent,
courier, parcel, delivery, mail, internet package, data package, bundles, salary package, benefits package,
free, pdf, images, wallpaper, template, sacco, student, school trip, uber, bus, matatu, visa only, flight only,
hostel, airbnb, booking.com (add others after reading the search terms report).

Why "package" negatives matter: the word also means courier parcels and data bundles in Kenya.

## Responsive search ad copy (headlines up to 30 characters, descriptions up to 90)

Headlines: Holiday Packages from Nairobi (pin to position 1) | Free Holiday Quote Today | Request a Call Back Today |
Kenya Safari Packages | Maasai Mara Safari Packages | Mombasa Beach Holidays | Dubai Packages from Nairobi |
Zanzibar Holiday Packages | IATA Certified Since 1994 | Packages from KES 33,500 | Flights, Hotels, Transfers |
Pay 2 Stay 3 Maasai Mara | Luxury Safari Lodges Kenya | Visa Help for Trips Abroad | Easy Holidays, One Team

Descriptions:
1. Safari, beach and international holidays from Nairobi. We sort flights, hotels, visas.
2. Request a call back and get your free holiday quote today. No obligation.
3. Kenya lodges from KES 33,500 and trips abroad from USD 895 per person sharing.
4. IATA-certified Nairobi travel agency since 1994. Visa help for trips abroad.

Swap the matching destination into headline 2 for each ad group (for example "Dubai Packages from Nairobi" in the Dubai group).

## Final URLs and tracking
- All ad groups: the page URL above. Mara special offers can use `#sl-offers`, Beach and Dubai can use `#sl-packages`.
- Tracking template: `{lpurl}?utm_source=google&utm_medium=cpc&utm_campaign={campaignid}&utm_term={keyword}&utm_content={adgroupid}`
- Conversion: GTM custom event `generate_lead` (fires only when the CF7 mail is sent). `lead_type` is `packages_callback` or `quick_callback`.

## Notes
- Do not advertise the Mauritius and Seychelles prices until the team confirms current rates (posters said "valid till 30 Sep").
- Pause the Hemingways and Sand River offers after 19 Dec 2026 (the page hides them automatically).
- In the old account, "best holiday packages" got a 27% CTR but only a 1.4% conversion rate: the page did not match the search. Use the specific keywords above instead of generic "best ..." terms.
- Search terms report every 2 to 3 days in week 1. Move to target CPA after about 30 conversions.
