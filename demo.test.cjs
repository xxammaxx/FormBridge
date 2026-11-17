const test = require('node:test');
const assert = require('node:assert/strict');
const modulePath = './demo.js';
function decision(value) { return require(modulePath).decision(value); }
test('unselected or invalid selection has no export', () => {
  for(const value of ['', 'bad', null]) assert.deepEqual(decision(value), {approved:false, target:null, value:null});
});
test('applicant confirmation maps the synthetic name', () => {
  assert.deepEqual(decision('applicant'), {approved:true, target:'Antragstellende Person', value:'Alex Muster'});
});
test('household confirmation maps only the explicitly selected target', () => {
  assert.deepEqual(decision('household'), {approved:true, target:'Haushaltsmitglied', value:'Alex Muster'});
});
test('unknown field never exports the synthetic value', () => {
  assert.deepEqual(decision('unknown'), {approved:true, target:null, value:null});
});
