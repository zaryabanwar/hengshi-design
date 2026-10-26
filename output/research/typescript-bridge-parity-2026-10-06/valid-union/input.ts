export type Panel = {kind: "ready"; label: string} | {kind: "missing"};
export function label(panel: Panel): string { return panel.kind === "ready" ? panel.label : "Unavailable"; }
