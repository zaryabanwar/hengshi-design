import { useRef, useState } from "react";
import { createRoot } from "react-dom/client";
function Counter({initial}: {initial: number}) {
 const [count, setCount] = useState(initial);
 const ref = useRef<HTMLButtonElement | null>(null);
 return <button ref={ref} onClick={event => { event.currentTarget.disabled = true; setCount(count + 1); }}>{count}</button>;
}
createRoot(document.createElement("div")).render(<Counter initial={0} />);
