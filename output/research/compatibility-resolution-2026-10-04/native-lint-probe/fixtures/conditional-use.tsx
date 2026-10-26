import {use} from 'react'; export function Room({ready,promise}){if(ready){const value=use(promise);return <div>{value}</div>;}return null;}
