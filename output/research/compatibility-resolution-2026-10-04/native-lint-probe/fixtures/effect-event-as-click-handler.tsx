import {useEffectEvent} from 'react'; export function Room({theme}){const onConnected=useEffectEvent(()=>console.log(theme));return <button onClick={onConnected}>Connect</button>;}
