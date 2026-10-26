import type { ReactNode } from "react";
async function Detail({title}: {title: string}): Promise<ReactNode> { return <section>{title}</section>; }
export const view = <Detail title="Synthetic" />;
