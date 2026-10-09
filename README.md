# Evergreen Car Shipping — homepage

## What's here
- `index.html` — the homepage, with the Ship Guy pricing tool already embedded (recolored to Evergreen green; the tool's own code is untouched, only its PQ_CONFIG block was set).
- City pages (`seattle-`, `bellevue-`, `tacoma-`, `everett-`, `kent-`, `renton-`, `spokane-`, `yakima-car-shipping.html`) — SEO city pages (1,500+ words each, LocalBusiness + FAQ schema, office phone/address/map). Each page's quote tool and phone links use that office's number.
- `sitemap.xml`, `robots.txt` — update the domain in both (and the canonical tags in the city pages) if the site isn't evergreencarshipping.com.
- `build_cities.py` — regenerates the city pages from `index.html` styles; edit content there and re-run `python3 build_cities.py` to add or change cities.
- `assets/logo.png`, `assets/favicon.png`
- `functions/api/quote/[[path]].js` — Cloudflare Pages function that forwards quote requests to BeRocker using Evergreen's Lead Source key `6ac92656d0180` (already filled in). Leads will land under Evergreen's own source. Each lead's secondary_id is also tagged `EVG-`.

## Before going live — edit the settings block at the top of index.html
```
window.EG_SITE = {
  phoneDisplay: '(253) 364-1610',   // main (Seattle) number — already set; city pages use their own office number
  phoneTel:     '+12533641610',
  email:        'info@evergreencarshipping.com',
  googleRating: '5.0'
};
```
These fill every phone/email/USDOT/MC spot on the page AND the quote tool's consent text and "Call to Book" button.

Also:
1. Confirm the contact email (info@evergreencarshipping.com is assumed) in `index.html` EG_SITE and `build_cities.py`.
2. Google Maps: add Evergreen's domain to the referrer restrictions of the key in PQ_CONFIG (or paste a new key). ZIP city/state hints need it; the tool works without it.
3. Privacy / Terms / Licensing links in the footer point to `#` — link them to real pages.
4. If the site URL isn't evergreencarshipping.com, update `siteUrl` / `siteLabel` in PQ_CONFIG (bottom of index.html).

## Known gap
- **Renton map:** the Renton embed code supplied was a duplicate of Yakima's, so `renton-car-shipping.html` uses a plain address-based Google Map. Replace the iframe `src` in `build_cities.py` (Renton entry, `map=`) with the correct embed and re-run the script.

## SEO — what's built in
- Unique title (≤60 chars) and meta description (≤160) on every page; one H1 per page; canonical URLs; Open Graph/Twitter tags.
- Structured data: Organization (with all 8 offices) + WebSite + FAQPage on the homepage; LocalBusiness + FAQPage + BreadcrumbList on each city page.
- `sitemap.xml` (with lastmod/priority) and `robots.txt`; `_headers` sets cache + security headers on Cloudflare.
- Phone numbers, addresses, and all copy are in static HTML (not script-filled), so Google indexes them without JS.
- Internal links: homepage → every city page; each city page → homepage sections + all other offices.

## SEO — launch checklist (your side)
1. Set the real domain: replace `evergreencarshipping.com` in `index.html`, `build_cities.py` (then re-run it), `sitemap.xml`, and `robots.txt` if different.
2. Google Search Console: verify the domain, submit `https://<domain>/sitemap.xml`.
3. Google Business Profile: create/claim a profile for each of the 8 offices with the exact address and phone used on its page, and link each profile's website field to its city page.
4. Fix the Renton map embed (see Known gap).
5. After launch, run the homepage and one city page through Google's Rich Results Test to confirm the schema validates.

## Deploy (Cloudflare Pages)
Upload this whole folder as the project root. The `functions` folder is picked up automatically.
Prefer setting the key as an env var: Pages project → Settings → Environment variables → `BEROCKER_LEAD_KEY = 6ac92656d0180` (the file's default is the same key, so either works).

## Test after deploy (phone + desktop)
- ZIP fields accept 5 digits only; 4 digits shows "Enter a 5-digit ZIP code."
- Year → Make → Model load live from BeRocker.
- Submitting without the consent box checked is blocked.
- After submit: "Getting your best price…" → price → redirect to booking link.
- The lead appears in BeRocker under the Evergreen lead source (not shipguy.com).
