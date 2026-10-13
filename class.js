/* Aion 2 Class Guides: renders one class page (body[data-class]) from
   data/macros.json (macros), data/stigmas.json (stigma builds, skills, specs, tiers), data/classes.json (overview, gear,
   patches), data/plans.json + data/topplayers.json (max damage plan, top-player numbers), data/genus.json (Pet Genus),
   data/stigma_db.json (stigmas),
   data/skills.json + data/descriptions.json (skill names, icons, hover text).
   To update a class, edit the JSON files only. */
(function () {
  const CLS = document.body.dataset.class;
  const $ = (id) => document.getElementById(id);
  const esc = (s) => String(s == null ? "" : s).replace(/[&<>"]/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));
  const DOT = " · ", ARROW = "→", DASH = "–";
  let SK = {}, DS = {}, DB = {}, MAC = null, STG = null, OV = null, PL = null, TP = null, GN = null;
  let M = null, S = null, O = null; // this class's macro / stigma / overview objects
  let mmode = "late", smode = "gl", gmode = "";

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

  /* ---------- max damage plan (data/plans.json + data/topplayers.json) ---------- */
  const pkBoxes = (n, picks) => picks.map((x) => {
    const o = ((DS[n] || {}).s || [])[x - 1];
    return `<i class="o${x}"${o ? ` title="${esc(x + ": " + o[1] + " (Lv " + o[0] + ")")}"` : ""}>${x}</i>`;
  }).join("");
  function plan() {
    const p = PL && PL.classes[CLS];
    if (!p) return "";
    const g = TP && TP.classes[CLS], kr = TP && TP.kr && TP.kr[CLS];
    const glLv = (n) => g && g.levels.find((r) => r[0] === n);
    const krAct = (n) => kr && kr.act.find((r) => r[0] === n);
    const order = p.order.map((o, i) => {
      const gl = glLv(o.n), k = krAct(o.n);
      const ev = [gl ? `Global top players: <b>${gl[1]}%</b> at 16+${DOT}<b>${gl[2]}%</b> at 20` : "", k ? `Korea top 20: Lv <b>${k[1]}</b>${k[2] ? " (" + k[2].split("").join(DOT) + ")" : ""}` : ""].filter(Boolean).join(DOT);
      const steps = o.steps.map(([lv, picks, t]) => `<li><span class="st-lv">Lv ${lv}</span><span class="pk">${pkBoxes(o.n, picks)}</span><span class="st-t">${esc(t)}</span></li>`).join("");
      return `<li${hov(o.n)}><span class="ord">${i + 1}</span>${img(o.n)}<div><b class="hd">${esc(nice(o.n))} <span class="to">${ARROW} ${o.to}</span>${o.gain ? `<em class="gain">${esc(o.gain)}</em>` : ""}</b>
        <span class="why">${esc(o.why)}</span><ol class="spsteps">${steps}</ol>${ev ? `<small class="ev">${ev}</small>` : ""}</div></li>`;
    }).join("");
    const dmg = g ? `<div class="tbl-wrap"><table class="dmgt"><thead><tr><th>Skill</th><th>% of damage</th><th>Casts / min</th><th>Top 10%</th></tr></thead><tbody>${g.dmg.map(([n, sh, c, ct]) => {
      const ch = (SK[n] || {}).chain, pet = (SK[n] || {}).pet;
      return `<tr><td${hov(n)}><span class="dn">${ic(n, "ic sm")}${esc(nice(n))}${ch ? `<small>${esc(ch)} chain</small>` : pet ? "<small>spirit, automatic</small>" : ""}</span></td><td><span class="bar"><i style="width:${Math.min(100, sh * 2.5)}%"></i></span>${sh}%</td><td>${c}</td><td>${ct}</td></tr>`;
    }).join("")}</tbody></table></div>
      <p class="snote">${g.parses} boss parses from ${g.players} top Global ${esc(M.en)}s (top 20 per boss; median combat power ${g.cp.toLocaleString("en-US")}). The top 10% of them did <b style="color:#fff">${g.topGain}%</b> more damage than their combat power predicts. Casts per minute cover the whole fight, downtime included, so a training dummy runs higher. Passive procs count as casts.</p>` : "";
    const auto = p.auto.map(([h, e, t]) => `<li><b>${esc(h)}<em class="est">${esc(e)}</em></b><span>${esc(t)}</span></li>`).join("");
    const stg = g ? g.stigmas.map(([n, pct, lv]) => `<span class="chip"${hov(n)}>${ic(n, "ic sm")}${esc(nice(n))} <span class="to">${pct}%</span>${lv ? ` <span class="tc">Lv ${lv}</span>` : ""}</span>`).join("") : "";
    const krb = kr ? `<div class="krend"><h4 class="sh">Korea endgame target (top 20 ${esc(M.en)}s, ${esc(kr.asof)})</h4>
        <ul class="lvl skl prio2">${kr.act.slice(0, 8).map(([n, lv, pk]) => `<li${hov(n)}>${img(n)}<div><b>${esc(nice(n))}</b><span class="pk">${pk ? pkBoxes(n, pk.split("").map(Number)) : "<em>no picks</em>"}</span></div><div class="lt"><b class="lvb ${lv >= 20 ? "l20" : "lo"}">${lv}</b></div></li>`).join("")}</ul>
        <p class="snote"><b style="color:#fff">Stigmas:</b> ${kr.stig.slice(0, 6).map(([n, eq, lv]) => `${esc(nice(n))} ${lv}`).join(DOT)} (6 slots, max 25 in Korea).</p>
        <p class="snote"><b style="color:#fff">Rings (active skill lines):</b> ${kr.rings.map((n) => esc(nice(n))).join(DOT)}${DOT}<b style="color:#fff">Arcana skill lines:</b> ${kr.arcana.slice(0, 7).map(([n, lv]) => `${esc(nice(n))} +${lv}`).join(DOT)}</p>
        <p class="snote"><b style="color:#fff">Passives:</b> ${kr.pas.slice(0, 5).map(([n, lv]) => `${esc(nice(n))} ${lv}`).join(DOT)}</p></div>` : "";
    return `<section class="panel" id="plan" aria-labelledby="h-plan">
      <h2 id="h-plan">Max damage plan<small>What to level first · specialty picks at each skill level · what automating costs · from top Global players this week</small></h2>
      <p class="ov-sum">${esc(p.sum)}</p>
      <div class="plan-grid">
        <div><h4 class="sh">Level order: skill level 16 is hard to reach, so go in this order</h4><ol class="lvord">${order}</ol>
          <p class="snote">Colored boxes are the specialty options to have slotted at that skill level (1 green … 5 red; hover a box for its effect). One slot at 8, two at 12, option 5 unlocks at 16, three slots at 20. The gain is an estimate for a player at the same gear, from top Global players' parses.</p></div>
        <div><h4 class="sh">Where top players' damage comes from</h4>${dmg}
          <h4 class="sh" style="margin-top:16px">Macro or by hand: what it costs</h4><ul class="auto">${auto}</ul></div>
      </div>
      <div class="cols2">
        <div><h4 class="sh">Stigmas top Global players run</h4><div class="chips">${stg}</div><p class="snote" style="margin-top:8px">${esc(p.stig)}</p></div>
        ${krb}
      </div>
      <p class="src">Data: <a href="https://notmeter.com/" target="_blank" rel="noopener">NotMeter</a> public statistics${TP ? ` (Global week of ${esc((TP.meta.week[0] || "").slice(0, 10))}, published ${esc(TP.meta.published)})` : ""}. Specialty picks are read from each parse's skill codes; level shares count a player as 16+ when option 5 is slotted and 20 when three options are. Estimates compare players at the same combat power, so treat ±3% as noise.</p>
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
    const sh = O.sheet || {};
    const prioList = (sh.skills || []).map(([n, lv, picks]) => `<li${hov(n)}>${img(n)}<div><b>${esc(nice(n))}<small>${esc(tw(n))}</small></b>
        <span class="pk">${picks.length ? picks.map((x) => `<i class="o${x}">${x}</i>`).join("") : '<em>no picks needed</em>'}</span></div>
      <div class="lt"><b class="lvb ${lv === "20" ? "l20" : "lo"}">${lv ? esc(lv) : "–"}</b></div></li>`).join("");
    const shPas = (sh.passives || []).map((n, i) => `<span class="chip"${hov(n)}>${img(n)}${i + 1}. ${esc(nice(n))}</span>`).join("");
    const sheetBlock = prioList ? `<div class="sheet-prio"><h4 class="sh">Global sheet: skill priority, target level and specialty picks</h4>
        <p class="snote">From the shared Global class sheet. Prioritize the skills marked 20 while leveling. Numbers in colored boxes are the specialty options to pick (1 green … 5 red); see Skill specializations below for what each one does.</p>
        <ul class="lvl skl prio2">${prioList}</ul>
        ${shPas ? `<div><span class="k">Passive priority (sheet)</span><div class="crow">${shPas}</div></div>` : ""}</div>` : "";
    return `<section class="panel" id="skills" aria-labelledby="h-skl"><h2 id="h-skl">Skills to level<small>Regular skills · target skill level · specialty picks</small></h2>
      ${sheetBlock}
      <div class="first2"><span class="k">Push these two to 20 first</span><div class="crow">${first}</div>
        <p>Skill points only reach level 10. Levels 11${DASH}20 come from ring and weapon lines, Daevanion tiles and Arcana cards. Global launches with fewer Arcana cards, so lock in two skills before spreading out.</p></div>
      <div class="skl-grid">
        <div><h4 class="sh">Why these skills (Korean endgame guides)</h4><ul class="lvl skl">${act}</ul></div>
        <div><h4 class="sh">Passives, with reasons</h4><ul class="lvl skl">${pas}</ul>
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
      return `<article class="spec"><div class="spec-h"${hov(sp.n)}>${img(sp.n)}<div><b>${esc(nice(sp.n))}</b><small>${esc(tw(sp.n))}</small></div><span class="pick">${sp.lvl ? `<small>Lv ${esc(sp.lvl)}</small>` : ""}${sp.pick.join(DOT)}</span></div>
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

  /* ---------- Pet Genus (data/genus.json, built by tools/build_genus.py) ---------- */
  const TAGC = { BiS: "t-bis", Conditional: "t-cond", "Low priority": "t-low", Unverified: "t-unv", "Preferred alternative": "t-alt", "Budget target": "t-bud" };
  function genus() {
    if (!GN || !GN.classes[CLS]) return "";
    const builds = GN.classes[CLS];
    const b = builds.find((x) => x.id === gmode) || builds[0];
    const tabs = builds.map((x) => `<button type="button" data-g="${esc(x.id)}" aria-pressed="${x === b}">${esc(x.name)}</button>`).join("");
    const pool = (board, s) => {
      const p = GN.pools[board][s - 1].by;
      return ["heroic", "unique", "epic"].filter((g) => p[g]).map((g) => `<p><b>${g[0].toUpperCase() + g.slice(1)}:</b> ${p[g].map(([n, lo, hi, pc]) => `${esc(n)} ${esc(lo)}–${esc(hi)}`).join(DOT)}</p>`).join("");
    };
    const board = (name) => {
      const rows = b.boards[name].map((l) => `<tr><td><b>${l.s}</b></td><td><b class="gpick">${esc(l.best)}</b><span class="gtag ${TAGC[l.tag] || ""}">${esc(l.tag)}</span></td>
        <td>${esc(l.alt)}</td><td>${esc(l.grade)}${l.target && l.target !== "—" ? `<br><small>${esc(l.target)}</small>` : ""}</td><td>${l.est ? `<b>${esc(l.est)}</b>` : `<small>${l.prio <= 3 ? "" : "low"}</small>`}</td>
        <td class="gwhy">${esc(l.why)}</td><td><span class="gconf c-${esc(l.conf.toLowerCase())}">${esc(l.conf)}</span></td></tr>`).join("");
      return `<div class="gboard"><h4 class="sh">${esc(name)}</h4><div class="tbl-wrap"><table class="gtbl"><thead><tr><th>Line</th><th>Pick</th><th>Alternative</th><th>Target</th><th>Max roll ≈</th><th>Why</th><th>Confidence</th></tr></thead><tbody>${rows}</tbody></table></div>
        <details><summary>Everything that can roll on ${esc(name)} (Global client)</summary><div class="inner gpool">${[1, 2, 3, 4, 5, 6, 7, 8, 9].map((s) => `<div><b>Line ${s}</b>${pool(name, s)}</div>`).join("")}</div></details></div>`;
    };
    const old = (O.gear || {}).genusOld || "";
    return `<section class="panel" id="genus" aria-labelledby="h-genus"><div class="sec-h"><h2 id="h-genus">Pet Genus<small>Global client · all 5 boards × 9 lines · what to roll for ${esc(M.en)} and why</small></h2>
        <div class="switch" role="group" aria-label="Build">${tabs}</div></div>
      <div class="gaudit"><b>Audit, Oct 13:</b> this page used to say <i>${esc(old || "")}</i>. That is Korea's layout: on Korea's client Double Chance rolls on slots 3 and 9. On the Global client (build ${esc(GN.meta.client)}), Double Chance rolls <b>only on Special line 4</b> (max 3%), lines 3/6/9 are crit / accuracy lines and lines 2/8 are defensive. Everything below is built from the Global client's own tables, cross-checked line by line against a second datamine. <a href="index.html#h-genus">How Genus works on Global</a>.</div>
      <p class="ov-sum"><b>${esc(b.name)}</b>${DOT}${esc(b.role)}. ${esc(b.profile)}</p>
      <div class="cols2">
        <div><h4 class="sh">Where to spend first (all boards)</h4><ol class="grank">${b.rank.map(([t, e]) => `<li><span>${esc(t)}</span>${e ? `<b>${esc(e)}</b>` : ""}</li>`).join("")}</ol>
          <p class="snote">“Max roll ≈” is the estimated damage gain from a top-of-range Heroic roll for a ${esc(M.en)} at top Global players' crit and positioning. It's a model, not a measurement: ranks are solid, exact percentages are ±30%.</p></div>
        <div><h4 class="sh">Caps, breakpoints and exceptions</h4><ul class="facts">${b.caps.map((c) => `<li>${esc(c)}</li>`).join("")}</ul>
          <p class="snote"><b style="color:#fff">Budget:</b> ${esc(b.budget)}</p><p class="snote"><b style="color:#fff">Endgame:</b> ${esc(b.endgame)}</p></div>
      </div>
      <div class="gboards">${["Special", "Cogni", "Fera", "Natura", "Varian"].map(board).join("")}</div>
      <p class="snote"><span class="gtag t-bis">BiS</span> best supported pick${DOT}<span class="gtag t-cond">Conditional</span> best only under the stated condition${DOT}<span class="gtag t-low">Low priority</span> fill last, never lock${DOT}Confidence: <span class="gconf c-high">High</span> robust under every assumption tested${DOT}<span class="gconf c-medium">Medium</span> depends on Global stat totals or an unpublished value${DOT}<span class="gconf c-low">Low</span> PvP or thin evidence.</p>
      ${O.sheet && O.sheet.genus ? `<details><summary>What the Global class sheet lists (for comparison)</summary><div class="inner cols3">${Object.entries(O.sheet.genus).map(([bd, lines]) => `<div><b>${esc(bd)}</b><ul class="facts">${lines.map((l) => `<li>${esc(l)}</li>`).join("")}</ul></div>`).join("")}</div><p class="snote" style="padding:0 14px 12px">The sheet copies Kanon's Global list: its line layout is right, but it puts Critical Damage Boost, Weapon Damage Boost, Multi-hit or Front/Back Damage Boost on line 4 and Crit / Accuracy / Power Shard on 3/6/9 for every class. The tables above re-rank line 4 for Global's smaller Damage Boost totals and set 3/6/9 by each class's real crit rate.</p></details>` : ""}
      <p class="src">Sources: ${GN.meta.sources.map(([t, u]) => `<a href="${esc(u)}" target="_blank" rel="noopener">${esc(t)}</a>`).join(DOT)}.</p>
    </section>`;
  }

  /* ---------- gear, patches, sources ---------- */
  function gear() {
    const g = O.gear || {};
    const rows = [["Manastones / Soulstones", g.stones], ["Pet Genus", g.genus], ["Gear passives", g.passives], ["Wings", g.wings], ["Note", g.note]].filter((r) => r[1]);
    const wings = S.skills && S.skills.wings;
    return `<section class="panel gear" id="gear" aria-labelledby="h-gear"><h2 id="h-gear">Gear and stats<small>What changes for ${esc(M.en)} · Global class sheet + Korean endgame advice</small></h2>
      <dl>${rows.map(([k, v]) => `<dt>${esc(k)}</dt><dd>${esc(v)}</dd>`).join("")}
        ${g.board ? `<dt>Daevanion</dt><dd>Take the skill tiles for your key actives first, then the orange tiles. Class node guide: <a href="${esc(g.board[1])}" target="_blank" rel="noopener">${esc(g.board[0])}</a></dd>` : `<dt>Daevanion</dt><dd>Take the skill tiles for your key actives first (they push skills past 10), then the orange tiles. Respec is nearly free.</dd>`}</dl>
      ${sheetGear()}
      <p class="snote"><b style="color:#fff">Every class (Korean endgame):</b> ${esc(OV.gearCommon)} <a href="index.html#h-gear">Stat values, Arcana and boards</a>.</p>
      ${wings && !g.wings ? `<p class="snote">Wings: ${esc(wings)}</p>` : ""}
    </section>`;
  }
  function sheetGear() {
    const sh = O.sheet;
    if (!sh) return "";
    const tbl = (head, rows) => rows.length ? `<div class="tbl-wrap"><table><thead><tr>${head.map((h) => `<th>${esc(h)}</th>`).join("")}</tr></thead><tbody>${rows.map((r) => `<tr>${r.map((c, i) => `<td>${i ? esc(c) : `<b>${esc(c)}</b>`}</td>`).join("")}</tr>`).join("")}</tbody></table></div>` : "";
    const gear = Object.entries(sh.gear || {});
    const acc = Object.entries(sh.acc || {});
    const genus = Object.entries(sh.genus || {});
    const misc = [["Manastone stats", sh.stones], ["Enhancing priority", sh.enhance], ["Meta wings", sh.wings], ["Wings worth leveling", sh.wingsLevel], ["Theostones", sh.theostones]]
      .concat(Object.entries(sh.titles || {})).concat(Object.entries(sh.pantheon || {}).map(([k, v]) => ["Pantheon " + k.toLowerCase(), v])).filter((r) => r[1]);
    return `<div class="sheet-gear"><h4 class="sh">Global class sheet: soul binding lines by piece (best first)</h4>
      <div class="cols2">${tbl(["Piece", "Lines to keep, best first"], gear)}${tbl(["Accessory", "Lines to keep, best first"], acc)}</div>
      <h4 class="sh">Arcana, god stats and equip effects to target</h4>
      ${tbl(["Arcana card", "God stat", "Equip effect / skills to target"], (sh.cards || []).map((r) => [r[0], r[1], r[2].replace(/\s*\(\d\)\s*/g, ", ").replace(/^, /, "").replace(/\s+/g, " ").trim()]))}
      <dl>${misc.map(([k, v]) => `<dt>${esc(k)}</dt><dd>${esc(v)}</dd>`).join("")}</dl>
      ${genus.length ? `<details><summary>Pet Genus lines by board (Global)</summary><div class="inner cols3">${genus.map(([b, lines]) => `<div><b>${esc(b)}</b><ul class="facts">${lines.map((l) => `<li>${esc(l)}</li>`).join("")}</ul></div>`).join("")}</div></details>` : ""}
      <p class="src">Source: <a href="${esc(OV.sheet.src)}" target="_blank" rel="noopener">Global class sheet by ${esc(OV.sheet.author)}</a>${sh.guide ? `${DOT}<a href="${esc(sh.guide)}" target="_blank" rel="noopener">${esc(M.en)} in-depth guide</a>` : ""}${sh.creator ? `${DOT}<a href="${esc(sh.creator)}" target="_blank" rel="noopener">content creator</a>` : ""}. The sheet's author notes it's a base to adjust as you learn, not 100% guaranteed.</p></div>`;
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
    $("view").innerHTML = overview() + plan() + macros() + stigmas() + skills() + specs() + tiers() + gear() + genus() + patches();
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
    const b = e.target.closest("button[data-m],button[data-s],button[data-g]");
    if (!b) return;
    if (b.dataset.m) { mmode = b.dataset.m; try { localStorage.setItem("aion2-mode", mmode); } catch (x) {} }
    if (b.dataset.s) { smode = b.dataset.s; try { localStorage.setItem("aion2-stigma-mode", smode); } catch (x) {} }
    if (b.dataset.g) { gmode = b.dataset.g; try { localStorage.setItem("aion2-genus-build", gmode); } catch (x) {} }
    const id = b.closest("section").id, y = b.getBoundingClientRect().top;
    render();
    const k = b.dataset.m ? "m" : b.dataset.s ? "s" : "g";
    const nb = document.querySelector(`#${id} button[data-${k}="${b.dataset[k]}"]`);
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
  try { gmode = localStorage.getItem("aion2-genus-build") || ""; } catch (e) {}
  const q = new URLSearchParams(location.search);
  if (["early", "late", "full"].includes(q.get("macro"))) mmode = q.get("macro");
  if (["gl", "kr"].includes(q.get("stigma"))) smode = q.get("stigma");
  const load = (f) => fetch(f, { cache: "no-cache" }).then((r) => { if (!r.ok) throw new Error(f + " " + r.status); return r.json(); });
  const opt = (f) => load(f).catch(() => null);
  Promise.all(["data/macros.json", "data/stigmas.json", "data/classes.json", "data/stigma_db.json", "data/skills.json"].map(load).concat([opt("data/descriptions.json"), opt("data/plans.json"), opt("data/topplayers.json"), opt("data/genus.json")]))
    .then(([mac, stg, ov, db, sk, ds, pl, tp, gn]) => {
      MAC = mac; STG = stg; OV = ov; DB = db; SK = sk; DS = ds || {}; PL = pl; TP = tp; GN = gn;
      M = mac.classes.find((c) => c.id === CLS); S = stg.classes.find((c) => c.id === CLS); O = ov.classes[CLS];
      if (!M || !S || !O) throw new Error("no data for " + CLS);
      head(); render();
      if (location.hash) { const el = document.getElementById(location.hash.slice(1)); if (el) el.scrollIntoView(); }
    })
    .catch((e) => { $("view").innerHTML = `<p class="err">Couldn't load the class data (${esc(e.message)}). Refresh the page to try again.</p>`; });
})();
