import {useState,useEffect} from 'react'; export function Scene({ready}){const [n]=useState(0);useEffect(()=>{},[]);if(!ready)return null;return <div>{n}</div>;}
