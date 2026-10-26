import {useState as useCounter} from 'react';
export function View({ready}: {ready: boolean}) {
 if (!ready) return null;
 const [value] = useCounter(0);
 return <p>{value}</p>;
}
