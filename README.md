# UGN GTA VI Guide 🌴

**Explore Leonida. Track your discoveries.** An independent, fan-made Grand Theft Auto VI companion by Universal Gaming Network.

**[Open the live website](https://universal-gaming.github.io/GTA-6-Guide/)** · [UGN](https://universalgaming.us/)

## Implemented features

- Responsive UGN / Vice City themed homepage, character dossiers, region guides, research index and introduction.
- Interactive **schematic** map: pan, zoom, fullscreen, search, six illustrative region markers and browser-saved favorites.
- Personal map pins (up to 100), stored locally, clearly distinguished from verified game locations.
- Official printable map link and 15-place grid-square reference finder.
- 95-mission, five-chapter index with completion tracking and spoiler controls. Dynamic mission dossiers include sourced walkthrough steps for **nine** missions, plus two reference-only entries.
- Previous/next mission navigation and per-mission private notes.
- Collectible Field Journal: 13 source-backed leads (one VGC whale-statue lead plus 12 Push Square sculpture leads), custom entries, found status, filtering and JSON export/import.
- Collectible directory on the map shares found status with the journal via localStorage.
- Separate personal goal tracker with JSON backup, and optional WebGL 3D experience with fallback.
- **Progress Vault**: one-file export and validated restore for mission completion, notes, collectibles, personal map pins, saved places and tracker data. Local-only reset controls.
- Sitemap, robots.txt and automated static link/sitemap and inline JavaScript syntax checks.

- Research Desk documenting primary sources, verification policy and corrections workflow.

## Accuracy and map limitations

**This is not yet a complete game guide.** The map is illustrative, **not** an accurate in-game map or GPS system. Marker coordinates on it are not real game coordinates. Collectible entries provide published descriptive directions, **not** verified pin coordinates. Mission details are incomplete and some titles are spoilers. Personal pins and notes are user-authored, not independently verified.

The official Leonida map can be accessed via [Rockstar's GTA VI media page](https://www.rockstargames.com/VI/media). We link to it rather than copying proprietary artwork. For corrections, link to primary or reputable published sources.

## Development and checks

The website is static HTML, CSS and JavaScript, deployed on GitHub Pages; no backend or build process is required. Python 3.12+ and Node.js 22+ are used for optional local checks:

```sh
python validate_site.py
python validate_javascript.py
```

GitHub Actions runs both checks on pushes and pull requests. These checks verify static paths, sitemap and inline JavaScript **syntax**; they do not replace real browser, mobile, accessibility, or end-to-end testing.

## Data and privacy

Progress, custom discoveries, mission notes and map pins are stored in your browser's localStorage. No UGN account or server-side sync is provided. Clearing browser storage or using a different device can lose progress. Export backups from the collectible journal and progress tracker where available.

## Roadmap

1. Obtain permission or a suitable original/licensed base map and calibrate actual positions.
2. Add more sourced walkthroughs, collectibles and in-game mechanics.
3. Improve accessible keyboard/touch map controls and add end-to-end tests for Progress Vault export/restore.
4. Add automated browser smoke tests and mobile performance benchmarks.
5. Implement routing only after a validated navigable road graph is available.

## Contributing

Open an issue with precise reproduction steps, source-backed corrections, or new location research. Do not submit copyrighted map tiles, game textures or proprietary assets without permission. Avoid presenting guesses or unverified spoilers as fact.

## Disclaimer

Independent fan project. Not affiliated with or endorsed by Rockstar Games or Take-Two Interactive. Trademarks belong to their owners.
