# Google Ads keywords for the ONE generic page (flights + packages + corporate)

Page: `https://spicetravel.co.ke/travel-agent-nairobi/` (set noindex in Yoast)
One page, four Final URLs. The headline and the form change with `?s=`:

| Final URL | Use for |
| --- | --- |
| `/travel-agent-nairobi/` | generic keywords (travel agent, tour agency ...) |
| `/travel-agent-nairobi/?s=corporate` | corporate and business keywords (H1: Corporate Travel Agent in Nairobi) |
| `/travel-agent-nairobi/?s=flights` | flight keywords (H1: Flight Booking Agent in Nairobi) |
| `/travel-agent-nairobi/?s=packages` | holiday and safari keywords (H1: Holiday Packages from Nairobi) |

Campaign: `Search | Travel Agent | Nairobi | Leads`. Phrase and exact match. Location Kenya (Nairobi first), presence only.

## What your own data says (all-time Search report)
Best converters were the generic agency words: "travel agent" 24 conversions at GBP 1.89, "tour agency" 9 at GBP 0.83 (18% conversion rate),
"tour companies" 14 at GBP 2.63, "tour and travel agency" 11 at GBP 3.49, "tour operators" 9 at GBP 3.82.
Weak: "best travel agency near me" and "best travel agency" (CTR 32 to 34%, 0 conversions), "travel agency near me" (GBP 7.53 per conversion),
"top travel agencies" (GBP 7.42), "travel agency" (GBP 6.15). Start with the strong group; test the weak ones only with a small budget.

## Ad groups

| Ad group | Keywords | Final URL |
| --- | --- | --- |
| Travel agent (generic, start here) | travel agent nairobi, travel agent kenya, travel agency nairobi, tour and travel agency nairobi, tour agency nairobi, travel company nairobi, travel agents in nairobi, iata travel agent nairobi | base URL |
| Tour companies | tour companies nairobi, tour operators nairobi, tour operators kenya, kenya tour companies, tour and travel companies kenya | base URL |
| Local | travel agency westlands, travel agency parklands, travel agent westlands, travel agency near me (small budget) | base URL |
| Corporate | corporate travel agent nairobi, corporate travel agency nairobi, business travel agents nairobi, corporate travel management nairobi, conference travel nairobi, corporate retreat kenya, team building packages kenya | ?s=corporate |
| Flights | flight booking agents nairobi, flight booking agency nairobi, flight ticket agents nairobi, cheap flights from nairobi, book flights nairobi, travel agent for flights nairobi | ?s=flights |
| Holiday packages | holiday packages from nairobi, holiday packages kenya, tour packages from nairobi, vacation packages from nairobi, december holiday packages kenya | ?s=packages |
| Safari | kenya safari packages, safari packages from nairobi, maasai mara safari packages, luxury safari packages kenya, maasai mara special offers | ?s=packages |
| Beach and abroad | mombasa holiday packages, zanzibar holiday packages from nairobi, dubai holiday packages from nairobi, mauritius holiday packages from kenya, seychelles holiday packages from kenya | ?s=packages |
| Brand | spice travel, spice travel kenya, spice travel nairobi | base URL |

Start order: Travel agent, Tour companies, Corporate, Flights, Holiday packages. Add the rest after the first 30 leads.

## Negative keywords (campaign level)
jobs, job, career, salary, internship, course, training, how to become, become a travel agent, travel agent from home, franchise, software,
booking software, template, free, pdf, student, school trip, courier, parcel, delivery, internet package, data package, salary package,
visa only, uber, bus, matatu, hostel, airbnb.

## Ad copy (headlines up to 30 characters, descriptions up to 90)
Headlines: Travel Agent in Nairobi (pin to position 1) | IATA Certified Since 1994 | Free Quote, Call Back Today |
Flights, Holidays, Corporate Travel | Request a Call Back Today | Tour and Travel Agency Nairobi | Same-Day Travel Quote |
Flights, Hotels, Visas Sorted | Safari and Beach Holidays | 30+ Years in Nairobi | One Team for Every Trip

Descriptions:
1. IATA-certified Nairobi travel agent. Flights, holidays, safaris, visas and corporate travel.
2. Request a call back and get your free travel quote today. No obligation.
3. Holiday packages from KES 33,500. Group and corporate travel for teams of 5 to 100+.
4. Domestic and international flights on any airline, ticketed fast. Visa help included.

For the ?s= ad groups put the matching phrase in headline 2 (for example "Corporate Travel Agent Nairobi" or "Flight Booking Agents Nairobi").

## Tracking
- Tracking template: `{lpurl}?utm_source=google&utm_medium=cpc&utm_campaign={campaignid}&utm_term={keyword}&utm_content={adgroupid}`
  (Google adds this after your `?s=` value correctly when you put the template in the account or campaign.)
- Conversion: GTM custom event `generate_lead`. Parameters: `intent` (generic, corporate, flights, packages), `lead_type`, `source`.
  Make one conversion action for all leads, and use the `intent` / `lead_type` values to see which service produces leads.
- Every lead email starts with "GENERIC LANDING PAGE" and a REQUEST TYPE line (FLIGHT TICKETS, HOLIDAY PACKAGE, CORPORATE OR GROUP TRAVEL, VISA OR OTHER HELP).

## Is one page enough?
Yes to start. The `?s=` headline keeps the message match for each intent, and the form asks the right questions for each service.
Build separate pages later only for the service that brings the most spend (usually flights or packages), then compare conversion rate.
