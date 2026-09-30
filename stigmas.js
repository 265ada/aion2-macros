/* Aion 2 Stigma Builds: renders data/stigmas.json (builds, order, tiers, specs) + data/stigma_db.json (stigma names, icons,
   effects) + data/skills.json / data/descriptions.json (skill specializations). Two views: Global Season 1 (4 slots, max 20)
   and KR/TW (6 slots, max 25). To update the page, edit the JSON files only. This file shouldn't need changes. */
(function () {
  const $ = (id) => document.getElementById(id);
  const esc = (s) => String(s == null ? "" : s).replace(/[&<>"]/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));
  const DOT = " \u00b7 ", ARROW = "\u2192", DASH = "\u2013";
  let DB = {}, SK = {}, DS = {}, DATA = null, cur = "templar", mode = "gl";

  const key = (cls, n) => cls + ":" + n;
  const cdText = (cd) => (cd >= 60 && cd % 60 === 0 ? cd / 60 + " min" : cd + " s");
  // shard cost of one level (1..20 normal shards, 21..25 advanced)
  const lvCost = (l) => (l <= 5 ? 1 : l <= 10 ? 2 : l <= 15 ? 4 : l <= 20 ? 8 : 1);
  const costTo = (lv) => { let t = 0; for (let l = 1; l <= Math.min(lv, 20); l++) t += lvCost(l); return t; };

  function initials(n) { return n.replace(/^[^:]+:\s*/, "").split(/\s+/).map((w) => w[0]).join("").slice(0, 2); }
  function img(cls, n) {
    const s = DB[key(cls, n)];
    if (s && s.icon) return `<img src="icons/${s.icon}.webp" alt="" width="64" height="64" loading="lazy">`;
    return `<span class="none" aria-hidden="true">${esc(initials(n))}</span>`;
  }
  function skImg(n) {
    const s = SK[n];
    if (s && s.icon) return `<img src="icons/${s.icon}.webp" alt="" width="44" height="44" loading="lazy">`;
    return `<span class="none" aria-hidden="true">${esc(initials(n))}</span>`;
  }
  const hov = (cls, n) => (DB[key(cls, n)] ? ` data-sk="${esc(key(cls, n))}" tabindex="0"` : "");
  function lvClass(lv) { return lv >= 25 ? "l25" : lv > 20 ? "l2x" : lv === 20 ? "l20" : "lo"; }
  const V = (c) => (mode === "gl" && c.gl ? c.gl : c); // builds / order for the active view

  /* ---------- stigma window ---------- */
  function slots(cls, pick, opts) {
    opts = opts || {};
    return `<div class="slots n${pick.length}">${pick.map((p, i) => {
      const n = Array.isArray(p) ? p[0] : p, lv = Array.isArray(p) ? p[1] : null;
      const s = DB[key(cls, n)] || {};
      const mark = opts.against ? (opts.against.has(n) ? " hit" : " miss") : "";
      return `<div class="slot${mark}"${hov(cls, n)}>
        <div class="frame">${img(cls, n)}<i class="no">${i + 1}</i>${lv ? `<b class="lvb ${lvClass(lv)}">${lv}</b>` : ""}</div>
        <div class="nm">${esc(n)}<small>${esc(s.tw || "")}</small></div></div>`;
    }).join("")}</div>`;
  }
  const tagClass = (t) => ({ "Most used": "main", "Battle tank": "tank", "Battle healer": "heal", Raid: "raid", PvP: "pvp", Solo: "solo" }[t] || "");
  function srcHtml(src) {
    if (!src || !src.length) return "";
    return `<p class="src">Sources: ${src.map(([t, u]) => (u ? `<a href="${esc(u)}" target="_blank" rel="noopener">${esc(t)}</a>` : esc(t))).join(DOT)}</p>`;
  }
  function win(cls, b, small) {
    return `<article class="sw${small ? " small" : ""}">
      <div class="sw-top"><span class="sw-title">${esc(b.t)}</span><span class="tag ${tagClass(b.tag)}">${esc(b.tag)}</span></div>
      ${slots(cls, b.pick)}
      <div class="sw-body"><p>${esc(b.why)}</p>${srcHtml(b.src)}</div></article>`;
  }
  function imageWin(c, main) {
    const inMain = new Set(main.pick.map((p) => p[0]));
    const hits = c.image.filter((n) => inMain.has(n)).length;
    const note = (mode === "gl" && c.gl && c.gl.imageNote) || c.imageNote;
    const more = mode !== "gl" && c.image.length > main.pick.length ? ` Your image lists ${c.image.length}; with ${main.pick.length} slots, keep the ones outlined green.` : "";
    return `<article class="sw small">
      <div class="sw-top"><span class="sw-title">From your image</span><span class="tag img">${c.image.length} stigmas</span></div>
      ${slots(c.id, c.image, { against: inMain })}
      <div class="sw-body"><p class="match" style="color:${hits === Math.min(c.image.length, main.pick.length) ? "var(--ok)" : "var(--gold)"}">${hits} of ${c.image.length} are in the main build</p><p>${esc(note)}${esc(more)}</p>
      <p class="src">Green outline = also in the main build. Red dashed = not in it.</p></div></article>`;
  }

  /* ---------- level-up order with running shard totals ---------- */
  function prio(c) {
    const lv = {};
    let norm = 0, adv = 0;
    const steps = V(c).order.map((step) => {
      let stepN = 0, stepA = 0;
      const chips = step.s.map(([n, to]) => {
        const from = lv[n] || 0;
        for (let l = from + 1; l <= to; l++) { if (l > 20) stepA++; else stepN += lvCost(l); }
        lv[n] = Math.max(from, to);
        return `<span class="chip"${hov(c.id, n)}>${img(c.id, n)}${esc(n)} <span class="to${to > 20 ? " a" : ""}">${ARROW} ${to}</span></span>`;
      }).join("");
      norm += stepN; adv += stepA;
      const isAdv = stepA > 0 && stepN === 0;
      let cost = `+${stepN} shards${DOT}running total <b>${norm}</b>`;
      if (isAdv) {
        const at20 = Object.values(lv).filter((l) => l >= 20).length;
        const have = 5 + at20, short = adv - have;
        cost = `+${stepA} Advanced shards${DOT}you have <b>${have}</b> (${at20} stigmas at 20 + 5 from levels 46${DASH}50)`
          + (short > 0 ? `${DOT}the last ${short} need ${short} more stigma${short > 1 ? "s" : ""} at 20 (+${short * 75} shards)` : "");
      }
      return `<li class="${isAdv ? "adv" : ""}"><div><div class="steps">${chips}</div><div class="cost">${cost}</div>${step.n ? `<p class="pnote">${esc(step.n)}</p>` : ""}</div></li>`;
    }).join("");
    return `<ol class="prio">${steps}</ol>`;
  }

  /* ---------- how high to level each (Global view) ---------- */
  function levels(c) {
    if (!(mode === "gl" && c.gl && c.gl.levels)) return "";
    const rows = c.gl.levels.map(([n, lv, why]) => `<li${hov(c.id, n)}>${img(c.id, n)}<div><b>${esc(n)}</b><span>${esc(why)}</span></div>
      <div class="lt"><b class="lvb ${lvClass(lv)}">${lv}</b><small>${costTo(lv)} shards</small></div></li>`).join("");
    return `<section class="panel inset"><h3>How high to level each<small>Stigma max is 20 in Global Season 1 \u00b7 where to stop and why</small></h3><ul class="lvl">${rows}</ul></section>`;
  }

  function milestones(c) {
    const list = (c.milestones || []).filter(([label]) => mode !== "gl" || !/\b2[1-5]\b/.test(label));
    if (!list.length) return "";
    return `<section class="panel inset"><h3>Milestones to hit<small>Effects worth the shards</small></h3><ul class="ms">${list.map(([label, text]) => {
      const n = label.replace(/\s+\d+(\s*\/\s*\d+)?$/, "");
      return `<li${hov(c.id, n)}>${img(c.id, n)}<div><b>${esc(label)}</b>${esc(text)}</div></li>`;
    }).join("")}</ul></section>`;
  }

  function tiers(c) {
    const T = (mode === "gl" && c.gtiers) || c.tiers;
    const legend = mode === "gl"
      ? `<b style="color:var(--t-s)">S</b> always slot it, level 20${DOT}<b style="color:var(--t-a)">A</b> strong 4th pick or swap${DOT}<b style="color:var(--t-b)">B</b> situational${DOT}<b style="color:var(--t-c)">C</b> PvP or niche. PvE party play.`
      : `<b style="color:var(--t-s)">S</b> take to 25${DOT}<b style="color:var(--t-a)">A</b> core slot at 20${DOT}<b style="color:var(--t-b)">B</b> situational swap${DOT}<b style="color:var(--t-c)">C</b> PvP or niche. PvE party play.`;
    return `<div class="tiers">${["S", "A", "B", "C"].filter((t) => T[t]).map((t) => `
      <div class="tier ${t}"><b>${t}</b><div class="items">${T[t].map(([n, why]) =>
        `<div class="ti"${hov(c.id, n)}>${img(c.id, n)}<div class="t">${esc(n)}<small>${esc(why)}</small></div></div>`).join("")}</div></div>`).join("")}</div>
      <p class="tier-key">${legend}</p>`;
  }

  /* ---------- skill specializations ---------- */
  function specs(c) {
    if (!c.specs || !c.specs.length) return "";
    const cards = c.specs.map((sp) => {
      const s = SK[sp.n] || {}, d = DS[sp.n] || {};
      const opts = (d.s || []).map(([lv, t], i) => {
        const no = i + 1, rank = sp.pick.indexOf(no);
        return `<li class="o${no}${rank >= 0 ? " on" : ""}"><i>${no}</i><span>${esc(t)}</span><small>Lv ${lv}</small></li>`;
      }).join("");
      const u20 = sp.u20 ? `<p class="u20">Before skill Lv 20 (2 slots): <b>${sp.u20.join(" + ")}</b></p>` : "";
      return `<article class="spec">
        <div class="spec-h">${skImg(sp.n)}<div><b>${esc(sp.n)}</b><small>${esc(s.tw || "")}</small></div><span class="pick">${sp.pick.join(DOT)}</span></div>
        <ol class="opts">${opts}</ol>${u20}${sp.note ? `<p class="snote">${esc(sp.note)}</p>` : ""}
        <p class="src">Source: <a href="${esc(sp.src[1])}" target="_blank" rel="noopener">${esc(sp.src[0])}</a></p></article>`;
    }).join("");
    return `<section class="panel inset" id="specs"><h3>Skill specializations to pick<small>Your regular skills, not stigmas \u00b7 3 of 5 per skill</small></h3>
      <p class="spec-rule">Each skill gets <b>1</b> specialty slot at skill level <b>8</b>, <b>2</b> at <b>12</b> and <b>3</b> at <b>20</b>. Options 1${DASH}3 unlock at 8, option 4 at 12, option 5 at 16. Highlighted = pick. Stigmas don't use this: they get every effect automatically as they level (hover a stigma to see them).</p>
      <div class="specs">${cards}</div></section>`;
  }

  /* ---------- regular skills to level (DPS / buffs / passives) ---------- */
  const nice = (n) => n.replace(/\s*\((gladiator|templar|assassin|ranger|sorcerer|spiritmaster|cleric|chanter)\)$/, "");
  const hovS = (n) => (SK[n] ? ` data-skn="${esc(n)}" tabindex="0"` : "");
  function skillsSec(c) {
    const k = c.skills;
    if (!k) return "";
    const tagCls = { DPS: "t-dps", Buff: "t-buff", Heal: "t-heal", Debuff: "t-deb", Utility: "t-util" };
    const act = k.act.map(([n, lv, tag, why]) => `<li${hovS(n)}>${skImg(n)}<div><b>${esc(nice(n))}<small>${esc((SK[n] || {}).tw || "")}</small><i class="rt ${tagCls[tag] || ""}">${esc(tag)}</i></b><span>${esc(why)}</span></div>
      <div class="lt"><b class="lvb ${lv === "20" ? "l20" : "lo"}">${esc(lv.replace("-", "\u2013"))}</b></div></li>`).join("");
    const pas = k.pas.map(([n, why], i) => `<li${hovS(n)}>${skImg(n)}<div><b>${i + 1}. ${esc(nice(n))}<small>${esc((SK[n] || {}).tw || "")}</small></b><span>${esc(why)}</span></div></li>`).join("");
    const first = k.first.map((n) => `<span class="chip"${hovS(n)}>${skImg(n)}${esc(n)} <span class="to">${ARROW} 20</span></span>`).join("");
    return `<section class="panel inset" id="skills"><h3>Skills to level<small>Your regular skills \u00b7 best DPS and buff skills \u00b7 target skill level</small></h3>
      <div class="first2"><span class="k">Push these two to 20 first</span><div class="steps">${first}</div>
        <p>Skill points only reach level 10. Levels 11${DASH}20 come from ring and weapon lines, Daevanion tiles and Arcana cards, and Global launches with fewer Arcana cards, so lock in two skills before spreading out.</p></div>
      <div class="skl-grid">
        <div><h4 class="sh">Active skills</h4><ul class="lvl skl">${act}</ul></div>
        <div><h4 class="sh">Passives, in priority order</h4><ul class="lvl skl">${pas}</ul>
          <p class="snote">Passives have no picks: every level just adds more. Level them with armor, necklace and earring lines, Daevanion tiles and Bell / Mirror Arcana cards. Korean endgame players sit at 25${DASH}36 on their top passive.</p>
          ${k.wings ? `<p class="snote"><b>Most-used wings in Korea (Aug 21):</b> ${esc(k.wings)}. Some may not be in Global at launch.</p>` : ""}</div>
      </div>${srcHtml(k.src)}</section>`;
  }

  function view(c) {
    const v = V(c);
    const main = v.builds.find((b) => b.main) || v.builds[0];
    const others = v.builds.filter((b) => b !== main);
    const cap = mode === "gl" ? "4 slots \u00b7 max level 20" : "6 slots \u00b7 max level 25";
    return `<section class="panel" aria-labelledby="h-cls">
      <div class="cls-head"><h2 id="h-cls">${esc(c.en)}<span class="tc">${esc(c.tw)}</span></h2><span class="role">${esc(c.role)}${DOT}${cap}</span></div>
      <div class="cls-grid">
        <div class="col">
          <div>${win(c.id, main)}</div>
          <div class="variants"><h3 class="vh">Other versions</h3>${imageWin(c, main)}${others.map((b) => win(c.id, b, true)).join("")}</div>
        </div>
        <div class="col">
          ${levels(c)}
          <section class="panel inset"><h3>Level-up order<small>Top to bottom \u00b7 cheap unlocks first \u00b7 numbers are target levels</small></h3>${prio(c)}</section>
          ${milestones(c)}
        </div>
      </div>
      ${skillsSec(c)}
      ${specs(c)}
      <section class="panel inset"><h3>Tier list \u00b7 all 13 ${esc(c.en)} stigmas<small>Why each one is where it is</small></h3>${tiers(c)}</section></section>`;
  }

  /* ---------- hover / tap card ---------- */
  const tipEl = document.createElement("div");
  tipEl.className = "skilltip"; tipEl.hidden = true; tipEl.setAttribute("role", "tooltip");
  document.body.appendChild(tipEl);
  let tipFor = null;
  function tipHtml(k) {
    const s = DB[k] || {};
    const facts = ["Stigma", s.cd ? "Cooldown " + cdText(s.cd) : "No cooldown"];
    if (s.mp) facts.push("MP " + s.mp);
    if (s.m) facts.push("Castable while moving");
    facts.push("Learned at Lv 22");
    const specsL = (s.s || []).map(([lv, t]) => `<li><b>${lv}</b>${esc(t)}</li>`).join("")
      + (s.s25 ? `<li class="s25"><b>25</b>${esc(s.s25)} (KR/TW only)</li>` : "");
    return `<div class="tt-head">${s.icon ? `<img src="icons/${s.icon}.webp" alt="" width="44" height="44">` : ""}<div><div class="tt-name">${esc(s.en)}</div><div class="tt-sub">${esc(s.tw || "")}${DOT}${esc(s.ko || "")}</div></div></div>
      <div class="tt-facts">${facts.map((f) => `<span>${esc(f)}</span>`).join("")}</div>
      <p class="tt-desc">${esc(s.d || "No description in the database.")}</p>
      ${specsL ? `<div class="tt-spec-h">Effects by stigma level (all automatic)</div><ul class="tt-specs">${specsL}</ul>` : ""}
      ${s.note ? `<p class="tt-note">${esc(s.note)}</p>` : ""}
      <p class="tt-foot">Level 1${DASH}20 values from the Global client database; level 25 from KR/TW.</p>`;
  }
  function place(t) {
    const r = t.getBoundingClientRect(), w = tipEl.offsetWidth, h = tipEl.offsetHeight, pad = 10;
    let x = r.right + pad, y = r.top;
    if (x + w > innerWidth - pad) x = r.left - w - pad;
    if (x < pad) { x = Math.max(pad, Math.min(innerWidth - w - pad, r.left)); y = r.bottom + pad; }
    if (y + h > innerHeight - pad) y = Math.max(pad, innerHeight - h - pad);
    tipEl.style.left = x + "px"; tipEl.style.top = y + "px";
  }
  function skillTip(n) {
    const s = SK[n] || {}, d = DS[n] || {};
    const facts = [s.passive ? "Passive" : "Skill"];
    if (s.cd) facts.push("Cooldown " + cdText(s.cd));
    if (s.mp) facts.push("MP " + s.mp);
    if (d.m) facts.push("Castable while moving");
    const opts = (d.s || []).map(([lv, t], i) => `<li><b>${i + 1}</b>${esc(t)} (Lv ${lv})</li>`).join("");
    return `<div class="tt-head">${s.icon ? `<img src="icons/${s.icon}.webp" alt="" width="44" height="44">` : ""}<div><div class="tt-name">${esc(nice(n))}</div><div class="tt-sub">${esc(s.tw || "")}${DOT}${esc(s.ko || "")}</div></div></div>
      <div class="tt-facts">${facts.map((f) => `<span>${esc(f)}</span>`).join("")}</div>
      <p class="tt-desc">${esc(d.d || "No description in the database.")}</p>
      ${opts ? `<div class="tt-spec-h">Specialty options (pick up to 3)</div><ul class="tt-specs">${opts}</ul>` : ""}
      ${s.note ? `<p class="tt-note">${esc(s.note)}</p>` : ""}
      <p class="tt-foot">Skill level 1 values from the Global client database.</p>`;
  }
  function show(t) {
    const k = t.getAttribute("data-sk"), n = t.getAttribute("data-skn");
    if (!k && !n) return;
    if (tipFor !== t) { tipEl.innerHTML = k ? tipHtml(k) : skillTip(n); tipFor = t; }
    tipEl.hidden = false; place(t);
  }
  function hide() { tipEl.hidden = true; tipFor = null; }
  document.addEventListener("mouseover", (e) => { const t = e.target.closest("[data-sk],[data-skn]"); if (t) show(t); });
  document.addEventListener("mouseout", (e) => { const t = e.target.closest("[data-sk],[data-skn]"); if (t && !t.contains(e.relatedTarget)) hide(); });
  document.addEventListener("focusin", (e) => { const t = e.target.closest("[data-sk],[data-skn]"); if (t) show(t); });
  document.addEventListener("focusout", hide);
  document.addEventListener("click", (e) => { const t = e.target.closest("[data-sk],[data-skn]"); if (t) { tipFor === t && !tipEl.hidden ? hide() : show(t); } else if (!tipEl.contains(e.target)) hide(); });
  document.addEventListener("keydown", (e) => { if (e.key === "Escape") hide(); });
  addEventListener("scroll", () => { if (tipFor) place(tipFor); }, { passive: true });

  /* ---------- page ---------- */
  function ladder() {
    const top = mode === "gl" ? 20 : 25;
    let h = "";
    for (let l = 1; l <= top; l++) {
      const c = lvCost(l), cls = l > 20 ? "adv" : "t" + c, un = l % 5 === 0 ? " unlock" : "";
      h += `<div class="lv ${cls}${un}" title="Level ${l}: ${c} ${l > 20 ? "Advanced shard" : c === 1 ? "shard" : "shards"}"><i></i><span>${l % 5 === 0 || l === 1 ? l : ""}</span></div>`;
    }
    $("ladder").style.gridTemplateColumns = `repeat(${top},minmax(0,1fr))`;
    $("ladder").innerHTML = h;
  }
  function stamp() {
    const m = DATA.meta;
    $("stamp").innerHTML = mode === "gl"
      ? `<b>Global Season 1</b>${DOT}4 slots${DOT}stigma max 20${DOT}balance = Global client DB${DOT}updated ${esc(m.updated)}`
      : `Current as of <b>${esc(m.baseline)}</b>${DOT}updated ${esc(m.updated)}`;
  }
  function select(id, push) {
    const c = DATA.classes.find((x) => x.id === id) || DATA.classes[0];
    cur = c.id; hide();
    $("view").innerHTML = view(c);
    document.querySelectorAll("#picker button").forEach((b) => b.setAttribute("aria-pressed", b.dataset.id === cur));
    try { localStorage.setItem("aion2-stigma-class", cur); } catch (e) {}
    if (push) history.replaceState(null, "", "#" + cur);
  }
  function setMode(m, keep) {
    mode = m; document.body.dataset.mode = m;
    ["gl", "kr"].forEach((x) => { const b = $("btn-" + x); if (b) b.setAttribute("aria-pressed", x === m); });
    $("h1").textContent = m === "gl" ? "Stigmas & Skills" : "Stigmas & Skills KR/TW";
    ladder();
    if (DATA) { stamp(); select(cur, false); }
    if (!keep) { try { localStorage.setItem("aion2-stigma-mode", m); } catch (e) {} }
  }

  try { const m = localStorage.getItem("aion2-stigma-mode"); if (m === "kr" || m === "gl") mode = m; } catch (e) {}
  ["gl", "kr"].forEach((x) => { const b = $("btn-" + x); if (b) b.addEventListener("click", () => setMode(x)); });
  setMode(mode, true);
  const load = (f) => fetch(f).then((r) => { if (!r.ok) throw new Error(f + " " + r.status); return r.json(); });
  Promise.all([load("data/stigmas.json"), load("data/stigma_db.json"), load("data/skills.json"), load("data/descriptions.json").catch(() => ({}))])
    .then(([m, db, sk, ds]) => {
      DATA = m; DB = db; SK = sk; DS = ds;
      $("picker").innerHTML = m.classes.map((c) => `<button type="button" data-id="${c.id}" aria-pressed="false">${esc(c.en)}<small>${esc(c.tw)}</small></button>`).join("");
      $("picker").addEventListener("click", (e) => { const b = e.target.closest("button"); if (b) select(b.dataset.id, true); });
      stamp();
      if (m.meta.notice) { $("notice").textContent = m.meta.notice; $("notice").hidden = false; }
      $("changelog").innerHTML = (m.changelog || []).map((c) => `<li><b>${esc(c.date)}</b>${esc(c.text)}</li>`).join("");
      let start = cur;
      try { start = localStorage.getItem("aion2-stigma-class") || start; } catch (e) {}
      const h = location.hash.slice(1);
      if (m.classes.some((c) => c.id === h)) start = h;
      select(start, false);
      addEventListener("hashchange", () => { const x = location.hash.slice(1); if (x !== cur && m.classes.some((c) => c.id === x)) select(x, false); });
    })
    .catch((e) => { $("view").innerHTML = `<p class="err">Couldn't load the stigma data (${esc(e.message)}). Refresh the page to try again.</p>`; });
})();
