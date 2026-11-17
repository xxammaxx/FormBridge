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
test('household target conflicts with the visible applicant section and must not export', () => {
  assert.deepEqual(decision('household'), {approved:true, target:null, value:null, conflict:true});
});
test('unknown field never exports the synthetic value', () => {
  assert.deepEqual(decision('unknown'), {approved:true, target:null, value:null});
});
test('story visits every paper station, crosses it out, then signs and sends digitally', () => {
  const { storyStage } = require(modulePath);
  assert.deepEqual(Array.from({length:10}, (_, i) => storyStage(i)), [
    'paper-download', 'paper-print', 'paper-sign', 'paper-scan', 'paper-send',
    'paper-cross', 'digital-download', 'digital-sign', 'digital-send', 'story-done'
  ]);
  assert.equal(storyStage(10), 'story-done');
});
