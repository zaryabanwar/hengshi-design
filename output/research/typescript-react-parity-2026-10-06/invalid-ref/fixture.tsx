import { useRef } from "react";
export function Control() { const ref = useRef<HTMLDivElement | null>(null); return <button ref={ref} />; }
