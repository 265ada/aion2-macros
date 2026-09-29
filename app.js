/* Aion 2 Macro Sheet: renders data/macros.json + data/skills.json + data/descriptions.json.
   To update the sheet, edit the JSON files only. This file shouldn't need changes. */
(function () {
  const $ = (id) => document.getElementById(id);
  const esc = (s) => String(s == null ? "" : s).replace(/[&<>"]/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));
  let SK = {}, DS = {}, DATA = null, mode = "late";

  const base = (n) => String(n || "").replace(/\s*\(.*\)$/, "").replace(/ line$/, "").replace(/\?$/, "");
  const cdText = (cd) => (cd >= 60 && cd % 60 === 0 ? cd / 60 + " min" : cd + " s");

  function icon(name, size) {
    const s = SK[base(name)];
    const cls = size === "sm" ? "ic sm" : "ic";
    if (s && s.icon) return `<img class="${cls}" src="icons/${s.icon}.webp" alt="" width="40" height="40" loading="lazy">`;
    return `<span class="${cls} none" aria-hidden="true"></span>`;
  }
  function meta(name) {
    const s = SK[base(name)];
    if (!s) return "";
    const bits = [];
    if (s.cd) bits.push("CD " + cdText(s.cd));
    if (s.mp) bits.push("MP " + s.mp);
    return bits.join(" \u00b7 ");
  }
  const hov = (name) => (SK[base(name)] ? ` data-skill="${esc(base(name))}" tabindex="0"` : "");

  function row(name, i) {
    const p0 = i === 0 ? " p0" : "";
    if (!name) return `<div class="sk empty"><i class="pr${p0}">${i}</i><span class="ic none" aria-hidden="true"></span><div class="nm">empty</div></div>`;
    const likely = /\?$/.test(name);
    const s = SK[base(name)];
    const m = meta(name);
    return `<div class="sk"${hov(name)}><i class="pr${p0}">${i}</i>${icon(name)}<div class="nm">${esc(base(name))}${likely ? '<span class="flag">likely</span>' : ""}<small>${s ? `<span class="tc">${esc(s.tw)}</span>` : ""}${m ? `<span class="cd">${m}</span>` : ""}</small></div></div>`;
  }
  function stackHtml(stack) {
    // Drawn like the game: row 3 on top, row 0 just above the key.
    return `<div class="stack">${[3, 2, 1, 0].map((i) => row(stack[i] || null, i)).join("")}</div>`;
  }
  function entry(stack, n, delay) {
    return `<div class="entry"><span class="n">${n}</span><div class="stackwrap">${stackHtml(stack)}
      <div class="keyrow">${icon(stack[0], "sm")}<span>Hotbar key \u00b7 the macro presses this slot, row 0 first</span></div>
      <div class="delay"><span class="tc">\u5ef6\u9072</span> Delay <b>${delay || 10}</b> ms</div></div></div>`;
  }
  function macroWindow(macros, delays, badge) {
    return `<div class="mw"><div class="mw-top">Macro <span class="tc">\u57fa\u672c\u6280\u80fd\u8f14\u52a9\u529f\u80fd</span>${badge || ""}<span class="x">\u00d7</span></div>${macros
      .map((m, i) => entry(m, i + 1, delays && delays[i])).join("")}<span class="add">Add Macro</span></div>`;
  }
  function chip(n) {
    const s = SK[base(n)];
    return s ? `<span class="chip"${hov(n)}>${icon(n, "sm")}${esc(n)} <span class="tc">${esc(s.tw)}</span></span>` : `<span class="chip key">${esc(n)}</span>`;
  }
  const chips = (a) => `<div class="chips">${a.map((x, i) => (i ? '<span class="plus">+</span>' : "") + chip(x)).join("")}</div>`;
  const list = (a) => `<div class="chips">${a.map(chip).join("")}</div>`;

  function altHtml(a) {
    const extra = (a.extra || []).map((e) => `<div class="extra"><span class="k gold">${esc(e.label)}</span><div class="stackwrap">${stackHtml(e.stack)}
      <div class="keyrow">${icon(e.stack[0], "sm")}<span>Not in the macro</span></div></div></div>`).join("");
    return `<div class="alt"><b>${esc(a.t)}</b>
      ${macroWindow(a.macros, a.delays)}
      ${a.hold ? `<div><span class="k">Hold together</span>${chips(a.hold)}</div>` : ""}
      ${extra}
      ${a.s ? `<p>${esc(a.s)}</p>` : ""}</div>`;
  }

  function card(c) {
    const d = c[mode];
    const alts = (d.alts || []).map(altHtml).join("");
    return `<section class="cls" id="${c.id}" aria-labelledby="h-${c.id}">
      <div class="cls-h"><h2 id="h-${c.id}">${esc(c.en)}<span class="tc">${esc(c.tw)}</span></h2><span class="role">${esc(c.role)}</span></div>
      ${macroWindow(d.macros, d.delays, mode === "early" ? '<span class="rec">Improved</span>' : "")}
      <div class="notes">
        <div><span class="k">Hold together</span>${chips(d.hold)}</div>
        <div><span class="k gold">Press yourself</span>${list(d.manual)}</div>
        <p><span class="k">Why</span>${esc(d.why)}</p>
        ${d.tip ? `<p><span class="k gold">Tips</span>${esc(d.tip)}</p>` : ""}
        ${d.patch ? `<p class="patch"><span class="k red">Patch</span>${esc(d.patch)}</p>` : ""}
        ${d.queue ? `<p><span class="k blue">Skill queue</span>${esc(d.queue)} <span class="tc">\u6280\u80fd\u9810\u7d04</span></p>` : ""}
        ${d.src ? `<p class="src">Source: <a href="${esc(d.link)}" target="_blank" rel="noopener">${esc(d.src)}</a></p>` : `<p class="src">Improved build: the tested late-game order using only early skills. The video's version is under "Other versions".</p>`}
        ${alts ? `<details><summary>Other versions seen (${d.alts.length})</summary><div class="inner">${alts}</div></details>` : ""}
      </div></section>`;
  }

  /* ---------- hover / tap skill card ---------- */
  const tipEl = document.createElement("div");
  tipEl.className = "skilltip"; tipEl.hidden = true; tipEl.setAttribute("role", "tooltip");
  document.body.appendChild(tipEl);
  let tipFor = null;

  function tipHtml(name) {
    const s = SK[name] || {}, d = DS[name] || {};
    const facts = [];
    if (d.k) facts.push(d.k === "Stigma" ? "Stigma" : "Mastery skill");
    if (s.cd) facts.push("Cooldown " + cdText(s.cd)); else facts.push("No cooldown");
    if (s.mp) facts.push("MP " + s.mp);
    if (d.r) facts.push("Range " + d.r);
    if (d.m) facts.push("Castable while moving");
    if (d.q) facts.push("Learned at Lv " + d.q);
    const specs = (d.s || []).map(([lv, t]) => `<li><b>${lv}</b>${esc(t)}</li>`).join("");
    return `<div class="tt-head">${s.icon ? `<img src="icons/${s.icon}.webp" alt="" width="44" height="44">` : ""}<div><div class="tt-name">${esc(name)}</div><div class="tt-sub">${esc(s.tw || "")} \u00b7 ${esc(s.ko || "")}</div></div></div>
      <div class="tt-facts">${facts.map((f) => `<span>${esc(f)}</span>`).join("")}</div>
      ${d.d ? `<p class="tt-desc">${esc(d.d)}</p>` : '<p class="tt-desc">No description in the database.</p>'}
      ${specs ? `<div class="tt-spec-h">Specialties (unlock at skill level)</div><ul class="tt-specs">${specs}</ul>` : ""}
      ${s.note ? `<p class="tt-note">${esc(s.note)}</p>` : ""}
      <p class="tt-foot">Skill level 1 values from the Global client database.</p>`;
  }
  function place(target) {
    const r = target.getBoundingClientRect();
    const w = tipEl.offsetWidth, h = tipEl.offsetHeight, pad = 10;
    let x = r.right + pad, y = r.top;
    if (x + w > innerWidth - pad) x = r.left - w - pad;
    if (x < pad) { x = Math.max(pad, Math.min(innerWidth - w - pad, r.left)); y = r.bottom + pad; }
    if (y + h > innerHeight - pad) y = Math.max(pad, innerHeight - h - pad);
    tipEl.style.left = x + "px"; tipEl.style.top = y + "px";
  }
  function show(target) {
    const name = target.getAttribute("data-skill");
    if (!name) return;
    if (tipFor !== target) { tipEl.innerHTML = tipHtml(name); tipFor = target; }
    tipEl.hidden = false; place(target);
  }
  function hide() { tipEl.hidden = true; tipFor = null; }
  document.addEventListener("mouseover", (e) => { const t = e.target.closest("[data-skill]"); if (t) show(t); });
  document.addEventListener("mouseout", (e) => { const t = e.target.closest("[data-skill]"); if (t && !t.contains(e.relatedTarget)) hide(); });
  document.addEventListener("focusin", (e) => { const t = e.target.closest("[data-skill]"); if (t) show(t); });
  document.addEventListener("focusout", hide);
  document.addEventListener("click", (e) => { const t = e.target.closest("[data-skill]"); if (t) { tipFor === t && !tipEl.hidden ? hide() : show(t); } else if (!tipEl.contains(e.target)) hide(); });
  document.addEventListener("keydown", (e) => { if (e.key === "Escape") hide(); });
  addEventListener("scroll", () => { if (tipFor) place(tipFor); }, { passive: true });

  function render() {
    hide();
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

  const load = (f) => fetch(f).then((r) => { if (!r.ok) throw new Error(f + " " + r.status); return r.json(); });
  Promise.all([load("data/macros.json"), load("data/skills.json"), load("data/descriptions.json").catch(() => ({}))])
    .then(([m, s, d]) => {
      DATA = m; SK = s; DS = d; render();
      const cl = $("changelog");
      if (cl) cl.innerHTML = (m.changelog || []).map((c) => `<li><b>${esc(c.date)}</b> ${esc(c.text)}</li>`).join("");
      const nt = $("notice");
      if (nt && m.meta.notice) { nt.textContent = m.meta.notice; nt.hidden = false; }
    })
    .catch((e) => { $("board").innerHTML = `<p class="err">Couldn't load the macro data (${esc(e.message)}). Refresh the page to try again.</p>`; });
})();
