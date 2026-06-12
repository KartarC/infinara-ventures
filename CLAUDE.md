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

## Pages
- `index.html` — Hero → Kardashev Scale (73% bar) → Seven Divisions (Energy, Space, Bio, AI, Education, Coordination, Future Industrial Manufacturing → links to portfolio) → Roadmap → Vision → Contact
  - Scroll story: Earth evolves through 4 eras as you scroll (S.t thresholds 0/.28/.52/.78): satellites on linear orbit lines → Earth space stations → Moon (textured, orbits in background) gains outposts → Type I utopia (energy grid, golden mega-ring, Earth↔Moon travel lane with two-way ship traffic, brighter city lights). "Planetary Status" HUD (bottom-left) narrates eras 2026/2040/2060/2075 and goes gold at utopia.
- `portfolio.html` — companies under the belt, grouped: Industrial Manufacturing (Machinist's Vault, Wavlon Lasers), Aerospace (SkyLife Aircrafts), AI (Axon AI — text monogram, no logo asset exists). Logos in `assets/` on white plates. Lightweight starfield bg.
- `cornerstones.html` — Nine Cornerstones interactive 3D experience: scroll-driven intro narrative → energy Earth → 9 crystalline pillars rise in a ring around a glowing nucleus; hover/click pillars → info cards; all 9 viewed → grand finale (TYPE I CIVILIZATION, fade to final statement). UnrealBloomPass via three/addons importmap; adaptive quality drops bloom then DPR on weak GPUs.

## Repo
GitHub: KartarC/infinara-ventures, deployed on Vercel.
