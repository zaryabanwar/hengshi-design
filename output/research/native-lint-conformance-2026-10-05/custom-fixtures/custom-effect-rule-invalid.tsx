import {useSpecialEffect} from './custom-effects';
export function View({value}: {value: number}) {
 useSpecialEffect(() => { console.log(value); }, []);
 return <p>{value}</p>;
}
