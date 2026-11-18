(() => {
  'use strict';

  const film = document.querySelector('.fb-film');
  if (!film) return;

  const nodes = Object.fromEntries(
    [...film.querySelectorAll('[id^="film-"]')].map(node => [node.id.slice(5), node])
  );
  const player = film.querySelector('.film-player');
  const transcript = film.querySelector('.film-transcript');
  const motion = matchMedia('(prefers-reduced-motion: reduce)');
  const scenes = [
    ['Formular herunterladen', 'Ein Antrag landet als PDF auf dem Computer.'],
    ['Ausdrucken', 'Der Drucker gibt dasselbe Formular auf Papier aus.'],
    ['Von Hand unterschreiben', 'Die Unterschrift kommt mit dem Stift aufs Papier.'],
    ['Wieder einscannen', 'Das unterschriebene Blatt wird wieder zu einer Datei.'],
    ['Datei verschicken', 'Der Scan wird digital verschickt.'],
    ['Der Umweg über Papier', 'Für die Unterschrift wurde aus einer Datei wieder ein Blatt Papier.'],
    ['Auf dem Smartphone öffnen', 'Das Formular erscheint auf dem Smartphone.'],
    ['Mit dem Finger unterschreiben', 'Die Unterschrift entsteht direkt auf dem Display.'],
    ['Digital versenden', 'Ein Tipp auf Senden übermittelt das Formular im gezeigten Beispiel.'],
    ['Durchgängig digital', 'In dieser Zukunftsvision bleibt das Formular von Anfang bis Ende digital.']
  ];
  const sceneDuration = 2000;
  const totalDuration = sceneDuration * scenes.length;

  // Both media share this origin. Zoom keeps the midpoint of the signing line fixed.
  const centerX = 320;
  const signatureY = 263;
  const phoneFormWidthScale = 0.34;
  const phoneFormHeightScale = 0.47;
  const phoneCloseUp = 2;
  const signature = nodes['signature-shape'];
  const signatureLength = signature.getTotalLength();

  const clamp = value => Math.max(0, Math.min(1, value));
  const mix = (from, to, t) => from + (to - from) * t;
  const ease = (t, from, to) => {
    const part = clamp((t - from) / (to - from));
    return part * part * (3 - 2 * part);
  };

  function move(node, x, y, scale = 1, angle = 0) {
    node.setAttribute('transform', `translate(${x} ${y}) scale(${scale}) rotate(${angle})`);
  }

  function fade(node, amount) {
    node.setAttribute('opacity', amount);
  }

  function trace(node, progress) {
    node.style.strokeDasharray = '1';
    node.style.strokeDashoffset = 1 - progress;
    fade(node, progress > 0 ? 1 : 0);
    return signature.getPointAtLength(progress * signatureLength);
  }

  function drawPaper(scene, t) {
    let x = centerX;
    let y = signatureY;
    let scale = 1;
    let angle = 0;
    let ink = scene > 2 ? 1 : 0;
    let opacity = 1;
    let mailOpacity = 0;
    const feeding = scene === 1 || scene === 3;
    const paperWindow = nodes['paper-window'];

    if (feeding) paperWindow.setAttribute('clip-path', 'url(#film-feed)');
    else paperWindow.removeAttribute('clip-path');

    fade(nodes.browser, scene === 0 ? 1 : 0);
    fade(nodes.printer, scene === 1 ? 1 : 0);
    fade(nodes.scanner, scene === 3 ? 1 : 0);
    fade(nodes.pen, 0);

    if (scene === 0) {
      const click = ease(t, 0.15, 0.48);
      move(nodes.cursor, mix(475, 450, click), mix(308, 281, click));
      nodes['download-pulse'].setAttribute('r', mix(24, 34, ease(t, 0.48, 0.88)));
      fade(nodes['download-pulse'], Math.sin(Math.PI * ease(t, 0.44, 0.92)));
      y = mix(285, 299, ease(t, 0.52, 0.83));
      scale = 0.78;
    } else if (scene === 1) {
      y = mix(85, 345, ease(t, 0.08, 0.92));
    } else if (scene === 2) {
      ink = ease(t, 0.14, 0.86);
      const point = signature.getPointAtLength(ink * signatureLength);
      move(nodes.pen, centerX + point.x, signatureY + point.y);
      fade(nodes.pen, ease(t, 0, 0.12));
    } else if (scene === 3) {
      const insert = ease(t, 0.06, 0.92);
      y = mix(345, 85, insert);
      fade(nodes['scan-light'], Math.sin(Math.PI * ease(t, 0.05, 0.94)));
    } else if (scene === 4) {
      const seal = ease(t, 0.03, 0.53);
      const send = ease(t, 0.51, 0.96);
      x = mix(centerX, 310, seal);
      y = mix(signatureY, 216, seal);
      scale = mix(0.66, 0.14, seal);
      angle = mix(0, 7, seal);
      opacity = 1 - ease(t, 0.38, 0.59);
      mailOpacity = ease(t, 0.05, 0.32) * (1 - ease(t, 0.86, 1));
      move(nodes.mail, mix(310, 544, send), mix(216, 111, send), mix(1.15, 0.63, send), -11 * send);
    }

    fade(nodes.mail, mailOpacity);
    trace(nodes['paper-signature'], ink);
    move(nodes.paper, x, y, scale, angle);
    fade(paperWindow, opacity);
  }

  function drawPhone(scene, t) {
    const zoom = scene === 6 ? mix(1, phoneCloseUp, ease(t, 0.4, 0.95)) : phoneCloseUp;
    move(nodes.mobile, centerX, signatureY, zoom);

    const progress = scene === 6 ? 0 : scene === 7 ? ease(t, 0.14, 0.88) : 1;
    const point = trace(nodes.signature, progress);
    const tap = scene >= 8 ? ease(t, 0.06, 0.58) : 0;
    const entry = scene === 6 ? ease(t, 0.75, 1) : 1;
    const x = mix(mix(44, point.x * phoneFormWidthScale, entry), 1, tap);
    const y = mix(mix(38, point.y * phoneFormHeightScale, entry), 12, tap);
    move(nodes.finger, x, y);

    const fingerOpacity = scene === 6 ? entry : scene === 9 ? 0 : 1 - ease(t, 0.63, 0.94) * tap;
    fade(nodes.finger, fingerOpacity);
    fade(nodes.send, scene < 8 ? 0 : scene === 8 ? ease(t, 0, 0.25) : 1);

    const send = ease(t, 0.58, 0.98);
    move(nodes.mail, mix(centerX, 487, send), mix(signatureY + 26, 123, send), mix(0.64, 0.86, send), -10 * send);
    fade(nodes.mail, scene === 8 ? Math.sin(Math.PI * send) : 0);
  }

  let previousScene = -1;
  function draw(time) {
    const scene = Math.min(scenes.length - 1, Math.floor(time / sceneDuration));
    const t = clamp((time - scene * sceneDuration) / sceneDuration);
    if (scene !== previousScene) {
      nodes.chapter.textContent = scene < 6 ? 'Heute · Der Papierumweg' : 'Zukunftsvision · Digital';
      nodes.count.textContent = String(scene + 1).padStart(2, '0') + ' / ' + scenes.length;
      [nodes.title.textContent, nodes.description.textContent] = scenes[scene];
      previousScene = scene;
    }

    if (scene < 6) {
      fade(nodes.mobile, 0);
      drawPaper(scene, t);
    } else {
      fade(nodes.browser, 0);
      fade(nodes.printer, 0);
      fade(nodes.scanner, 0);
      fade(nodes['paper-window'], 0);
      fade(nodes.pen, 0);
      fade(nodes.mobile, 1);
      drawPhone(scene, t);
    }

    const paperVerdict = scene === 5;
    const digitalVerdict = scene === 9;
    fade(nodes.verdict, paperVerdict || digitalVerdict ? ease(t, 0.02, 0.28) : 0);
    move(nodes.verdict, paperVerdict ? 443 : 429, paperVerdict ? 145 : 141);
    nodes.verdict.setAttribute('color', paperVerdict ? '#983d33' : '#20664e');
    nodes['verdict-stroke'].setAttribute('d', paperVerdict
      ? 'm-8-8 16 16m0-16-16 16' : 'm-10 0 7 7 13-15');
    nodes.progress.value = time / sceneDuration;
  }

  let elapsed = 0;
  let lastFrameTime = 0;
  let frame = 0;
  let running = false;

  function stop(label) {
    running = false;
    cancelAnimationFrame(frame);
    nodes.toggle.textContent = label;
  }

  function tick(now) {
    if (!running) return;
    elapsed = Math.min(totalDuration, elapsed + Math.max(0, now - lastFrameTime));
    lastFrameTime = now;
    draw(elapsed);
    if (elapsed >= totalDuration) stop('Erneut abspielen');
    else frame = requestAnimationFrame(tick);
  }

  function play() {
    if (running || motion.matches) return;
    if (elapsed >= totalDuration) elapsed = 0;
    lastFrameTime = performance.now();
    running = true;
    nodes.toggle.textContent = 'Anhalten';
    draw(elapsed);
    frame = requestAnimationFrame(tick);
  }

  nodes.toggle.addEventListener('click', () => running ? stop('Fortsetzen') : play());
  nodes.restart.addEventListener('click', () => {
    stop('Film starten');
    elapsed = 0;
    play();
  });

  function showMotionPreference() {
    stop('Film starten');
    elapsed = 0;
    draw(0);
    player.hidden = motion.matches;
    transcript.open = motion.matches;
  }

  showMotionPreference();
  motion.addEventListener('change', showMotionPreference);
  document.addEventListener('visibilitychange', () => {
    if (document.hidden && running) stop('Fortsetzen');
  });
})();
