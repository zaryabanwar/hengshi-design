import * as React from 'react';
export function View({value}: {value: number}) {
 React.useEffect(() => { console.log(value); }, [value]);
 return <p>{value}</p>;
}
