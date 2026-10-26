import * as React from 'react';
export function View({ready}: {ready: boolean}) {
 if (!ready) return null;
 const [value] = React.useState(0);
 return <p>{value}</p>;
}
