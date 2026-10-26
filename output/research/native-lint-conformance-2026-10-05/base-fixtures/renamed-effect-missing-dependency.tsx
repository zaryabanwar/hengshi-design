import {useEffect as effect} from 'react';
export function View({value}: {value: number}) {
 effect(() => { console.log(value); }, []);
 return <p>{value}</p>;
}
