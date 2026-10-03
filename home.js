/* Aion 2 Class Guides home: class cards, stamp, stigma shard ladder and the merged update log. */
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
      const upd = mac.meta.updated > stg.meta.updated ? mac.meta.updated : stg.meta.updated;
      $("stamp").innerHTML = `Macros: <b>${esc(mac.meta.patchBaseline)}</b> · Stigmas: <b>Global Season 1</b> + KR/TW · updated ${esc(upd)}`;
      if (mac.meta.notice) { $("notice").textContent = mac.meta.notice; $("notice").hidden = false; }
      const log = (mac.changelog || []).concat(stg.changelog || []).sort((a, b) => (a.date < b.date ? 1 : a.date > b.date ? -1 : 0));
      const seen = new Set();
      $("changelog").innerHTML = log.filter((c) => !seen.has(c.text) && seen.add(c.text)).map((c) => `<li><b>${esc(c.date)}</b>${esc(c.text)}</li>`).join("");
    })
    .catch((e) => { $("cards").innerHTML = `<p class="err">Couldn't load the class data (${esc(e.message)}). Refresh the page to try again.</p>`; });
})();
