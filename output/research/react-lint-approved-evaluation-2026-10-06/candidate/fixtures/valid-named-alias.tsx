import {useState as useCounter} from 'react'; export function View(){ const [value]=useCounter(0); return <p>{value}</p>; }
