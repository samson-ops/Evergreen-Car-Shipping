import re, json, html as H

SRC = open('index.html').read()
HEAD_CSS = re.search(r'<style>\n/\* ===== Evergreen site styles.*?</style>', SRC, re.S).group(0)
EMBED = re.search(r'<!-- ============================================================\n     SHIP GUY PRICING TOOL.*?<!-- ===================== /SHIP GUY PRICING TOOL ===================== -->\n\s*<style>\n/\* Evergreen brand colors.*?</style>', SRC, re.S).group(0)
SITE_JS = re.search(r"\(function\(\)\{\n  var s=window\.EG_SITE;.*?\}\)\(\);\n</script>", SRC, re.S).group(0)

CHECK = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="m5 12 4 4L19 6"/></svg>'
PHONE_SVG = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.5 2.1L8.1 9.9a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.8.7a2 2 0 0 1 1.7 2Z"/></svg>'

CITIES = [
 dict(slug='seattle', city='Seattle', phone='(253) 364-1610', tel='+12533641610', street='3250 Airport Wy S #1500', zip='98134', lat=47.574971, lng=-122.3210079,
  map='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3473.185082829288!2d-122.3210079!3d47.574971!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x549041d656b0f1ab%3A0xb2dfe4aa1bb8dfcf!2sEvergreen%20Car%20Shipping!5e1!3m2!1sen!2sus!4v1791567854968!5m2!1sen!2sus',
  title='Seattle Car Shipping &amp; Auto Transport | Evergreen',
  desc='Licensed, insured Seattle car shipping. Door-to-door open & enclosed auto transport to all 50 states. Instant quote or call (253) 364-1610.',
  h1='Seattle Car Shipping &amp; Auto Transport',
  tagline='Licensed, insured door-to-door vehicle shipping from Seattle to anywhere in the United States — with a local office in SoDo and a real person on the phone.',
  areas=['Capitol Hill','Ballard','Queen Anne','West Seattle','Fremont','Green Lake','Beacon Hill','Rainier Valley','Shoreline','Edmonds','Lynnwood','Everett','Kent','Renton','Burien','SeaTac','Tukwila','Federal Way','Bothell','Mountlake Terrace'],
  routes=[('Seattle → Los Angeles, CA','1,135 mi','3–5 days'),('Seattle → San Francisco Bay Area','810 mi','2–4 days'),('Seattle → Phoenix, AZ','1,420 mi','4–6 days'),('Seattle → Denver, CO','1,320 mi','4–6 days'),('Seattle → Dallas, TX','2,100 mi','6–8 days'),('Seattle → Chicago, IL','2,060 mi','6–8 days'),('Seattle → New York, NY','2,850 mi','8–10 days'),('Seattle → Miami, FL','3,300 mi','9–12 days')],
  faq=[('How much does it cost to ship a car from Seattle?','Most open-carrier shipments out of Seattle run roughly $650–$900 to California, $900–$1,300 to the Mountain West and Texas, and $1,300–$1,800 to the East Coast for a standard sedan. SUVs, trucks, enclosed transport, and non-running vehicles cost more. The quote tool on this page gives you an exact all-in price for your route in about 30 seconds.'),
       ('How long does it take to ship a car from Seattle?','Pickup is usually scheduled within 1–5 days of booking. Once loaded, West Coast runs to California take 2–5 days, the Southwest and Rockies 4–6 days, and cross-country to the East Coast 8–10 days.'),
       ('Can you pick up my car in downtown Seattle or on Capitol Hill?','Yes. Full-size car haulers can\'t always navigate narrow streets or steep hills, so for tight downtown and Capitol Hill addresses the driver will arrange a nearby meeting spot — a wide street, a large parking lot, or a shopping center — usually within a mile or two of your door.'),
       ('Do you ship cars from Seattle to Alaska or Hawaii?','We ship vehicles to and from the Port of Tacoma and Port of Seattle for ocean carriers serving Alaska and Hawaii. Call our Seattle office at (253) 364-1610 and we\'ll quote the full door-to-port or door-to-door move.'),
       ('Is open transport safe in Seattle\'s rain?','Yes. Open carriers are the industry standard and move the vast majority of new and used cars in the Pacific Northwest. Your car may arrive needing a wash, but rain itself does no harm. For luxury, classic, or exotic vehicles, enclosed transport keeps the car fully covered.')],
  body="""
<h2>Car shipping in Seattle, done the easy way</h2>
<p>Seattle is one of the busiest vehicle shipping markets in the western United States. Tech relocations to and from South Lake Union and the Eastside, University of Washington students arriving and leaving every semester, military families moving through Joint Base Lewis-McChord, retirees heading south for the winter, and collectors buying cars at auction all need the same thing: a dependable way to move a vehicle without driving it. Evergreen Car Shipping's Seattle office, located on Airport Way South in the SoDo district just minutes from I-5 and I-90, exists to make that simple.</p>
<p>We are a licensed and bonded auto transport broker. That means we don't own a single truck — we own something more useful: relationships with hundreds of vetted, FMCSA-registered carriers that run the I-5 corridor, I-90 across the mountains, and every major lane out of the Puget Sound region every week. When you book with us, we match your vehicle with a carrier already heading your direction, confirm their insurance and safety record, lock in your price, and manage the shipment until the keys are back in your hand.</p>

<h2>Why Seattle residents choose Evergreen Car Shipping</h2>
<p>There are plenty of national lead-generation websites that will take your Seattle car shipping request and sell it to five brokers who then call you nonstop. We work differently. You get one point of contact in our Seattle office, one all-in price, and one phone number — <a data-city-tel href="#">(253) 364-1610</a> — that reaches someone who actually knows your shipment.</p>
<ul class="checks">
<li>{CHECK}<b>All-in pricing.</b> The quote you see online is what you pay. No fuel surcharges, no "dispatch fees," no surprise balance on delivery day.</li>
<li>{CHECK}<b>Door-to-door service.</b> Pickup and delivery as close to your address as a 75-foot car hauler can safely get, whether that's a driveway in Ballard or a parking lot in Bellevue.</li>
<li>{CHECK}<b>Open and enclosed carriers.</b> Budget-friendly open transport for daily drivers, or fully enclosed trailers for Teslas, Porsches, classics, and anything you don't want exposed to road grime.</li>
<li>{CHECK}<b>Fully insured.</b> Every carrier we dispatch carries cargo insurance, and your car's condition is documented on a bill of lading at pickup and delivery.</li>
<li>{CHECK}<b>Local knowledge.</b> We know which Seattle neighborhoods a semi can and can't reach, which days the I-90 pass is a problem in winter, and how to time a pickup around the Port of Seattle and SeaTac traffic.</li>
</ul>

<h2>Seattle neighborhoods and suburbs we serve</h2>
<p>Our Seattle auto transport service covers the entire city and the greater King and Snohomish County area. Carriers pick up and deliver regularly in {AREAS}, and everywhere in between. If you're outside the city — Bainbridge Island, Vashon, or up toward Marysville and Mount Vernon — we can still help; the driver will simply coordinate a convenient meeting point on the mainland or along I-5.</p>
<p>A quick note on Seattle's geography: hills, narrow residential streets, and low-hanging trees in neighborhoods like Queen Anne, Capitol Hill, and Madrona can make it impossible for a full-size transport truck to reach your front door. When that's the case, your driver will call ahead and arrange to meet somewhere nearby with room to load safely — a wide arterial, a grocery store parking lot, or a park-and-ride. It takes a few extra minutes and is completely routine.</p>

<h2>Popular car shipping routes from Seattle</h2>
<p>Because Seattle sits at the top of the I-5 corridor and the western end of I-90, carriers run south to California and east across the country constantly. That volume keeps prices competitive and pickup windows short. Here are the lanes we book most often, with typical transit times once your vehicle is loaded:</p>
{ROUTES}
<p>Shipping a car <em>to</em> Seattle? Every route runs both directions. Inbound shipments from California, Arizona, Texas, and the East Coast are just as common, especially during summer relocation season and when snowbirds return in spring.</p>

<h2>What it costs to ship a car from Seattle</h2>
<p>Seattle car shipping cost depends on five things: distance, vehicle size and weight, open versus enclosed transport, whether the vehicle runs, and how flexible you are on pickup dates. As a rough guide, a standard sedan on an open carrier costs about $650–$900 to Southern California, $900–$1,300 to Phoenix, Denver, or Dallas, and $1,300–$1,800 to New York or Florida. A large SUV or pickup adds $100–$250. Enclosed transport runs roughly 40–60% more than open. A non-running vehicle that needs a winch adds around $150.</p>
<p>Timing matters too. Summer is the busiest season on West Coast lanes as families move for school and work; booking a week or two ahead gets the best price. Flexibility on your pickup window — giving the carrier a two- or three-day range instead of one specific day — is the single easiest way to lower your rate. Rather than estimate, use the quote tool at the top of this page: enter two ZIP codes and your vehicle, and you'll see an exact, all-in price in about 30 seconds.</p>

<h2>Open vs. enclosed transport in the Pacific Northwest</h2>
<p>Open transport is the standard — the two-level haulers you see on I-5 carrying new cars to dealerships. It's safe, it's the most affordable, and it's what the vast majority of Seattle customers choose. Yes, it rains here, and your car may arrive needing a wash, but weather exposure during a few days in transit is no different from parking on the street.</p>
<p>Enclosed transport puts your vehicle inside a hard-sided trailer, protected from rain, road debris, and prying eyes. We recommend it for luxury and exotic cars, classics and restorations, low-clearance sports cars, and high-value EVs. Given how many Teslas, Rivians, and Porsches live in the Seattle area, enclosed is a popular choice here — and because enclosed carriers cross the Cascades and run the I-5 corridor regularly, availability is good.</p>

<h2>Relocating to or from Seattle? Here's how it works</h2>
<ol class="numbered">
<li><b>Get your quote.</b> Use the instant quote tool or call our Seattle office. Tell us the pickup and delivery ZIP codes, your vehicle, and when you'd like it picked up.</li>
<li><b>Book and schedule.</b> Once you approve the price, we assign a vetted carrier on your lane and confirm the driver's name, truck, and pickup window with you. A small deposit holds your spot; the balance is paid at delivery.</li>
<li><b>Pickup and inspection.</b> The driver inspects your car with you, notes any existing scratches or dings on the bill of lading, and loads it. Keep a copy — it's your record.</li>
<li><b>In transit.</b> We keep you updated as your car moves, and you can reach the driver or our office any time.</li>
<li><b>Delivery.</b> Inspect the car against the bill of lading, sign, pay the balance, and you're done.</li>
</ol>

<h2>Preparing your car for shipping from Seattle</h2>
<p>A little preparation makes pickup day smooth. Wash the car so the inspection is accurate. Leave about a quarter tank of fuel — enough to load and unload, not so much that it adds weight. Remove toll transponders (Good To Go! passes will keep billing you otherwise), parking permits, and loose items. Fold in mirrors and retract antennas. Note any existing damage with photos. Personal items are allowed up to about 100 pounds in the trunk or below the window line, but they aren't covered by cargo insurance, so keep anything valuable with you. If your car has an alarm, disable it or tell the driver how.</p>

<h2>Military, student, and snowbird shipping from Seattle</h2>
<p>With Joint Base Lewis-McChord and Naval Base Kitsap nearby, we handle a steady stream of PCS moves. We offer active-duty discounts and can work around orders and report dates. For UW, Seattle U, and Seattle Pacific students, we ship cars to and from campus housing every fall and spring — and we know how to coordinate pickup when a parent is on the other end. Seattle snowbirds heading to Arizona, Palm Springs, or Florida should book early; October and November are the peak months southbound, and March and April northbound.</p>

<h2>Visit or call our Seattle office</h2>
<p>Evergreen Car Shipping's Seattle location is at 3250 Airport Way S, Suite 1500, Seattle, WA 98134 — in SoDo, a short drive from downtown, the stadiums, and the I-5/I-90 interchange. Call <a data-city-tel href="#">(253) 364-1610</a> Monday through Saturday, or get your instant quote online any time. We also have Washington offices in <a href="bellevue-car-shipping.html">Bellevue</a>, <a href="tacoma-car-shipping.html">Tacoma</a>, and <a href="spokane-car-shipping.html">Spokane</a>.</p>
"""),

 dict(slug='spokane', city='Spokane', phone='(509) 581-4566', tel='+15095814566', street='1020 N Washington St #333', zip='99201', lat=47.6674695, lng=-117.4169804,
  map='https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d13868.18144827786!2d-117.4169804!3d47.6674695!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x549e193720d1f74d%3A0xe3f483f405489b3c!2sEvergreen%20Car%20Shipping!5e1!3m2!1sen!2sus!4v1791567862387!5m2!1sen!2sus',
  title='Spokane Car Shipping &amp; Auto Transport | Evergreen',
  desc='Licensed, insured Spokane car shipping. Door-to-door open & enclosed auto transport to all 50 states. Instant quote or call (509) 581-4566.',
  h1='Spokane Car Shipping &amp; Auto Transport',
  tagline='Licensed, insured vehicle shipping from Spokane and the Inland Northwest to anywhere in the country — from a local office downtown on North Washington Street.',
  areas=['Downtown Spokane','South Hill','Browne\'s Addition','North Side','Shadle Park','Hillyard','Spokane Valley','Liberty Lake','Cheney','Airway Heights','Medical Lake','Mead','Colbert','Nine Mile Falls','Deer Park','Millwood','Otis Orchards','Post Falls, ID','Coeur d\'Alene, ID','Pullman'],
  routes=[('Spokane → Seattle, WA','280 mi','1–2 days'),('Spokane → Portland, OR','350 mi','1–2 days'),('Spokane → Boise, ID','420 mi','1–3 days'),('Spokane → Salt Lake City, UT','710 mi','2–4 days'),('Spokane → Denver, CO','1,100 mi','3–5 days'),('Spokane → Los Angeles, CA','1,230 mi','4–6 days'),('Spokane → Phoenix, AZ','1,380 mi','4–6 days'),('Spokane → Minneapolis, MN','1,330 mi','4–6 days'),('Spokane → Chicago, IL','1,760 mi','5–7 days'),('Spokane → New York, NY','2,550 mi','7–10 days')],
  faq=[('How much does it cost to ship a car from Spokane?','For a standard sedan on an open carrier, expect roughly $400–$600 to Seattle or Portland, $700–$1,000 to Salt Lake, Denver, or Boise, $900–$1,300 to California and Arizona, and $1,300–$1,800 to the East Coast. Enclosed transport, larger vehicles, and winter weather can raise the price. Use the quote tool for an exact figure.'),
       ('How long does car shipping from Spokane take?','Pickup is typically scheduled within 2–7 days — slightly longer than Seattle because fewer carriers originate in Eastern Washington. Once loaded, Seattle and Portland are 1–2 days, the Mountain West 2–5 days, and the East Coast 7–10 days.'),
       ('Can you ship my car from Spokane in winter?','Yes. Carriers run I-90 and US-395 year-round. Snow and pass closures can occasionally add a day, and we build that into the schedule we give you. Enclosed transport is worth considering in winter if your vehicle is high-value.'),
       ('Do you serve Coeur d\'Alene and North Idaho?','Yes. Our Spokane office handles Post Falls, Coeur d\'Alene, Hayden, Sandpoint, and the rest of the Idaho panhandle. Pickups there are usually bundled with Spokane-area loads, which keeps prices in line.'),
       ('Where will the driver pick up my car in Spokane?','Most Spokane addresses are accessible to a full-size car hauler. On the South Hill or in older neighborhoods with narrow streets, the driver may ask to meet at a nearby lot or wide arterial. The driver calls ahead to confirm the spot.')],
  body="""
<h2>Car shipping in Spokane and the Inland Northwest</h2>
<p>Spokane is the hub of the Inland Northwest — the largest city between Seattle and Minneapolis, and the place where I-90, US-2, and US-395 come together. That makes it a natural staging point for vehicle shipping across Eastern Washington, North Idaho, and western Montana. Whether you're relocating for a job at Fairchild Air Force Base, sending a student to Gonzaga, Whitworth, EWU, or WSU, moving a lake car to or from Coeur d'Alene, or heading south for the winter, Evergreen Car Shipping's Spokane office on North Washington Street is your local point of contact.</p>
<p>We're a licensed and bonded auto transport broker. Rather than operating a handful of trucks, we work with a network of vetted, FMCSA-registered carriers that run I-90 between Seattle and Chicago and the north–south corridors toward Boise, Salt Lake City, and the Southwest. When you book, we match your vehicle with a carrier already scheduled on your lane, verify their insurance and safety record, lock in your all-in price, and stay with you until delivery.</p>

<h2>Why Spokane customers choose Evergreen Car Shipping</h2>
<p>Eastern Washington is a different shipping market than the I-5 corridor. Fewer carriers originate here, so who you book with matters more. A national call center won't know that a carrier running Seattle-to-Minneapolis passes right through Spokane, or that a Boise-bound truck can swing through Cheney. Our Spokane team does — and that local knowledge turns into shorter pickup windows and better prices.</p>
<ul class="checks">
<li>{CHECK}<b>One local number.</b> Call <a data-city-tel href="#">(509) 581-4566</a> and reach someone in Spokane who knows your shipment, not a rotating queue of agents.</li>
<li>{CHECK}<b>All-in pricing.</b> The quote is the price. No add-ons for I-90 pass crossings, no winter surcharges invented on delivery day.</li>
<li>{CHECK}<b>Door-to-door across the region.</b> Spokane, Spokane Valley, Liberty Lake, Cheney, Airway Heights, Deer Park, and into North Idaho.</li>
<li>{CHECK}<b>Open and enclosed options.</b> Affordable open carriers for daily drivers; enclosed trailers for classics, collector cars, and anything you'd rather keep out of winter road grime.</li>
<li>{CHECK}<b>Fully insured.</b> Every carrier carries cargo coverage, and your vehicle's condition is documented on a bill of lading at both ends.</li>
</ul>

<h2>Spokane-area neighborhoods and communities we serve</h2>
<p>Our Spokane auto transport service covers the city and all of Spokane County, plus the Idaho panhandle. Carriers regularly pick up and deliver in {AREAS}, and the surrounding farm country. Wheat-country addresses outside town are no problem — if a gravel road or low-clearance driveway can't take a semi, the driver will arrange a meeting spot on the nearest paved highway or in town.</p>
<p>Because our Spokane office also serves North Idaho, we frequently combine pickups across the state line. A car leaving Coeur d'Alene and one leaving Spokane Valley often ride the same truck, which keeps costs down for both customers. If you're in Pullman, Moscow, Sandpoint, or Lewiston, call us — we'll tell you honestly what pickup timing looks like for your area.</p>

<h2>Popular car shipping routes from Spokane</h2>
<p>Spokane's position on I-90 means east–west lanes are strongest: carriers heading to Seattle, Montana, Minneapolis, and Chicago pass through constantly. Southbound lanes to Boise, Salt Lake City, and the Southwest run via US-395 and I-84. Typical transit times after pickup:</p>
{ROUTES}
<p>Inbound shipping to Spokane follows the same lanes in reverse. We move a lot of vehicles <em>into</em> the area from Seattle, Portland, California, and Arizona — new residents, returning snowbirds, and online car purchases from larger markets.</p>

<h2>What it costs to ship a car from Spokane</h2>
<p>Spokane car shipping cost comes down to distance, vehicle size, open versus enclosed, whether the vehicle runs, and date flexibility. As a rough guide for a sedan on an open carrier: Seattle or Portland $400–$600; Boise, Salt Lake, or Denver $700–$1,000; California and Arizona $900–$1,300; Texas, the Midwest, and the East Coast $1,300–$1,800. Trucks and SUVs add $100–$250, enclosed runs 40–60% more, and a non-running vehicle adds roughly $150 for a winch.</p>
<p>One Spokane-specific tip: flexibility on pickup dates matters more here than in Seattle. Because fewer trucks originate in Eastern Washington, giving the carrier a 3–5 day window instead of a single day can noticeably lower your price and speed up assignment. The instant quote tool at the top of the page gives you an exact, all-in number in about 30 seconds — no obligation.</p>

<h2>Shipping a car from Spokane in winter</h2>
<p>Spokane winters are real — snow from November through March, cold snaps, and the occasional closure of Snoqualmie or Lookout Pass. Carriers run year-round, but we plan around weather honestly: if a storm is forecast on I-90, we'll tell you it might add a day rather than promise a date we can't keep. If your vehicle is high-value or freshly detailed, enclosed transport keeps it out of road salt, mag chloride, and gravel spray. For everyday vehicles, open transport is perfectly fine; a wash on arrival is all it takes.</p>
<p>Snowbirds leaving Spokane for Arizona, Palm Springs, or Texas should book in early fall. October and November are the busiest southbound months, and March and April are busiest coming back. Booking two to three weeks ahead gets you the best rates and the widest choice of pickup dates.</p>

<h2>How Spokane car shipping works</h2>
<ol class="numbered">
<li><b>Quote.</b> Enter your pickup and delivery ZIP codes and vehicle in the quote tool, or call the Spokane office. You'll get an all-in price with no obligation.</li>
<li><b>Book.</b> Approve the price, choose a pickup window, and we assign a vetted carrier. We confirm the driver, truck, and ETA with you. A small deposit reserves your spot; the balance is paid at delivery.</li>
<li><b>Pickup.</b> The driver inspects the car with you, records existing condition on the bill of lading, and loads it.</li>
<li><b>Transit.</b> We keep you updated along the way, and you can reach the driver or our office directly.</li>
<li><b>Delivery.</b> Inspect, sign, pay the balance, done.</li>
</ol>

<h2>Preparing your vehicle for transport</h2>
<p>Wash the car so the pickup inspection is accurate — especially in winter when road grime hides scratches. Leave about a quarter tank of fuel. Remove toll tags, parking passes, and loose items from the cabin. Fold in mirrors, remove roof racks or bike carriers, and retract antennas. Photograph the car from all sides. Personal items up to about 100 pounds can ride in the trunk, but they aren't insured, so keep valuables with you. If the vehicle has a quirk — a tricky starter, an alarm, a manual choke on a classic — tell the driver.</p>

<h2>Military, student, and collector shipping from Spokane</h2>
<p>Fairchild Air Force Base generates steady PCS traffic, and we offer active-duty discounts and can work around report dates. Gonzaga, Whitworth, Eastern Washington University, and WSU in Pullman mean a surge of student car shipments every August and May; we coordinate with parents on the other end routinely. Spokane and North Idaho also have a strong collector-car community — if you've bought a classic at auction or are sending one to a restorer out of state, ask about enclosed transport and we'll match you with a carrier that handles collector vehicles regularly.</p>

<h2>Visit or call our Spokane office</h2>
<p>Evergreen Car Shipping's Spokane location is at 1020 N Washington St, Suite 333, Spokane, WA 99201 — just north of downtown and the Spokane River, minutes from I-90. Call <a data-city-tel href="#">(509) 581-4566</a> Monday through Saturday, or use the instant quote tool any time. We also have Washington offices in <a href="seattle-car-shipping.html">Seattle</a>, <a href="bellevue-car-shipping.html">Bellevue</a>, and <a href="tacoma-car-shipping.html">Tacoma</a>.</p>
"""),

 dict(slug='bellevue', city='Bellevue', phone='(425) 380-2729', tel='+14253802729', street='355 118th Ave SE #790', zip='98005', lat=47.6067573, lng=-122.1834651,
  map='https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d13884.304966325108!2d-122.1834651!3d47.6067573!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x54906d8e1fe12161%3A0xaf5755f653a4bbf8!2sEvergreen%20Car%20Shipping!5e1!3m2!1sen!2sus!4v1791567870236!5m2!1sen!2sus',
  title='Bellevue Car Shipping &amp; Auto Transport | Evergreen',
  desc='Licensed, insured Bellevue & Eastside car shipping. Open & enclosed door-to-door auto transport nationwide. Instant quote or call (425) 380-2729.',
  h1='Bellevue Car Shipping &amp; Eastside Auto Transport',
  tagline='Licensed, insured vehicle shipping for Bellevue, Redmond, Kirkland, and the Eastside — open and enclosed carriers to anywhere in the U.S., from a local office off I-405.',
  areas=['Downtown Bellevue','West Bellevue','Crossroads','Factoria','Somerset','Eastgate','Lake Hills','Newport Hills','Bridle Trails','Redmond','Kirkland','Issaquah','Sammamish','Mercer Island','Medina','Clyde Hill','Newcastle','Renton','Woodinville','Bothell'],
  routes=[('Bellevue → San Francisco Bay Area','830 mi','2–4 days'),('Bellevue → Los Angeles, CA','1,140 mi','3–5 days'),('Bellevue → San Diego, CA','1,260 mi','4–6 days'),('Bellevue → Phoenix, AZ','1,430 mi','4–6 days'),('Bellevue → Denver, CO','1,310 mi','4–6 days'),('Bellevue → Austin, TX','2,150 mi','6–8 days'),('Bellevue → Chicago, IL','2,050 mi','6–8 days'),('Bellevue → Boston, MA','3,050 mi','8–11 days'),('Bellevue → New York, NY','2,850 mi','8–10 days')],
  faq=[('How much does it cost to ship a car from Bellevue?','For a sedan on an open carrier, roughly $650–$900 to California, $900–$1,300 to Arizona, Colorado, or Texas, and $1,300–$1,800 to the East Coast. Enclosed transport — popular on the Eastside for luxury cars and EVs — runs 40–60% more. The quote tool on this page gives an exact all-in price.'),
       ('Can a car hauler get to my condo in downtown Bellevue?','Usually not directly — parking garages, tight turns, and traffic on Bellevue Way and NE 8th make it impractical. Your driver will arrange a nearby meeting spot with room to load, often a large retail lot or a wide street in the Spring District or Factoria. It\'s routine and takes a few minutes.'),
       ('Do you ship Teslas and other EVs from Bellevue?','Yes, constantly. EVs ship like any other car; the driver just needs the vehicle to have enough charge to load and unload (about 30% is plenty). Many EV owners choose enclosed transport. Tell us the model and we\'ll make sure the carrier is comfortable with it.'),
       ('I\'m relocating for a tech job — how far ahead should I book?','Two weeks is ideal for the best price and widest choice of pickup dates, especially in summer. We can often arrange pickup within a few days if your start date is close — call the Bellevue office and we\'ll tell you what\'s realistic.'),
       ('Do you serve Redmond, Kirkland, Issaquah, and Sammamish?','Yes. Our Bellevue office covers the entire Eastside, from Mercer Island and Medina to Woodinville, Issaquah, and the Sammamish Plateau.')],
  body="""
<h2>Car shipping for Bellevue and the Eastside</h2>
<p>Bellevue has become one of the most active vehicle shipping markets in the Pacific Northwest. Microsoft, Amazon, T-Mobile, Meta, and hundreds of smaller tech companies bring new employees to the Eastside every month — and send them to other offices just as often. Add a high concentration of luxury vehicles, EVs, and collector cars, families relocating to and from the Bay Area and Austin, and international assignees who need a car moved to a port, and you have a market that needs a shipping partner who knows the area. Evergreen Car Shipping's Bellevue office, on 118th Avenue SE just off I-405 and I-90, is that partner.</p>
<p>We are a licensed and bonded auto transport broker. We don't operate trucks; we operate a vetted network of FMCSA-registered carriers that run the I-5 corridor, I-90, and every major lane out of the Puget Sound region every week — including enclosed carriers that specialize in high-value vehicles. When you book with our Bellevue team, we match your vehicle with the right carrier, verify their insurance and safety record, lock in an all-in price, and manage the shipment door to door.</p>

<h2>Why Eastside customers choose Evergreen Car Shipping</h2>
<p>Bellevue customers tend to have two priorities: protect the vehicle, and don't waste my time. We've built our service around both. One phone number — <a data-city-tel href="#">(425) 380-2729</a> — reaches a local coordinator who knows your shipment. One all-in price, confirmed before you commit. And a carrier roster that includes enclosed specialists used to handling Porsches, Teslas, Range Rovers, and restored classics.</p>
<ul class="checks">
<li>{CHECK}<b>Enclosed transport expertise.</b> A higher share of our Bellevue shipments go enclosed than anywhere else we operate. We know which carriers use liftgates for low-clearance cars and which handle EVs daily.</li>
<li>{CHECK}<b>All-in pricing.</b> The quote is the price — no fuel surcharges, no dispatch fees, no surprises at delivery.</li>
<li>{CHECK}<b>Door-to-door with a plan for downtown.</b> We know a 75-foot hauler can't pull up to a Bellevue Way high-rise, so we arrange a convenient loading spot up front instead of leaving it to the day of pickup.</li>
<li>{CHECK}<b>Fully insured, fully documented.</b> Cargo insurance on every carrier and a detailed bill of lading at both ends.</li>
<li>{CHECK}<b>Relocation-friendly scheduling.</b> We work around start dates, lease end dates, and flights — and we can hold a car for a short time if your housing isn't ready.</li>
</ul>

<h2>Eastside neighborhoods and cities we serve</h2>
<p>Our Bellevue auto transport service covers the entire Eastside of King County. Carriers pick up and deliver regularly in {AREAS}, and the surrounding communities along I-405, I-90, and SR-520. Gated communities and HOA neighborhoods on the Sammamish Plateau and in Newcastle are common for us; we'll coordinate gate access and the loading location with you ahead of time.</p>
<p>Downtown Bellevue, the Spring District, and dense parts of Kirkland and Redmond are generally not reachable by a full-size transport truck. In those cases your driver will call ahead and meet you at a nearby location with room to load safely — a large retail parking lot, a park-and-ride, or a wide side street. It's completely routine and usually within a mile or two of your address.</p>

<h2>Popular car shipping routes from Bellevue</h2>
<p>Because so many Eastside relocations connect to other tech hubs, the strongest lanes out of Bellevue run to the Bay Area, Southern California, Austin, Denver, and the Northeast. Carriers run these routes weekly, which keeps pickup windows short. Typical transit times once your vehicle is loaded:</p>
{ROUTES}
<p>Shipping a car to Bellevue? Inbound lanes from California, Texas, and the East Coast are just as busy — new hires, returning students, and vehicles purchased out of state all arrive through our Bellevue office. Every route runs both directions at similar pricing.</p>

<h2>What it costs to ship a car from Bellevue</h2>
<p>Bellevue car shipping cost depends on distance, vehicle size and weight, open versus enclosed transport, whether the vehicle runs, and how flexible your pickup dates are. For a sedan on an open carrier, expect roughly $650–$900 to the Bay Area or Los Angeles, $900–$1,300 to Phoenix, Denver, or Texas, and $1,300–$1,800 to Boston, New York, or Florida. SUVs and trucks add $100–$250. Enclosed transport runs 40–60% more than open; for a high-value vehicle, most Eastside customers consider that well worth it.</p>
<p>Summer is peak season, and the weeks around major tech start dates can get tight. Booking two weeks ahead gets the best rates. The instant quote tool at the top of this page gives you an exact, all-in price in about 30 seconds — enter your ZIP codes and vehicle, and there's no obligation.</p>

<h2>Shipping luxury cars, EVs, and classics from the Eastside</h2>
<p>If you own something you care about, enclosed transport is the right call. Your vehicle rides inside a hard-sided trailer, protected from rain, gravel, road salt on mountain passes, and public view. Enclosed carriers typically use liftgates rather than ramps, which matters for low-clearance sports cars, and carry higher cargo insurance limits. We ship Teslas, Rivians, Lucids, Porsches, Mercedes, BMWs, and restored classics out of Bellevue every week.</p>
<p>A note on electric vehicles: they ship like any other car. Have the battery at roughly 30% or more so the driver can load and unload, disable Sentry Mode or similar features that drain the battery and record constantly, and leave a key card or fob with the driver. Open transport is fine for an everyday EV; enclosed is the choice for a new or high-end one.</p>

<h2>How Bellevue car shipping works</h2>
<ol class="numbered">
<li><b>Quote.</b> Use the instant quote tool or call our Bellevue office with your pickup and delivery ZIP codes, your vehicle, and your timing.</li>
<li><b>Book.</b> Approve the price and we assign a vetted carrier on your lane — open or enclosed — and confirm the driver, truck, and pickup window with you. A small deposit holds your spot; the balance is paid at delivery.</li>
<li><b>Pickup and inspection.</b> The driver inspects the car with you, documents its condition on the bill of lading, and loads it. For downtown addresses, this happens at the agreed meeting spot.</li>
<li><b>Transit.</b> You get updates as the car moves and can reach the driver or our office directly.</li>
<li><b>Delivery.</b> Inspect against the bill of lading, sign, pay the balance, and you're done.</li>
</ol>

<h2>Preparing your vehicle for pickup</h2>
<p>Wash the car so the inspection is accurate and photograph all sides. Leave about a quarter tank of fuel (or 30%+ charge for an EV). Remove your Good To Go! toll pass, parking permits, garage openers, and loose items. Fold in mirrors, remove roof boxes and bike racks, and retract antennas. Personal items up to about 100 pounds can ride in the trunk but aren't insured — keep valuables with you. Disable alarms, or show the driver how. If the car has a custom suspension, air ride, or unusually low clearance, tell us at booking so we assign a carrier with a liftgate.</p>

<h2>Corporate relocations and international moves</h2>
<p>We work with Eastside HR teams and relocation companies on employee moves, including bulk bookings and invoicing to the employer. For international assignees, we ship vehicles between Bellevue and the Port of Tacoma or Port of Seattle for ocean carriers, and we can coordinate with your freight forwarder. Call the Bellevue office and ask for a relocation coordinator.</p>

<h2>Visit or call our Bellevue office</h2>
<p>Evergreen Car Shipping's Bellevue location is at 355 118th Ave SE, Suite 790, Bellevue, WA 98005 — just east of I-405 near the I-90 interchange, minutes from downtown, Factoria, and Eastgate. Call <a data-city-tel href="#">(425) 380-2729</a> Monday through Saturday, or get an instant quote online any time. We also have Washington offices in <a href="seattle-car-shipping.html">Seattle</a>, <a href="tacoma-car-shipping.html">Tacoma</a>, and <a href="spokane-car-shipping.html">Spokane</a>.</p>
"""),

 dict(slug='tacoma', city='Tacoma', phone='(253) 364-0882', tel='+12533640882', street='705 S 9th St STE 805', zip='98405', lat=47.2549079, lng=-122.4468914,
  map='https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d13977.439111699436!2d-122.4468914!3d47.2549079!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x5490555c98f473e7%3A0xd3f8d9fb4a30460b!2sEvergreen%20Car%20Shipping!5e1!3m2!1sen!2sus!4v1791567877240!5m2!1sen!2sus',
  title='Tacoma Car Shipping &amp; JBLM Auto Transport | Evergreen',
  desc='Licensed, insured Tacoma car shipping. JBLM military PCS moves, open & enclosed door-to-door transport nationwide. Call (253) 364-0882.',
  h1='Tacoma Car Shipping &amp; Auto Transport',
  tagline='Licensed, insured vehicle shipping from Tacoma, Pierce County, and Joint Base Lewis-McChord to anywhere in the United States — from a local office downtown.',
  areas=['Downtown Tacoma','North End','Stadium District','Proctor','Old Town','Hilltop','South Tacoma','East Tacoma','Lakewood','University Place','Fircrest','Puyallup','Gig Harbor','Federal Way','DuPont','Steilacoom','Parkland','Spanaway','Sumner','Olympia'],
  routes=[('Tacoma → San Diego, CA (Naval Base)','1,250 mi','4–6 days'),('Tacoma → Los Angeles, CA','1,120 mi','3–5 days'),('Tacoma → Phoenix, AZ','1,400 mi','4–6 days'),('Tacoma → Colorado Springs, CO','1,350 mi','4–6 days'),('Tacoma → El Paso, TX (Fort Bliss)','1,700 mi','5–7 days'),('Tacoma → Killeen, TX (Fort Cavazos)','2,150 mi','6–8 days'),('Tacoma → Fayetteville, NC (Fort Liberty)','2,900 mi','8–10 days'),('Tacoma → Columbus, GA (Fort Moore)','2,700 mi','8–10 days'),('Tacoma → Norfolk, VA','2,900 mi','8–10 days'),('Tacoma → Honolulu, HI (via port)','ocean','call for schedule')],
  faq=[('How much does it cost to ship a car from Tacoma?','For a sedan on an open carrier, roughly $650–$900 to California, $900–$1,300 to Arizona, Colorado, or Texas, and $1,300–$1,800 to the Southeast and East Coast. Active-duty military receive a discount. The quote tool on this page gives an exact, all-in price in about 30 seconds.'),
       ('Do you offer military discounts for JBLM PCS moves?','Yes. Active-duty service members get a discount on every shipment, and we can work around report dates, orders, and deployments. We handle Fort Lewis and McChord Field moves to every major installation in the country.'),
       ('Can you pick up on base at JBLM?','Carriers generally can\'t enter the installation. We\'ll arrange pickup at your off-base housing or at a convenient spot just outside the gate — DuPont, Lakewood, and the Madigan area are common meeting points.'),
       ('Do you ship cars from Tacoma to Alaska or Hawaii?','Yes. The Port of Tacoma is the primary departure point for vehicles going to Alaska and Hawaii. We handle the door-to-port leg and coordinate with the ocean carrier, or quote the full door-to-door move. Call the Tacoma office for current sailing schedules.'),
       ('How long does car shipping from Tacoma take?','Pickup is usually scheduled within 1–5 days of booking. Once loaded, California runs take 3–5 days, the Southwest and Rockies 4–6 days, and the Southeast and East Coast 8–10 days.')],
  body="""
<h2>Car shipping in Tacoma, Pierce County, and JBLM</h2>
<p>Tacoma moves more vehicles per resident than almost any city in the Pacific Northwest, and the reason is simple: Joint Base Lewis-McChord. Tens of thousands of soldiers, airmen, and families PCS in and out of JBLM every year, and most of them need a car shipped. Add the Port of Tacoma — the departure point for vehicles going to Alaska and Hawaii — plus University of Puget Sound and PLU students, families relocating along the I-5 corridor, and retirees heading south for the winter, and Tacoma is a city that needs a reliable local auto transport partner. Evergreen Car Shipping's Tacoma office, on South 9th Street downtown, is that partner.</p>
<p>We are a licensed and bonded auto transport broker working with a vetted network of FMCSA-registered carriers that run I-5, SR-16, SR-167, and every major lane out of the South Sound every week. When you book with our Tacoma team, we match your vehicle with a carrier already headed your way, verify their insurance and safety record, lock in an all-in price, and manage the shipment from your driveway to your destination.</p>

<h2>Why Tacoma and JBLM families choose Evergreen Car Shipping</h2>
<p>Military moves run on orders and report dates, not on a carrier's convenience. Our Tacoma office is built around that reality. We know how to time a pickup around a final-out date, how to ship a car to a gaining installation before the family arrives, and what to do when orders change. And every shipment, military or civilian, comes with one local number — <a data-city-tel href="#">(253) 364-0882</a> — that reaches someone who knows your car.</p>
<ul class="checks">
<li>{CHECK}<b>Military discounts and PCS expertise.</b> Active-duty pricing on every shipment, flexible scheduling around orders, and experience with every major installation from Fort Liberty to Fort Cavazos to Naval Base San Diego.</li>
<li>{CHECK}<b>Port of Tacoma shipping.</b> Door-to-port and door-to-door moves to Alaska and Hawaii, coordinated with the ocean carriers.</li>
<li>{CHECK}<b>All-in pricing.</b> The quote is the price. No dispatch fees, no fuel surcharges, no surprise balance at delivery.</li>
<li>{CHECK}<b>Door-to-door across Pierce County.</b> Tacoma, Lakewood, University Place, Puyallup, Gig Harbor, DuPont, and beyond.</li>
<li>{CHECK}<b>Open and enclosed carriers, fully insured.</b> Affordable open transport for daily drivers, enclosed for classics and high-value vehicles, cargo insurance on every truck.</li>
</ul>

<h2>Tacoma neighborhoods and South Sound communities we serve</h2>
<p>Our Tacoma auto transport service covers the city, all of Pierce County, and the South Sound down to Olympia. Carriers regularly pick up and deliver in {AREAS}, and the surrounding communities along I-5, SR-16, and SR-167. Gig Harbor and the Key Peninsula across the Narrows Bridge are routine for us, as are the Puyallup Valley and the South Hill area.</p>
<p>Tacoma's older neighborhoods — the North End, Stadium District, and Proctor — have narrow streets and mature trees that a 75-foot car hauler can't always navigate. When that's the case, your driver will call ahead and meet you nearby with room to load: a wide arterial like 6th Avenue or Pearl Street, a large retail lot, or a park-and-ride. It's routine and usually within a mile of your door.</p>

<h2>Popular car shipping routes from Tacoma</h2>
<p>Military lanes dominate: Tacoma to San Diego, El Paso, Killeen, Colorado Springs, Fayetteville, Columbus, Norfolk, and Honolulu run constantly as families PCS between installations. Civilian lanes to California, Arizona, and the East Coast follow the same corridors. Typical transit times once your vehicle is loaded:</p>
{ROUTES}
<p>Shipping a car to Tacoma? Inbound PCS moves to JBLM are as common as outbound ones, and we ship vehicles into the area from every major installation. Every lane runs both directions.</p>

<h2>What it costs to ship a car from Tacoma</h2>
<p>Tacoma car shipping cost depends on distance, vehicle size and weight, open versus enclosed transport, whether the vehicle runs, and your flexibility on pickup dates. For a sedan on an open carrier, expect roughly $650–$900 to California, $900–$1,300 to Arizona, Colorado, or Texas, and $1,300–$1,800 to North Carolina, Georgia, Virginia, or the Northeast. Trucks and SUVs — and there are a lot of lifted trucks in Pierce County — add $100–$300 depending on size and modifications. Enclosed transport runs 40–60% more than open. A non-running vehicle adds about $150 for a winch.</p>
<p>Summer PCS season (May through August) is the busiest time of year on military lanes; booking two to three weeks ahead gets the best price and the most pickup options. Giving the carrier a two- or three-day pickup window instead of a single date also lowers your rate. The instant quote tool at the top of this page gives an exact, all-in price in about 30 seconds — and the military discount is applied when you book.</p>

<h2>Military PCS car shipping from JBLM</h2>
<p>Here's how a typical PCS shipment works with us. Call or get a quote as soon as you have orders, even if dates are tentative — we'll hold a price and adjust the schedule as things firm up. Since carriers can't enter the installation, we arrange pickup at your off-base housing or a meeting point near the gate in DuPont, Lakewood, or near Madigan. If you're flying ahead of the car, we can deliver to a family member, a friend, or your new unit's area and coordinate payment with you remotely. If orders change, call us; we re-route rather than charge you to start over.</p>
<p>The government reimburses privately owned vehicle shipping only in specific cases (OCONUS moves, for example). For most CONUS PCS moves the cost is yours, which is why we keep the military discount simple and apply it to every active-duty booking. Keep your bill of lading and receipt for your records.</p>

<h2>Shipping to Alaska and Hawaii from the Port of Tacoma</h2>
<p>The Port of Tacoma is the main gateway for vehicles headed to Anchorage and Honolulu. We handle the land leg — picking up your car anywhere in Washington and delivering it to the ocean carrier's terminal — and coordinate the booking with the shipping line. Sailings run weekly, and the car needs to arrive at the port a few days before departure with a quarter tank or less of fuel and no personal items (ocean carriers are strict about this). Call the Tacoma office and we'll walk you through the schedule, the documents the port needs, and the full door-to-door cost.</p>

<h2>How Tacoma car shipping works</h2>
<ol class="numbered">
<li><b>Quote.</b> Use the instant quote tool or call the Tacoma office with your ZIP codes, vehicle, and timing.</li>
<li><b>Book.</b> Approve the price and we assign a vetted carrier, confirm the driver and pickup window, and apply any military discount. A small deposit holds your spot; the balance is paid at delivery.</li>
<li><b>Pickup.</b> The driver inspects the car with you, documents its condition on the bill of lading, and loads it.</li>
<li><b>Transit.</b> Updates as the car moves; reach the driver or our office any time.</li>
<li><b>Delivery.</b> Inspect, sign, pay the balance, done — or have a family member receive it if you've already reported.</li>
</ol>

<h2>Preparing your vehicle for transport</h2>
<p>Wash the car and photograph all sides so the inspection is accurate. Leave about a quarter tank of fuel. Remove toll passes, base decals you no longer need, parking permits, and loose items. Fold in mirrors, remove roof racks and bike carriers, and retract antennas. Personal items up to about 100 pounds can ride in the trunk on domestic shipments (none for ocean shipments) but aren't insured. If your truck is lifted or has oversized tires, tell us at booking so we assign a carrier with the right clearance.</p>

<h2>Visit or call our Tacoma office</h2>
<p>Evergreen Car Shipping's Tacoma location is at 705 S 9th St, Suite 805, Tacoma, WA 98405 — downtown, a few blocks from the Tacoma Dome and I-705, about 15 minutes from the JBLM main gate. Call <a data-city-tel href="#">(253) 364-0882</a> Monday through Saturday, or get an instant quote online any time. We also have Washington offices in <a href="seattle-car-shipping.html">Seattle</a>, <a href="bellevue-car-shipping.html">Bellevue</a>, and <a href="spokane-car-shipping.html">Spokane</a>.</p>
"""),
 dict(slug='everett', city='Everett', phone='(425) 532-3379', tel='+14255323379', street='3216 Wetmore Ave #808', zip='98201', lat=47.9745854, lng=-122.207443,
  map='https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d13786.381537177405!2d-122.207443!3d47.9745854!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x549aab17da2b192f%3A0x3361f53d0e38785!2sEvergreen%20Car%20Shipping!5e1!3m2!1sen!2sus!4v1791567905469!5m2!1sen!2sus',
  title='Everett Car Shipping &amp; Auto Transport | Evergreen',
  desc='Licensed, insured Everett car shipping. Navy PCS and Boeing relocations, open & enclosed door-to-door transport nationwide. Call (425) 532-3379.',
  h1='Everett Car Shipping &amp; Auto Transport',
  tagline='Licensed, insured vehicle shipping from Everett and Snohomish County to anywhere in the U.S. — from a local office downtown on Wetmore Avenue.',
  areas=['Downtown Everett','North Everett','Port Gardner','Silver Lake','Mill Creek','Lynnwood','Mukilteo','Marysville','Lake Stevens','Snohomish','Monroe','Bothell','Edmonds','Mountlake Terrace','Arlington','Stanwood','Granite Falls','Tulalip','Mount Vernon','Whidbey Island'],
  routes=[('Everett → San Diego, CA (Naval Base)','1,290 mi','4–6 days'),('Everett → Los Angeles, CA','1,160 mi','3–5 days'),('Everett → San Francisco Bay Area','840 mi','2–4 days'),('Everett → Phoenix, AZ','1,450 mi','4–6 days'),('Everett → Denver, CO','1,350 mi','4–6 days'),('Everett → Norfolk, VA (Naval Station)','2,900 mi','8–10 days'),('Everett → Jacksonville, FL (NAS)','3,100 mi','9–11 days'),('Everett → Charleston, SC','2,950 mi','8–10 days'),('Everett → Chicago, IL','2,080 mi','6–8 days'),('Everett → New York, NY','2,870 mi','8–10 days')],
  faq=[('How much does it cost to ship a car from Everett?','For a sedan on an open carrier, roughly $650–$950 to California, $900–$1,350 to Arizona, Colorado, or Texas, and $1,350–$1,850 to the East Coast. Active-duty Navy and other service members receive a discount. The quote tool on this page gives an exact, all-in price.'),
       ('Do you handle Naval Station Everett PCS moves?','Yes. We ship for sailors and families moving between Naval Station Everett and San Diego, Norfolk, Jacksonville, Pearl Harbor, and every other Navy installation. We work around report dates and offer a military discount. Carriers can\'t enter the base, so pickup happens at your housing or a spot near the gate.'),
       ('Can you pick up in Mukilteo, Marysville, or Lake Stevens?','Yes. Our Everett office covers all of Snohomish County and south Skagit County. Suburban addresses are usually reachable by a full-size hauler; where streets are tight, the driver arranges a nearby meeting spot.'),
       ('Do you ship from Whidbey Island or Camano Island?','Yes. Carriers generally don\'t ride the ferry, so for Whidbey we arrange a meeting point on the mainland in Mukilteo or at the north end via the Deception Pass bridge; Camano Island is reachable by road via Stanwood.'),
       ('How long does car shipping from Everett take?','Pickup is usually scheduled within 1–5 days of booking. Once loaded, California runs take 3–5 days, the Southwest and Rockies 4–6 days, and the East Coast 8–10 days.')],
  body="""
<h2>Car shipping in Everett and Snohomish County</h2>
<p>Everett is the northern anchor of the Puget Sound metro — home to Naval Station Everett, the Boeing Everett factory, Paine Field, and a fast-growing population spread from Mukilteo and Mill Creek up to Marysville and Lake Stevens. All of that generates a steady need for vehicle shipping: sailors and families moving between Navy installations, aerospace engineers relocating for work, Everett Community College and WSU Everett students, families moving in and out along I-5, and retirees heading south for the winter. Evergreen Car Shipping's Everett office, on Wetmore Avenue downtown, is the local point of contact for all of it.</p>
<p>We are a licensed and bonded auto transport broker. We don't run our own trucks; we work with a vetted network of FMCSA-registered carriers that run I-5 between Vancouver, B.C. and California, I-90 east over the Cascades, and every major lane out of the Puget Sound region every week. When you book with our Everett team, we match your vehicle with a carrier already headed your direction, verify their insurance and safety record, lock in an all-in price, and manage the shipment door to door.</p>

<h2>Why Everett customers choose Evergreen Car Shipping</h2>
<p>Everett sits at the north end of the Seattle metro, and national brokers tend to treat it as an afterthought — "we'll get a truck up there eventually." We don't. Because carriers heading south from the Canadian border and from Skagit County pass directly through Everett, we book pickups here as readily as in Seattle. And every shipment comes with one local number — <a data-city-tel href="#">(425) 532-3379</a> — that reaches someone who knows your car.</p>
<ul class="checks">
<li>{CHECK}<b>Navy and military expertise.</b> Active-duty discounts, scheduling around orders and deployments, and experience with every major Navy installation from San Diego to Norfolk.</li>
<li>{CHECK}<b>All-in pricing.</b> The quote is the price. No dispatch fees, no fuel surcharges, no surprise balance at delivery.</li>
<li>{CHECK}<b>Door-to-door across Snohomish County.</b> Everett, Mukilteo, Lynnwood, Mill Creek, Marysville, Lake Stevens, Snohomish, Monroe, Arlington, and beyond.</li>
<li>{CHECK}<b>Open and enclosed carriers.</b> Affordable open transport for daily drivers; enclosed trailers for classics, collector cars, and high-value vehicles.</li>
<li>{CHECK}<b>Fully insured, fully documented.</b> Cargo insurance on every truck and a bill of lading inspection at pickup and delivery.</li>
</ul>

<h2>Everett neighborhoods and Snohomish County communities we serve</h2>
<p>Our Everett auto transport service covers the city, all of Snohomish County, and the southern part of Skagit County. Carriers regularly pick up and deliver in {AREAS}, and the rural areas along US-2 and SR-9. Farm addresses out toward Snohomish and Monroe are fine; if a driveway can't handle a semi, the driver meets you on the nearest paved road or in town.</p>
<p>Older parts of North Everett and the Port Gardner neighborhood have narrow streets and mature trees that a 75-foot hauler can't always navigate. When that's the case, your driver will call ahead and meet you nearby with room to load safely — Broadway, Evergreen Way, a large retail lot near the Everett Mall, or a park-and-ride. It's routine and usually within a mile or two of your door. Whidbey Island customers: carriers don't ride the ferry, so we'll arrange a meeting point in Mukilteo or at the north end of the island.</p>

<h2>Popular car shipping routes from Everett</h2>
<p>Naval Station Everett makes the Navy lanes the busiest ones out of this office: San Diego, Norfolk, Jacksonville, Charleston, and Pearl Harbor (via the Port of Tacoma). Civilian lanes to California, Arizona, Colorado, and the East Coast follow the same I-5 and I-90 corridors. Typical transit times once your vehicle is loaded:</p>
{ROUTES}
<p>Shipping a car to Everett? Inbound Navy moves and Boeing relocations are just as common as outbound ones. Every lane runs both directions at similar pricing.</p>

<h2>What it costs to ship a car from Everett</h2>
<p>Everett car shipping cost depends on distance, vehicle size and weight, open versus enclosed transport, whether the vehicle runs, and your flexibility on pickup dates. For a sedan on an open carrier, expect roughly $650–$950 to California, $900–$1,350 to Arizona, Colorado, or Texas, and $1,350–$1,850 to Virginia, Florida, or the Northeast. SUVs and pickups add $100–$300. Enclosed transport runs 40–60% more than open. A non-running vehicle adds about $150 for a winch.</p>
<p>Summer is peak season on Navy lanes and for family relocations; booking two to three weeks ahead gets the best price and the most pickup options. Giving the carrier a two- or three-day pickup window instead of a single date also lowers your rate. The instant quote tool at the top of this page gives an exact, all-in price in about 30 seconds — no obligation.</p>

<h2>Navy PCS car shipping from Naval Station Everett</h2>
<p>Here's how a typical Navy move works with us. Get a quote as soon as you have orders, even if dates are tentative — we'll hold a price and adjust the schedule as things firm up. Carriers can't enter the installation, so we arrange pickup at your off-base housing or a convenient spot near the gate on West Marine View Drive. If you're flying ahead of the car or deploying, we can deliver to a spouse, family member, or your new command's area and handle payment with you remotely. If orders change, call us and we re-route rather than start over. For Pearl Harbor and other OCONUS moves, we handle the land leg to the Port of Tacoma and coordinate with the ocean carrier.</p>

<h2>Boeing and aerospace relocations</h2>
<p>The Boeing Everett plant and the supplier network around Paine Field move engineers and technicians in and out constantly — to Charleston, Renton, St. Louis, Arizona, and beyond. We work with relocating employees and HR teams on individual and bulk vehicle moves, including invoicing to the employer when a relocation package covers it. Tell us your start date and we'll work backward to a pickup window that gets the car there when you do.</p>

<h2>How Everett car shipping works</h2>
<ol class="numbered">
<li><b>Quote.</b> Use the instant quote tool or call the Everett office with your ZIP codes, vehicle, and timing.</li>
<li><b>Book.</b> Approve the price and we assign a vetted carrier, confirm the driver and pickup window, and apply any military discount. A small deposit holds your spot; the balance is paid at delivery.</li>
<li><b>Pickup.</b> The driver inspects the car with you, documents its condition on the bill of lading, and loads it.</li>
<li><b>Transit.</b> Updates as the car moves; reach the driver or our office any time.</li>
<li><b>Delivery.</b> Inspect, sign, pay the balance, done.</li>
</ol>

<h2>Preparing your vehicle for transport</h2>
<p>Wash the car and photograph all sides so the inspection is accurate. Leave about a quarter tank of fuel. Remove your Good To Go! toll pass, base decals, parking permits, and loose items. Fold in mirrors, remove roof racks, bike carriers, and kayak mounts, and retract antennas. Personal items up to about 100 pounds can ride in the trunk but aren't insured — keep valuables with you. If your truck is lifted or your car is lowered, tell us at booking so we assign a carrier with the right clearance.</p>

<h2>Snowbirds and seasonal moves from Snohomish County</h2>
<p>Every fall, a wave of Snohomish County retirees heads for Arizona, Palm Springs, and Florida, and we move their cars so they can fly. October and November are the busiest southbound months; March and April are busiest coming back. Book two to three weeks ahead for the best rate, and if you're shipping two vehicles, ask about a multi-car discount — they'll usually ride the same truck.</p>

<h2>Visit or call our Everett office</h2>
<p>Evergreen Car Shipping's Everett location is at 3216 Wetmore Ave, Suite 808, Everett, WA 98201 — downtown, a few blocks from the Snohomish County Courthouse and Angel of the Winds Arena, minutes from I-5. Call <a data-city-tel href="#">(425) 532-3379</a> Monday through Saturday, or get an instant quote online any time. We also have Washington offices in <a href="seattle-car-shipping.html">Seattle</a>, <a href="bellevue-car-shipping.html">Bellevue</a>, <a href="tacoma-car-shipping.html">Tacoma</a>, and <a href="spokane-car-shipping.html">Spokane</a>.</p>
"""),

 dict(slug='kent', city='Kent', phone='(253) 364-5448', tel='+12533645448', street='555 W Smith St #440', zip='98032', lat=47.3835608, lng=-122.2386922,
  map='https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d13943.44577747343!2d-122.2386922!3d47.3835608!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x54905b91e6f536ad%3A0xb2f5f718e537e7de!2sEvergreen%20Car%20Shipping!5e1!3m2!1sen!2sus!4v1791567912902!5m2!1sen!2sus',
  title='Kent Car Shipping &amp; Auto Transport | Evergreen',
  desc='Licensed, insured Kent car shipping. Door-to-door open & enclosed auto transport from South King County to all 50 states. Call (253) 364-5448.',
  h1='Kent Car Shipping &amp; Auto Transport',
  tagline='Licensed, insured vehicle shipping from Kent and South King County to anywhere in the U.S. — from a local office on West Smith Street in downtown Kent.',
  areas=['Downtown Kent','East Hill','West Hill','Kent Valley','Panther Lake','Lake Meridian','Auburn','Covington','Maple Valley','Des Moines','SeaTac','Federal Way','Tukwila','Renton','Burien','Black Diamond','Enumclaw','Algona','Pacific','Normandy Park'],
  routes=[('Kent → Los Angeles, CA','1,145 mi','3–5 days'),('Kent → San Francisco Bay Area','825 mi','2–4 days'),('Kent → Las Vegas, NV','1,150 mi','3–5 days'),('Kent → Phoenix, AZ','1,430 mi','4–6 days'),('Kent → Salt Lake City, UT','850 mi','2–4 days'),('Kent → Denver, CO','1,330 mi','4–6 days'),('Kent → Houston, TX','2,350 mi','6–8 days'),('Kent → Atlanta, GA','2,650 mi','7–9 days'),('Kent → Chicago, IL','2,070 mi','6–8 days'),('Kent → New York, NY','2,860 mi','8–10 days')],
  faq=[('How much does it cost to ship a car from Kent?','For a sedan on an open carrier, roughly $650–$900 to California or Nevada, $900–$1,300 to Arizona, Utah, Colorado, or Texas, and $1,300–$1,800 to the Southeast and East Coast. Trucks and SUVs add $100–$300. The quote tool on this page gives an exact, all-in price in about 30 seconds.'),
       ('Why is Kent a good place to ship a car from?','The Kent Valley is the largest warehouse and distribution district in the Pacific Northwest, so trucks — including car haulers — are in and out constantly. Wide industrial streets and easy access to I-5, SR-167, and SR-18 make pickups fast and simple, and the volume keeps prices competitive.'),
       ('Do you serve Auburn, Covington, and Maple Valley?','Yes. Our Kent office covers all of South King County, from Des Moines and Federal Way on the west to Covington, Maple Valley, Black Diamond, and Enumclaw on the east.'),
       ('Can you pick up a car I bought at an auction or dealer in Kent?','Yes. We ship from dealers, auctions, and warehouses in the Kent Valley every week. Give us the business name and a contact, and we\'ll coordinate pickup directly with them so you don\'t have to be there.'),
       ('How long does car shipping from Kent take?','Pickup is usually scheduled within 1–4 days of booking — faster than average because of truck volume in the valley. Once loaded, California runs take 3–5 days, the Southwest and Rockies 4–6 days, and the East Coast 8–10 days.')],
  body="""
<h2>Car shipping in Kent and South King County</h2>
<p>Kent is the working heart of South King County — the Kent Valley is the largest industrial and distribution district in the Northwest, Boeing Space &amp; Defense and Blue Origin are headquartered here, and the surrounding neighborhoods on East Hill and West Hill, plus Auburn, Covington, Maple Valley, Des Moines, and Federal Way, make up one of the most diverse and fastest-growing parts of the Seattle metro. Families move in and out constantly, car buyers pick up vehicles from the valley's dealers and auctions, and plenty of residents head south for the winter. Evergreen Car Shipping's Kent office, on West Smith Street downtown, is the local point of contact for all of it.</p>
<p>We are a licensed and bonded auto transport broker working with a vetted network of FMCSA-registered carriers that run I-5, SR-167, SR-18, and every major lane out of the Puget Sound region every week. Because the Kent Valley is already full of trucks, carriers are happy to pick up here — which means fast scheduling and competitive pricing. When you book with our Kent team, we match your vehicle with a carrier already headed your direction, verify their insurance and safety record, lock in an all-in price, and manage the shipment door to door.</p>

<h2>Why Kent customers choose Evergreen Car Shipping</h2>
<p>South King County residents are practical. They want a fair price, a straight answer, and a car that shows up when promised. That's what we're built for. One local number — <a data-city-tel href="#">(253) 364-5448</a> — reaches someone in our Kent office who knows your shipment. One all-in price, confirmed before you commit. And a carrier roster we've vetted so you don't have to.</p>
<ul class="checks">
<li>{CHECK}<b>Fast pickups.</b> Truck volume in the Kent Valley means we usually schedule pickup within 1–4 days, often faster than anywhere else in the region.</li>
<li>{CHECK}<b>All-in pricing.</b> The quote is the price. No dispatch fees, no fuel surcharges, no surprise balance at delivery.</li>
<li>{CHECK}<b>Door-to-door across South King County.</b> Kent, Auburn, Covington, Maple Valley, Des Moines, Federal Way, Tukwila, Renton, and more.</li>
<li>{CHECK}<b>Dealer and auction pickups.</b> We coordinate directly with the seller so you don't have to be there.</li>
<li>{CHECK}<b>Open and enclosed, fully insured.</b> Affordable open transport for daily drivers, enclosed for classics and high-value vehicles, cargo insurance on every truck.</li>
</ul>

<h2>Kent neighborhoods and South King County communities we serve</h2>
<p>Our Kent auto transport service covers the city and all of South King County. Carriers regularly pick up and deliver in {AREAS}, and the rural areas out toward the Green River and the foothills. The valley floor is the easiest place in the region for a car hauler to operate — wide streets, big lots, easy freeway access. East Hill and West Hill neighborhoods are mostly accessible too; where a cul-de-sac or steep street is a problem, the driver will call ahead and meet you at a nearby shopping center or arterial. It's routine and usually within a mile.</p>

<h2>Popular car shipping routes from Kent</h2>
<p>Lanes out of Kent follow the I-5 corridor south to California and the Southwest, and I-90 east to the Rockies, Midwest, and East Coast. We also see a lot of Kent-to-Las Vegas, Kent-to-Houston, and Kent-to-Atlanta traffic from families relocating. Typical transit times once your vehicle is loaded:</p>
{ROUTES}
<p>Shipping a car to Kent? Inbound vehicles from California, Texas, and the Southeast — new residents, returning snowbirds, and online car purchases — arrive through our Kent office constantly. Every lane runs both directions.</p>

<h2>What it costs to ship a car from Kent</h2>
<p>Kent car shipping cost depends on distance, vehicle size and weight, open versus enclosed transport, whether the vehicle runs, and your flexibility on pickup dates. For a sedan on an open carrier, expect roughly $650–$900 to California or Nevada, $900–$1,300 to Arizona, Utah, Colorado, or Texas, and $1,300–$1,800 to Georgia, Florida, or the Northeast. Pickups and SUVs — and South King County has plenty of full-size trucks — add $100–$300 depending on size and lift. Enclosed transport runs 40–60% more than open. A non-running vehicle adds about $150 for a winch.</p>
<p>Summer is peak season; booking two weeks ahead gets the best price and the most pickup options. Giving the carrier a two- or three-day pickup window instead of a single date also lowers your rate. The instant quote tool at the top of this page gives an exact, all-in price in about 30 seconds — no obligation.</p>

<h2>Shipping a car you bought in the Kent Valley</h2>
<p>The Kent Valley and the Auburn auto row are full of dealers, wholesalers, and auction lots, and we ship vehicles out of them every week for buyers across the country. Here's how it works: give us the seller's business name, address, and a contact, and we coordinate pickup directly with them. The driver inspects the car at pickup and documents its condition on the bill of lading, so you have an independent record before it ever leaves the lot. Tell us if the car is non-running or has no keys and we'll assign a carrier with a winch. Payment to the seller is between you and them; we handle the transport.</p>

<h2>Open vs. enclosed transport</h2>
<p>Open transport is the standard — the two-level haulers you see on I-5 carrying new cars to dealerships. It's safe, it's the most affordable, and it's what most Kent customers choose. Enclosed transport puts your vehicle inside a hard-sided trailer, protected from rain, gravel, and road grime. We recommend it for classics, restorations, luxury and exotic cars, and anything you'd rather keep out of sight. Enclosed carriers run the I-5 corridor regularly, so availability from Kent is good.</p>

<h2>How Kent car shipping works</h2>
<ol class="numbered">
<li><b>Quote.</b> Use the instant quote tool or call the Kent office with your ZIP codes, vehicle, and timing.</li>
<li><b>Book.</b> Approve the price and we assign a vetted carrier and confirm the driver, truck, and pickup window with you. A small deposit holds your spot; the balance is paid at delivery.</li>
<li><b>Pickup.</b> The driver inspects the car with you (or with the seller), documents its condition on the bill of lading, and loads it.</li>
<li><b>Transit.</b> Updates as the car moves; reach the driver or our office any time.</li>
<li><b>Delivery.</b> Inspect, sign, pay the balance, done.</li>
</ol>

<h2>Preparing your vehicle for transport</h2>
<p>Wash the car and photograph all sides so the inspection is accurate. Leave about a quarter tank of fuel. Remove your Good To Go! toll pass, parking permits, and loose items. Fold in mirrors, remove roof racks and bike carriers, and retract antennas. Personal items up to about 100 pounds can ride in the trunk but aren't insured — keep valuables with you. If your truck is lifted, has oversized tires, or a canopy, tell us at booking so we assign a carrier with the right clearance and deck space.</p>

<h2>Military, student, and snowbird shipping from South King County</h2>
<p>With Joint Base Lewis-McChord a short drive south, we handle PCS moves from South King County regularly and offer an active-duty discount. For Green River College and Highline College students, and for families sending a car to a student out of state, we coordinate pickup and delivery with whoever's on each end. Snowbirds heading to Arizona, Palm Springs, or Texas should book in early fall — October and November are the busiest southbound months.</p>

<h2>Visit or call our Kent office</h2>
<p>Evergreen Car Shipping's Kent location is at 555 W Smith St, Suite 440, Kent, WA 98032 — downtown, near Kent Station and the Sounder stop, minutes from SR-167 and I-5. Call <a data-city-tel href="#">(253) 364-5448</a> Monday through Saturday, or get an instant quote online any time. We also have Washington offices in <a href="seattle-car-shipping.html">Seattle</a>, <a href="renton-car-shipping.html">Renton</a>, <a href="tacoma-car-shipping.html">Tacoma</a>, and <a href="bellevue-car-shipping.html">Bellevue</a>.</p>
"""),

 dict(slug='yakima', city='Yakima', phone='(509) 428-7152', tel='+15094287152', street='307 N 3rd St #699', zip='98901', lat=46.6073502, lng=-120.50473,
  map='https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d14147.466603146273!2d-120.50473!3d46.6073502!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x5499d7bfd0e56153%3A0x38155c6d81477c2d!2sEvergreen%20Car%20Shipping!5e1!3m2!1sen!2sus!4v1791567921709!5m2!1sen!2sus',
  title='Yakima Car Shipping &amp; Auto Transport | Evergreen',
  desc='Licensed, insured Yakima car shipping. Door-to-door open & enclosed auto transport from Central Washington nationwide. Call (509) 428-7152.',
  h1='Yakima Car Shipping &amp; Auto Transport',
  tagline='Licensed, insured vehicle shipping from Yakima and Central Washington to anywhere in the country — from a local office downtown on North 3rd Street.',
  areas=['Downtown Yakima','West Valley','Terrace Heights','Nob Hill','Union Gap','Selah','Moxee','Naches','Wapato','Toppenish','Zillah','Sunnyside','Grandview','Prosser','Ellensburg','Cle Elum','Goldendale','Tri-Cities','Richland','Kennewick'],
  routes=[('Yakima → Seattle, WA','145 mi','1 day'),('Yakima → Portland, OR','185 mi','1–2 days'),('Yakima → Spokane, WA','200 mi','1–2 days'),('Yakima → Boise, ID','400 mi','1–3 days'),('Yakima → San Francisco Bay Area','780 mi','2–4 days'),('Yakima → Los Angeles, CA','1,070 mi','3–5 days'),('Yakima → Phoenix, AZ','1,360 mi','4–6 days'),('Yakima → Denver, CO','1,180 mi','3–5 days'),('Yakima → Dallas, TX','1,950 mi','6–8 days'),('Yakima → Chicago, IL','1,950 mi','6–8 days')],
  faq=[('How much does it cost to ship a car from Yakima?','For a sedan on an open carrier, roughly $350–$550 to Seattle, Portland, or Spokane, $800–$1,100 to Boise, Salt Lake, or Denver, $900–$1,300 to California and Arizona, and $1,300–$1,800 to Texas, the Midwest, and the East Coast. The quote tool on this page gives an exact, all-in price.'),
       ('How long does car shipping from Yakima take?','Pickup is typically scheduled within 2–6 days — a bit longer than Seattle because fewer carriers originate in Central Washington. Once loaded, Seattle and Portland are 1 day, the Mountain West 2–5 days, and the East Coast 7–10 days.'),
       ('Do you serve the Lower Valley and the Tri-Cities?','Yes. Our Yakima office covers the whole Yakima Valley — Union Gap, Wapato, Toppenish, Zillah, Sunnyside, Grandview, Prosser — plus Ellensburg, Goldendale, and the Tri-Cities. Valley pickups are often bundled with Yakima loads to keep prices down.'),
       ('Can you ship a car from Yakima over the passes in winter?','Yes. Carriers run I-82, I-90, and US-97 year-round. Snoqualmie and White Pass closures can occasionally add a day, and we build that into the schedule. Enclosed transport keeps a high-value vehicle out of road salt and gravel.'),
       ('Where will the driver pick up my car in Yakima?','Most Yakima addresses are reachable by a full-size hauler — the valley is flat with wide streets. For orchard or ranch addresses with narrow or gravel roads, the driver meets you on the nearest paved highway or in town.')],
  body="""
<h2>Car shipping in Yakima and Central Washington</h2>
<p>Yakima is the center of Central Washington — the largest city between the Cascades and Spokane, the hub of the Yakima Valley's agricultural economy, and the crossroads of I-82, US-97, and US-12. Families relocate here for work in agriculture, healthcare, and the Yakima Training Center; Yakima Valley College and Central Washington University students in nearby Ellensburg come and go every semester; and a lot of residents head south to Arizona and California for the winter. All of them need a reliable way to move a vehicle without driving it. Evergreen Car Shipping's Yakima office, on North 3rd Street downtown, is the local point of contact.</p>
<p>We are a licensed and bonded auto transport broker working with a vetted network of FMCSA-registered carriers that run I-82 and I-90 between the Puget Sound and the rest of the country, US-97 north to Wenatchee and south to Oregon, and the lanes toward Boise and the Southwest. When you book with our Yakima team, we match your vehicle with a carrier already scheduled through Central Washington, verify their insurance and safety record, lock in an all-in price, and stay with you until delivery.</p>

<h2>Why Yakima customers choose Evergreen Car Shipping</h2>
<p>Central Washington is a different shipping market than the I-5 corridor. Fewer carriers originate here, so who you book with matters. A national call center doesn't know that a Seattle-to-Boise truck comes right through Yakima on I-82, or that a Tri-Cities load can be combined with one from Sunnyside. Our Yakima team does — and that local knowledge turns into shorter pickup windows and better prices. Every shipment comes with one local number — <a data-city-tel href="#">(509) 428-7152</a> — that reaches someone who knows your car.</p>
<ul class="checks">
<li>{CHECK}<b>Local lane knowledge.</b> We know which carriers run I-82 and when, so we can give you an honest pickup window instead of a guess.</li>
<li>{CHECK}<b>All-in pricing.</b> The quote is the price. No pass-crossing surcharges, no dispatch fees, no surprise balance at delivery.</li>
<li>{CHECK}<b>Door-to-door across the valley.</b> Yakima, Selah, Union Gap, West Valley, Terrace Heights, Moxee, the Lower Valley, Ellensburg, and the Tri-Cities.</li>
<li>{CHECK}<b>Open and enclosed carriers.</b> Affordable open transport for daily drivers and farm trucks; enclosed trailers for classics and collector cars.</li>
<li>{CHECK}<b>Fully insured, fully documented.</b> Cargo insurance on every truck and a bill of lading inspection at pickup and delivery.</li>
</ul>

<h2>Yakima neighborhoods and Central Washington communities we serve</h2>
<p>Our Yakima auto transport service covers the city, all of Yakima County, and the surrounding region. Carriers regularly pick up and deliver in {AREAS}, and the orchard and ranch country in between. The valley floor is flat with wide streets, so most addresses are easy for a full-size hauler. For orchard or ranch addresses with narrow or gravel access roads, the driver will arrange to meet you on the nearest paved highway, at a fruit-stand lot, or in town — it's routine.</p>
<p>Because our Yakima office covers such a large area, we frequently combine pickups. A car leaving Sunnyside and one leaving Yakima often ride the same truck, which keeps costs down for both. If you're in the Tri-Cities, Ellensburg, Goldendale, or Wenatchee, call us — we'll tell you honestly what pickup timing looks like for your area.</p>

<h2>Popular car shipping routes from Yakima</h2>
<p>Yakima's strongest lanes run west over the passes to Seattle and Portland, east to Spokane, and south along I-82 and I-84 toward Boise, Salt Lake City, and the Southwest. Carriers crossing the state on I-90 and I-82 pass through regularly. Typical transit times once your vehicle is loaded:</p>
{ROUTES}
<p>Shipping a car to Yakima? Inbound lanes from Seattle, Portland, California, and Arizona are just as common — new residents, returning snowbirds, and vehicles purchased in larger markets all arrive through our Yakima office.</p>

<h2>What it costs to ship a car from Yakima</h2>
<p>Yakima car shipping cost depends on distance, vehicle size, open versus enclosed, whether the vehicle runs, and date flexibility. For a sedan on an open carrier, expect roughly $350–$550 to Seattle, Portland, or Spokane; $800–$1,100 to Boise, Salt Lake City, or Denver; $900–$1,300 to California and Arizona; and $1,300–$1,800 to Texas, the Midwest, and the East Coast. Pickups and SUVs add $100–$300 — and the valley has a lot of full-size trucks. Enclosed transport runs 40–60% more than open. A non-running vehicle adds about $150 for a winch.</p>
<p>One Central Washington tip: flexibility on pickup dates matters more here than in Seattle. Because fewer trucks originate in the valley, giving the carrier a 3–5 day window instead of a single day can noticeably lower your price and speed up assignment. The instant quote tool at the top of this page gives an exact, all-in number in about 30 seconds — no obligation.</p>

<h2>Shipping over the passes in winter</h2>
<p>Getting a car from Yakima to the west side means crossing Snoqualmie Pass on I-90 or White Pass on US-12, and both can close for hours during winter storms. Carriers run year-round, but we plan around weather honestly: if a storm is forecast, we'll tell you it might add a day rather than promise a date we can't keep. For everyday vehicles, open transport is fine; a wash on arrival is all it takes. For a classic, a collector car, or a freshly detailed vehicle, enclosed transport keeps it out of road salt, de-icer, and gravel spray on the passes.</p>

<h2>How Yakima car shipping works</h2>
<ol class="numbered">
<li><b>Quote.</b> Use the instant quote tool or call the Yakima office with your ZIP codes, vehicle, and timing.</li>
<li><b>Book.</b> Approve the price and we assign a vetted carrier and confirm the driver, truck, and pickup window with you. A small deposit holds your spot; the balance is paid at delivery.</li>
<li><b>Pickup.</b> The driver inspects the car with you, documents its condition on the bill of lading, and loads it.</li>
<li><b>Transit.</b> Updates as the car moves; reach the driver or our office any time.</li>
<li><b>Delivery.</b> Inspect, sign, pay the balance, done.</li>
</ol>

<h2>Preparing your vehicle for transport</h2>
<p>Wash the car — orchard dust hides scratches — and photograph all sides so the inspection is accurate. Leave about a quarter tank of fuel. Remove toll tags, parking permits, and loose items. Fold in mirrors, remove roof racks, toolboxes, and bike carriers, and retract antennas. Personal items up to about 100 pounds can ride in the trunk but aren't insured. If your truck is lifted, has a canopy, or oversized tires, tell us at booking so we assign a carrier with the right clearance and deck space.</p>

<h2>Military, student, and snowbird shipping from the Yakima Valley</h2>
<p>The Yakima Training Center brings rotating units through the area, and we handle military moves with an active-duty discount and scheduling around orders. For Yakima Valley College, Heritage University, and CWU students, we ship cars to and from campus every August and May, coordinating with parents on the other end. Valley snowbirds heading to Arizona, Palm Springs, or Texas should book in early fall — October and November are the busiest southbound months, and March and April are busiest coming back.</p>

<h2>Visit or call our Yakima office</h2>
<p>Evergreen Car Shipping's Yakima location is at 307 N 3rd St, Suite 699, Yakima, WA 98901 — downtown, a few blocks from the Capitol Theatre and Yakima Avenue, minutes from I-82. Call <a data-city-tel href="#">(509) 428-7152</a> Monday through Saturday, or get an instant quote online any time. We also have Washington offices in <a href="spokane-car-shipping.html">Spokane</a>, <a href="seattle-car-shipping.html">Seattle</a>, <a href="tacoma-car-shipping.html">Tacoma</a>, and <a href="bellevue-car-shipping.html">Bellevue</a>.</p>
"""),

 dict(slug='renton', city='Renton', phone='(425) 371-5089', tel='+14253715089', street='212 Wells Ave S Unit 1455', zip='98057', lat=47.4790, lng=-122.2060,
  map='https://www.google.com/maps?q=212+Wells+Ave+S,+Renton,+WA+98057&output=embed',
  title='Renton Car Shipping &amp; Auto Transport | Evergreen',
  desc='Licensed, insured Renton car shipping. Door-to-door open & enclosed auto transport to all 50 states. Instant quote or call (425) 371-5089.',
  h1='Renton Car Shipping &amp; Auto Transport',
  tagline='Licensed, insured vehicle shipping from Renton and the south end of Lake Washington to anywhere in the U.S. — from a local office on Wells Avenue in downtown Renton.',
  areas=['Downtown Renton','Renton Highlands','Kennydale','Benson Hill','Cascade','Fairwood','Talbot Hill','East Renton','Newcastle','Tukwila','SeaTac','Skyway','Maple Valley','Kent','Burien','Normandy Park','Mercer Island','Issaquah','Bellevue','Seattle'],
  routes=[('Renton → Los Angeles, CA','1,140 mi','3–5 days'),('Renton → San Francisco Bay Area','820 mi','2–4 days'),('Renton → San Diego, CA','1,260 mi','4–6 days'),('Renton → Phoenix, AZ','1,430 mi','4–6 days'),('Renton → Las Vegas, NV','1,150 mi','3–5 days'),('Renton → Denver, CO','1,320 mi','4–6 days'),('Renton → Austin, TX','2,140 mi','6–8 days'),('Renton → Charleston, SC','2,950 mi','8–10 days'),('Renton → Chicago, IL','2,060 mi','6–8 days'),('Renton → New York, NY','2,850 mi','8–10 days')],
  faq=[('How much does it cost to ship a car from Renton?','For a sedan on an open carrier, roughly $650–$900 to California or Nevada, $900–$1,300 to Arizona, Colorado, or Texas, and $1,300–$1,800 to the Southeast and East Coast. SUVs and trucks add $100–$300; enclosed transport runs 40–60% more. The quote tool on this page gives an exact, all-in price.'),
       ('Can a car hauler get to my house in the Renton Highlands or Fairwood?','Usually, yes — most Renton neighborhoods have streets wide enough for a full-size hauler. Where a cul-de-sac, steep hill, or tight turn is a problem, the driver arranges a nearby meeting spot at The Landing, a park-and-ride, or a wide arterial. It\'s routine.'),
       ('Do you serve Newcastle, Tukwila, and Skyway?','Yes. Our Renton office covers the south end of Lake Washington and the surrounding area — Newcastle, Tukwila, SeaTac, Skyway, Fairwood, Maple Valley, and parts of Kent and Bellevue.'),
       ('I work at Boeing Renton and I\'m relocating — can you work around my start date?','Yes. We handle Boeing and aerospace relocations between Renton, Everett, Charleston, St. Louis, and Arizona regularly, and we plan pickup backward from your report date. Employer invoicing is available when a relocation package covers the move.'),
       ('How long does car shipping from Renton take?','Pickup is usually scheduled within 1–4 days of booking. Once loaded, California runs take 3–5 days, the Southwest and Rockies 4–6 days, and the East Coast 8–10 days.')],
  body="""
<h2>Car shipping in Renton and the south end of Lake Washington</h2>
<p>Renton sits where I-405, I-5, and SR-167 come together at the south tip of Lake Washington — which makes it one of the most convenient places in the Seattle metro to ship a car from. It's also a city on the move: Boeing's 737 factory, the Seahawks' headquarters, The Landing, a booming Highlands, and a steady flow of families relocating between Renton, the Eastside, and South King County. Whether you're a Boeing employee transferring to Charleston, a family moving to Texas, a student heading to school in California, or a snowbird leaving for Arizona, Evergreen Car Shipping's Renton office, on Wells Avenue South downtown, is your local point of contact.</p>
<p>We are a licensed and bonded auto transport broker working with a vetted network of FMCSA-registered carriers that run I-5, I-405, I-90, and every major lane out of the Puget Sound region every week. Renton's freeway access means carriers can pick up here without going out of their way, which keeps scheduling fast and pricing competitive. When you book with our Renton team, we match your vehicle with a carrier already headed your direction, verify their insurance and safety record, lock in an all-in price, and manage the shipment door to door.</p>

<h2>Why Renton customers choose Evergreen Car Shipping</h2>
<p>Renton residents have options — the city is surrounded by shipping companies, lead-gen websites, and national brokers that will sell your request to five different dispatchers. We do it differently. One local number — <a data-city-tel href="#">(425) 371-5089</a> — reaches someone in our Renton office who knows your shipment. One all-in price, confirmed before you commit. And a vetted carrier roster so you never have to wonder who's actually showing up with the truck.</p>
<ul class="checks">
<li>{CHECK}<b>Fast, convenient pickups.</b> Renton's freeway access means carriers reach you quickly; most pickups are scheduled within 1–4 days.</li>
<li>{CHECK}<b>All-in pricing.</b> The quote is the price. No dispatch fees, no fuel surcharges, no surprise balance at delivery.</li>
<li>{CHECK}<b>Door-to-door across the area.</b> Renton, the Highlands, Kennydale, Fairwood, Benson Hill, Newcastle, Tukwila, Skyway, and beyond.</li>
<li>{CHECK}<b>Relocation-friendly scheduling.</b> We plan backward from start dates, lease end dates, and flights, and work with employers on invoicing.</li>
<li>{CHECK}<b>Open and enclosed, fully insured.</b> Affordable open transport for daily drivers, enclosed for classics and high-value vehicles, cargo insurance on every truck.</li>
</ul>

<h2>Renton neighborhoods and nearby communities we serve</h2>
<p>Our Renton auto transport service covers the city and the south end of Lake Washington. Carriers regularly pick up and deliver in {AREAS}, and everywhere in between. Most Renton neighborhoods — the Highlands, Fairwood, Benson Hill, Cascade — have streets wide enough for a full-size hauler. In Kennydale and parts of downtown, steep hills and tight turns can be a problem; when that's the case, your driver will call ahead and meet you at The Landing, a park-and-ride, or a wide arterial like Rainier Avenue or Sunset Boulevard. It's routine and usually within a mile or two of your door.</p>

<h2>Popular car shipping routes from Renton</h2>
<p>Lanes out of Renton follow I-5 south to California, Nevada, and the Southwest, and I-90 east to the Rockies, Midwest, and East Coast. Boeing relocations add steady traffic to Charleston, St. Louis, and Arizona. Typical transit times once your vehicle is loaded:</p>
{ROUTES}
<p>Shipping a car to Renton? Inbound vehicles from California, Texas, and the Southeast — new hires, returning snowbirds, and online car purchases — arrive through our Renton office constantly. Every lane runs both directions at similar pricing.</p>

<h2>What it costs to ship a car from Renton</h2>
<p>Renton car shipping cost depends on distance, vehicle size and weight, open versus enclosed transport, whether the vehicle runs, and your flexibility on pickup dates. For a sedan on an open carrier, expect roughly $650–$900 to California or Nevada, $900–$1,300 to Arizona, Colorado, or Texas, and $1,300–$1,800 to South Carolina, Florida, or the Northeast. SUVs and pickups add $100–$300. Enclosed transport runs 40–60% more than open. A non-running vehicle adds about $150 for a winch.</p>
<p>Summer is peak season; booking two weeks ahead gets the best price and the most pickup options. Giving the carrier a two- or three-day pickup window instead of a single date also lowers your rate. The instant quote tool at the top of this page gives an exact, all-in price in about 30 seconds — no obligation.</p>

<h2>Boeing and corporate relocations from Renton</h2>
<p>The Boeing Renton plant moves engineers, technicians, and managers between Renton, Everett, Charleston, St. Louis, Mesa, and Seattle constantly, and we've built a process around it. Tell us your report date and we work backward to a pickup window that gets the car there when you do — or a few days after, if you'd rather drive a rental the first week. If your relocation package covers vehicle shipping, we can invoice your employer or relocation company directly. If orders change, we re-route rather than start over. The same process works for any corporate move; just call the Renton office and ask for a relocation coordinator.</p>

<h2>Open vs. enclosed transport</h2>
<p>Open transport is the standard — the two-level haulers you see on I-405 carrying new cars to dealerships. It's safe, it's the most affordable, and it's what most Renton customers choose. Enclosed transport puts your vehicle inside a hard-sided trailer, protected from rain, gravel, and road grime, with liftgate loading for low-clearance cars. We recommend it for luxury and exotic cars, classics and restorations, and high-end EVs. Enclosed carriers run the I-5 corridor regularly, so availability from Renton is good.</p>

<h2>How Renton car shipping works</h2>
<ol class="numbered">
<li><b>Quote.</b> Use the instant quote tool or call the Renton office with your ZIP codes, vehicle, and timing.</li>
<li><b>Book.</b> Approve the price and we assign a vetted carrier and confirm the driver, truck, and pickup window with you. A small deposit holds your spot; the balance is paid at delivery.</li>
<li><b>Pickup.</b> The driver inspects the car with you, documents its condition on the bill of lading, and loads it.</li>
<li><b>Transit.</b> Updates as the car moves; reach the driver or our office any time.</li>
<li><b>Delivery.</b> Inspect, sign, pay the balance, done.</li>
</ol>

<h2>Preparing your vehicle for transport</h2>
<p>Wash the car and photograph all sides so the inspection is accurate. Leave about a quarter tank of fuel (or 30%+ charge for an EV). Remove your Good To Go! toll pass, parking permits, garage openers, and loose items. Fold in mirrors, remove roof racks and bike carriers, and retract antennas. Personal items up to about 100 pounds can ride in the trunk but aren't insured — keep valuables with you. If your vehicle is lifted, lowered, or has a canopy, tell us at booking so we assign the right carrier.</p>

<h2>Military, student, and snowbird shipping from Renton</h2>
<p>With Joint Base Lewis-McChord a short drive south on I-5, we handle PCS moves from the Renton area regularly and offer an active-duty discount. For Renton Technical College students and families sending a car to a student out of state, we coordinate pickup and delivery with whoever is on each end. Snowbirds heading to Arizona, Palm Springs, or Texas should book in early fall — October and November are the busiest southbound months, and March and April are busiest coming back.</p>

<h2>Visit or call our Renton office</h2>
<p>Evergreen Car Shipping's Renton location is at 212 Wells Ave S, Unit 1455, Renton, WA 98057 — downtown, a few blocks from the Renton Transit Center and Piazza Park, minutes from I-405 and SR-167. Call <a data-city-tel href="#">(425) 371-5089</a> Monday through Saturday, or get an instant quote online any time. We also have Washington offices in <a href="seattle-car-shipping.html">Seattle</a>, <a href="bellevue-car-shipping.html">Bellevue</a>, <a href="kent-car-shipping.html">Kent</a>, and <a href="tacoma-car-shipping.html">Tacoma</a>.</p>
"""),
]

NAV = '''<nav class="main" aria-label="Main">
      <a href="index.html#how">How It Works</a>
      <a href="index.html#services">Services</a>
      <a href="index.html#locations">Locations</a>
      <a href="index.html#faq">FAQ</a>
      <a href="#office">Contact</a>
    </nav>'''

def page(c):
    routes = '<div class="route-table"><table><thead><tr><th>Route</th><th>Distance</th><th>Transit time</th></tr></thead><tbody>' + ''.join(f'<tr><td>{r}</td><td>{d}</td><td>{t}</td></tr>' for r,d,t in c['routes']) + '</tbody></table></div>'
    areas = ', '.join(c['areas'][:-1]) + ', and ' + c['areas'][-1]
    body = re.sub(r'<li>\{CHECK\}(.*?)</li>', r'<li>{CHECK}<span>\1</span></li>', c['body'], flags=re.S).replace('{CHECK}', CHECK).replace('{AREAS}', areas).replace('{ROUTES}', routes)
    faq_html = ''.join(f'<details{" open" if i==0 else ""}><summary>{H.escape(q)}</summary><p>{H.escape(a)}</p></details>' for i,(q,a) in enumerate(c['faq']))
    schema = json.dumps({
      "@context":"https://schema.org","@type":"AutoTransport" if False else "LocalBusiness","name":f"Evergreen Car Shipping - {c['city']}",
      "image":"https://evergreencarshipping.com/assets/logo.png","url":f"https://evergreencarshipping.com/{c['slug']}-car-shipping","telephone":c['tel'],
      "address":{"@type":"PostalAddress","streetAddress":c['street'],"addressLocality":c['city'],"addressRegion":"WA","postalCode":c['zip'],"addressCountry":"US"},
      "geo":{"@type":"GeoCoordinates","latitude":c['lat'],"longitude":c['lng']},
      "openingHours":"Mo-Sa 07:00-19:00","priceRange":"$$","areaServed":{"@type":"City","name":c['city']},
      "parentOrganization":{"@type":"Organization","name":"Evergreen Car Shipping"}})
    faq_schema = json.dumps({"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in c['faq']]})
    crumb_schema = json.dumps({"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Home","item":"https://evergreencarshipping.com/"},{"@type":"ListItem","position":2,"name":"Locations","item":"https://evergreencarshipping.com/#locations"},{"@type":"ListItem","position":3,"name":c['city']+", WA","item":f"https://evergreencarshipping.com/{c['slug']}-car-shipping"}]})
    others = [o for o in CITIES if o['slug']!=c['slug']]
    other_links = ''.join(f'<li><a href="{o["slug"]}-car-shipping.html">{o["city"]}</a></li>' for o in CITIES)
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{c['title']}</title>
<meta name="description" content="{H.escape(c['desc'])}">
<link rel="canonical" href="https://evergreencarshipping.com/{c['slug']}-car-shipping">
<meta property="og:title" content="{c['title']}"><meta property="og:description" content="{H.escape(c['desc'])}"><meta property="og:type" content="website"><meta property="og:image" content="https://evergreencarshipping.com/assets/logo.png">
<link rel="icon" href="assets/favicon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Plus+Jakarta+Sans:wght@600;700;800&display=swap" rel="stylesheet">
<script type="application/ld+json">{schema}</script>
<script type="application/ld+json">{faq_schema}</script>
<script type="application/ld+json">{crumb_schema}</script>
<meta name="robots" content="index, follow, max-image-preview:large">
<meta property="og:url" content="https://evergreencarshipping.com/{c['slug']}-car-shipping"><meta property="og:site_name" content="Evergreen Car Shipping"><meta name="twitter:card" content="summary_large_image"><meta name="theme-color" content="#0f6b3a">
{HEAD_CSS}
<style>
.city-hero{{padding:48px 0 56px}}
.city-hero h1{{font-size:clamp(30px,4vw,46px)}}
.crumbs{{font-size:13.5px;color:var(--eg-muted);margin-bottom:14px}}.crumbs a:hover{{color:var(--eg-green)}}
.nap{{display:flex;flex-wrap:wrap;gap:14px 22px;margin-top:22px;font-weight:600;font-size:15px;color:var(--eg-ink-2)}}
.nap span{{display:inline-flex;align-items:center;gap:8px}}.nap svg{{width:18px;height:18px;color:var(--eg-green);flex:0 0 auto}}
.content{{max-width:800px}}
.content h2{{font-size:clamp(22px,2.6vw,28px);margin:40px 0 14px;color:#10201a}}
.content h2:first-child{{margin-top:0}}
.content p{{font-size:16.5px;color:var(--eg-ink-2);margin-bottom:14px;line-height:1.65}}
.content p a{{color:var(--eg-green);font-weight:600}}
.content .checks{{margin:14px 0 8px}}.content .checks li{{font-size:16px;line-height:1.55}}.content .checks b{{color:var(--eg-ink);margin-right:4px}}
.numbered{{padding-left:22px;margin:0 0 14px;display:grid;gap:10px;color:var(--eg-ink-2);font-size:16px;line-height:1.55}}.numbered b{{color:var(--eg-ink)}}
.route-table{{margin:14px 0 18px;overflow-x:auto;border:1px solid var(--eg-line);border-radius:14px}}
.route-table table{{width:100%;border-collapse:collapse;font-size:15px}}
.route-table th{{text-align:left;background:var(--eg-tint);color:var(--eg-green-deep);font-family:var(--eg-font-display);font-size:13px;letter-spacing:.04em;text-transform:uppercase;padding:12px 16px}}
.route-table td{{padding:12px 16px;border-top:1px solid var(--eg-line);color:var(--eg-ink-2)}}.route-table td:first-child{{font-weight:600;color:var(--eg-ink)}}
.city-layout{{display:grid;grid-template-columns:1fr 340px;gap:48px;align-items:start}}
.side{{position:sticky;top:96px;display:grid;gap:18px}}
.side-card{{background:#fff;border:1px solid var(--eg-line);border-radius:var(--eg-r);padding:22px}}
.side-card h3{{font-size:16px;margin-bottom:12px}}
.side-card .big{{font-family:var(--eg-font-display);font-weight:800;font-size:22px;color:var(--eg-green);display:block;margin:4px 0 8px}}
.side-card p{{font-size:14.5px;color:var(--eg-ink-2)}}
.side-card ul{{list-style:none;padding:0;margin:0;display:grid;gap:8px;font-size:14.5px;font-weight:600}}
.side-card ul a:hover{{color:var(--eg-green)}}
.map-wrap{{border-radius:var(--eg-r);overflow:hidden;border:1px solid var(--eg-line);margin-top:28px}}
.map-wrap iframe{{width:100%;height:380px;border:0;display:block}}
.office{{display:grid;grid-template-columns:1fr 1fr;gap:40px;align-items:center}}
@media (max-width:1000px){{.city-layout{{grid-template-columns:1fr}}.side{{position:static}}.office{{grid-template-columns:1fr}}}}
</style>
<script>
/* ===== EVERGREEN SITE SETTINGS ({c['city']} office) ===== */
window.EG_SITE = {{
  phoneDisplay: '{c['phone']}',
  phoneTel:     '{c['tel']}',
  email:        'info@evergreencarshipping.com',
  googleRating: '5.0'
}};
</script>
</head>
<body>

<div class="topbar">
  <div class="wrap">
    <span><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3l7 3v5c0 5-3.5 8.5-7 10-3.5-1.5-7-5-7-10V6l7-3Z"/></svg>Licensed &amp; insured nationwide auto transport</span>
    <span class="tb-right"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/></svg>Mon–Sat 7am–7pm PT &nbsp;·&nbsp; <a data-eg-tel href="#">[PHONE]</a></span>
  </div>
</div>

<header class="site">
  <div class="wrap">
    <a class="logo" href="index.html" aria-label="Evergreen Car Shipping home"><img src="assets/logo.png" alt="Evergreen Car Shipping logo" width="1320" height="702"></a>
    {NAV}
    <div class="hdr-right">
      <a class="btn-call" data-eg-tel href="#">{PHONE_SVG}<span class="num" data-eg-phone>[PHONE]</span><span class="num-short eg-short">Call</span></a>
      <button class="menu-btn" id="menuBtn" aria-label="Open menu" aria-expanded="false"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M4 7h16M4 12h16M4 17h16"/></svg></button>
    </div>
  </div>
  <div class="mobile-nav" id="mobileNav">
    <a href="#quote-widget">Get a Quote</a><a href="index.html#how">How It Works</a><a href="index.html#services">Services</a><a href="index.html#locations">Locations</a><a href="index.html#faq">FAQ</a><a href="#office">Contact</a>
  </div>
</header>

<main id="top">

<section class="hero city-hero" id="quote">
  <div class="wrap">
    <div>
      <div class="crumbs"><a href="index.html">Home</a> › <a href="index.html#locations">Locations</a> › {c['city']}, WA</div>
      <div class="eyebrow">Local office · {c['city']}, Washington</div>
      <h1>{c['h1']}</h1>
      <p class="sub">{c['tagline']}</p>
      <ul class="hero-points">
        <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="m8 12 3 3 5-6"/></svg>Fully insured open &amp; enclosed transport</li>
        <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="m8 12 3 3 5-6"/></svg>Instant all-in quote — no hidden fees, no obligation</li>
        <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="m8 12 3 3 5-6"/></svg>Door-to-door pickup across the {c['city']} area</li>
      </ul>
      <div class="nap">
        <span><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0Z"/><circle cx="12" cy="10" r="3"/></svg>{c['street']}, {c['city']}, WA {c['zip']}</span>
        <span>{PHONE_SVG}<a data-eg-tel href="#"><span data-eg-phone>[PHONE]</span></a></span>
      </div>
    </div>
    <div class="quote-col" id="quote-widget">
{EMBED}
    </div>
  </div>
</section>

<section class="trust" aria-label="Highlights">
  <div class="wrap">
    <div><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3a14 14 0 0 1 0 18M12 3a14 14 0 0 0 0 18"/></svg>All 50 states covered</div>
    <div><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3l7 3v5c0 5-3.5 8.5-7 10-3.5-1.5-7-5-7-10V6l7-3Z"/><path d="m9 12 2 2 4-4"/></svg>100% insured &amp; bonded</div>
    <div><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M13 2 4.5 13.5H11l-1 8.5L19.5 10H13l1-8Z"/></svg>Free instant quotes</div>
    <div><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M3 7h11v9H3zM14 10h4l3 3v3h-7z"/><circle cx="7" cy="18" r="2"/><circle cx="17" cy="18" r="2"/></svg>Vetted carrier network</div>
  </div>
</section>

<section class="section">
  <div class="wrap city-layout">
    <article class="content">
{body}
    </article>
    <aside class="side">
      <div class="side-card">
        <h3>{c['city']} office</h3>
        <a class="big" data-eg-tel href="#"><span data-eg-phone>[PHONE]</span></a>
        <p>{c['street']}<br>{c['city']}, WA {c['zip']}<br>Mon–Sat 7am–7pm PT</p>
        <a class="btn btn-green" href="#quote-widget" style="width:100%;margin-top:14px">Get My Instant Quote</a>
      </div>
      <div class="side-card">
        <h3>Our Washington offices</h3>
        <ul>{other_links}</ul>
      </div>
      <div class="side-card">
        <h3>Services</h3>
        <ul><li><a href="index.html#services">Open Transport</a></li><li><a href="index.html#services">Enclosed Transport</a></li><li><a href="index.html#services">Door-to-Door</a></li><li><a href="index.html#services">Expedited Shipping</a></li><li><a href="index.html#services">Snowbird Transport</a></li><li><a href="index.html#services">Military &amp; Relocation</a></li></ul>
      </div>
    </aside>
  </div>
</section>

<section class="section soft" id="city-faq">
  <div class="wrap">
    <div class="center">
      <div class="eyebrow">FAQ</div>
      <h2 class="h2">{c['city']} car shipping questions</h2>
    </div>
    <div class="faq">{faq_html}</div>
  </div>
</section>

<section class="section" id="office">
  <div class="wrap office">
    <div>
      <div class="eyebrow">Find us</div>
      <h2 class="h2">Evergreen Car Shipping — {c['city']}</h2>
      <p class="lead">{c['street']}<br>{c['city']}, WA {c['zip']}</p>
      <p class="lead" style="margin-top:10px"><b>Phone:</b> <a data-eg-tel href="#" style="color:var(--eg-green);font-weight:700"><span data-eg-phone>[PHONE]</span></a><br><b>Hours:</b> Monday–Saturday, 7am–7pm PT</p>
      <div style="display:flex;gap:12px;flex-wrap:wrap;margin-top:22px">
        <a class="btn btn-green" href="#quote-widget">Get Your Free Quote</a>
        <a class="btn btn-outline" data-eg-tel href="#">{PHONE_SVG}<span data-eg-phone>[PHONE]</span></a>
      </div>
    </div>
    <div class="map-wrap" style="margin-top:0"><iframe src="{c['map']}" allowfullscreen="" loading="lazy" referrerpolicy="strict-origin-when-cross-origin" title="Evergreen Car Shipping {c['city']} office map"></iframe></div>
  </div>
</section>

<section class="cta">
  <div class="wrap">
    <h2>Ready to ship your car from {c['city']}?</h2>
    <p>Get an instant, all-in quote in 30 seconds — or call our {c['city']} office and talk to a real person.</p>
    <div class="btns">
      <a class="btn btn-white" href="#quote-widget">Get Your Free Quote</a>
      <a class="btn btn-ghost" data-eg-tel href="#">{PHONE_SVG}<span data-eg-phone>[PHONE]</span></a>
    </div>
  </div>
</section>

</main>

{FOOTER}

<div class="sticky-bar">
  <a class="btn btn-outline" data-eg-tel href="#">Call Now</a>
  <a class="btn btn-green" href="#quote-widget">Get Quote</a>
</div>

<script>
{SITE_JS}
</body>
</html>
'''

FOOTER = re.search(r'<footer>.*?</footer>', SRC, re.S).group(0)
import io
for c in CITIES:
    out = page(c).replace('{FOOTER}', FOOTER)
    out = out.replace('data-city-tel', 'data-eg-tel').replace('[PHONE]', c['phone']).replace('(253) 364-1610', c['phone']).replace('+12533641610', c['tel']).replace('(866)&nbsp;499-2815', c['phone'].replace(' ','&nbsp;')).replace('(866) 499-2815', c['phone']).replace('+18664992815', c['tel']).replace('[EMAIL]','info@evergreencarshipping.com')
    open(f"{c['slug']}-car-shipping.html", 'w').write(out)
    text = re.sub(r'<[^>]+>', ' ', c['body'] + ' '.join(q+' '+a for q,a in c['faq']) + c['tagline'])
    print(c['slug'], len(text.split()), 'words')

# sitemap + robots
urls = ['https://evergreencarshipping.com/'] + [f"https://evergreencarshipping.com/{c['slug']}-car-shipping" for c in CITIES]
open('sitemap.xml','w').write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + ''.join(f'  <url><loc>{u}</loc><changefreq>monthly</changefreq></url>\n' for u in urls) + '</urlset>\n')
open('robots.txt','w').write('User-agent: *\nAllow: /\nSitemap: https://evergreencarshipping.com/sitemap.xml\n')
