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
  if (typeof module !== 'undefined') module.exports = {decision, storyStage};
  if (typeof document === 'undefined') return;
  const story = document.getElementById('story');
  if (story) {
    const cross = document.getElementById('paper-cross');
    const done = document.getElementById('story-done');
    const lane = document.getElementById('paper-lane');
    const controls = document.getElementById('story-controls');
    const restart = document.getElementById('story-restart');
    const pause = document.getElementById('story-pause');
    const motion = window.matchMedia('(prefers-reduced-motion: reduce)');
    let index = 0, timer, paused = false, started = false;
    function render() {
      story.querySelectorAll('[aria-current]').forEach(el => el.removeAttribute('aria-current'));
      const current = document.getElementById(storyStage(index));
      if (current.classList.contains('story-step')) current.setAttribute('aria-current', 'step');
      cross.hidden = index < 5;
      lane.classList.toggle('crossed', index >= 5);
      done.hidden = index < 9;
      pause.disabled = index >= 9;
    }
    function schedule() {
      if (!paused && index < 9) timer = window.setTimeout(() => { index++; render(); schedule(); }, 1800);
    }
    function reset() {
      window.clearTimeout(timer);
      started = true;
      index = 0; paused = false;
      story.classList.remove('paused');
      pause.textContent = 'Animation anhalten';
      render(); schedule();
    }
    function staticView() {
      window.clearTimeout(timer);
      index = 9; render();
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
