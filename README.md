# Aion 2 Macro Sheet

In-game macro (基本技能輔助功能 / Macro) setups for all 8 Aion 2 classes. It has a late-game tab (current patch) and an improved early-game tab. Every macro entry shows its full 4-row slot stack, with English and Taiwan-client (繁中) names, real skill icons and cooldowns.

Static site: `index.html` + `app.js` read the two JSON files in `data/`. No build step.

## Updating the info

All content lives in two files. You never need to touch the HTML or JS.

| File | What's in it |
|---|---|
| `data/macros.json` | Per-class stacks, held keys, manual skills, notes, sources, alternate versions, changelog, "updated" date |
| `data/skills.json` | Skill reference: TW/KO names, cooldown, MP, icon file, optional `note` (shown in the hover card, e.g. KR/TW patch changes the Global DB doesn't have yet). Add a skill here before using it in a stack. |
| `data/descriptions.json` | Hover-card text: English description, specialties by unlock level, range, castable-while-moving, Mastery/Stigma. Generated, don't hand-edit. Refresh with `python tools/fetch_descriptions.py` after adding skills or after a patch. |

Each class has three tabs: `late` (best tested setup), `full` (longer full-rotation macro with buffs; add a `loss` string describing the DPS trade-off) and `early` (improved leveling setup). Any of them can have `keys`: `[{"label": ..., "stack": [4 rows]}]` for held/mashed hotbar keys that are not in the macro; these are drawn under the macro window.

Alternate versions (`alts`) use the same stack format: `{"t": title, "s": note, "macros": [[...]], "delays": [ms per entry], "hold": [...], "extra": [{"label": ..., "stack": [...]}]}`. `extra` draws a hand-pressed key stack that isn't part of the macro.

### Stack format

A macro is a list of entries, and each entry is the 4 rows of one hotbar key, **row 0 first** (row 0 fires first and sits just above the key in game):

```json
"macros": [["Insignia Explosion", "Heart Gore", "Savage Roar", null]]
```

- `null` = empty row.
- End a name with `?` to flag it as "likely" (icon-matched, not named by the source).
- Two entries = two lists: `[[...], [...]]`.

### After a patch

1. Edit `data/macros.json` (and `data/skills.json` if cooldowns changed).
2. Bump `meta.updated` and `meta.patchBaseline`, and add a line to `changelog`.
3. Commit and push. GitHub Pages redeploys in about a minute.

### Adding a skill icon

Icons come from the aion2.app skill database: `https://aion2.app/db-item-icons/<ICON_ID>.webp`. Save the file into `icons/` and set `"icon": "<ICON_ID>"` in `skills.json`.

## Preview locally

```bash
python -m http.server 8777
```

Then open http://127.0.0.1:8777/

## Sources

The newest post-patch Korean Inven class guides (Sep 5–24, 2026), a Taiwanese Bahamut built-in-macro guide, official TW patch notes, and the aion2.app client database. Full links are in the page footer and in each class card.

Skill icons and names © NC. This is a fan-made reference.
