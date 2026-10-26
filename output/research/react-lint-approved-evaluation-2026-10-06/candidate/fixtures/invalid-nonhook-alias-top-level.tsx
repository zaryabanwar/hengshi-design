import {useState as state} from 'react'; export function View(){ const [value]=state(0); return <p>{value}</p>; }
