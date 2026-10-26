import {useEffectEvent} from 'react'; export function Room({theme}){const onConnected=useEffectEvent(()=>console.log(theme));onConnected();return null;}
