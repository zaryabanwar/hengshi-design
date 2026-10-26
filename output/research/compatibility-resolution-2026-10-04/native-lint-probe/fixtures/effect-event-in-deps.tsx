import {useEffect,useEffectEvent} from 'react'; export function Room({theme}){const onConnected=useEffectEvent(()=>console.log(theme));useEffect(()=>{onConnected();},[onConnected]);return null;}
