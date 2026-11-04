# Google Ads keywords for the BEST page (corporate first, plus flights and holiday packages)

Page: `https://spicetravel.co.ke/best-travel-agent-nairobi/` (set noindex in Yoast)
One page, four Final URLs. The headline and the form change with `?s=`:

| Final URL | Headline shown | Use for |
| --- | --- | --- |
| `/best-travel-agent-nairobi/` | Best Corporate Travel Management in Nairobi | corporate keywords (main focus) |
| `/best-travel-agent-nairobi/?s=agent` | Best Travel Agent in Nairobi | "best travel agent" and generic agency keywords |
| `/best-travel-agent-nairobi/?s=flights` | Flight Booking Agent in Nairobi | flight keywords |
| `/best-travel-agent-nairobi/?s=packages` | Holiday Packages from Nairobi | holiday, safari and destination keywords |

Campaign: `Search | Travel Agent | Nairobi | Leads`. Phrase and exact match. Location Kenya (Nairobi first), presence only.
Sitelink anchors on the same page: `#sl-corporate`, `#sl-flights`, `#sl-packages`, `#sl-offers`, `#sl-retreats`.

## Ad groups

| Ad group | Keywords | Final URL |
| --- | --- | --- |
| Corporate core (start here) | corporate travel management nairobi, corporate travel management company kenya, corporate travel agent nairobi, corporate travel agency nairobi, business travel agent nairobi, business travel agents kenya, travel management company nairobi, corporate flight booking nairobi | base URL |
| Best corporate (test) | best corporate travel management nairobi, best corporate travel agent nairobi, best corporate travel agency kenya, best business travel agent nairobi | base URL |
| Conferences and retreats | conference travel nairobi, event travel management kenya, corporate retreat kenya, team building packages kenya, incentive travel kenya, group travel packages kenya corporate | base URL |
| Best travel agent (test) | best travel agent in nairobi, best travel agency in nairobi, best travel agents nairobi, top travel agent nairobi | ?s=agent |
| Travel agent (generic) | travel agent nairobi, travel agency nairobi, tour and travel agency nairobi, tour agency nairobi, tour companies nairobi, tour operators nairobi, travel company nairobi, iata travel agent nairobi | ?s=agent |
| Flight booking | flight booking agent nairobi, flight booking agents in nairobi, flight booking agency nairobi, flight ticket agent nairobi, book flights nairobi, cheap flights from nairobi, best flight booking agent nairobi | ?s=flights |
| Holiday packages | holiday packages from nairobi, holiday packages kenya, tour packages from nairobi, vacation packages from nairobi, december holiday packages kenya | ?s=packages |
| Safari | kenya safari packages, safari packages from nairobi, maasai mara safari packages, amboseli safari packages, luxury safari packages kenya, maasai mara special offers, maasai mara flying package | ?s=packages |
| Beach and abroad | mombasa holiday packages, watamu holiday packages, zanzibar holiday packages from nairobi, dubai holiday packages from nairobi, mauritius holiday packages from kenya, seychelles holiday packages from kenya | ?s=packages |
| Brand | spice travel, spice travel kenya, spice travel nairobi | base URL |

Start order: Corporate core, Conferences and retreats, Travel agent (generic), Flight booking, Holiday packages.
Then add the two "best" test groups with a small budget.

## About "best" keywords (use your own data)
In your all-time report "best travel agency near me" and "best travel agency" had CTR of 32 to 34% but 0 conversions, and "top travel agencies" cost GBP 7.42 per conversion.
"best tour companies" did convert (6 conversions, GBP 2.18). The new page headline now matches "best ..." searches, which should help, but keep these groups small until they prove themselves.
Strong performers in your data: "travel agent", "tour agency", "tour companies", "tour and travel agency", "tour operators".
Google Ads may ask you to substantiate "best". The page shows proof: IATA certified, 30+ years, 5.0 on Google (27 reviews), 100+ attendee events.

## Negative keywords (campaign level)
jobs, job, career, salary, internship, course, training, how to become, become a travel agent, travel agent from home, franchise, software,
booking software, template, free, pdf, student, school trip, courier, parcel, delivery, internet package, data package, salary package,
visa only, uber, bus, matatu, hostel, airbnb.

## Ad copy (headlines up to 30 characters, descriptions up to 90)
Headlines: Corporate Travel Management (pin to position 1 in corporate groups) | Best Travel Agent in Nairobi (travel agent groups) | Flight Booking Agent Nairobi (flight group) |
Holiday Packages from Nairobi (packages groups) | IATA Certified Since 1994 | Rated 5 on Google | Free Quote, Call Back Today | Request a Call Back Today |
Groups From 5 to 100+ People | Flights, Hotels, Conferences | Team Retreats in Kenya | Same-Day Corporate Quote | 24/7 Support for Travellers | Packages from KES 33,500 | One Team, One Invoice

Descriptions:
1. IATA-certified corporate travel agent in Nairobi. Flights, hotels, conferences and retreats.
2. Request a call back and get your free corporate quote the same day. No obligation.
3. Domestic and international flights on any airline, ticketed fast. Group bookings welcome.
4. Holiday and safari packages from KES 33,500. Visa help and transfers included in one quote.

## Tracking
- Tracking template: `{lpurl}?utm_source=google&utm_medium=cpc&utm_campaign={campaignid}&utm_term={keyword}&utm_content={adgroupid}`
- Conversion: GTM custom event `generate_lead`. Parameters: `intent` (corporate, agent, flights, packages), `lead_type`, `source`, `need`, `package`.
- Every lead email starts with "BEST LANDING PAGE" and a REQUEST TYPE line (CORPORATE OR GROUP TRAVEL, FLIGHT TICKETS, HOLIDAY PACKAGE, VISA OR OTHER HELP).
