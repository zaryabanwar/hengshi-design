# Component inventory

The source defines 62 UI primitives (`docs/phase-1-ui-reference-design/component-primitives.csv`) as anatomy, variant and state contracts; no primitive has code yet. Stable IDs are `PRIM-###` and are never reassigned. Every interactive primitive carries the pseudo-states base, hover, focus-visible, pressed and disabled, and every state is shown as visible text plus shape, icon, border, pattern or position, never colour alone. Seven CSS components in this system are hand-written from the identity board; the last column tracks them against the inventory.

## Shell and navigation (5)

| ID | Primitive | Interaction | Required variants | Built here |
|---|---|---|---|---|
| PRIM-001 | Public semantic shell | composite interactive | public, no_script, offline, unsupported_browser, prior_release, stream_high, stream_medium, stream_low, stream_semantic | Not built |
| PRIM-002 | Primary navigation and narrow disclosure | composite interactive | wide_inline, narrow_disclosure, staff_separate | Not built |
| PRIM-003 | Breadcrumb trail | interactive | public, staff, collapsed_overflow_only_if_reviewed | Not built |
| PRIM-004 | Directory and search | composite interactive | semantic_header, world_HUD, static_directory_index | Not built |
| PRIM-006 | Excluded-surface guard and safe destination | composite interactive | world, admin, nonpublic_publication, chat_session, internal_search, tracking_variant, filter_sort_variant, staging, defense_absent | Not built |

## Content and evidence (9)

| ID | Primitive | Interaction | Required variants | Built here |
|---|---|---|---|---|
| PRIM-005 | Directory result row | interactive | canonical_only, canonical_plus_optional_location, closed_room | Not built |
| PRIM-007 | Evidence state label | static | verified, demo, proposed, conditional, unavailable, error | Yes: EvidenceStateLabel |
| PRIM-008 | Release and availability label | status announced | planned, active, prior_active, candidate_nonpublic, closed, held_content, opening, open, unavailable | Not built |
| PRIM-009 | Collection template | composite interactive | work, demos, insights, experts, trust, services, industries | Not built |
| PRIM-010 | Collection item card or row | interactive | work, demo, insight, expert, trust, service, industry, empty_placeholder_not_allowed | Partial: Card (item card only) |
| PRIM-011 | Detail decision module | composite interactive | work_detail, demo_detail, article, person, trust_topic, about | Not built |
| PRIM-012 | Service wing and service decision unit | composite interactive | wing, service, closed, held_content, opening, open | Not built |
| PRIM-013 | Industry intersection unit | composite interactive | industry_collection, agriculture, mining, held_context | Not built |
| PRIM-062 | Logo and entity lockup | static | primary_dark, light_surface, monochrome, reverse, standard_mark, small_optical, favicon_context, text_only_asset_failure | Yes: Lockup |

## Actions and input (12)

| ID | Primitive | Interaction | Required variants | Built here |
|---|---|---|---|---|
| PRIM-014 | Primary booking CTA | interactive | global, contextual, compact, inverse | Yes: Button (primary) |
| PRIM-015 | General action button | interactive | primary, secondary, quiet, destructive_pending_approval, icon_plus_text | Yes: Button (secondary, disabled) |
| PRIM-016 | Semantic text link | interactive | inline, standalone, breadcrumb, source, skip, canonical | Not built |
| PRIM-017 | Icon control | interactive | labelled, compact_with_visible_text, universally_understood_icon_only_after_review | Not built |
| PRIM-018 | Form group | composite interactive | qualification, contact, consent, staff_editor, challenge, review | Not built |
| PRIM-019 | Text input and textarea | interactive | email, organization, role, desired_outcome, timing, optional_budget, contact_message, search, staff_text | Not built |
| PRIM-020 | Select or combobox | interactive | native_select, listbox_only_if_needed, timezone, wing, timing, bounded_staff_filter | Not built |
| PRIM-021 | Checkbox and consent control | interactive | unchecked, checked, mixed_only_if_semantically_required, consent_declined, consent_granted | Not built |
| PRIM-022 | Field validation message | status announced | error, warning, success, pending, information | Not built |
| PRIM-023 | Error summary | composite interactive | form, publication, booking, contact, staff | Not built |
| PRIM-024 | Consent notice and purpose panel | composite interactive | AI_retention, handoff_share, booking, contact, media | Not built |
| PRIM-038 | Contact form and status | composite interactive | channels_held, form_if_approved, alternate_channel, booking_fallback | Not built |

## AI and handoff (7)

| ID | Primitive | Interaction | Required variants | Built here |
|---|---|---|---|---|
| PRIM-025 | AI entry and identity panel | composite interactive | available, policy_unavailable, provider_unavailable, declined | Not built |
| PRIM-026 | AI transcript and composer | composite interactive | ephemeral, consented, resuming, expired, refused, unavailable | Not built |
| PRIM-027 | AI citation and source list | composite interactive | one_source, many_sources, source_unavailable, cannot_verify | Not built |
| PRIM-028 | AI refusal or cannot-verify block | composite interactive | cannot_verify, policy_refusal, sensitive_refusal, commitment_refusal, provider_unavailable | Not built |
| PRIM-029 | Human availability indicator | composite interactive | not_offered, available, unavailable, suppressed, stale, unknown | Not built |
| PRIM-030 | Handoff request and conversation status | composite interactive | requested, queued, accepted, text_active, ended, declined, expired, alert_failed | Not built |
| PRIM-031 | Voice or video opt-in | interactive | voice, video, permission_prompt, unsupported, held_alternatives | Not built |

## Booking (6)

| ID | Primitive | Interaction | Required variants | Built here |
|---|---|---|---|---|
| PRIM-032 | Booking progress stepper | composite interactive | qualification, email, availability, review, pending, confirmed, reschedule, cancel | Not built |
| PRIM-033 | Email ownership challenge | composite interactive | pending, expired, undeliverable, corrected, resent, verified, rate_limited, unknown | Not built |
| PRIM-034 | Availability calendar | composite interactive | day, week_or_period_pending_design, no_slots, provider_unavailable, owner_unavailable | Not built |
| PRIM-035 | Booking slot option | interactive | available, selected, stale, unavailable | Not built |
| PRIM-036 | Booking review | composite interactive | initial_booking, reschedule, cancel_review | Not built |
| PRIM-037 | Booking pending confirmation and reconciliation | composite interactive | not_submitted, pending, confirmed_qualified, reconciliation_error, reschedule_pending, cancel_pending, cancelled, failed | Not built |

## Overlay and immersive (6)

| ID | Primitive | Interaction | Required variants | Built here |
|---|---|---|---|---|
| PRIM-039 | Modal dialog | composite interactive | modal, alert_dialog_only_for_true_interrupt, nonmodal_preferred_when_possible | Not built |
| PRIM-040 | Drawer | composite interactive | navigation, directory, detail, staff_filter | Not built |
| PRIM-041 | Context panel | composite interactive | semantic_inline, world_panel, staff_side_panel | Not built |
| PRIM-042 | World onboarding and return choice | composite interactive | first_visit, return_valid, return_stale, reduced_motion, low_power | Not built |
| PRIM-043 | World HUD | composite interactive | reception, atrium, room, transition, reduced_motion, low_power, asset_failure | Not built |
| PRIM-044 | World escape and recovery | composite interactive | unsupported, loader_timeout, asset_error, network_error, context_loss, memory_or_thermal, checksum_mismatch | Not built |

## Media and data (4)

| ID | Primitive | Interaction | Required variants | Built here |
|---|---|---|---|---|
| PRIM-045 | Media player and alternatives | composite interactive | audio_only, prerecorded_synchronized, live_synchronized, held, unsupported | Not built |
| PRIM-059 | Data visualization | composite interactive | five_series, single_series, target, measured, missing, uncertainty | Partial: DataSeriesKey (legend only) |
| PRIM-060 | Data table | composite interactive | read_only, sortable_if_approved, comparison, audit, exact_values | Not built |
| PRIM-061 | Responsive data or record list | composite interactive | table_equivalent, queue, source_list, audit_chain, summary | Not built |

## Staff and publication (9)

| ID | Primitive | Interaction | Required variants | Built here |
|---|---|---|---|---|
| PRIM-046 | Staff shell and task navigation | composite interactive | author, reviewer, founder_approver, administrator, conversation_operator, booking_operator, audit_role | Not built |
| PRIM-047 | Staff availability toggle | interactive | available_on, available_off, delegate_if_approved, no_scope | Not built |
| PRIM-048 | Staff queue | composite interactive | conversation, alert_exception, assignment, booking_reconciliation, booking_exception, evidence_SEO, knowledge, audit | Not built |
| PRIM-049 | Staff work-item detail | composite interactive | handoff, conversation, alert, assignment, booking, publication, knowledge | Not built |
| PRIM-050 | Version and checksum display | status announced | draft_version, candidate_checksum, active_release_checksum, grounding_bundle_checksum, stale_mismatch | Not built |
| PRIM-051 | Staff decision controls | composite interactive | accept, decline, end, assign, reconcile, hold, escalate, pass, request_changes, approve, reject, activate | Not built |
| PRIM-052 | Publication draft editor | composite interactive | new_draft, editing, saved, conflict, held, ready_for_review | Not built |
| PRIM-053 | Publication candidate and release state | composite interactive | review_candidate, specialist_passed, founder_approved, rendering, validation_failed, ready, activating, active, prior_active | Not built |
| PRIM-054 | Audit event viewer | composite interactive | timeline, table, detail, durable_fallback, integrity_gap | Not built |

## System access (2)

| ID | Primitive | Interaction | Required variants | Built here |
|---|---|---|---|---|
| PRIM-055 | Staff sign-in and reauthentication | composite interactive | Entra, reauthentication, approved_break_glass_route_only | Not built |
| PRIM-056 | Session and permission state | composite interactive | signed_out, active_role, forbidden, idle_expired, absolute_expired, CSRF_failure, ambiguous_role | Not built |

## System feedback (2)

| ID | Primitive | Interaction | Required variants | Built here |
|---|---|---|---|---|
| PRIM-057 | Notification and live status region | status announced | inline_status, page_banner, field_status, toast_only_for_supplemental_feedback, polite_live, assertive_error | Partial: Notice (static notice only) |
| PRIM-058 | Loading empty offline error and recovery container | composite interactive | loading, empty, offline, error, held, unavailable, stale, permission_denied, expired, unknown | Not built |

## Transactional and content states

Across the inventory the source names these content states, each requiring text plus a non-colour cue: loading, empty, offline, error, unavailable, held, stale, pending, success, current, expanded, collapsed, permission denied, not found, retired, expired, and the delivery-stream states (in force, pending, preference write failed). Build them from `hd-status-*` and the evidence-state grammar, never from new colours.
