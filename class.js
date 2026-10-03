/* Aion 2 Class Guides: renders one class page (body[data-class]) from
   data/macros.json (macros), data/stigmas.json (stigma builds, skills, specs, tiers), data/classes.json (overview, gear,
   patches), data/stigma_db.json (stigmas), data/skills.json + data/descriptions.json (skill names, icons, hover text).
   To update a class, edit the JSON files only. */
(function () {
  const CLS = document.body.dataset.class;
  const $ = (id) => document.getElementById(id);
  const esc = (s) => String(s == null ? "" : s).replace(/[&<>"]/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));
  const DOT = " · ", ARROW = "→", DASH = "–";
  let SK = {}, DS = {}, DB = {}, MAC = null, STG = null, OV = null;
  let M = null, S = null, O = null; // this class's macro / stigma / overview objects
  let mmode = "late", smode = "gl";

  /* ---------- name lookup (skills.json first, then this class's stigmas) ---------- */
  const base = (n) => String(n || "").replace(/\s*\((?!gladiator|templar|assassin|ranger|sorcerer|spiritmaster|cleric|chanter)[^)]*\)$/, "").replace(/ line$/, "").replace(/\?$/, "");
  const nice = (n) => String(n).replace(/\s*\((gladiator|templar|assassin|ranger|sorcerer|spiritmaster|cleric|chanter)\)$/, "");
  function find(n) {
    const b = base(n);
    if (SK[b]) return { s: SK[b], attr: ` data-skn="${esc(b)}" tabindex="0"` };
    if (SK[b + " (" + CLS + ")"]) return { s: SK[b + " (" + CLS + ")"], attr: ` data-skn="${esc(b + " (" + CLS + ")")}" tabindex="0"` };
    const k = CLS + ":" + b;
    if (DB[k]) return { s: DB[k], attr: ` data-sk="${esc(k)}" tabindex="0"` };
    return null;
  }
  const cdText = (cd) => (cd >= 60 && cd % 60 === 0 ? cd / 60 + " min" : cd + " s");
  const initials = (n) => nice(base(n)).split(/\s+/).map((w) => w[0]).join("").slice(0, 2);
  function ic(n, cls) {
    const f = find(n);
    if (f && f.s.icon) return `<img class="${cls || "ic"}" src="icons/${f.s.icon}.webp" alt="" width="40" height="40" loading="lazy">`;
    return `<span class="${cls || "ic"} none" aria-hidden="true">${cls ? esc(initials(n)) : ""}</span>`;
  }
  const img = (n) => { const f = find(n); return f && f.s.icon ? `<img src="icons/${f.s.icon}.webp" alt="" width="64" height="64" loading="lazy">` : `<span class="none" aria-hidden="true">${esc(initials(n))}</span>`; };
  const hov = (n) => { const f = find(n); return f ? f.attr : ""; };
  const tw = (n) => { const f = find(n); return f ? f.s.tw || "" : ""; };
  function srcHtml(src, label) {
    if (!src || !src.length) return "";
    return `<p class="src">${label || "Sources"}: ${src.map(([t, u]) => (u ? `<a href="${esc(u)}" target="_blank" rel="noopener">${esc(t)}</a>` : esc(t))).join(DOT)}</p>`;
  }

  /* ---------- overview ---------- */
  function overview() {
    const o = O;
    const brings = o.brings.map(([n, t]) => `<li${hov(n)}>${img(n)}<div><b>${esc(nice(n))}</b>${esc(t)}</div></li>`).join("");
    const core = o.core.map(([h, t, n]) => `<li${n ? hov(n) : ""}>${n ? img(n) : '<span class="none"></span>'}<div><b>${esc(h)}</b>${esc(t)}</div></li>`).join("");
    const li = (a) => a.map((x) => `<li>${esc(x)}</li>`).join("");
    return `<section class="panel" id="overview" aria-labelledby="h-ov">
      <h2 id="h-ov">How ${esc(M.en)} plays<small>Role, party value, core mechanics</small></h2>
      <p class="ov-sum">${esc(o.summary)}</p>
      <div class="ov">
        <div class="col"><h4>Core mechanics</h4><ul class="core">${core}</ul></div>
        <div class="col"><h4>What you bring to a party</h4><ul class="brings">${brings}</ul></div>
      </div>
      <div class="cols3">
        <div class="col"><h4>Opener and priority</h4><ol class="open">${o.opener.map((x) => `<li><div>${esc(x)}</div></li>`).join("")}</ol></div>
        <div class="col"><h4>Strengths</h4><ul class="facts">${o.good.map((x) => `<li class="good">${esc(x)}</li>`).join("")}</ul>
          <h4 style="margin-top:6px">Watch out for</h4><ul class="facts">${o.hard.map((x) => `<li class="warn">${esc(x)}</li>`).join("")}</ul></div>
        <div class="col"><h4>Common mistakes</h4><ul class="facts">${o.mistakes.map((x) => `<li class="warn">${esc(x)}</li>`).join("")}</ul></div>
      </div>
      <p class="snote">Effects quoted here are from the Global client database. Hover or tap any icon for the full skill text.</p>
    </section>`;
  }

  /* ---------- macros ---------- */
  /* row badges: stigmas (and whether they're in the Global 4-slot build), learn level of regular skills */
  let GL4 = null;
  const gl4 = () => GL4 || (GL4 = new Set(((S.gl && (S.gl.builds.find((b) => b.main) || S.gl.builds[0])) || { pick: [] }).pick.map((p) => p[0])));
  const isStigma = (n) => !!DB[CLS + ":" + base(n)];
  function badge(n) {
    const b = base(n);
    if (isStigma(n)) {
      return gl4().has(b) ? `<span class="bdg st" title="Stigma: needs character level 22+ and a free stigma slot (Global: 1 slot at 22, 2 at 27, 3 at 32, 4 at 37)">Stigma</span>`
        : `<span class="bdg kr" title="A stigma that isn't in the Global Season 1 4-slot build on this page. If you don't slot it, the game skips this row.">Not in Global 4</span>`;
    }
    const q = (DS[b] || {}).q;
    return mmode === "early" && q > 1 ? `<span class="bdg lv" title="Learned at character level ${q}; until then the game skips this row">Lv ${q}</span>` : "";
  }
  function row(name, i) {
    const p0 = i === 0 ? " p0" : "";
    if (!name) return `<div class="sk empty"><i class="pr${p0}">${i}</i><span class="ic none" aria-hidden="true"></span><div class="nm">empty</div></div>`;
    const likely = /\?$/.test(name), f = find(name);
    const bits = [];
    if (f && f.s.cd) bits.push("CD " + cdText(f.s.cd));
    if (f && f.s.mp) bits.push("MP " + f.s.mp);
    return `<div class="sk"${hov(name)}><i class="pr${p0}">${i}</i>${ic(name)}<div class="nm">${esc(nice(base(name)))}${likely ? '<span class="flag">likely</span>' : ""}${badge(name)}<small>${f ? `<span class="tc">${esc(f.s.tw || "")}</span>` : ""}${bits.length ? `<span class="cd">${bits.join(DOT)}</span>` : ""}</small></div></div>`;
  }
  const stackHtml = (st) => `<div class="stack">${[3, 2, 1, 0].map((i) => row(st[i] || null, i)).join("")}</div>`;
  function entry(st, n, delay) {
    return `<div class="entry"><span class="n">${n}</span><div class="stackwrap">${stackHtml(st)}
      <div class="keyrow">${ic(st[0], "ic sm")}<span>Hotbar key · the macro presses this slot, row 0 first</span></div>
      <div class="delay"><span class="tc">延遲</span> Delay <b>${delay || 10}</b> ms</div></div></div>`;
  }
  function macroWindow(macros, delays, badge) {
    const seen = {};
    return `<div class="mw"><div class="mw-top">Macro <span class="tc">基本技能輔助功能</span>${badge || ""}<span class="x">×</span></div>${macros
      .map((m, i) => {
        const key = JSON.stringify(m);
        if (seen[key]) { // same slot again: the game shows it as another entry pointing to the same hotbar key
          return `<div class="entry"><span class="n">${i + 1}</span><div class="stackwrap"><div class="keyrow again"${hov(m[0])}>${ic(m[0], "ic sm")}<span><b>${esc(nice(base(m[0])))}</b> slot again (same stack as entry ${seen[key]})</span></div>
            <div class="delay"><span class="tc">延遲</span> Delay <b>${(delays && delays[i]) || 10}</b> ms</div></div></div>`;
        }
        seen[key] = i + 1;
        return entry(m, i + 1, delays && delays[i]);
      }).join("")}<span class="add">Add Macro</span></div>`;
  }
  function chip(n) {
    const f = find(n);
    return f ? `<span class="chip"${f.attr}>${ic(n, "ic sm")}${esc(nice(n))} <span class="tc">${esc(f.s.tw || "")}</span>${badge(n)}</span>` : `<span class="chip key">${esc(n)}</span>`;
  }
  const chips = (a) => `<div class="chips">${(a || []).map((x, i) => (i ? '<span class="plus">+</span>' : "") + chip(x)).join("")}</div>`;
  const list = (a) => `<div class="chips">${(a || []).map(chip).join("")}</div>`;
  function keyStacks(arr, note) {
    return (arr || []).map((e) => `<div class="extra"><span class="k gold">${esc(e.label)}</span><div class="stackwrap">${stackHtml(e.stack)}
      <div class="keyrow">${ic(e.stack[0], "ic sm")}<span>${note}</span></div></div></div>`).join("");
  }
  function altHtml(a) {
    return `<div class="alt"><b>${esc(a.t)}</b>${a.s ? `<p>${esc(a.s)}</p>` : ""}
      ${macroWindow(a.macros, a.delays)}
      ${a.hold ? `<div><span class="k">Hold together</span>${chips(a.hold)}</div>` : ""}
      ${keyStacks(a.extra, "Not in the macro")}</div>`;
  }
  function macros() {
    const d = M[mmode];
    const badge = mmode === "early" ? '<span class="rec">Improved</span>' : mmode === "full" ? '<span class="rec full">Full rotation</span>' : "";
    const alts = (d.alts || []).map(altHtml).join("");
    const sub = { late: "Late game · best tested setup, current patch", full: "Full rotation · longer macro with buffs", early: "Early game · leveling setup" }[mmode];
    return `<section class="panel" id="macros" aria-labelledby="h-mac">
      <div class="sec-h"><h2 id="h-mac">Macros<small>${sub} · stacks shown bottom-up like the game, row 0 fires first</small></h2>
        <div class="switch" role="group" aria-label="Game stage">
          <button type="button" data-m="late" aria-pressed="${mmode === "late"}">Late game</button>
          <button type="button" data-m="full" aria-pressed="${mmode === "full"}">Full rotation</button>
          <button type="button" data-m="early" aria-pressed="${mmode === "early"}">Early game</button></div></div>
      <div class="mac">
        <div class="mac-l">${macroWindow(d.macros, d.delays, badge)}
          ${d.keys ? `<div class="keys"><div class="keys-h">Other keys (not in the macro)</div>${keyStacks(d.keys, "Its own hotbar key · row 0 first")}</div>` : ""}</div>
        <div class="notes">
          ${d.loss ? `<p class="loss"><span class="k red">Trade-off</span>${esc(d.loss)}</p>` : ""}
          <div><span class="k">Hold together</span>${chips(d.hold)}</div>
          <div><span class="k gold">Press yourself</span>${list(d.manual)}</div>
          <p><span class="k">Why</span>${esc(d.why)}</p>
          ${d.tip ? `<p><span class="k gold">Tips</span>${esc(d.tip)}</p>` : ""}
          ${d.patch ? `<p class="patch"><span class="k red">Patch</span>${esc(d.patch)}</p>` : ""}
          ${d.queue ? `<p><span class="k blue">Skill queue</span>${esc(d.queue)} <span class="tc">技能預約</span></p>` : ""}
          ${O.hits && mmode !== "early" ? `<p class="check"><span class="k blue">Check your numbers</span>${esc(O.hits)}. Test for 1 minute on the training dummy with the DPS meter (<kbd>Ctrl</kbd>+<kbd>X</kbd>).</p>` : ""}
          ${d.src ? `<p class="src">Source: <a href="${esc(d.link)}" target="_blank" rel="noopener">${esc(d.src)}</a></p>` : `<p class="src">Built from the class's tested order using the skills you have while leveling. Alternatives are under "Other versions".</p>`}
          <div class="legend"><span><i class="pr p0">0</i> fires first when ready</span><span><i class="pr">3</i> fires last (filler)</span><span><span class="k blue" style="margin:0">likely</span> icon match, not named in the source</span><span><span class="bdg st">Stigma</span> level 22+</span><span><span class="bdg kr">Not in Global 4</span> KR/TW stigma, row skipped unless slotted</span></div>
          <p class="snote">New to the macro window? <a href="index.html#h-how">How a slot stack works</a>${DOT}<a href="index.html#h-setup">set it up</a>${DOT}<a href="index.html#h-chain">when a second line helps</a>.</p>
        </div>
      </div>
      ${alts ? `<details><summary>Other versions seen (${d.alts.length})</summary><div class="inner alts">${alts}</div></details>` : ""}
    </section>`;
  }

  /* ---------- stigmas ---------- */
  const lvCost = (l) => (l <= 5 ? 1 : l <= 10 ? 2 : l <= 15 ? 4 : l <= 20 ? 8 : 1);
  const costTo = (lv) => { let t = 0; for (let l = 1; l <= Math.min(lv, 20); l++) t += lvCost(l); return t; };
  const lvClass = (lv) => (lv >= 25 ? "l25" : lv > 20 ? "l2x" : lv === 20 ? "l20" : "lo");
  const V = () => (smode === "gl" && S.gl ? S.gl : S);
  function slots(pick, opts) {
    opts = opts || {};
    return `<div class="slots n${pick.length}">${pick.map((p, i) => {
      const n = Array.isArray(p) ? p[0] : p, lv = Array.isArray(p) ? p[1] : null;
      const mark = opts.against ? (opts.against.has(n) ? " hit" : " miss") : "";
      return `<div class="slot${mark}"${hov(n)}><div class="frame">${img(n)}<i class="no">${i + 1}</i>${lv ? `<b class="lvb ${lvClass(lv)}">${lv}</b>` : ""}</div>
        <div class="nm">${esc(n)}<small>${esc(tw(n))}</small></div></div>`;
    }).join("")}</div>`;
  }
  const tagClass = (t) => ({ "Most used": "main", "Battle tank": "tank", "Battle healer": "heal", Raid: "raid", PvP: "pvp", Solo: "solo" }[t] || "");
  function win(b, small) {
    return `<article class="sw${small ? " small" : ""}"><div class="sw-top"><span class="sw-title">${esc(b.t)}</span><span class="tag ${tagClass(b.tag)}">${esc(b.tag)}</span></div>
      ${slots(b.pick)}<div class="sw-body"><p>${esc(b.why)}</p>${srcHtml(b.src)}</div></article>`;
  }
  function imageWin(main) {
    const inMain = new Set(main.pick.map((p) => p[0]));
    const hits = S.image.filter((n) => inMain.has(n)).length;
    const note = (smode === "gl" && S.gl && S.gl.imageNote) || S.imageNote;
    const more = smode !== "gl" && S.image.length > main.pick.length ? ` Your image lists ${S.image.length}; with ${main.pick.length} slots, keep the ones outlined green.` : "";
    return `<article class="sw small"><div class="sw-top"><span class="sw-title">From your image</span><span class="tag img">${S.image.length} stigmas</span></div>
      ${slots(S.image, { against: inMain })}
      <div class="sw-body"><p class="match" style="color:${hits === Math.min(S.image.length, main.pick.length) ? "var(--ok)" : "var(--gold)"}">${hits} of ${S.image.length} are in the main build</p><p>${esc(note)}${esc(more)}</p>
      <p class="src">Green outline = also in the main build. Red dashed = not in it.</p></div></article>`;
  }
  function prio() {
    const lv = {};
    let norm = 0, adv = 0;
    return `<ol class="prio">${V().order.map((step) => {
      let sN = 0, sA = 0;
      const ch = step.s.map(([n, to]) => {
        const from = lv[n] || 0;
        for (let l = from + 1; l <= to; l++) { if (l > 20) sA++; else sN += lvCost(l); }
        lv[n] = Math.max(from, to);
        return `<span class="chip"${hov(n)}>${img(n)}${esc(n)} <span class="to${to > 20 ? " a" : ""}">${ARROW} ${to}</span></span>`;
      }).join("");
      norm += sN; adv += sA;
      const isAdv = sA > 0 && sN === 0;
      let cost = `+${sN} shards${DOT}running total <b>${norm}</b>`;
      if (isAdv) {
        const at20 = Object.values(lv).filter((l) => l >= 20).length, have = 5 + at20, short = adv - have;
        cost = `+${sA} Advanced shards${DOT}you have <b>${have}</b> (${at20} stigmas at 20 + 5 from levels 46${DASH}50)` + (short > 0 ? `${DOT}the last ${short} need ${short} more stigma${short > 1 ? "s" : ""} at 20 (+${short * 75} shards)` : "");
      }
      return `<li class="${isAdv ? "adv" : ""}"><div><div class="crow">${ch}</div><div class="cost">${cost}</div>${step.n ? `<p class="pnote">${esc(step.n)}</p>` : ""}</div></li>`;
    }).join("")}</ol>`;
  }
  function levels() {
    if (!(smode === "gl" && S.gl && S.gl.levels)) return "";
    return `<section class="panel inset"><h3>How high to level each<small>Stigma max is 20 in Global Season 1 · where to stop and why</small></h3><ul class="lvl">${S.gl.levels.map(([n, l, why]) =>
      `<li${hov(n)}>${img(n)}<div><b>${esc(n)}</b><span>${esc(why)}</span></div><div class="lt"><b class="lvb ${lvClass(l)}">${l}</b><small>${costTo(l)} shards</small></div></li>`).join("")}</ul></section>`;
  }
  function milestones() {
    const L = (S.milestones || []).filter(([label]) => smode !== "gl" || !/\b2[1-5]\b/.test(label));
    if (!L.length) return "";
    return `<section class="panel inset"><h3>Milestones to hit<small>Effects worth the shards</small></h3><ul class="ms">${L.map(([label, t]) => {
      const n = label.replace(/\s+\d+(\s*\/\s*\d+)?$/, "");
      return `<li${hov(n)}>${img(n)}<div><b>${esc(label)}</b>${esc(t)}</div></li>`;
    }).join("")}</ul></section>`;
  }
  function stigmas() {
    const v = V(), main = v.builds.find((b) => b.main) || v.builds[0], others = v.builds.filter((b) => b !== main);
    return `<section class="panel" id="stigmas" aria-labelledby="h-stg">
      <div class="sec-h"><h2 id="h-stg">Stigmas<small>${smode === "gl" ? "Global Season 1 · 4 slots · max level 20" : "KR/TW now · 6 slots · max level 25"} · hover a stigma for its effects by level</small></h2>
        <div class="switch" role="group" aria-label="Game version">
          <button type="button" data-s="gl" aria-pressed="${smode === "gl"}">Global · Season 1</button>
          <button type="button" data-s="kr" aria-pressed="${smode === "kr"}">KR/TW · 6 slots</button></div></div>
      <div class="cls-grid">
        <div class="stk"><div>${win(main)}</div>
          <div class="variants"><h3 class="vh">Other versions</h3>${imageWin(main)}${others.map((b) => win(b, true)).join("")}</div></div>
        <div class="stk">${levels()}
          <section class="panel inset"><h3>Level-up order<small>Top to bottom · cheap unlocks first · numbers are target levels</small></h3>${prio()}</section>
          ${milestones()}</div>
      </div>
      <p class="snote">Shard costs, slots and Advanced shards are explained on the <a href="index.html#h-stig">home page</a>.</p>
    </section>`;
  }

  /* ---------- skills to level, specializations, tiers ---------- */
  function skills() {
    const k = S.skills;
    if (!k) return "";
    const tagCls = { DPS: "t-dps", Buff: "t-buff", Heal: "t-heal", Debuff: "t-deb", Utility: "t-util" };
    const act = k.act.map(([n, lv, tag, why]) => `<li${hov(n)}>${img(n)}<div><b>${esc(nice(n))}<small>${esc(tw(n))}</small><i class="rt ${tagCls[tag] || ""}">${esc(tag)}</i></b><span>${esc(why)}</span></div>
      <div class="lt"><b class="lvb ${lv === "20" ? "l20" : "lo"}">${esc(lv.replace("-", DASH))}</b></div></li>`).join("");
    const pas = k.pas.map(([n, why], i) => `<li${hov(n)}>${img(n)}<div><b>${i + 1}. ${esc(nice(n))}<small>${esc(tw(n))}</small></b><span>${esc(why)}</span></div></li>`).join("");
    const first = k.first.map((n) => `<span class="chip"${hov(n)}>${img(n)}${esc(n)} <span class="to">${ARROW} 20</span></span>`).join("");
    return `<section class="panel" id="skills" aria-labelledby="h-skl"><h2 id="h-skl">Skills to level<small>Regular skills · best DPS and buff skills · target skill level</small></h2>
      <div class="first2"><span class="k">Push these two to 20 first</span><div class="crow">${first}</div>
        <p>Skill points only reach level 10. Levels 11${DASH}20 come from ring and weapon lines, Daevanion tiles and Arcana cards. Global launches with fewer Arcana cards, so lock in two skills before spreading out.</p></div>
      <div class="skl-grid">
        <div><h4 class="sh">Active skills</h4><ul class="lvl skl">${act}</ul></div>
        <div><h4 class="sh">Passives, in priority order</h4><ul class="lvl skl">${pas}</ul>
          <p class="snote" style="margin-top:10px">Passives have no picks: every level just adds more. Level them with armor, necklace and earring lines, Daevanion tiles and Bell / Mirror Arcana cards. Korean endgame players sit at 25${DASH}36 on their top passive.</p></div>
      </div>${srcHtml(k.src)}</section>`;
  }
  function specs() {
    if (!S.specs || !S.specs.length) return "";
    const cards = S.specs.map((sp) => {
      const d = DS[sp.n] || {};
      const opts = (d.s || []).map(([lv, t], i) => {
        const no = i + 1;
        return `<li class="o${no}${sp.pick.includes(no) ? " on" : ""}"><i>${no}</i><span>${esc(t)}</span><small>Lv ${lv}</small></li>`;
      }).join("");
      return `<article class="spec"><div class="spec-h"${hov(sp.n)}>${img(sp.n)}<div><b>${esc(nice(sp.n))}</b><small>${esc(tw(sp.n))}</small></div><span class="pick">${sp.pick.join(DOT)}</span></div>
        <ol class="opts">${opts}</ol>${sp.u20 ? `<p class="u20">Before skill Lv 20 (2 slots): <b>${sp.u20.join(" + ")}</b></p>` : ""}${sp.note ? `<p class="snote">${esc(sp.note)}</p>` : ""}
        <p class="src">Source: <a href="${esc(sp.src[1])}" target="_blank" rel="noopener">${esc(sp.src[0])}</a></p></article>`;
    }).join("");
    return `<section class="panel" id="specs" aria-labelledby="h-spc"><h2 id="h-spc">Skill specializations<small>Your regular skills, not stigmas · 3 of 5 per skill</small></h2>
      <p class="spec-rule">Each skill gets <b>1</b> specialty slot at skill level <b>8</b>, <b>2</b> at <b>12</b> and <b>3</b> at <b>20</b>. Options 1${DASH}3 unlock at 8, option 4 at 12, option 5 at 16. Highlighted = pick. Stigmas don't use this: they get every effect automatically as they level.</p>
      <div class="specs">${cards}</div></section>`;
  }
  function tiers() {
    const T = (smode === "gl" && S.gtiers) || S.tiers;
    const legend = smode === "gl"
      ? `<b style="color:var(--t-s)">S</b> always slot it, level 20${DOT}<b style="color:var(--t-a)">A</b> strong 4th pick or swap${DOT}<b style="color:var(--t-b)">B</b> situational${DOT}<b style="color:var(--t-c)">C</b> PvP or niche. PvE party play.`
      : `<b style="color:var(--t-s)">S</b> take to 25${DOT}<b style="color:var(--t-a)">A</b> core slot at 20${DOT}<b style="color:var(--t-b)">B</b> situational swap${DOT}<b style="color:var(--t-c)">C</b> PvP or niche. PvE party play.`;
    return `<section class="panel" id="tiers" aria-labelledby="h-tier"><h2 id="h-tier">Stigma tier list<small>All 13 ${esc(M.en)} stigmas · ${smode === "gl" ? "Global Season 1" : "KR/TW"} view · why each one is where it is</small></h2>
      <div class="tiers">${["S", "A", "B", "C"].filter((t) => T[t]).map((t) => `<div class="tier ${t}"><b>${t}</b><div class="items">${T[t].map(([n, why]) =>
        `<div class="ti"${hov(n)}>${img(n)}<div class="t">${esc(n)}<small>${esc(why)}</small></div></div>`).join("")}</div></div>`).join("")}</div>
      <p class="tier-key">${legend}</p></section>`;
  }

  /* ---------- gear, patches, sources ---------- */
  function gear() {
    const g = O.gear || {};
    const rows = [["Manastones / Soulstones", g.stones], ["Pet Genus", g.genus], ["Gear passives", g.passives], ["Wings", g.wings], ["Note", g.note]].filter((r) => r[1]);
    const wings = S.skills && S.skills.wings;
    return `<section class="panel gear" id="gear" aria-labelledby="h-gear"><h2 id="h-gear">Gear and stats<small>What changes for ${esc(M.en)} · Korean endgame advice</small></h2>
      <dl>${rows.map(([k, v]) => `<dt>${esc(k)}</dt><dd>${esc(v)}</dd>`).join("")}
        ${g.board ? `<dt>Daevanion</dt><dd>Take the skill tiles for your key actives first, then the orange tiles. Class node guide: <a href="${esc(g.board[1])}" target="_blank" rel="noopener">${esc(g.board[0])}</a></dd>` : `<dt>Daevanion</dt><dd>Take the skill tiles for your key actives first (they push skills past 10), then the orange tiles. Respec is nearly free.</dd>`}</dl>
      <p class="snote"><b style="color:#fff">Every class:</b> ${esc(OV.gearCommon)} <a href="index.html#h-gear">Stat values, Arcana and boards</a>.</p>
      ${wings && !g.wings ? `<p class="snote">Wings: ${esc(wings)}</p>` : ""}
    </section>`;
  }
  function patches() {
    const P = O.patches || [];
    const src = [].concat(O.src || []);
    return `<section class="panel" id="patches" aria-labelledby="h-pat"><h2 id="h-pat">Patches and sources<small>KR/TW changes that affect this page · Global can lag behind</small></h2>
      ${P.length ? `<div class="tbl-wrap"><table><thead><tr><th>Date</th><th>Change</th></tr></thead><tbody>${P.map(([d, t]) => `<tr><td><b>${esc(d)}</b></td><td>${esc(t)}</td></tr>`).join("")}</tbody></table></div>` : `<p class="snote">No ${esc(M.en)} changes in the recent KR/TW patches this page tracks (through Sep 30, 2026).</p>`}
      <p class="snote">Sep 23 (KR/TW): during Abyss boss fights, Rifts and Time-Space battles, Battlefield Might replaces party synergies such as Undefeated Mantra, Light of Protection, Power of the Storm, Fury and Experienced Counterstrike.</p>
      ${srcHtml(src, "Class guides used")}
    </section>`;
  }

  /* ---------- page ---------- */
  function render() {
    hide();
    document.body.dataset.mode = smode;
    $("view").innerHTML = overview() + macros() + stigmas() + skills() + specs() + tiers() + gear() + patches();
    spy();
  }
  function head() {
    document.title = `${M.en} · Aion 2 Class Guide`;
    $("h1").innerHTML = `${esc(M.en)}<span class="tc">${esc(M.tw)}</span>`;
    $("role").textContent = M.role;
    $("glance").textContent = O.glance;
    $("stamp").innerHTML = `Macros: <b>${esc(MAC.meta.patchBaseline)}</b>${DOT}Stigmas: <b>Global Season 1</b> + KR/TW${DOT}updated ${esc(MAC.meta.updated > STG.meta.updated ? MAC.meta.updated : STG.meta.updated)}`;
    if (MAC.meta.notice) { $("notice").textContent = MAC.meta.notice; $("notice").hidden = false; }
  }
  $("view").addEventListener("click", (e) => {
    const b = e.target.closest("button[data-m],button[data-s]");
    if (!b) return;
    if (b.dataset.m) { mmode = b.dataset.m; try { localStorage.setItem("aion2-mode", mmode); } catch (x) {} }
    if (b.dataset.s) { smode = b.dataset.s; try { localStorage.setItem("aion2-stigma-mode", smode); } catch (x) {} }
    const id = b.closest("section").id, y = b.getBoundingClientRect().top;
    render();
    const nb = document.querySelector(`#${id} button[data-${b.dataset.m ? "m" : "s"}="${b.dataset.m || b.dataset.s}"]`);
    if (nb) scrollBy(0, nb.getBoundingClientRect().top - y);
  });

  /* section nav highlight */
  let io = null;
  function spy() {
    const links = [...document.querySelectorAll("#secnav a")];
    if (io) io.disconnect();
    if (!("IntersectionObserver" in window)) return;
    io = new IntersectionObserver((ents) => {
      ents.forEach((en) => { if (en.isIntersecting) links.forEach((a) => a.classList.toggle("on", a.getAttribute("href") === "#" + en.target.id)); });
    }, { rootMargin: "-45% 0px -50% 0px" });
    document.querySelectorAll("#view > section[id]").forEach((s) => io.observe(s));
  }

  /* ---------- hover / tap card ---------- */
  const tipEl = document.createElement("div");
  tipEl.className = "skilltip"; tipEl.hidden = true; tipEl.setAttribute("role", "tooltip");
  document.body.appendChild(tipEl);
  let tipFor = null;
  function stigmaTip(k) {
    const s = DB[k] || {};
    const facts = ["Stigma", s.cd ? "Cooldown " + cdText(s.cd) : "No cooldown"];
    if (s.mp) facts.push("MP " + s.mp);
    if (s.m) facts.push("Castable while moving");
    facts.push("Learned at Lv 22");
    const L = (s.s || []).map(([lv, t]) => `<li><b>${lv}</b>${esc(t)}</li>`).join("") + (s.s25 ? `<li class="s25"><b>25</b>${esc(s.s25)} (KR/TW only)</li>` : "");
    return `<div class="tt-head">${s.icon ? `<img src="icons/${s.icon}.webp" alt="" width="44" height="44">` : ""}<div><div class="tt-name">${esc(s.en)}</div><div class="tt-sub">${esc(s.tw || "")}${DOT}${esc(s.ko || "")}</div></div></div>
      <div class="tt-facts">${facts.map((f) => `<span>${esc(f)}</span>`).join("")}</div>
      <p class="tt-desc">${esc(s.d || "No description in the database.")}</p>
      ${L ? `<div class="tt-spec-h">Effects by stigma level (all automatic)</div><ul class="tt-specs">${L}</ul>` : ""}
      ${s.note ? `<p class="tt-note">${esc(s.note)}</p>` : ""}
      <p class="tt-foot">Level 1${DASH}20 values from the Global client database; level 25 from KR/TW.</p>`;
  }
  function skillTip(n) {
    const s = SK[n] || {}, d = DS[n] || {};
    const k = CLS + ":" + nice(n);
    if (d.k === "Stigma" && DB[k]) return stigmaTip(k);
    const facts = [s.passive ? "Passive" : d.k === "Stigma" ? "Stigma" : "Skill"];
    if (s.cd) facts.push("Cooldown " + cdText(s.cd)); else if (!s.passive) facts.push("No cooldown");
    if (s.mp) facts.push("MP " + s.mp);
    if (d.r) facts.push("Range " + d.r);
    if (d.m) facts.push("Castable while moving");
    if (d.q) facts.push("Learned at Lv " + d.q);
    const opts = (d.s || []).map(([lv, t], i) => `<li><b>${s.passive ? lv : i + 1}</b>${esc(t)}${s.passive ? "" : ` (Lv ${lv})`}</li>`).join("");
    return `<div class="tt-head">${s.icon ? `<img src="icons/${s.icon}.webp" alt="" width="44" height="44">` : ""}<div><div class="tt-name">${esc(nice(n))}</div><div class="tt-sub">${esc(s.tw || "")}${DOT}${esc(s.ko || "")}</div></div></div>
      <div class="tt-facts">${facts.map((f) => `<span>${esc(f)}</span>`).join("")}</div>
      <p class="tt-desc">${esc(d.d || "No description in the database.")}</p>
      ${opts ? `<div class="tt-spec-h">Specialty options (pick up to 3)</div><ul class="tt-specs">${opts}</ul>` : ""}
      ${s.note ? `<p class="tt-note">${esc(s.note)}</p>` : ""}
      <p class="tt-foot">Skill level 1 values from the Global client database.</p>`;
  }
  function place(t) {
    const r = t.getBoundingClientRect(), w = tipEl.offsetWidth, h = tipEl.offsetHeight, pad = 10;
    let x = r.right + pad, y = r.top;
    if (x + w > innerWidth - pad) x = r.left - w - pad;
    if (x < pad) { x = Math.max(pad, Math.min(innerWidth - w - pad, r.left)); y = r.bottom + pad; }
    if (y + h > innerHeight - pad) y = Math.max(pad, innerHeight - h - pad);
    tipEl.style.left = x + "px"; tipEl.style.top = y + "px";
  }
  function show(t) {
    const k = t.getAttribute("data-sk"), n = t.getAttribute("data-skn");
    if (!k && !n) return;
    if (tipFor !== t) { tipEl.innerHTML = k ? stigmaTip(k) : skillTip(n); tipFor = t; }
    tipEl.hidden = false; place(t);
  }
  function hide() { tipEl.hidden = true; tipFor = null; }
  const SEL = "[data-sk],[data-skn]";
  document.addEventListener("mouseover", (e) => { const t = e.target.closest(SEL); if (t) show(t); });
  document.addEventListener("mouseout", (e) => { const t = e.target.closest(SEL); if (t && !t.contains(e.relatedTarget)) hide(); });
  document.addEventListener("focusin", (e) => { const t = e.target.closest(SEL); if (t) show(t); });
  document.addEventListener("focusout", hide);
  document.addEventListener("click", (e) => { const t = e.target.closest(SEL); if (t) { tipFor === t && !tipEl.hidden ? hide() : show(t); } else if (!tipEl.contains(e.target)) hide(); });
  document.addEventListener("keydown", (e) => { if (e.key === "Escape") hide(); });
  addEventListener("scroll", () => { if (tipFor) place(tipFor); }, { passive: true });

  /* ---------- load ---------- */
  try { const m = localStorage.getItem("aion2-mode"); if (["early", "late", "full"].includes(m)) mmode = m; } catch (e) {}
  try { const m = localStorage.getItem("aion2-stigma-mode"); if (m === "kr" || m === "gl") smode = m; } catch (e) {}
  const q = new URLSearchParams(location.search);
  if (["early", "late", "full"].includes(q.get("macro"))) mmode = q.get("macro");
  if (["gl", "kr"].includes(q.get("stigma"))) smode = q.get("stigma");
  const load = (f) => fetch(f).then((r) => { if (!r.ok) throw new Error(f + " " + r.status); return r.json(); });
  Promise.all(["data/macros.json", "data/stigmas.json", "data/classes.json", "data/stigma_db.json", "data/skills.json"].map(load).concat(load("data/descriptions.json").catch(() => ({}))))
    .then(([mac, stg, ov, db, sk, ds]) => {
      MAC = mac; STG = stg; OV = ov; DB = db; SK = sk; DS = ds;
      M = mac.classes.find((c) => c.id === CLS); S = stg.classes.find((c) => c.id === CLS); O = ov.classes[CLS];
      if (!M || !S || !O) throw new Error("no data for " + CLS);
      head(); render();
      if (location.hash) { const el = document.getElementById(location.hash.slice(1)); if (el) el.scrollIntoView(); }
    })
    .catch((e) => { $("view").innerHTML = `<p class="err">Couldn't load the class data (${esc(e.message)}). Refresh the page to try again.</p>`; });
})();
