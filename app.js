/* Aion 2 Macro Sheet: renders data/macros.json + data/skills.json.
   To update the sheet, edit the JSON files only. This file shouldn't need changes. */
(function () {
  const $ = (id) => document.getElementById(id);
  const esc = (s) => String(s).replace(/[&<>"]/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));
  let SK = {}, DATA = null, mode = "late";

  const base = (n) => n.replace(/\s*\(.*\)$/, "").replace(/ line$/, "").replace(/\?$/, "");
  function icon(name, size) {
    const s = SK[base(name || "")];
    const cls = size === "sm" ? "ic sm" : "ic";
    if (s && s.icon) return `<img class="${cls}" src="icons/${s.icon}.webp" alt="" width="40" height="40" loading="lazy">`;
    return `<span class="${cls} none" aria-hidden="true"></span>`;
  }
  function meta(name) {
    const s = SK[base(name)];
    if (!s) return "";
    const bits = [];
    if (s.cd) bits.push(`CD ${s.cd >= 60 && s.cd % 60 === 0 ? s.cd / 60 + " min" : s.cd + " s"}`);
    if (s.mp) bits.push(`MP ${s.mp}`);
    return bits.join(" \u00b7 ");
  }
  function tip(name) {
    const s = SK[base(name)];
    return s ? ` title="${esc(base(name))} \u00b7 ${esc(s.tw)} \u00b7 ${esc(s.ko)}${s.note ? " \u2014 " + esc(s.note) : ""}"` : "";
  }
  function row(name, i) {
    const p0 = i === 0 ? " p0" : "";
    if (!name) return `<div class="sk empty"><i class="pr${p0}">${i}</i><span class="ic none" aria-hidden="true"></span><div class="nm">empty</div></div>`;
    const likely = /\?$/.test(name);
    const s = SK[base(name)];
    const m = meta(name);
    return `<div class="sk"${tip(name)}><i class="pr${p0}">${i}</i>${icon(name)}<div class="nm">${esc(base(name))}${likely ? '<span class="flag">likely</span>' : ""}<small>${s ? `<span class="tc">${esc(s.tw)}</span>` : ""}${m ? `<span class="cd">${m}</span>` : ""}</small></div></div>`;
  }
  function entry(stack, n) {
    // Draw like the game: row 3 on top, row 0 just above the key.
    const rows = [3, 2, 1, 0].map((i) => row(stack[i] || null, i)).join("");
    return `<div class="entry"><span class="n">${n}</span><div class="stackwrap"><div class="stack">${rows}</div>
      <div class="keyrow">${icon(stack[0], "sm")}<span>Hotbar key \u00b7 the macro presses this slot, row 0 first</span></div>
      <div class="delay"><span class="tc">\u5ef6\u9072</span> Delay <b>10</b> ms</div></div></div>`;
  }
  function chip(n) {
    const s = SK[base(n)];
    return s ? `<span class="chip"${tip(n)}>${icon(n, "sm")}${esc(n)} <span class="tc">${esc(s.tw)}</span></span>` : `<span class="chip key">${esc(n)}</span>`;
  }
  const chips = (a) => `<div class="chips">${a.map((x, i) => (i ? '<span class="plus">+</span>' : "") + chip(x)).join("")}</div>`;
  const list = (a) => `<div class="chips">${a.map(chip).join("")}</div>`;

  function card(c) {
    const d = c[mode];
    const entries = d.macros.map((m, i) => entry(m, i + 1)).join("");
    const alts = (d.alts || []).map((a) => `<div class="alt"><b>${esc(a.t)}</b><span>${esc(a.s).replace(/([A-Z][\w' :]*?)\?/g, '$1 <span class="flag">likely</span>')}</span></div>`).join("");
    return `<section class="cls" id="${c.id}" aria-labelledby="h-${c.id}">
      <div class="cls-h"><h2 id="h-${c.id}">${esc(c.en)}<span class="tc">${esc(c.tw)}</span></h2><span class="role">${esc(c.role)}</span></div>
      <div class="mw"><div class="mw-top">Macro <span class="tc">\u57fa\u672c\u6280\u80fd\u8f14\u52a9\u529f\u80fd</span>${mode === "early" ? '<span class="rec">Improved</span>' : ""}<span class="x">\u00d7</span></div>${entries}<span class="add">Add Macro</span></div>
      <div class="notes">
        <div><span class="k">Hold together</span>${chips(d.hold)}</div>
        <div><span class="k gold">Press yourself</span>${list(d.manual)}</div>
        <p><span class="k">Why</span>${esc(d.why)}</p>
        ${d.tip ? `<p><span class="k gold">Tips</span>${esc(d.tip)}</p>` : ""}
        ${d.patch ? `<p class="patch"><span class="k red">Patch</span>${esc(d.patch)}</p>` : ""}
        ${d.queue ? `<p><span class="k blue">Skill queue</span>${esc(d.queue)} <span class="tc">\u6280\u80fd\u9810\u7d04</span></p>` : ""}
        ${d.src ? `<p class="src">Source: <a href="${esc(d.link)}" target="_blank" rel="noopener">${esc(d.src)}</a></p>` : `<p class="src">Improved build: the tested late-game order using only early skills. The video's version is under "Other versions".</p>`}
        ${alts ? `<details><summary>Other versions seen</summary><div class="inner">${alts}</div></details>` : ""}
      </div></section>`;
  }

  function render() {
    $("board").innerHTML = DATA.classes.map(card).join("");
    $("title").textContent = mode === "late" ? "Late Game Macros" : "Early Game Macros";
    $("stamp").innerHTML = mode === "late"
      ? `Current as of <b>${esc(DATA.meta.patchBaseline)}</b> \u00b7 updated ${esc(DATA.meta.updated)}`
      : `<b>Improved</b> from the video using the tested late-game orders \u00b7 updated ${esc(DATA.meta.updated)}`;
    $("btn-late").setAttribute("aria-pressed", mode === "late");
    $("btn-early").setAttribute("aria-pressed", mode === "early");
  }
  function setMode(m) { mode = m; render(); try { localStorage.setItem("aion2-mode", m); } catch (e) {} }

  $("btn-late").addEventListener("click", () => setMode("late"));
  $("btn-early").addEventListener("click", () => setMode("early"));
  try { const m = localStorage.getItem("aion2-mode"); if (m === "early" || m === "late") mode = m; } catch (e) {}
  if (location.hash === "#early") mode = "early";

  Promise.all([fetch("data/macros.json").then((r) => r.json()), fetch("data/skills.json").then((r) => r.json())])
    .then(([m, s]) => {
      DATA = m; SK = s; render();
      const cl = $("changelog");
      if (cl) cl.innerHTML = (m.changelog || []).map((c) => `<li><b>${esc(c.date)}</b> ${esc(c.text)}</li>`).join("");
      const nt = $("notice");
      if (nt && m.meta.notice) { nt.textContent = m.meta.notice; nt.hidden = false; }
    })
    .catch((e) => { $("board").innerHTML = `<p class="err">Couldn't load the macro data (${esc(e.message)}). Refresh the page to try again.</p>`; });
})();
