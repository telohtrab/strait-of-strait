# The Strait of the Strait of Hormuz

*This is not a map.*

A 3D data-driven terrain piece: an imaginary strait whose coastline is shaped by real maritime traffic through the Strait of Hormuz, January to July 2026. Outbound vessels form the northern coast, inbound vessels the southern coast, and the channel narrows or widens exactly as recorded traffic did.

![The Strait of the Strait of Hormuz — poster](assets/strait-of-strait_1.png)

📄 [Full-resolution poster (PDF)](https://drive.google.com/file/d/18YxYB5r9AkpdW3qxX9Pq2zp--ofcToEp/view?usp=sharing)

## About

The data draws its own strait, one that squeezed a real trade route, oil and gas included, down to almost nothing. Vessel counts are raised above the raw AIS numbers, using Lloyd's List Intelligence findings on tankers running dark, transponders off, to dodge detection. Full methodology and limitations: [`data/SOURCES.md`](data/SOURCES.md).

![Detail: containers and vessel wakes](assets/strait-preview-3.png)

## Pipeline

1. `scripts/get_ais_data.py` — data acquisition (UKMTO, AIS)
2. `scripts/merge_data.py` — merge and clean into `data/transits.csv`
3. `scripts/visualize_svg.py` — coastline silhouette, reference geometry (SVG)
4. `scripts/heightmap.py` — signed-distance heightmap for terrain generation
5. Blender — terrain, water, ships, lighting, render (Cycles)
6. DaVinci Resolve — video edit, color, grain

## Credits

Analysis & Design: **Benjamin Bartholet** — [trab.studio](https://trab.studio) · [github.com/telohtrab](https://github.com/telohtrab)

Data: UKMTO · hormuz.data-tracking.net · WTO/AXSMarine Trade Tracker · UNCTAD · Lloyd's List Intelligence
