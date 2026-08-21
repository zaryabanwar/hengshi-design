# {{ Feature Name }} — Requirements Checklist

## Status and Authority

| Field | Value |
|---|---|
| Status | Draft |
| Spec | `specs/{{ number }}-{{ slug }}/spec.md` |
| Producer | |
| Independent reviewer | |
| Founder approver | |
| Created | {{ date }} |
| Last updated | {{ date }} |

## Authority and Definition Quality

- [ ] Approved decision and product references are explicit
- [ ] Facts, assumptions, open decisions, exclusions, and protected scope are distinct
- [ ] User journeys include failure, denial, recovery, and accessible-equivalent paths
- [ ] Requirements are measurable, implementation-independent, and traceable to evidence
- [ ] No stale prototype, fictional proof, or draft claim is presented as production truth

## Functional and Contract Requirements

- [ ] Every functional requirement has an observable verification method
- [ ] API, event, provider, and data contracts name producer/consumer, auth, data
  class, idempotency, failure, resume, and compatibility behavior as applicable
- [ ] Draft isolation, approval separation, publication atomicity, and rollback are
  explicit for publishable content

## Technology Compatibility

- [ ] Coupled packages/runtimes/browsers/cloud services are evaluated as a graph
- [ ] Context7 library IDs, query dates, and official primary sources are recorded
- [ ] Current and proposed stable targets, peers, breaking changes, security,
  migration tests, exact locks, and rollback are defined
- [ ] No preview, beta, RC, nightly, experimental, floating `latest`, unbounded
  production dependency, mutable action tag, or mutable production image remains
- [ ] Any blocked newest stable major has an approved ADR and quarterly recheck

## SEO, Content, and Entity Truth

- [ ] Indexable routes provide complete semantic HTML before JavaScript
- [ ] Canonical, title, description, H1, robots, social metadata, breadcrumbs,
  internal links, schema, sitemap, status, redirects, and retired URLs are defined
- [ ] Structured data matches visible verified content and contains no fabricated
  reviews, prices, clients, awards, people, or locations
- [ ] AI-assisted content requires named expert verification and original value

## Security, Privacy, and AI

- [ ] Authentication, roles, separation of duties, negative authorization, cookie,
  CSRF, rate-limit, audit, and break-glass requirements are measurable
- [ ] Data purpose, consent, classification, region/provider, retention, deletion,
  backup/tombstone, and legal dependencies are explicit
- [ ] AI grounding, visible sources, refusal, prohibited commitments, injection,
  residency, timeout, policy routing, and permitted failover are explicit
- [ ] Secrets cannot enter source, documentation, logs, evidence, or chat

## Accessibility, Performance, 3D, and Recovery

- [ ] WCAG 2.2 AA, keyboard, screen-reader, reduced-motion, low-power,
  non-JavaScript/non-WebGL, asset-failure, and mobile behavior are specified
- [ ] Core Web Vitals, bundle/asset, memory, FPS, concurrency, availability, RPO,
  and RTO targets are measurable where applicable
- [ ] Backup, restore, migration, rollback, provider loss, Redis/search/database
  loss, reconnect/resume, and prior-release continuity are testable

## Evidence, Review, and Approval

- [ ] Exact validation commands and evidence locations are defined
- [ ] Producer and independent reviewers are different
- [ ] Revision limit is two, or three only for brand/UI/motion/3D
- [ ] Root state, decisions, risks, manual actions, and changelog sync is required
- [ ] Founder click-based approval and separate Git/external action gates are explicit

## Sign-Off

| Reviewer | Scope | Date | Status/findings |
|---|---|---|---|
| | | | Pending |
