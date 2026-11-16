#!/usr/bin/env node
// Validates events/data.json against _tools/events-data-spec.md (schema_version 1).
// Usage: node _tools/validate_events.mjs [path/to/data.json]
// Exit code 0 = valid (warnings allowed), 1 = errors found.
import fs from 'fs';

const file = process.argv[2] || new URL('../events/data.json', import.meta.url).pathname;
const errors = [], warnings = [];
const err = (m) => errors.push(m), warn = (m) => warnings.push(m);

let data;
try { data = JSON.parse(fs.readFileSync(file, 'utf8')); }
catch (e) { console.error('ERROR  not valid JSON: ' + e.message); process.exit(1); }

const REGIONS = ['sf', 'east-bay', 'south-bay', 'peninsula', 'north-bay'];
const LINK_TYPES = ['event', 'listing'];
const isDate = (s) => typeof s === 'string' && /^\d{4}-\d{2}-\d{2}$/.test(s) && !isNaN(Date.parse(s + 'T00:00:00Z'));
const isTime = (s) => typeof s === 'string' && /^([01]\d|2[0-3]):[0-5]\d$/.test(s);
const isStr = (s) => typeof s === 'string' && s.trim().length > 0;
const RELATIVE = /本周|下周|上周|今天|明天|昨天|本期|下期|上期|今晚|明晚/;

if (data.schema_version !== 1) err('schema_version must be 1');
if (!isDate(data.updated)) err('updated must be YYYY-MM-DD');
if (!isStr(data.headline)) err('headline is required');
else if ([...data.headline].length > 28) warn(`headline is ${[...data.headline].length} chars; keep it within 28`);

const days = Array.isArray(data.days) ? data.days : [];
if (days.length < 1 || days.length > 6) err('days must have 1 to 6 entries');
const dayDates = new Set();
days.forEach((d, i) => {
  if (!isDate(d.date)) return err(`days[${i}].date must be YYYY-MM-DD`);
  if (dayDates.has(d.date)) err(`days[${i}].date ${d.date} is duplicated`);
  dayDates.add(d.date);
  if (d.title != null && !isStr(d.title)) err(`days[${i}].title must be a non-empty string when present`);
  if (isStr(d.title) && RELATIVE.test(d.title)) err(`days[${i}].title uses a relative date word; the page adds 今天 / 明天 itself`);
  if (d.picks != null && (!Array.isArray(d.picks) || d.picks.length > 3)) err(`days[${i}].picks must be an array of at most 3 ids`);
});
if (data.updated && days.length && isDate(data.updated)) {
  const last = [...dayDates].sort().pop();
  if (last < data.updated) err(`every day (${last}) is before updated (${data.updated})`);
}

const events = Array.isArray(data.events) ? data.events : [];
if (!events.length) err('events must not be empty');
const ids = new Map();
events.forEach((e, i) => {
  const at = `events[${i}]${e && e.id ? ' (' + e.id + ')' : ''}`;
  if (!e || typeof e !== 'object') return err(`${at} must be an object`);
  if (!isStr(e.id) || !/^[a-z0-9]+(-[a-z0-9]+)*$/.test(e.id)) err(`${at}.id must be lowercase letters, digits and hyphens`);
  else if (ids.has(e.id)) err(`${at}.id duplicates events[${ids.get(e.id)}]`);
  else ids.set(e.id, i);
  for (const k of ['title', 'city', 'venue', 'price', 'desc', 'url', 'source']) if (!isStr(e[k])) err(`${at}.${k} is required`);
  if (!REGIONS.includes(e.region)) err(`${at}.region must be one of ${REGIONS.join(', ')}`);
  for (const k of ['free', 'family', 'outdoor']) if (typeof e[k] !== 'boolean') err(`${at}.${k} must be true or false`);
  if (!LINK_TYPES.includes(e.link_type)) err(`${at}.link_type must be "event" or "listing"`);
  if (isStr(e.url) && !/^https:\/\//.test(e.url)) (/^http:\/\//.test(e.url) ? warn : err)(`${at}.url should be https`);
  if (!Array.isArray(e.tags) || e.tags.length > 4 || e.tags.some((t) => !isStr(t))) err(`${at}.tags must be an array of 0 to 4 strings`);
  if (isStr(e.url) && /[?&](utm_[a-z]+|aff|hxref|hxchl)=/.test(e.url)) warn(`${at}.url carries tracking parameters; strip them`);
  for (const k of ['venue', 'price', 'time_note']) if (isStr(e[k]) && /见活动页|查看活动页|见官网/.test(e[k])) warn(`${at}.${k} says "${e[k]}"; fill it in or write 待确认`);
  if (isStr(e.title) && [...e.title].length > 40) warn(`${at}.title is ${[...e.title].length} chars; keep it within 40`);
  if (isStr(e.desc) && [...e.desc].length > 160) warn(`${at}.desc is ${[...e.desc].length} chars; keep it within 160`);
  for (const k of ['title', 'desc', 'time_note', 'price']) if (isStr(e[k]) && RELATIVE.test(e[k])) err(`${at}.${k} uses a relative date word ("${e[k].match(RELATIVE)[0]}"); write the actual date`);
  if (e.free === true && isStr(e.price) && /\$\s?\d/.test(e.price) && !/免费|捐/.test(e.price)) warn(`${at} is free:true but price shows an amount`);
  if (e.free === false && isStr(e.price) && /^免费/.test(e.price)) warn(`${at} is free:false but price starts with 免费`);

  if (!Array.isArray(e.sessions) || !e.sessions.length) return err(`${at}.sessions must have at least one entry`);
  const seen = new Set();
  e.sessions.forEach((s, j) => {
    const sat = `${at}.sessions[${j}]`;
    if (!isDate(s.date)) return err(`${sat}.date must be YYYY-MM-DD`);
    if (!dayDates.has(s.date)) err(`${sat}.date ${s.date} is not one of days[].date`);
    if (seen.has(s.date)) err(`${sat}.date ${s.date} appears twice; use one session per date and put extra showtimes in time_note`);
    seen.add(s.date);
    if (s.start !== null && !isTime(s.start)) err(`${sat}.start must be "HH:MM" (24h) or null`);
    if (s.end != null && !isTime(s.end)) err(`${sat}.end must be "HH:MM" (24h) when present`);
    if (s.start === null && s.end != null) err(`${sat}.end needs a start`);
    if (s.start === null && !isStr(e.time_note)) err(`${sat}.start is null, so ${at}.time_note is required`);
  });
});

days.forEach((d, i) => (d.picks || []).forEach((id) => {
  const e = events[ids.get(id)];
  if (!e) err(`days[${i}].picks: "${id}" is not an event id`);
  else if (!(e.sessions || []).some((s) => s.date === d.date)) err(`days[${i}].picks: "${id}" has no session on ${d.date}`);
}));
dayDates.forEach((d) => { if (!events.some((e) => (e.sessions || []).some((s) => s.date === d))) warn(`no events on ${d}`); });

if (data.notes != null) {
  if (!Array.isArray(data.notes)) err('notes must be an array');
  else data.notes.forEach((n, i) => { if (!isStr(n.body)) err(`notes[${i}].body is required`); });
}

const listing = events.filter((e) => e.link_type === 'listing').length;
if (events.length && listing / events.length > 0.25) warn(`${listing} of ${events.length} events link to a listing page (target: 25% or less)`);
const noTime = events.filter((e) => (e.sessions || []).some((s) => s.start === null)).length;
if (events.length && noTime / events.length > 0.1) warn(`${noTime} of ${events.length} events have no start time (target: 10% or less)`);

warnings.forEach((w) => console.log('WARN   ' + w));
errors.forEach((e) => console.log('ERROR  ' + e));
console.log(`${events.length} events, ${days.length} days: ${errors.length} error(s), ${warnings.length} warning(s)`);
process.exit(errors.length ? 1 : 0);
