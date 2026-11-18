(function () {
  'use strict';
  const samples = {
    applicant: {
      section: 'Angaben zur antragstellenden Person', name: 'Muster',
      role: 'Antragstellende Person',
      hint: 'Die Abschnittsüberschrift nennt die antragstellende Person. Vorschlag für „Name“: ihr Familienname.'
    },
    household: {
      section: 'Weitere Personen in Ihrem Haushalt', name: 'Beispiel',
      role: 'Haushaltsmitglied',
      hint: 'Die Überschrift nennt weitere Personen im Haushalt. Vorschlag für „Name“: der Familienname eines Haushaltsmitglieds.'
    },
    ambiguous: {
      section: '[Überschrift fehlt]', name: 'Probe',
      hint: 'Hier fehlt die Abschnittsüberschrift. „Name“ allein verrät nicht, welche Person gemeint ist. Lassen Sie die Zuordnung offen.'
    }
  };

  function decide(context, choice) {
    if (!Object.hasOwn(samples, context) || !['applicant', 'household', 'unknown'].includes(choice)) {
      return {message: 'Bitte wählen Sie ein Ziel.', record: null};
    }
    if (choice === 'unknown' || context === 'ambiguous') {
      return {message: 'Keine Zuordnung. Der Eintrag bleibt zur Prüfung offen und wird nicht ausgegeben.', record: null};
    }
    if (choice !== context) {
      return {message: 'Widerspruch zur Abschnittsüberschrift. Keine Ausgabe. Prüfen Sie das ausgewählte Ziel.', record: null};
    }
    const {role, name} = samples[context];
    return {
      message: 'Bestätigte Beispielausgabe für den gewählten Ausschnitt',
      record: {rolle: role, feld: 'F60000227V1.1', familienname: name}
    };
  }

  if (typeof module !== 'undefined') module.exports = {decide};
  if (typeof document === 'undefined') return;
  const context = document.getElementById('lab-context');
  if (!context) return;
  const choice = document.getElementById('mapping');
  const confirm = document.getElementById('confirm');
  const reset = document.getElementById('reset');
  const result = document.getElementById('result');
  const output = document.getElementById('lab-output');

  function clearResult() {
    result.textContent = 'Die Beispielausgabe erscheint nach Ihrer Bestätigung.';
    output.hidden = true;
    output.textContent = '';
    confirm.disabled = !choice.value;
  }

  function showSample() {
    const sample = samples[context.value];
    document.getElementById('lab-section').textContent = sample.section;
    document.getElementById('lab-name').textContent = sample.name;
    document.getElementById('lab-hint').textContent = sample.hint;
    choice.value = '';
    clearResult();
  }

  context.disabled = choice.disabled = reset.disabled = false;
  context.addEventListener('change', showSample);
  choice.addEventListener('change', clearResult);
  confirm.addEventListener('click', () => {
    const {message, record} = decide(context.value, choice.value);
    result.textContent = message;
    output.textContent = record ? JSON.stringify(record, null, 2) : '';
    output.hidden = !record;
  });
  reset.addEventListener('click', () => {
    context.value = 'applicant';
    showSample();
    context.focus();
  });
  showSample();
})();
