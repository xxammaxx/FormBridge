(function () {
  'use strict';
  function decision(value) {
    if (value === 'applicant') return {approved:true, target:'Antragstellende Person', value:'Alex Muster'};
    if (value === 'household') return {approved:true, target:'Haushaltsmitglied', value:'Alex Muster'};
    if (value === 'unknown') return {approved:true, target:null, value:null};
    return {approved:false, target:null, value:null};
  }
  if (typeof module !== 'undefined') module.exports = {decision};
  if (typeof document === 'undefined') return;
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
    result.textContent = d.target ? 'Bestätigte Beispielzuordnung: ' + d.target + ' → Name: ' + d.value + '. Dies ist keine amtliche Datenvalidierung.' : 'Keine Zuordnung: Das Feld wird nicht exportiert. Weitere Prüfung erforderlich.';
    result.hidden = false;
  });
  reset.addEventListener('click', () => {
    choice.value = '';
    clearResult();
    choice.focus();
  });
  clearResult();
})();
