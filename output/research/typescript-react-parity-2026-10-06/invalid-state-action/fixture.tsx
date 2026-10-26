import { useState } from "react";
export function Counter() { const [count, setCount] = useState<number>(0); setCount("wrong"); return <output>{count}</output>; }
