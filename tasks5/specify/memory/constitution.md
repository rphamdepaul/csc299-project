# [PROJECT_NAME] Constitution
<!-- Example: Spec Constitution, TaskFlow Constitution, etc. -->

## Core Principles

### [PRINCIPLE_1_NAME]
<!-- Example: I. Library-First -->
[PRINCIPLE_1_DESCRIPTION]
<!-- Example: Every feature starts as a standalone library; Libraries must be self-contained, independently testable, documented; Clear purpose required - no organizational-only libraries -->

### [PRINCIPLE_2_NAME]
<!-- Example: II. CLI Interface -->
[PRINCIPLE_2_DESCRIPTION]
<!-- Example: Every library exposes functionality via CLI; Text in/out protocol: stdin/args → stdout, errors → stderr; Support JSON + human-readable formats -->

### [PRINCIPLE_3_NAME]
<!-- Example: III. Test-First (NON-NEGOTIABLE) -->
[PRINCIPLE_3_DESCRIPTION]
<!-- Example: TDD mandatory: Tests written → User approved → Tests fail → Then implement; Red-Green-Refactor cycle strictly enforced -->

### [PRINCIPLE_4_NAME]
<!-- Example: IV. Integration Testing -->
[PRINCIPLE_4_DESCRIPTION]
<!-- Example: Focus areas requiring integration tests: New library contract tests, Contract changes, Inter-service communication, Shared schemas -->

### [PRINCIPLE_5_NAME]
<!-- Example: V. Observability, VI. Versioning & Breaking Changes, VII. Simplicity -->
[PRINCIPLE_5_DESCRIPTION]
<!-- Example: Text I/O ensures debuggability; Structured logging required; Or: MAJOR.MINOR.BUILD format; Or: Start simple, YAGNI principles -->

## [SECTION_2_NAME]
<!-- Example: Additional Constraints, Security Requirements, Performance Standards, etc. -->

[SECTION_2_CONTENT]
<!-- Example: Technology stack requirements, compliance standards, deployment policies, etc. -->

## [SECTION_3_NAME]
<!-- Example: Development Workflow, Review Process, Quality Gates, etc. -->

[SECTION_3_CONTENT]
<!-- Example: Code review requirements, testing gates, deployment approval process, etc. -->

## Governance
<!-- Example: Constitution supersedes all other practices; Amendments require documentation, approval, migration plan -->

# Project Constitution — v1.0.0

Version: v1.0.0 | Ratified: 2025-11-19 | Last Amended: 2025-11-19

Purpose
- This Constitution captures the team's baseline principles for code clarity, simplicity, quality, testing, and user experience. It is an actionable governance document: follow it by default, document justified exceptions, and iterate the document via the amendment process below.

Scope
- Applies to all code, tests, CI configuration, UX assets, and repository governance for the project named in the repository root. Infrastructure runbooks and organizational policies may supplement but not contradict this Constitution.

Core Principles (short form)
1. Clarity over cleverness — prefer readable, explicit code.
2. Simplicity first — choose the simplest solution that meets requirements.
3. Test-first, reproducible safety net — tests are the primary guardrails.
4. Fail-fast and observable — detect and surface failure early and clearly.
5. Consistent UX and accessibility — predictable behavior and WCAG AA baseline.
6. Minimize moving parts — limit dependencies and isolate third-party code.
7. Measurable quality — track and act on metrics, not opinions alone.
8. Respect ergonomics — make it easy for contributors and users.

Principles, Rules, and Practical Guidance

1) Clarity over cleverness
- Rationale: Readable code reduces time-to-ship, review cost, and future bugs.
- Rules:
	- Use descriptive names that explain intent, not implementation.
	- Keep functions small and focused (aim for single responsibility).
	- Document public modules/APIs with a one-sentence intent and usage example.
	- Prefer explicit control flow over clever implicit behavior.

2) Simplicity first
- Rationale: Simple systems are easier to debug, test, and evolve.
- Rules:
	- Avoid indirection layers unless they solve a clear, repeated problem.
	- Prefer built-in types and simple data shapes (avoid unnecessary custom formats).
	- When in doubt, pick the option that reduces cognitive burden for future contributors.

3) Test-first, reproducible safety net
- Rationale: Tests document behavior and reduce regressions.
- Rules:
	- New features MUST include unit tests and, when appropriate, integration tests that exercise external contracts.
	- Tests should be deterministic. Flaky tests must be quarantined and fixed within one sprint.
	- Use fixtures and seeds for any randomized behavior.
	- Maintain minimal, module-level coverage targets where appropriate; enforce critical-path tests (not only global %).

4) Fail-fast and observable
- Rationale: Fast detection and useful diagnostics reduce MTTR.
- Rules:
	- Validate inputs early and return clear, structured errors (error code + human message + context id).
	- Log structured events for key actions and external calls; include correlation IDs.
	- Add timeouts and circuit-breakers to external dependencies.
	- Use feature flags for risky rollouts and provide quick rollback paths.

5) Consistent UX and accessibility
- Rationale: Predictability improves user trust and reduces support load.
- Rules:
	- Maintain a shared component/playbook for UI patterns: loading states, empty states, errors, forms.
	- Enforce accessibility checks for public UI changes (WCAG AA minimum).
	- Use visual regression tests for critical components.

6) Minimize moving parts
- Rationale: Each dependency increases maintenance burden and security surface.
- Rules:
	- New dependencies must list purpose, alternatives, owner, and maintenance plan in the PR.
	- Wrap third-party clients behind small adapter interfaces to make replacement easier.
	- Prefer widely-used, actively maintained libraries; avoid one-off niche packages.

7) Measurable quality
- Rationale: Metrics drive objective improvement.
- Rules:
	- Track these baseline metrics: CI pass rate, PR review lead time, production error rate, MTTR.
	- Publish monthly snapshots and assign owners for remediation when thresholds are breached.

8) Respect ergonomics
- Rationale: Good DX improves productivity and code quality.
- Rules:
	- Provide a documented, reproducible developer quickstart.
	- Keep CI feedback actionable; tests should surface failing assertions and logs.

Governance and Decision Framework

Decision documentation (required for significant changes)
- For any change that affects architecture, dependencies, cross-team contracts, or introduces non-trivial risk, authors MUST provide in the PR or design doc:
	1. Problem statement and why the change is needed.
 2. Alternatives considered (at least two) and trade-offs.
 3. Recommended approach, rollout plan, and rollback strategy.
 4. Testing strategy and metrics to validate success.

Architecture Review Board (ARB)
- Light-weight ARB convenes for changes that:
	- Add new major dependencies or infra components.
	- Modify external contracts or public APIs.
	- Introduce long-lived technical debt or cross-team coupling.
- ARB decisions are recorded and linked from the PR/design doc. For routine changes, a documented PR review suffices.

CI, Linters, and Gates
- Enforce mechanical checks via automation:
	- Pre-commit: formatters and simple linters.
	- CI quick stage (required for merge): format + lint + unit tests + type checks.
	- CI extended stage (blocking for release branches): integration tests, security scans, visual/regression tests.
	- Block merges on failing quick-stage checks or on high/critical security findings.

Code Reviews
- Process:
	- All PRs require at least one reviewer with domain knowledge.
	- Reviewers must confirm principle alignment using the PR checklist.
	- For disputed or risky PRs, request a short design review meeting and document the outcome.

Exceptions and Expiry
- Exceptions to this Constitution are allowed but must be:
	- Documented in the PR: reason, mitigations, and an explicit revisit date.
	- Timeboxed: an exception must include an expiration (e.g., 90 days) and owner.

Amendments
- To change this Constitution:
	- Propose an amendment in a PR that updates this file.
	- Stewards (2 maintainers) review and publish; changes are subject to a 7-day comment period.
	- Major version bumps (breaking changes to governance) require explicit notification to stakeholders and a ratification meeting.

Stewardship and Ownership
- Two stewards are assigned to maintain this Constitution, review amendment PRs, and ensure periodic reviews (quarterly).
- Stewards are responsible for publishing the monthly quality snapshots and coordinating remediation work.

Enforcement vs Coaching
- Prioritize coaching and education. Use automation for mechanical enforcement (format/lint/tests). Use reviewers and ARB for judgement calls.

PR Checklist (required for merges)
- Intent summary and problem statement.
- Alternatives considered.
- Tests added/updated and instructions to run locally.
- CI status and any blocked items explained.
- UX checklist for UI changes: design link, ARIA, keyboard navigation.
- New dependency note: purpose, owner, and maintenance plan.
- Constitution alignment: short answers for clarity, tests, and UX.

Acceptance Criteria (how we measure adoption)
- PRs include intent summary and tests (spot checks in reviews).
- CI enforces format, lint, and unit tests on PRs; high/critical security issues block merges.
- Public UI changes meet accessibility baseline.
- Monthly quality metrics published and tracked by stewards.

Examples (short)
- Adding a dependency: include purpose, alternatives, owner in PR; wrap in an adapter.
- Hard-to-test external API: provide a mock contract for unit tests and an integration stage in CI that hits a sandbox.

Where to find help
- For questions or to request an ARB review, open an issue titled "ARB: <short topic>" and tag the stewards.

This document is the canonical Constitution for this repository. Keep it updated in `.specify/memory/constitution.md` and mirror to `.github/CONSTITUTION.md` for public visibility.

Mandatory merge rule (master/main)
- Any Pull Request merged into the `main` or `master` branch MUST ensure the repository Constitution is present and up-to-date.
- Concretely, before a PR can be merged to `main`/`master`, the author must do one of the following:
	1. Include an update to `.specify/memory/constitution.md` (and mirror to `.github/CONSTITUTION.md`) when the change affects governance, policies, or any items referenced by this Constitution; or
	2. Add a clear confirmation in the PR (checkbox) titled "Constitution checked and up-to-date" that either:
		 - Confirms the current Constitution already covers the change, or
		 - Notes a linked issue/PR that will update the Constitution in the same release window.

Enforcement and automation guidance
- Implement a lightweight CI check on `pull_request` that:
	- Verifies at least one of the Constitution files exists (`.specify/memory/constitution.md` or `.github/CONSTITUTION.md`).
	- Fails the quick-check stage if the PR modifies governance-relevant files but does not include a Constitution update or the "Constitution checked and up-to-date" confirmation.
- The PR template must include the "Constitution checked and up-to-date" checkbox (see `.github/pull_request_template.md`) to make this confirmation explicit in every PR.
- Exceptions: emergency hotfixes may be merged with steward approval; such merges must open a follow-up PR to update the Constitution or document why an update is not required.

Why this rule exists
- Having an up-to-date Constitution in the canonical branch ensures contributors and reviewers can reason about governance expectations when reviewing and merging code. It prevents accidental drift between policy and implementation.

