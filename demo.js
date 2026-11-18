(function () {
  'use strict';
  function decision(value) {
    if (value === 'applicant') return {approved:true, target:'Antragstellende Person', value:'Alex Muster'};
    if (value === 'household') return {approved:true, target:null, value:null, conflict:true};
    if (value === 'unknown') return {approved:true, target:null, value:null};
    return {approved:false, target:null, value:null};
  }
  const storyStages = ['paper-download', 'paper-print', 'paper-sign', 'paper-scan', 'paper-send', 'paper-cross', 'digital-download', 'digital-sign', 'digital-send', 'story-done'];
  function storyStage(index) { return storyStages[Math.min(index, storyStages.length - 1)]; }
  const frameCopy = [
    ['Formular herunterladen', 'Ein PDF landet auf dem Computer.'],
    ['Zum Drucker', 'Das digitale Dokument wird wieder zu Papier.'],
    ['Von Hand unterschreiben', 'Die Unterschrift kommt auf das Blatt.'],
    ['Zurück zum Scanner', 'Das Papier muss erneut digitalisiert werden.'],
    ['Antrag versenden', 'Erst jetzt kann der Antrag abgeschickt werden.'],
    ['Warum dieser Umweg?', 'Drucken und Einscannen könnten entfallen.'],
    ['Formular herunterladen', 'Das Dokument bleibt von Anfang an digital.'],
    ['Direkt unterschreiben', 'Die Unterschrift entsteht mit dem Finger auf dem Display.'],
    ['Digital abschicken', 'Das Dokument bleibt digital bis zur Übermittlung.'],
    ['Weniger Umwege.', 'Ein durchgängig digitaler Antrag als Zukunftsvision.']
  ];
  function storyFrame(index) {
    const i = Math.min(Math.max(index, 0), 9);
    const phase = i < 5 ? 'paper' : i === 5 ? 'transition' : i < 9 ? 'digital' : 'finish';
    return {id: storyStage(i), phase, position: phase === 'paper' ? i + 1 : phase === 'digital' ? i - 5 : 0,
      total: phase === 'paper' ? 5 : phase === 'digital' ? 3 : 0, title: frameCopy[i][0], description: frameCopy[i][1]};
  }
  if (typeof module !== 'undefined') module.exports = {decision, storyStage, storyFrame};
  if (typeof document === 'undefined') return;
  const story = document.getElementById('story');
  if (story) {
    const cross = document.getElementById('paper-cross');
    const done = document.getElementById('story-done');
    const lane = document.getElementById('paper-lane');
    const controls = document.getElementById('story-controls');
    const restart = document.getElementById('story-restart');
    const pause = document.getElementById('story-pause');
    const stage = document.getElementById('story-stage');
    const art = document.getElementById('story-art');
    const title = document.getElementById('story-title');
    const desc = document.getElementById('story-description');
    const chapter = document.getElementById('story-chapter');
    const progress = document.getElementById('story-progress');
    const motion = window.matchMedia('(prefers-reduced-motion: reduce)');
    let index = 0, timer, paused = false, started = false;
    function render() {
      story.querySelectorAll('[aria-current]').forEach(el => el.removeAttribute('aria-current'));
      const frame = storyFrame(index);
      const current = document.getElementById(frame.id);
      if (current.classList.contains('story-step')) current.setAttribute('aria-current', 'step');
      cross.hidden = index < 5;
      lane.classList.toggle('crossed', index >= 5);
      done.hidden = index < 9;
      pause.disabled = index >= 9;
      stage.dataset.phase = frame.phase;
      chapter.textContent = frame.total ? (frame.phase === 'paper' ? 'Heute · ' : 'Zukunftsvision · ') + frame.position + ' / ' + frame.total : frame.phase === 'transition' ? 'Der Medienbruch' : 'Das Zielbild';
      title.textContent = frame.title;
      desc.textContent = frame.description;
      progress.value = index + 1;
      const source = current.querySelector('svg');
      const illustration = source.cloneNode(true);
      illustration.classList.add('scene-illustration');
      art.replaceChildren(illustration);
      story.querySelectorAll('.story-step').forEach(el => el.classList.toggle('visited', storyStages.indexOf(el.id) < index));
    }
    function schedule() {
      if (!paused && index < 9) timer = window.setTimeout(() => { index++; render(); schedule(); }, 2400);
    }
    function reset() {
      window.clearTimeout(timer);
      started = true;
      story.classList.add('is-player');
      stage.hidden = false;
      index = 0; paused = false;
      story.classList.remove('paused');
      pause.textContent = 'Animation anhalten';
      render(); schedule();
    }
    function staticView() {
      window.clearTimeout(timer);
      index = 9; render();
      stage.hidden = true;
      story.classList.remove('is-player');
      controls.hidden = true;
    }
    restart.addEventListener('click', reset);
    pause.addEventListener('click', () => {
      if (index >= 9) return;
      paused = !paused;
      story.classList.toggle('paused', paused);
      pause.textContent = paused ? 'Animation fortsetzen' : 'Animation anhalten';
      window.clearTimeout(timer);
      schedule();
    });
    if (motion.matches) staticView();
    else {
      controls.hidden = false;
      pause.disabled = true;
      lane.classList.add('crossed');
      if ('IntersectionObserver' in window) {
        const observer = new IntersectionObserver(entries => {
          if (entries.some(entry => entry.isIntersecting)) {
            observer.disconnect();
            if (!started && !motion.matches) reset();
          }
        }, {threshold: 0.12});
        observer.observe(story);
      }
    }
    motion.addEventListener('change', () => {
      if (motion.matches) staticView();
      else { controls.hidden = false; reset(); }
    });
  }
  const choice = document.getElementById('mapping');
  const confirm = document.getElementById('confirm');
  const reset = document.getElementById('reset');
  const result = document.getElementById('result');
  function clearResult() {
    result.hidden = true;
    result.textContent = '';
    confirm.disabled = !decision(choice.value).approved;
  }
  choice.addEventListener('change', clearResult);
  confirm.addEventListener('click', () => {
    const d = decision(choice.value);
    if (!d.approved) return;
    result.textContent = d.conflict ? 'Widerspruch zum Formularabschnitt: Das Feld gehört zur antragstellenden Person. Keine Ausgabe – bitte Zuordnung korrigieren.' : d.target ? 'Bestätigte Beispielzuordnung: ' + d.target + ' → Name: ' + d.value + '. Dies ist keine amtliche Datenvalidierung.' : 'Keine Zuordnung: Das Feld wird nicht exportiert. Weitere Prüfung erforderlich.';
    result.hidden = false;
  });
  reset.addEventListener('click', () => {
    choice.value = '';
    clearResult();
    choice.focus();
  });
  clearResult();
})();
