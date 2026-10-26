import {useState,useEffect} from 'react'; export function Scene({ready}){const [n]=useState(0);if(!ready)return null;useEffect(()=>{},[]);return <div>{n}</div>;}
