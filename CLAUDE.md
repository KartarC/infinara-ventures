# Infinara Ventures Website

Marketing/vision site for Infinara Ventures (https://infinaraventures.com) — "Advancing Humanity Toward a Type I Civilization."

## Stack (Skylife template pattern)
- Single `index.html`, no framework, no build step
- Full 3D experience: Three.js v0.160 via jsDelivr CDN (importmap) — realistic Earth (blue-marble day map, night city lights as emissive, topology bump, cloud layer, fresnel atmosphere, axial tilt), starfield with exclusion zone, satellite particle ring
- GSAP 3.12 + ScrollTrigger: preloader intro, masked headline reveal, scrubbed Earth "journey" across sections, reveals, counters, marquee
- Adaptive quality: renderer starts at DPR 1, measures frame times, steps up to DPR 2 on fast GPUs or down to 0.7 on weak ones
- Mobile: ≤880px breakpoint — burger menu overlay, Earth centered above hero, reduced star/particle counts, 16px inputs (no iOS zoom), prefers-reduced-motion respected
- Fonts: Space Grotesk + Inter (Google Fonts)
- Brand: deep space `#030712`, cyan `#22d3ee`, violet `#8b5cf6`, gold `#fbbf24`
- Contact form posts via formsubmit.co to mrextuber@gmail.com (no backend)
- Vercel auto-deploy on push to `main`, `vercel.json` with cleanUrls

## Sections
Hero → Kardashev Scale (Type 0–III, 73% progress bar) → Six Divisions (Energy, Space, Bio, AI, Education, Coordination) → Roadmap (4 phases to 2075) → Vision quote → Partner contact form

## Repo
GitHub: KartarC/infinara-ventures, deployed on Vercel.
