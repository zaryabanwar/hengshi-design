import {useState} from 'react';
function useSession() { return useState(0); }
export function View({ready}: {ready: boolean}) {
 if (!ready) return null;
 const [value] = useSession();
 return <p>{value}</p>;
}
