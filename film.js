(() => {
  'use strict';

  const film = document.querySelector('.fb-film');
  if (!film) return;
  const get = id => film.querySelector('#film-' + id);
  const player = film.querySelector('.film-player');
  const still = film.querySelector('.film-transcript');
  const motion = matchMedia('(prefers-reduced-motion: reduce)');
  const duration = 2600;
  const scenes = [
    ['Formular herunterladen', 'Ein Antrag landet als PDF auf dem Computer.'],
    ['Ausdrucken', 'Der Drucker gibt das Formular auf Papier aus.'],
    ['Von Hand unterschreiben', 'Die Person trägt ihre Unterschrift auf dem Blatt ein.'],
    ['Wieder einscannen', 'Das unterschriebene Blatt wird wieder zu einer Datei.'],
    ['Datei verschicken', 'Am Computer geht die eingescannte Fassung auf den Weg.'],
    ['Der Umweg über Papier', 'Drucker und Scanner waren für den Wechsel des Mediums nötig.'],
    ['Auf dem Smartphone öffnen', 'In dieser Zukunftsvision bleibt derselbe Antrag digital.'],
    ['Mit dem Finger unterschreiben', 'Die Linie entsteht unmittelbar unter der Fingerspitze.'],
    ['Digital versenden', 'Eine Berührung löst die Übermittlung im dargestellten Beispiel aus.'],
    ['Durchgängig digital', 'In diesem Zielbild entfällt der Weg über Drucker und Scanner.']
  ];
  const total = duration * scenes.length;
  const clamp = value => Math.max(0, Math.min(1, value));
  const ease = value => value * value * (3 - 2 * value);
  const mix = (a, b, t) => a + (b - a) * t;
  function interval(t, start, end) {
    return ease(clamp((t - start) / (end - start)));
  }
  const nodes = Object.fromEntries([...film.querySelectorAll('[id^="film-"]')].map(el => [el.id.slice(5), el]));
  const move = (name, x, y, angle = 0, scale = 1) =>
    nodes[name].setAttribute('transform', 'translate(' + x + ' ' + y + ') rotate(' + angle + ') scale(' + scale + ')');
  const fade = (name, opacity) => nodes[name].setAttribute('opacity', opacity);
  const path = (name, d) => nodes[name].setAttribute('d', d);
  function paperScene(i, t) {
    const locations = [151, 248, 358, 486, 151, 151];
    const start = locations[Math.max(0, i - 1)];
    const end = locations[i];
    const walk = interval(t, 0, .55);
    const x = mix(start, end, walk);
    const stride = Math.sin(walk * Math.PI * 6) * Math.min(1, Math.abs(start - end) / 50) * 10;
    move('avatar', x, 0);
    path('leg-a', 'M-7 218l' + (-3 - stride * .3) + ' 33L' + (-9 - stride) + ' 281h-7');
    path('leg-b', 'M6 218l' + (4 + stride * .3) + ' 33L' + (12 + stride) + ' 281h7');
    const contact = interval(t, .48, .72);
    let hand = [mix(24, 31, contact), mix(203, 199, contact)];
    let sheetX = 0, sheetY = 0, angle = 0, scale = .75;
    if (i === 1) {
      sheetX = 254; sheetY = mix(184, 200, interval(t,.38,.84)); angle = -83;
      hand = [mix(24, 30, contact), mix(203, 193, contact)];
    } else if (i === 2 || i === 3) {
      const previousX = i === 2 ? 254 : 394;
      const currentX = i === 2 ? 394 : 528;
      sheetX = mix(previousX, currentX, walk);
      sheetY = 199 - Math.sin(walk * Math.PI) * 6;
      angle = -83;
      hand = [mix(sheetX - x + 4, i === 2 ? 45 + 4 * Math.sin(t * 20) : 50, contact), mix(sheetY, i === 2 ? 189 : 191, contact)];
    }
    if (i === 4) {
      sheetX=528; sheetY=199; angle=-83;
    }
    const elbowX = hand[0] * .43 + 3, elbowY = hand[1] - 2;
    path('arm', 'M1 176Q' + elbowX + ' ' + elbowY + ' ' + hand[0] + ' ' + hand[1]);
    path('sleeve', 'M1 176l' + (elbowX * .65) + ' ' + ((elbowY - 176) * .65));
    fade('moving-sheet', i >= 1 && i <= 4 ? (i === 1 ? interval(t,.38,.52) : 1) : 0);
    move('moving-sheet', sheetX, sheetY, angle, scale);
    nodes.ink.style.strokeDasharray = '1';
    nodes.ink.style.strokeDashoffset = i < 2 ? 1 : i > 2 ? 0 : 1 - interval(t,.59,.9);
    fade('pen', i === 2 ? contact : 0);
    path('pen','M' + (x+hand[0]+2) + ' ' + (hand[1]-9) + 'l-4 15');
    fade('scanlight', i === 3 ? Math.sin(interval(t,.59,.96)*Math.PI) : 0);
    move('scanlight',0, i === 3 ? interval(t,.59,.96)*6 : 0);
    const send = interval(t,.52,.97);
    fade('mail', i === 4 ? Math.sin(send*Math.PI) : 0);
    move('mail',mix(145,251,send),mix(143,62,send),-12*send,.75);
  }

  const signature = get('signature');
  const signatureLength = signature.getTotalLength();
  function phoneScene(i, t) {
    const trace = i < 7 ? 0 : i > 7 ? 1 : interval(t,.15,.9);
    const point = signature.getPointAtLength(trace * signatureLength);
    signature.style.strokeDasharray = '1';
    signature.style.strokeDashoffset = 1 - trace;
    let x = point.x, y = point.y;
    if (i === 6) {
      const enter = interval(t,0,1);
      x = mix(469,point.x,enter); y = mix(235,point.y,enter);
    } else if (i >= 8) {
      const tap = i === 9 ? 1 : interval(t,0,.52);
      x = mix(point.x,352,tap); y = mix(point.y,237,tap);
    }
    move('finger',x,y);
    const send = interval(t,.51,.98);
    fade('mobile-mail', i === 8 ? Math.sin(send*Math.PI) : 0);
    move('mobile-mail',mix(350,465,send),mix(226,61,send),-10*send,1);
  }
  let previous = -1;
  function draw(time) {
    const i = Math.min(scenes.length - 1, Math.floor(time / duration));
    const t = clamp((time - i * duration) / duration);
    if (i !== previous) {
      get('chapter').textContent = i < 6 ? 'Heute · Der Papierumweg' : 'Zukunftsvision · Digital';
      get('count').textContent = String(i + 1).padStart(2,'0') + ' / 10';
      [get('title').textContent, get('description').textContent] = scenes[i];
      previous = i;
    }
    fade('desk', i <= 5 ? 1 : 0);
    fade('mobile', i < 6 ? 0 : i === 6 ? interval(t,0,.17) : 1);
    if (i < 6) paperScene(i,t); else phoneScene(i,t);
    const verdict = i === 5 || i === 9;
    fade('verdict',verdict ? interval(t,0,.22) : 0);
    move('verdict',i === 5 ? 423 : 482,i === 5 ? 123 : 103,0,.86 + .14 * interval(t,0,.22));
    nodes.verdict.style.color = i === 5 ? '#a5362b' : '#207157';
    path('verdict-stroke',i === 5 ? 'm-14-14 28 28m0-28-28 28' : 'm-19 0 13 13 25-28');
    get('progress').value = time / duration;
  }
  let elapsed = 0, last = 0, raf = 0, running = false;
  const toggle = get('toggle');
  function stop(label) {
    running = false;
    cancelAnimationFrame(raf);
    toggle.textContent = label;
  }
  function tick(now) {
    if (!running) return;
    elapsed = Math.min(total, elapsed + Math.max(0, now - last));
    last = now;
    draw(elapsed);
    if (elapsed >= total) stop('Erneut abspielen');
    else raf = requestAnimationFrame(tick);
  }
  function play() {
    if (running || motion.matches) return;
    if (elapsed >= total) elapsed = 0;
    last = performance.now();
    running = true;
    toggle.textContent = 'Anhalten';
    draw(elapsed);
    raf = requestAnimationFrame(tick);
  }
  toggle.addEventListener('click', () => running ? stop('Fortsetzen') : play());
  get('restart').addEventListener('click', () => {
    stop('Film starten'); elapsed = 0; play();
  });
  function preference() {
    stop('Film starten');
    elapsed = 0; draw(0);
    player.hidden = motion.matches;
    still.open = motion.matches;
  }
  preference();
  motion.addEventListener('change',preference);
  document.addEventListener('visibilitychange', () => {
    if (document.hidden && running) stop('Fortsetzen');
  });
})();
