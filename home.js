/* Aion 2 Class Guides home: class cards, DPS tier lists, stamp, stigma shard ladder and the merged update log. */
(function () {
  const $ = (id) => document.getElementById(id);
  const esc = (s) => String(s == null ? "" : s).replace(/[&<>"]/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));
  const ORDER = ["gladiator", "templar", "assassin", "ranger", "sorcerer", "spiritmaster", "cleric", "chanter"];

  // shard ladder (levels 1-25; 21-25 are KR/TW only)
  const cost = (l) => (l <= 5 ? 1 : l <= 10 ? 2 : l <= 15 ? 4 : l <= 20 ? 8 : 1);
  let h = "";
  for (let l = 1; l <= 25; l++) {
    const c = cost(l), cls = l > 20 ? "adv" : "t" + c, un = l % 5 === 0 ? " unlock" : "";
    h += `<div class="lv ${cls}${un}" title="Level ${l}: ${c} ${l > 20 ? "Advanced shard" : c === 1 ? "shard" : "shards"}"><i></i><span>${l % 5 === 0 || l === 1 ? l : ""}</span></div>`;
  }
  $("ladder").innerHTML = h;

  const load = (f) => fetch(f, { cache: "no-cache" }).then((r) => { if (!r.ok) throw new Error(f + " " + r.status); return r.json(); });

  // DPS tier lists: tiers are hand-set (see index.html), numbers come from data/topplayers.json (tools/notmeter_snapshot.py)
  const TIERS = {
    gl: { S: ["chanter"], A: ["gladiator", "sorcerer", "ranger"], B: ["assassin", "templar", "spiritmaster"], C: ["cleric"] },
    kr: { S: ["assassin", "sorcerer", "spiritmaster", "ranger"], A: ["gladiator", "templar"], B: ["chanter"], C: ["cleric"] },
  };
  // Pet Genus (data/genus.json, built by tools/build_genus.py from the Global client tables)
  function genusHome() {
    const el = $("genusHome");
    if (!el) return;
    load("data/genus.json").then((g) => {
      const n = (x) => Number(x).toLocaleString("en-US");
      const layout = `<div class="tbl-wrap"><table><thead><tr><th>Line</th><th>Type</th><th>What can roll (same on every board unless named)</th></tr></thead><tbody>${g.layout.map(([s, t, w]) => `<tr><td><b>${s}</b></td><td>${esc(t)}</td><td>${esc(w)}</td></tr>`).join("")}</tbody></table></div>`;
      const kr = `<p class="snote"><b style="color:#fff">Korea / Taiwan for comparison</b> (Inven, Jan 2026): ${g.kr.map(([s, t]) => `${esc(s)} ${esc(t)}`).join(" · ")}. Korean pets also level to 5; Global pets stop at 3.</p>`;
      const odds = `<div class="tbl-wrap"><table><thead><tr><th>Insight</th><th>XP to next</th><th>Lines open</th><th>Common</th><th>Rare</th><th>Epic</th><th>Unique</th><th>Heroic</th></tr></thead><tbody>${g.odds.map(([lv, o]) => `<tr><td><b>${lv}</b></td><td>${lv < 10 ? n(g.need[lv - 1]) : "max"}</td><td>${Math.min(lv, 9)}</td>${["common", "rare", "epic", "unique", "heroic"].map((k) => `<td>${o[k] ? o[k] + "%" : "–"}</td>`).join("")}</tr>`).join("")}</tbody></table></div>`;
      const plan = `<div class="tbl-wrap"><table><thead><tr><th>Board</th><th>Pets</th><th>Pet XP (all at Lv 3)</th><th>Analyses to Lv 9</th><th>to Lv 10</th><th>Crystals + kinah to 10</th></tr></thead><tbody>${Object.entries(g.plan).map(([b, v]) => `<tr><td><b>${esc(b)}</b></td><td>${v.pets}</td><td>${v.petXp ? n(v.petXp) : "none"}</td><td>${v.to9}</td><td>${v.to10}</td><td>${n(v.crystals10)} + ${n(v.kinah10)}</td></tr>`).join("")}</tbody></table></div>`;
      const lk = g.cost.lock.map((c, i) => `${i + 1}: ${g.cost.crystal + c} / ${n(g.cost.kinah + g.cost.lockKinah[i])}`).join(" · ");
      const chase = `<div class="tbl-wrap"><table><thead><tr><th>Target (at Insight 10)</th><th>Heroic</th><th>Unique or better</th><th>Epic or better</th></tr></thead><tbody>${g.chase.map(([t, h, u, e]) => `<tr><td>${esc(t)}</td><td>~${h}</td><td>~${u}</td><td>${e ? "~" + e : "–"}</td></tr>`).join("")}</tbody></table></div>`;
      const owned = g.owned.map(([b, c, t]) => `<li><b>${esc(b)}</b> (${c} pets at Lv 3): ${esc(t)}</li>`).join("");
      const cm = Object.entries(g.community.slot4).map(([b, t]) => `<li><b>${esc(b)} 4:</b> ${esc(t)}</li>`).join("");
      el.innerHTML = `<div class="cols2"><div><h4 class="sh">The Global line layout</h4>${layout}${kr}</div>
        <div><h4 class="sh">How to level and roll</h4><ol class="steps">
          <li><div><b>Collect pets to level 3</b> (5 + 25 + 75 souls each). Each pet level gives its board ${g.petExp.join(" / ")} Insight XP, and level 3 gives a permanent stat (below). Global caps pets at 3.</div></li>
          <li><div><b>Analyze without locks until Insight 10.</b> Each Analyze gives <b>${g.perLine} XP per unlocked open line</b> (locked lines give none), costs ${g.cost.crystal} of that board's soul crystals + ${n(g.cost.kinah)} kinah, and opens one more line per level. Heroic only appears at 9 (1%) and 10 (5%), so rolling for keepers before 10 wastes crystals.</div></li>
          <li><div><b>At 10, Special line 4 first:</b> Auto Analysis for Double Chance. Special only takes Special or rainbow (all-board) crystals and gets no XP from pets, so spend rainbow crystals there.</div></li>
          <li><div><b>Then line 4 on the other four boards</b>, then your class's 3/6/9 and 1/5 picks. Lock one keeper at a time: locks raise every later Analyze steeply.</div></li>
        </ol>
        <p class="snote"><b style="color:#fff">Analyze cost with locked lines</b> (crystals / kinah per Analyze): 0: ${g.cost.crystal} / ${n(g.cost.kinah)} · ${lk}.</p></div></div>
      <div class="cols2"><div><h4 class="sh">Grade odds and XP per Insight level</h4>${odds}</div>
        <div><h4 class="sh">How many Analyses it takes</h4>${plan}<p class="snote">Assumes no locks and every pet at level 3 (Special: no pet XP). Real totals are lower if you collect pets as you go.</p>
        <h4 class="sh" style="margin-top:12px">Expected Analyses to hit one specific line</h4>${chase}<p class="snote">From the client's grade odds and roll weights. With locked lines, multiply by the per-Analyze cost above: e.g. ~200 Analyses for a Heroic Critical Hit with one line locked ≈ ${n(200 * (g.cost.crystal + g.cost.lock[0]))} crystals.</p></div></div>
      <div class="cols2"><div><h4 class="sh">Pet owned effects (permanent, all at Lv 3)</h4><ul class="facts">${owned}</ul>
          <p class="snote">Might and Precision first (Kanon): in Korea each point of Might is +0.1% Attack and each point of Precision is +0.1% accuracy and crit (Inven). The Critical Hit +82 and Accuracy +130 from Cogni and Fera pets also show up in questlog's Global builds.</p></div>
        <div><h4 class="sh">What ${g.community.n} public Global builds put on line 4</h4><ul class="facts">${cm}</ul>
          <p class="snote">questlog.gg planners, a community signal rather than proof. Note how few take Critical Damage Boost on Cogni: on Global's smaller Damage Boost totals, PvE Damage Boost (2–4%) out-values it for every class. Class pages show the math.</p></div></div>
      <p class="src">Sources: ${g.meta.sources.map(([t, u]) => `<a href="${esc(u)}" target="_blank" rel="noopener">${esc(t)}</a>`).join(" · ")}.</p>`;
    }).catch(() => { el.innerHTML = '<p class="snote">Couldn&#39;t load the Genus data. Refresh to try again.</p>'; });
  }
  genusHome();

  function tierLists(mac) {
    const name = (id) => (mac.classes.find((c) => c.id === id) || { en: id }).en;
    const draw = (el, tiers, val) => {
      el.innerHTML = ["S", "A", "B", "C"].map((t) => `<div class="tier ${t}"><b>${t}</b><div class="items">${tiers[t].map((id) =>
        `<a class="ti" href="${id}.html"><div class="t">${esc(name(id))}<small>${val(id)}</small></div></a>`).join("")}</div></div>`).join("");
    };
    load("data/topplayers.json").then((tp) => {
      const cp = Object.fromEntries((tp.tiers.globalCp || []).map((r) => [r[0], r[1]]));
      const nm = Object.fromEntries((tp.tiers.globalNm || []).map((r) => [r[0], r[1]]));
      const kr = Object.fromEntries((tp.tiers.kr800 || []).map((r) => [r[0], r[1]]));
      const sgn = (v) => (v > 0 ? "+" : "") + v.toFixed(1) + "%";
      draw($("tierGl"), TIERS.gl, (id) => `${cp[id] != null ? sgn(cp[id]) + " at equal power" : ""}${nm[id] != null ? " · score " + Math.round(nm[id]) : ""}`);
      draw($("tierKr"), TIERS.kr, (id) => (kr[id] != null ? "score " + kr[id].toFixed(1) : ""));
    }).catch(() => { $("tierGl").innerHTML = $("tierKr").innerHTML = `<p class="snote">Couldn't load the tier numbers. Refresh to try again.</p>`; });
  }
  Promise.all(["data/macros.json", "data/stigmas.json", "data/classes.json", "data/stigma_db.json", "data/skills.json"].map(load))
    .then(([mac, stg, ov, db, sk]) => {
      const icon = (cls, n) => {
        const b = String(n || "").replace(/\?$/, "");
        const s = sk[b] || db[cls + ":" + b];
        return s && s.icon ? `<img src="icons/${s.icon}.webp" alt="${esc(b)}" title="${esc(b)}" width="30" height="30" loading="lazy">`
          : `<span class="none" title="${esc(b)}">${esc(b.split(/\s+/).map((w) => w[0]).join("").slice(0, 2))}</span>`;
      };
      $("cards").innerHTML = ORDER.map((id) => {
        const m = mac.classes.find((c) => c.id === id), s = stg.classes.find((c) => c.id === id), o = ov.classes[id];
        const cnt = {}; // show the entry the macro repeats most (the main damage line)
        m.late.macros.forEach((e) => { const k = JSON.stringify(e); cnt[k] = (cnt[k] || 0) + 1; });
        const top = m.late.macros.reduce((a, e) => (cnt[JSON.stringify(e)] > cnt[JSON.stringify(a)] ? e : a), m.late.macros[0]);
        const line = top.filter(Boolean).map((n) => icon(id, n)).join("");
        const gl = (s.gl ? s.gl.builds.find((b) => b.main) || s.gl.builds[0] : s.builds[0]).pick.map((p) => icon(id, p[0])).join("");
        return `<a class="card" href="${id}.html"><h2>${esc(m.en)}<span class="tc">${esc(m.tw)}</span></h2>
          <div class="role">${esc(m.role)}</div><p>${esc(o.glance)}</p>
          <div class="mini"><span>Macro line</span>${line}</div>
          <div class="mini"><span>Global stigmas</span>${gl}</div>
          <span class="go">Open the ${esc(m.en)} page →</span></a>`;
      }).join("");
      tierLists(mac);
      const upd = mac.meta.updated > stg.meta.updated ? mac.meta.updated : stg.meta.updated;
      $("stamp").innerHTML = `Macros: <b>${esc(mac.meta.patchBaseline)}</b> · Stigmas: <b>Global Season 1</b> + KR/TW · updated ${esc(upd)}`;
      if (mac.meta.notice) { $("notice").textContent = mac.meta.notice; $("notice").hidden = false; }
      const log = (mac.changelog || []).concat(stg.changelog || []).sort((a, b) => (a.date < b.date ? 1 : a.date > b.date ? -1 : 0));
      const seen = new Set();
      $("changelog").innerHTML = log.filter((c) => !seen.has(c.text) && seen.add(c.text)).map((c) => `<li><b>${esc(c.date)}</b>${esc(c.text)}</li>`).join("");
    })
    .catch((e) => { $("cards").innerHTML = `<p class="err">Couldn't load the class data (${esc(e.message)}). Refresh the page to try again.</p>`; });
})();
