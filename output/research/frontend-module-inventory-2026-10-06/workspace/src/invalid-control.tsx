function RequiredTitle({ title }: { title: string }) { return <p>{title}</p>; }
export const invalidControl = <RequiredTitle title={42} />;
