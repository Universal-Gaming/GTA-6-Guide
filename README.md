# UGN GTA VI Guide 🌴

**Explore Leonida. Track your discoveries.** An independent, fan-made Grand Theft Auto VI companion by Universal Gaming Network.

**[Open the live website](https://universal-gaming.github.io/GTA-6-Guide/)** · [UGN](https://universalgaming.us/)

## Implemented features

- Responsive UGN / Vice City themed homepage, character dossiers, region guides, research index and introduction.
- Interactive **schematic** map: pan, zoom, fullscreen, search, six illustrative region markers and browser-saved favorites.
- Personal map pins (up to 100), stored locally, clearly distinguished from verified game locations.
- Official printable map link and 15-place grid-square reference finder.
- 95-mission, five-chapter index with completion tracking and spoiler controls. Dynamic mission dossiers currently include **94 source-linked quick-route walkthroughs** within the legacy 95-entry index. The original index is not the complete canonical story sequence.
- A separate [chronological Chapter 4–5 story catalog](story-catalog-audit.html) lists 49 source-index entries (including optional and transitional beats), links to legacy guides, and tracks completion without renumbering existing saved progress.
- Two-way mapped mission checkmarks, explicit legacy-progress import, and JSON backup/restore for the chronological catalog and legacy mission tracker.
- Previous/next mission navigation and per-mission private notes.
- Collectible Field Journal: 13 source-backed leads (one VGC whale-statue lead plus 12 Push Square sculpture leads), custom entries, found status, filtering and JSON export/import.
- Collectible directory on the map shares found status with the journal via localStorage.
- Separate personal goal tracker with JSON backup, and optional WebGL 3D experience with fallback.
- **Progress Vault**: one-file export and validated restore for mission completion, notes, collectibles, personal map pins, saved places and tracker data. Local-only reset controls.
- Sitemap, robots.txt and automated static link/sitemap and inline JavaScript syntax checks.

- Research Desk documenting primary sources, verification policy and corrections workflow.
- Searchable Gameplay Encyclopedia with 29 Rockstar-source-linked entries for vehicles, weapons, businesses, customization, places, protagonists and edition distinctions.

## Accuracy and map limitations

**This is not yet a complete game guide.** The map is illustrative, **not** an accurate in-game map or GPS system. Marker coordinates on it are not real game coordinates. Collectible entries provide published descriptive directions, **not** verified pin coordinates. Mission details are incomplete, the final legacy mission remains unsourced, and some titles are spoilers. The 94/95 metric measures only the older tracker, not complete-game coverage. Personal pins and notes are user-authored, not independently verified.

The official Leonida map can be accessed via [Rockstar's GTA VI media page](https://www.rockstargames.com/VI/media). We link to it rather than copying proprietary artwork. For corrections, link to primary or reputable published sources.

## Development and checks

GitHub Actions runs the content validator and Playwright Chromium browser tests on pushes to `main`, pull requests and manual dispatch. A workflow file being present does **not** establish that CI has passed. Review [Actions](https://github.com/Universal-Gaming/GTA-6-Guide/actions) for actual results.


The website is static HTML, CSS and JavaScript, deployed on GitHub Pages; no backend or build process is required. Python 3.12+ and Node.js 22+ are used for local checks:

```sh
python validate_site.py
python validate_javascript.py
python validate_content.py
```

GitHub Actions runs the static checks and mobile Chromium smoke tests on pushes and pull requests. To run browser smoke tests locally, install Playwright (`npm install --no-save playwright@1.58.2` and `npx playwright install chromium`), then run `node test_browser.mjs`. The browser suite covers key navigation, encyclopedia filtering, full-progress export and main page startup; it is **not** a complete accessibility, performance or gameplay-data audit.

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

- Practical Handbook: seven searchable, source-linked guides for saving, the Index, taxis, rideshare, public transit and local guide progress.
