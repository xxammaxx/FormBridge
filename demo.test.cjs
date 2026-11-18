const test = require('node:test');
const assert = require('node:assert/strict');
const {decide} = require('./demo.js');
test('confirmed context determines whose family name is written', () => {
  for (const [context, role, name] of [['applicant', 'Antragstellende Person', 'Muster'], ['household', 'Haushaltsmitglied', 'Beispiel']]) {
    assert.deepEqual(decide(context, context).record, {rolle: role, feld: 'F60000227V1.1', familienname: name});
  }
});
test('unknown, invalid, mismatched and ambiguous choices never release a name', () => {
  for (const context of ['applicant', 'household', 'ambiguous', 'bad', '__proto__']) {
    for (const target of ['', null, 'unknown', 'bad', 'applicant', 'household']) {
      if (context === target && ['applicant', 'household'].includes(context)) continue;
      assert.equal(decide(context, target).record, null);
    }
  }
});
