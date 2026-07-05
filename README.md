<div align="center">

<img src="icon.png" width="140" alt="GodDustry icon"/>

# ✨ GodDustry ✨

### A divine, batteries-included content template for **Mindustry** mods

*Learn Mindustry's JSON/Hjson modding API by example — a clean, heavily-commented starter pack you can fork, rename, and grow into your own mod.*

<br/>

![Type](https://img.shields.io/badge/type-content%20mod-ffd45e?style=for-the-badge)
![Format](https://img.shields.io/badge/format-Hjson-8fdcff?style=for-the-badge)
![Mindustry](https://img.shields.io/badge/Mindustry-v7%2B-f25555?style=for-the-badge)
![License](https://img.shields.io/badge/license-MIT-4caf50?style=for-the-badge)
![PRs](https://img.shields.io/badge/PRs-welcome-purple?style=for-the-badge)
![Verified](https://img.shields.io/badge/headless%20load-v146%20clean-2ea44f?style=for-the-badge)

</div>

---

> **TL;DR** — GodDustry is *not* a Java mod. It is a pure **data mod**: a folder of `.hjson` files and PNG sprites that Mindustry reads at runtime. There is nothing to compile. Drop it in your `mods/` folder and play. Read the files top-to-bottom and you will understand how items, liquids, drills, generators, turrets, units, factories and reconstructors are defined.

> ✅ **Verified:** the mod has been test-loaded on a headless Mindustry v146 server with zero content warnings.

---

## 📖 Table of Contents

- [What is this?](#-what-is-this)
- [Highlights](#-highlights)
- [The Content](#-the-content)
- [Project Structure](#-project-structure)
- [Installation](#-installation)
- [How Mindustry Mods Work](#-how-mindustry-mods-work)
- [Anatomy of `mod.hjson`](#-anatomy-of-modhjson)
- [Make It Your Own](#-make-it-your-own)
- [How Many Sprites Does Each Thing Need?](#-how-many-sprites-does-each-thing-need)
- [Spriting Rules](#-spriting-rules)
- [Publishing to the In-Game Browser](#-publishing-to-the-in-game-browser)
- [Troubleshooting](#-troubleshooting)
- [Learning Resources](#-learning-resources)
- [Contributing](#-contributing)
- [License](#-license)

---

## 🌟 What is this?

**GodDustry** is a small, opinionated example mod for [Mindustry](https://mindustrygame.github.io/) — the open-source automation tower-defense RTS by Anuken.

Most people learning to mod Mindustry hit the same wall: the official docs explain *concepts*, but a blank folder is intimidating. GodDustry fills that gap. It is a **fully working, minimal mod** that now demonstrates a complete starter content set:

- a custom **item** and **liquid**,
- a **production chain** from raw inputs to Holy Dust,
- a family of **drills**,
- **power generators**,
- multiple **turrets**,
- and a full **unit line** with a factory and reconstructors.

Every file is commented. Every sprite is the correct size and pixel format. Every cross-reference (`goddustry-holy-dust`, tech-tree `research`, `bundles`) is wired up so you can see how the pieces connect — then rip them out and replace them with your own ideas.

---

## 🔥 Highlights

| | |
|---|---|
| 🧩 **Zero build step** | Pure Hjson + PNG. No Gradle, no JDK, no compilation. |
| 📝 **Heavily commented** | Every field is explained inline so you learn *why*, not just *what*. |
| 🎨 **Correct sprites** | All PNGs are 32-bit RGBA at the exact sizes Mindustry expects. |
| 🌐 **Localised** | Ships with an English `bundle.properties`; add any language you like. |
| 🌳 **Tech-tree ready** | Content is slotted into the research tree via the `research` field. |
| 🔗 **Cross-references** | Shows how blocks consume/output your own custom items. |
| 🧪 **Verified load** | Headless Mindustry v146 loads the mod cleanly, with zero content warnings. |
| ♻ **Fork-friendly** | Rename one field and the whole mod becomes *yours*. |

---

## 🧪 The Content

GodDustry now ships a full little tech slice: raw resources, a dust production chain, mining drills, power generation, offensive turrets, and a unit path that climbs from T1 factory production into T2/T3 reconstruction.

### Resources

| Sprite | Name | Type | Purpose |
|:------:|------|------|---------|
| <img src="sprites/items/holy-dust.png" width="32"/> | **Holy Dust** | `Item` | Golden resource used by the mod's production and power blocks. |
| <img src="sprites/liquids/blessed-water.png" width="32"/> | **Blessed Water** | `Liquid` | Light-blue liquid used as a boost/consumption ingredient. |

### Production / Crafting

| Sprite | Name | Type | Purpose |
|:------:|------|------|---------|
| <img src="sprites/blocks/dust-forge.png" width="32"/> | **Dust Forge** | `GenericCrafter` | Converts copper and power into Holy Dust. |
| <img src="sprites/blocks/holy-refinery.png" width="32"/> | **Holy Refinery** | `GenericCrafter` | Refines copper, blessed water, and power into more Holy Dust. |

### Drills

| Sprite | Name | Type | Purpose |
|:------:|------|------|---------|
| <img src="sprites/blocks/holy-drill-i.png" width="32"/> | **Holy Drill I** | `Drill` | Starter ore drill for tier-3 resources. |
| <img src="sprites/blocks/holy-drill-ii.png" width="32"/> | **Holy Drill II** | `Drill` | Improved drill with a better mining tier and speed. |
| <img src="sprites/blocks/holy-drill-iii.png" width="32"/> | **Holy Drill III** | `Drill` | Larger drill for harder ore veins. |
| <img src="sprites/blocks/holy-bore.png" width="32"/> | **Holy Bore** | `Drill` | Power- and liquid-boosted bore for high throughput. |
| <img src="sprites/blocks/holy-quarry.png" width="32"/> | **Holy Quarry** | `Drill` | Massive end of the drill line with the fastest extraction. |

Tech-tree note: the drill line chains forward in order — Holy Drill I → II → III → Holy Bore → Holy Quarry.

### Power

| Sprite | Name | Type | Purpose |
|:------:|------|------|---------|
| <img src="sprites/blocks/dust-reactor.png" width="32"/> | **Dust Reactor** | `ConsumeGenerator` | Burns Holy Dust into steady power. |
| <img src="sprites/blocks/blessed-turbine.png" width="32"/> | **Blessed Turbine** | `ConsumeGenerator` | Turns blessed water into power. |
| <img src="sprites/blocks/holy-panel.png" width="32"/> | **Holy Panel** | `SolarGenerator` | Simple solar power source. |

### Turrets

| Sprite | Name | Type | Purpose |
|:------:|------|------|---------|
| <img src="sprites/blocks/divine-turret.png" width="32"/> | **Divine Turret** | `ItemTurret` | Starter turret with copper and Holy Dust ammo. |
| <img src="sprites/blocks/hallowed-mortar.png" width="32"/> | **Hallowed Mortar** | `ItemTurret` | Long-range artillery turret with arcing shells. |
| <img src="sprites/blocks/sanctifier.png" width="32"/> | **Sanctifier** | `PowerTurret` | Power laser turret built around a single beam shot. |
| <img src="sprites/blocks/radiant-cannon.png" width="32"/> | **Radiant Cannon** | `ItemTurret` | Heavy 3×3 cannon with stronger ammo options. |
| <img src="sprites/blocks/aegis-array.png" width="32"/> | **Aegis Array** | `ItemTurret` | Fast defensive turret that targets air and ground. |

### Units

| Sprite | Name | Type | Purpose |
|:------:|------|------|---------|
| <img src="sprites/units/holy-scout.png" width="32"/> | **Holy Scout** | `flying` | T1 scout unit for early production. |
| <img src="sprites/units/holy-guard.png" width="32"/> | **Holy Guard** | `mech` | T1 ground unit for basic combat. |
| <img src="sprites/units/holy-warden.png" width="32"/> | **Holy Warden** | `mech` | T2 upgrade path unit. |
| <img src="sprites/units/holy-seraph.png" width="32"/> | **Holy Seraph** | `flying` | T3 upgraded air unit. |
| <img src="sprites/units/holy-templar.png" width="32"/> | **Holy Templar** | `mech` | T3 upgraded ground unit. |

### Unit Production

| Sprite | Name | Type | Purpose |
|:------:|------|------|---------|
| <img src="sprites/blocks/holy-t1-shields.png" width="32"/> | **Holy T1 Shields** | `UnitFactory` | Produces the first holy units. |
| <img src="sprites/blocks/holy-ascender.png" width="32"/> | **Holy Ascender** | `Reconstructor` | Upgrades T1 units to T2. |
| <img src="sprites/blocks/holy-transcender.png" width="32"/> | **Holy Transcender** | `Reconstructor` | Upgrades T2 units to T3. |

Tech-tree note: `Holy T1 Shields` starts the unit line, `Holy Ascender` promotes T1 → T2, and `Holy Transcender` promotes T2 → T3.

> These stats are intentionally modest and *illustrative*. Treat them as a starting point for your own balancing, not as gospel.

---

## 📂 Project Structure

```text
GodDustry/
├── mod.hjson                       # required — mod metadata (name, author, version…)
├── icon.png                        # 128×128 icon shown in the in-game mod browser
├── content/
│   ├── items/
│   │   └── holy-dust.hjson         # → item id "holy-dust"
│   ├── liquids/
│   │   └── blessed-water.hjson     # → liquid id "blessed-water"
│   ├── blocks/
│   │   ├── aegis-array.hjson
│   │   ├── blessed-turbine.hjson
│   │   ├── divine-turret.hjson
│   │   ├── dust-forge.hjson
│   │   ├── dust-reactor.hjson
│   │   ├── hallowed-mortar.hjson
│   │   ├── holy-ascender.hjson
│   │   ├── holy-bore.hjson
│   │   ├── holy-drill-i.hjson
│   │   ├── holy-drill-ii.hjson
│   │   ├── holy-drill-iii.hjson
│   │   ├── holy-panel.hjson
│   │   ├── holy-quarry.hjson
│   │   ├── holy-refinery.hjson
│   │   ├── holy-t1-shields.hjson
│   │   ├── holy-transcender.hjson
│   │   ├── radiant-cannon.hjson
│   │   └── sanctifier.hjson
│   └── units/
│       ├── holy-guard.hjson
│       ├── holy-scout.hjson
│       ├── holy-seraph.hjson
│       ├── holy-templar.hjson
│       └── holy-warden.hjson
├── bundles/
│   └── bundle.properties           # English display names & descriptions
├── sprites/
│   ├── items/holy-dust.png
│   ├── liquids/blessed-water.png
│   ├── blocks/
│   │   ├── aegis-array.png
│   │   ├── blessed-turbine.png
│   │   ├── blessed-turbine-top.png
│   │   ├── divine-turret.png
│   │   ├── dust-forge.png
│   │   ├── dust-reactor.png
│   │   ├── dust-reactor-top.png
│   │   ├── hallowed-mortar.png
│   │   ├── holy-ascender.png
│   │   ├── holy-ascender-top.png
│   │   ├── holy-bore.png
│   │   ├── holy-bore-rotator.png
│   │   ├── holy-bore-top.png
│   │   ├── holy-drill-i.png
│   │   ├── holy-drill-i-rotator.png
│   │   ├── holy-drill-i-top.png
│   │   ├── holy-drill-ii.png
│   │   ├── holy-drill-ii-rotator.png
│   │   ├── holy-drill-ii-top.png
│   │   ├── holy-drill-iii.png
│   │   ├── holy-drill-iii-rotator.png
│   │   ├── holy-drill-iii-top.png
│   │   ├── holy-panel.png
│   │   ├── holy-quarry.png
│   │   ├── holy-quarry-rotator.png
│   │   ├── holy-quarry-top.png
│   │   ├── holy-refinery.png
│   │   ├── holy-t1-shields.png
│   │   ├── holy-t1-shields-top.png
│   │   ├── holy-transcender.png
│   │   ├── holy-transcender-top.png
│   │   ├── radiant-cannon.png
│   │   └── sanctifier.png
│   └── units/
│       ├── holy-guard-cell.png
│       ├── holy-guard.png
│       ├── holy-scout-cell.png
│       ├── holy-scout.png
│       ├── holy-seraph-cell.png
│       ├── holy-seraph.png
│       ├── holy-templar-cell.png
│       ├── holy-templar.png
│       ├── holy-warden-cell.png
│       ├── holy-warden.png
│       └── weapons/
│           ├── goddustry-holy-guard-caster.png
│           ├── goddustry-holy-scout-beam.png
│           ├── goddustry-holy-seraph-cannon.png
│           ├── goddustry-holy-templar-judge.png
│           └── goddustry-holy-warden-lance.png
└── tools/
    └── gen_sprites.py              # reproducible placeholder sprite generator
```

**The golden rule:** a piece of content is identified by its **file stem** (the filename without extension). `content/items/holy-dust.hjson` creates an item named `holy-dust`, and Mindustry will automatically look for `sprites/**/holy-dust.png` to draw it. When one mod references another mod's content, the id is prefixed with the mod name — hence `goddustry-holy-dust`.

---

## 💾 Installation

### Option A — Manual (works everywhere)

1. Download this repository (**Code → Download ZIP**, or `git clone`).
2. Copy the folder (or the `.zip` — unzipping is optional) into your Mindustry `mods/` directory:

   | Platform | Path |
   |----------|------|
   | Windows | `%appdata%/Mindustry/mods/` |
   | Linux | `~/.local/share/Mindustry/mods/` |
   | macOS | `~/Library/Application Support/Mindustry/mods/` |
   | Steam | `steam/steamapps/common/Mindustry/saves/mods/` |
   | Android | `Android/data/io.anuke.mindustry/files/mods/` |

3. Launch Mindustry → **Mods** → enable **GodDustry** → restart when prompted.

### Option B — In-game GitHub import

Mindustry can install any GitHub mod directly:

**Mods → Import → GitHub → `YOUR_USERNAME/GodDustry`**

---

## 🛠 How Mindustry Mods Work

Mindustry mods are **just directories of assets** — there is no magic. At startup the game:

1. reads `mod.hjson` for metadata,
2. walks the `content/` tree and parses each `.hjson`/`.json` file into a game object based on its `type` field,
3. resolves sprites from `sprites/` by matching content names,
4. loads display strings from `bundles/`,
5. injects everything into the tech tree, build menu and content database.

Content files are written in [**Hjson**](https://hjson.github.io/) — a friendlier superset of JSON that allows comments, unquoted keys and multi-line strings. Any valid JSON is valid Hjson, so you can use whichever you prefer.

A typical content file looks like this:

```hjson
type: ItemTurret     # which game class to instantiate — this is the important one
name: Divine Turret  # human-readable display name
# ...type-specific fields follow...
```

The `type` field is special: it selects the Java class the parser builds. Types **extend** each other, so an `ItemTurret` inherits every field of `Turret`, which inherits every field of `Block`. Field names are **case-sensitive** (`hitSize` ≠ `hitsize`).

---

## 🧾 Anatomy of `mod.hjson`

`mod.hjson` (or `mod.json`) is the **only required file**. GodDustry's looks like this:

```hjson
name: goddustry                       # internal id — kebab-case, no colors
displayName: "[gold]God[white]Dustry" # shown in UI, supports color markup
author: "JSHON"
description: "A divine content pack template for Mindustry…"
version: "1.0"
minGameVersion: 146                   # must be a number > 105
dependencies: []                      # other mods this one needs
hidden: false                         # content mods should stay visible
```

| Field | Required | Notes |
|-------|:--------:|-------|
| `name` | ✅ | Internal id. Lowercase, hyphen-separated, **no** color codes. |
| `displayName` | ➖ | UI name; may contain `[color]` markup. |
| `author` | ➖ | Your name / handle. |
| `description` | ➖ | Keep it short — it renders in the mod manager. |
| `version` | ➖ | Free-form version string. |
| `minGameVersion` | ✅ | Minimum build number; must be greater than `105`. |
| `dependencies` | ➖ | Array of other mod names. |
| `hidden` | ➖ | `true` only for texture packs / client-side plugins. |

---

## 🎨 Make It Your Own

Turning GodDustry into a brand-new mod takes about five minutes:

1. **Rename the mod.** In `mod.hjson`, change `name`, `displayName`, `author` and `description`. The `name` becomes the prefix for every cross-mod reference.
2. **Add content.** Drop a new `.hjson` file into the right `content/<type>/` folder. The filename is the content id.
3. **Add its sprite.** Save a matching PNG under `sprites/` (see [Spriting Rules](#-spriting-rules)).
4. **Name it.** Add `.name` / `.description` keys to `bundles/bundle.properties`.
5. **Slot it into research.** Add a `research: <parent-block>` field so players can unlock it.
6. **Reload in-game.** Mindustry hot-reloads mods from the Mods menu — no restart of your editor required.

> 💡 Tip: keep filenames **lowercase and hyphen-separated** (`plasma-drill.hjson`, not `Plasma Drill.hjson`). Capitals and spaces will break references.

---

## 🧩 How Many Sprites Does Each Thing Need?

The official spriting wiki is worth following closely, but the short version is:

| Content type | Sprites it looks for | Notes |
|--------------|----------------------|-------|
| Item / Liquid | 1 sprite | Usually `32×32`; the file stem is the id. |
| Wall / simple block | 1 sprite | Block sprites are `32 × size` pixels. |
| Drill | Base + `<name>-rotator` + `<name>-top` | Up to 3 sprites total. |
| Crafter | Base + optional `<name>-top` / `<name>-liquid` + drawer regions | Usually 1–4 sprites depending on visuals. |
| Turret | Base + optional `<name>-heat` / `<name>-glow`; liquid turrets add `<name>-liquid` | Leave transparent margin; the game adds the outline. |
| Generator | Base + optional `<name>-top` / `<name>-glow` | Usually 1–2 sprites. |
| Unit factory / reconstructor | Base + `<name>-top` | The top region rotates/overlays the body. |
| Unit | `<name>.png` + `<name>-cell.png` + one sprite per weapon | Legged units also need leg regions; recommended minimum is 48px. |

Quick reminders:

- Block sprite size = `32 × block size in tiles`.
- Leave about a 4px transparent margin around turrets and units so Mindustry's outline has room to breathe.
- PNGs must be **32-bit RGBA**.
- The vanilla reference sprites live at [Anuken/Mindustry/tree/master/core/assets-raw/sprites](https://github.com/Anuken/Mindustry/tree/master/core/assets-raw/sprites).
- The placeholders in this repo are generated by [`tools/gen_sprites.py`](tools/gen_sprites.py).

---

## 🖼 Spriting Rules

Mindustry is strict about art. Follow these or the game will refuse to load your sprite:

- **Format:** PNG, **32-bit RGBA**. Anything else (indexed/palette, 16-bit) can crash the game with a *"Pixmap decode error"*.
- **Block size:** a block sprite must be `32 × size` pixels. A `2×2` block ⇒ `64×64`. A `1×1` block ⇒ `32×32`.
- **Items & liquids:** `32×32`.
- **Turret borders:** the game auto-adds a black outline to turrets, so leave a transparent margin around turret art.
- **Atlas pages:** the first sub-folder under `sprites/` (e.g. `sprites/blocks/...`) decides the atlas page. Mirror the [vanilla layout](https://github.com/Anuken/Mindustry/tree/master/core/assets-raw/sprites) to avoid rendering lag.

Verify a PNG from the command line:

```bash
file sprites/blocks/divine-turret.png
# → PNG image data, 64 x 64, 8-bit/color RGBA, non-interlaced
```

---

## 🚀 Publishing to the In-Game Browser

To make your mod discoverable inside Mindustry:

1. Push it to a **public GitHub repository**.
2. Add the repository topic **`mindustry-mod`** (Repo → ⚙ next to *About* → *Topics*).
3. Within a day the [Mindustry mod scraper](https://github.com/Anuken/MindustryMods) will pick it up, and it will appear under **Mods → Browse** in-game.

Players can also install it instantly via **Mods → Import → GitHub → `you/YourMod`**.

---

## 🩺 Troubleshooting

| Symptom | Likely cause |
|---------|--------------|
| Mod won't enable | `minGameVersion` is higher than your game build, or `mod.hjson` has a syntax error. |
| Content missing in-game | Wrong `type`, or the file is in the wrong `content/<type>/` folder. |
| Pink/missing texture | Sprite filename ≠ content name, or wrong folder. |
| *"Pixmap decode error"* | A PNG is not 32-bit RGBA. Re-export it. |
| `NullPointerException` on load | A required field is missing from a content file. |
| Names show as `block.goddustry-…` | Missing key in `bundles/bundle.properties`. |

When in doubt, launch Mindustry from a terminal and read the log — parse errors point straight at the offending file and line.

---

## 📚 Learning Resources

This template was assembled after surveying the Mindustry modding ecosystem. Bookmark these:

**Official**
- 📘 [Mindustry Modding Wiki — Introduction](https://mindustrygame.github.io/wiki/modding/1-modding/)
- 🎨 [Modding Wiki — Spriting](https://mindustrygame.github.io/wiki/modding/4-spriting/)
- 🧬 [Modding Wiki — Content Types](https://mindustrygame.github.io/wiki/modding/5-types/)
- 📜 [Modding Wiki — Scripting (JS)](https://mindustrygame.github.io/wiki/modding/3-scripting/)
- 🔌 [Modding Wiki — Plugins / server mods](https://mindustrygame.github.io/wiki/modding/2-plugins/)
- 🧩 [Modding Wiki — Overriding vanilla content (data patches)](https://mindustrygame.github.io/wiki/)
- 📓 [Mindustry Javadoc (all classes & fields)](https://mindustrygame.github.io/docs/)

**Source & templates**
- 💠 [Anuken/Mindustry — game source](https://github.com/Anuken/Mindustry)
- 🖌 [Vanilla sprites (assets-raw)](https://github.com/Anuken/Mindustry/tree/master/core/assets-raw/sprites)
- ☕ [Anuken/MindustryModTemplate — Java mod template](https://github.com/Anuken/MindustryModTemplate)
- 🤖 [Anuken/MindustryMods — the mod scraper/index](https://github.com/Anuken/MindustryMods)

**Community**
- 💬 [Official Mindustry Discord](https://discord.gg/mindustry) — the `#modding` channels are gold
- 🌐 [Mindustry Wiki (Fandom)](https://mindustry.fandom.com/wiki/Modding)
- 👽 [r/Mindustry on Reddit](https://www.reddit.com/r/Mindustry/)
- 🛠 [Steam Workshop](https://steamcommunity.com/app/1127400/workshop/)
- 🧾 [Hjson language reference](https://hjson.github.io/)

---

## 🤝 Contributing

Contributions are welcome! Whether it's a typo fix, a better sprite, a new example block, or clearer comments:

1. Fork the repo.
2. Create a branch: `git checkout -b feature/my-improvement`.
3. Keep filenames lowercase and hyphen-separated; keep sprites 32-bit RGBA.
4. Open a Pull Request describing what you changed and why.

Please keep the *educational* spirit — new examples should be small, self-explanatory and well commented.

---

## 📄 License

Released under the **MIT License** — see [`LICENSE`](LICENSE). Use it, fork it, ship it, sell it. Attribution appreciated but not required.

---

<div align="center">

*Mindustry is © Anuken. GodDustry is an unofficial fan-made template and is not affiliated with or endorsed by the Mindustry developers.*

**Made with ✨ dust and a little divinity.**

</div>
