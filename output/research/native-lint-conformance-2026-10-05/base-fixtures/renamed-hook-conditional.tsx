import {useState as state} from 'react';
export function View({ready}: {ready: boolean}) {
 if (!ready) return null;
 const [value] = state(0);
 return <p>{value}</p>;
}
