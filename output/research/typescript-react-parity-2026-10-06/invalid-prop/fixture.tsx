function Card({title}: {title: string}) { return <article>{title}</article>; }
export const view = <Card title={42} />;
