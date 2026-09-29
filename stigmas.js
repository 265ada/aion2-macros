/* Aion 2 Stigma Builds: renders data/stigmas.json (builds, order, tiers) + data/stigma_db.json (names, icons, effects).
   To update the page, edit the JSON files only. This file shouldn't need changes. */
(function () {
  const $ = (id) => document.getElementById(id);
  const esc = (s) => String(s == null ? "" : s).replace(/[&<>"]/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));
  const DOT = " \u00b7 ", ARROW = "\u2192";
  let DB = {}, DATA = null, cur = "templar";

  const key = (cls, n) => cls + ":" + n;
  const cdText = (cd) => (cd >= 60 && cd % 60 === 0 ? cd / 60 + " min" : cd + " s");
  // shard cost of one level (1..20 normal shards, 21..25 advanced)
  const lvCost = (l) => (l <= 5 ? 1 : l <= 10 ? 2 : l <= 15 ? 4 : l <= 20 ? 8 : 1);

  function initials(n) { return n.replace(/^[^:]+:\s*/, "").split(/\s+/).map((w) => w[0]).join("").slice(0, 2); }
  function img(cls, n, extra) {
    const s = DB[key(cls, n)];
    if (s && s.icon) return `<img src="icons/${s.icon}.webp" alt="" width="64" height="64" loading="lazy"${extra || ""}>`;
    return `<span class="none" aria-hidden="true">${esc(initials(n))}</span>`;
  }
  const hov = (cls, n) => (DB[key(cls, n)] ? ` data-sk="${esc(key(cls, n))}" tabindex="0"` : "");
  function lvClass(lv) { return lv >= 25 ? "l25" : lv > 20 ? "l2x" : lv === 20 ? "l20" : "lo"; }

  /* ---------- stigma window (6 slots) ---------- */
  function slots(cls, pick, opts) {
    opts = opts || {};
    return `<div class="slots">${pick.map((p, i) => {
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
    return `<article class="sw small">
      <div class="sw-top"><span class="sw-title">From your image</span><span class="tag img">${c.image.length} stigmas</span></div>
      ${slots(c.id, c.image, { against: inMain })}
      <div class="sw-body"><p class="match" style="color:${hits === c.image.length ? "var(--ok)" : "var(--gold)"}">${hits} of ${c.image.length} are in the main build</p><p>${esc(c.imageNote)}</p>
      <p class="src">Green outline = also in the main build. Red dashed = not in it.</p></div></article>`;
  }

  /* ---------- priority list with running shard totals ---------- */
  function prio(c) {
    const lv = {};
    let norm = 0, adv = 0;
    return `<ol class="prio">${c.order.map((step) => {
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
        cost = `+${stepA} Advanced shards${DOT}you have <b>${have}</b> (${at20} stigmas at 20 + 5 from levels 46\u201350)`
          + (short > 0 ? `${DOT}the last ${short} need ${short} more stigma${short > 1 ? "s" : ""} at 20 (+${short * 75} shards)` : "");
      }
      return `<li class="${isAdv ? "adv" : ""}"><div><div class="steps">${chips}</div><div class="cost">${cost}</div>${step.n ? `<p class="pnote">${esc(step.n)}</p>` : ""}</div></li>`;
    }).join("")}</ol>`;
  }

  function milestones(c) {
    return `<ul class="ms">${c.milestones.map(([label, text]) => {
      const n = label.replace(/\s+\d+(\s*\/\s*\d+)?$/, "");
      return `<li${hov(c.id, n)}>${img(c.id, n)}<div><b>${esc(label)}</b>${esc(text)}</div></li>`;
    }).join("")}</ul>`;
  }

  function tiers(c) {
    const label = { S: "Take to 25", A: "Core slot, level 20", B: "Situational", C: "PvP / niche" };
    return `<div class="tiers">${["S", "A", "B", "C"].filter((t) => c.tiers[t]).map((t) => `
      <div class="tier ${t}" title="${label[t]}"><b>${t}</b><div class="items">${c.tiers[t].map(([n, why]) =>
        `<div class="ti"${hov(c.id, n)}>${img(c.id, n)}<div class="t">${esc(n)}<small>${esc(why)}</small></div></div>`).join("")}</div></div>`).join("")}</div>
      <p class="tier-key"><b style="color:var(--t-s)">S</b> take to 25${DOT}<b style="color:var(--t-a)">A</b> core slot at 20${DOT}<b style="color:var(--t-b)">B</b> situational swap${DOT}<b style="color:var(--t-c)">C</b> PvP or niche. PvE party play.</p>`;
  }

  function view(c) {
    const main = c.builds.find((b) => b.main) || c.builds[0];
    const others = c.builds.filter((b) => b !== main);
    return `<section class="panel" aria-labelledby="h-cls">
      <div class="cls-head"><h2 id="h-cls">${esc(c.en)}<span class="tc">${esc(c.tw)}</span></h2><span class="role">${esc(c.role)}</span></div>
      <div class="cls-grid">
        <div class="col">
          <div>${win(c.id, main)}</div>
          <div class="variants"><h3 class="vh">Other versions</h3>${imageWin(c, main)}${others.map((b) => win(c.id, b, true)).join("")}</div>
        </div>
        <div class="col">
          <section class="panel" style="background:#141920"><h3>Level-up order<small>Top to bottom \u00b7 cheap unlocks first \u00b7 numbers are target levels</small></h3>${prio(c)}</section>
          <section class="panel" style="background:#141920"><h3>Milestones to hit<small>Effects worth the shards</small></h3>${milestones(c)}</section>
        </div>
      </div>
      <section class="panel" style="background:#141920"><h3>Tier list \u00b7 all 13 ${esc(c.en)} stigmas<small>Why each one is where it is</small></h3>${tiers(c)}</section></section>`;
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
    const specs = (s.s || []).map(([lv, t]) => `<li><b>${lv}</b>${esc(t)}</li>`).join("")
      + (s.s25 ? `<li class="s25"><b>25</b>${esc(s.s25)} (KR/TW)</li>` : "");
    return `<div class="tt-head">${s.icon ? `<img src="icons/${s.icon}.webp" alt="" width="44" height="44">` : ""}<div><div class="tt-name">${esc(s.en)}</div><div class="tt-sub">${esc(s.tw || "")}${DOT}${esc(s.ko || "")}</div></div></div>
      <div class="tt-facts">${facts.map((f) => `<span>${esc(f)}</span>`).join("")}</div>
      <p class="tt-desc">${esc(s.d || "No description in the database.")}</p>
      ${specs ? `<div class="tt-spec-h">Effects by stigma level</div><ul class="tt-specs">${specs}</ul>` : ""}
      ${s.note ? `<p class="tt-note">${esc(s.note)}</p>` : ""}
      <p class="tt-foot">Level 1 values from the Global client database; level 25 from KR/TW.</p>`;
  }
  function place(t) {
    const r = t.getBoundingClientRect(), w = tipEl.offsetWidth, h = tipEl.offsetHeight, pad = 10;
    let x = r.right + pad, y = r.top;
    if (x + w > innerWidth - pad) x = r.left - w - pad;
    if (x < pad) { x = Math.max(pad, Math.min(innerWidth - w - pad, r.left)); y = r.bottom + pad; }
    if (y + h > innerHeight - pad) y = Math.max(pad, innerHeight - h - pad);
    tipEl.style.left = x + "px"; tipEl.style.top = y + "px";
  }
  function show(t) { const k = t.getAttribute("data-sk"); if (!k) return; if (tipFor !== t) { tipEl.innerHTML = tipHtml(k); tipFor = t; } tipEl.hidden = false; place(t); }
  function hide() { tipEl.hidden = true; tipFor = null; }
  document.addEventListener("mouseover", (e) => { const t = e.target.closest("[data-sk]"); if (t) show(t); });
  document.addEventListener("mouseout", (e) => { const t = e.target.closest("[data-sk]"); if (t && !t.contains(e.relatedTarget)) hide(); });
  document.addEventListener("focusin", (e) => { const t = e.target.closest("[data-sk]"); if (t) show(t); });
  document.addEventListener("focusout", hide);
  document.addEventListener("click", (e) => { const t = e.target.closest("[data-sk]"); if (t) { tipFor === t && !tipEl.hidden ? hide() : show(t); } else if (!tipEl.contains(e.target)) hide(); });
  document.addEventListener("keydown", (e) => { if (e.key === "Escape") hide(); });
  addEventListener("scroll", () => { if (tipFor) place(tipFor); }, { passive: true });

  /* ---------- page ---------- */
  function ladder() {
    let h = "";
    for (let l = 1; l <= 25; l++) {
      const c = lvCost(l), cls = l > 20 ? "adv" : "t" + c, un = l % 5 === 0 ? " unlock" : "";
      h += `<div class="lv ${cls}${un}" title="Level ${l}: ${c} ${l > 20 ? "Advanced shard" : c === 1 ? "shard" : "shards"}"><i></i><span>${l % 5 === 0 || l === 1 ? l : ""}</span></div>`;
    }
    $("ladder").innerHTML = h;
  }
  function select(id, push) {
    const c = DATA.classes.find((x) => x.id === id) || DATA.classes[0];
    cur = c.id; hide();
    $("view").innerHTML = view(c);
    document.querySelectorAll("#picker button").forEach((b) => b.setAttribute("aria-pressed", b.dataset.id === cur));
    try { localStorage.setItem("aion2-stigma-class", cur); } catch (e) {}
    if (push) history.replaceState(null, "", "#" + cur);
  }

  ladder();
  const load = (f) => fetch(f).then((r) => { if (!r.ok) throw new Error(f + " " + r.status); return r.json(); });
  Promise.all([load("data/stigmas.json"), load("data/stigma_db.json")])
    .then(([m, db]) => {
      DATA = m; DB = db;
      $("picker").innerHTML = m.classes.map((c) => `<button type="button" data-id="${c.id}" aria-pressed="false">${esc(c.en)}<small>${esc(c.tw)}</small></button>`).join("");
      $("picker").addEventListener("click", (e) => { const b = e.target.closest("button"); if (b) select(b.dataset.id, true); });
      $("stamp").innerHTML = `Current as of <b>${esc(m.meta.baseline)}</b>${DOT}updated ${esc(m.meta.updated)}`;
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
