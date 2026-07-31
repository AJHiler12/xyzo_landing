# XYZO AI Rules

## Purpose

This document defines how AI tools should behave when working on the XYZO website repository.

It applies to Replit Agent, coding assistants, automated refactoring tools, and future AI collaborators.

AI tools are implementation assistants. They are not the source of product truth.

---

## Required Reading

Before making any code, content, or design changes, read:

1. START_HERE.md
2. PROJECT_CONSTITUTION.md
3. PRODUCT_POSITIONING.md
4. WEBSITE_NARRATIVE.md
5. WEBSITE_GOALS.md
6. BRAND.md
7. DESIGN_LANGUAGE.md
8. WEBSITE_STYLING.md

The authority order defined in START_HERE.md must be respected.

---

## Product Truth

Do not invent, reinterpret, or broaden XYZO’s product positioning.

Do not:

- redefine what XYZO is
- introduce a new category claim
- reduce XYZO to a converter, viewer, pipeline tracker, publishing tool, or asset-management platform
- imply that XYZO replaces specialized creative tools
- imply that derived outputs are canonical authority
- imply that runtime state is persistent asset truth
- confuse source evidence with current canonical state
- describe planned capabilities as if they are working
- add unsupported customer, market, performance, adoption, or partnership claims

When product meaning is unclear, ask before changing copy.

For homepage work, do not invent a new narrative when `WEBSITE_NARRATIVE.md` already defines the public structure and message hierarchy.

---

## Approved Product Model

Preserve these distinctions:

- persistent identity: the stable identity of the asset
- source evidence: where the asset began and what was observed
- canonical state: what the asset is now
- runtime intent: temporary interaction or user-directed state
- derived representation: a target-specific output created from canonical state

Publishing may transform, optimize, repackage, or project a derived artifact.

Publishing must not mutate canonical authority.

Synchronization is the controlled evolution of trusted canonical state.

---

## Messaging Rules

Use approved language from PRODUCT_POSITIONING.md, WEBSITE_NARRATIVE.md, and BRAND.md.

Prefer direct, concrete statements.

Do not use generic startup language such as:

- revolutionary
- disruptive
- seamless
- magical
- effortless
- game-changing
- next-generation
- all-in-one
- end-to-end
- future-proof
- powered by AI
- unlock the power of
- transform your workflow

Do not rewrite approved core statements unless:

1. there is a clear problem,
2. the reason is explained,
3. the replacement is proposed for review,
4. approval is given before implementation.

Do not stack abstract terms such as infrastructure, orchestration, trust, provenance, canonical, and ecosystem without explaining the concrete product behavior behind them.

Do not treat the public homepage as a direct deck reproduction.

The public homepage should summarize and orient.

Protected deeper materials should eventually live in `/principles/` and `/advisor/`.

Do not front-load deep technical distinctions such as source evidence, runtime intent, and detailed publishing-boundary language before the visitor understands the problem, the model, and XYZO's product responsibility.

---

## Current Capability Discipline

Clearly distinguish:

- working today
- in active development
- planned
- long-term direction

Do not present future capabilities as current.

Current capability claims must remain consistent with the approved documentation and the actual repository.

When uncertain, inspect the implementation or ask.

Do not imply that all target-specific publishing profiles, APIs, team workflows, geometry synchronization, broader synchronization, or broader automation are complete unless the approved docs and implementation clearly support that claim.

---

## Design Rules

Follow DESIGN_LANGUAGE.md.

Do not introduce:

- generic SaaS styling
- cyberpunk aesthetics
- gamer visuals
- excessive glow
- decorative wireframes
- heavy gradients
- glassmorphism as a primary style
- crowded dashboards
- random 3D objects
- constant animation
- visual effects without meaning

Favor:

- clear hierarchy
- strong contrast
- disciplined spacing
- intentional typography
- purposeful motion
- authentic product imagery
- restrained color
- accessible interaction
- product evidence over decoration

Do not copy the Forge interface directly into the website.

Interpret the same visual principles at a more refined and editorial level.

---

## Technical Rules

GitHub is the source of truth.

Replit is a development environment.

Netlify remains the deployment path unless explicitly changed.

Work only on the active development branch unless instructed otherwise.

Do not:

- push directly to main
- change the deployment architecture
- introduce a framework without approval
- add a backend without approval
- add a database without approval
- add authentication without approval
- add third-party services without approval
- remove Netlify form behavior without review
- remove or rename existing assets without checking references
- modify unrelated files
- add dependencies for tasks that can be completed with the current stack
- replace working code solely because another approach is more fashionable

Preserve existing functionality unless the approved task requires changing it.

---

## Change Scope

Work in small, reviewable increments.

For each task:

1. inspect the relevant files
2. identify the exact problem
3. state the proposed scope
4. identify affected files
5. preserve unrelated behavior
6. implement the smallest complete change
7. test the result
8. review desktop and mobile behavior
9. summarize what changed and why
10. wait for approval before broadening scope

Do not redesign the entire site when asked to improve one section.

Do not combine copy, architecture, visual system, and deployment changes into one task unless explicitly requested.

---

## Review Before Editing

Before substantial work, provide:

- current-state observations
- the problem being solved
- the proposed approach
- files likely to change
- risks or tradeoffs
- questions that block accurate implementation

Do not begin broad changes until the approach is approved.

Small, obvious, reversible changes may proceed when the user has explicitly requested them.

---

## File Discipline

Modify only relevant files.

Do not:

- create duplicate implementations
- leave dead code behind
- generate unused assets
- scatter styles across multiple locations without reason
- create placeholder content that looks final
- rename files casually
- alter folder structure without explaining the impact

Keep generated files organized and remove unused artifacts before commit.

---

## Code Quality

Code should be:

- readable
- minimal
- maintainable
- accessible
- responsive
- consistent with the current project structure

Prefer simple solutions over unnecessary abstraction.

Do not introduce a build system or component framework merely to make the code feel more modern.

Comments should explain non-obvious intent, not restate the code.

---

## Accessibility

Accessibility is not optional.

Preserve or improve:

- text contrast
- keyboard navigation
- visible focus states
- semantic HTML
- heading order
- alternative text
- captions where applicable
- reduced-motion behavior
- readable text sizes
- touch-target sizing
- controls that do not rely on color alone

Do not trade accessibility for visual effect.

---

## Product Evidence

Use real product evidence wherever possible.

Do not invent:

- product screens
- workflows
- metrics
- customer quotes
- integrations
- capabilities
- validation results
- performance claims

Mockups must be clearly identified as conceptual when used.

Do not make conceptual visuals look like shipped functionality.

---

## Decision Rules

A proposed change is aligned when it:

- improves clarity
- strengthens product truth
- makes the site more credible
- preserves authority boundaries
- improves usability
- improves accessibility
- supports the approved narrative
- preserves the public/protected content split
- uses real evidence
- remains easy to review and reverse

A proposed change is misaligned when it:

- introduces unsupported claims
- weakens the canonical model
- creates ambiguity
- prioritizes novelty over clarity
- broadens scope without approval
- hides product reality
- collapses the homepage into protected deep-dive material
- adds unnecessary complexity
- imitates generic AI, SaaS, or technology-brand patterns

---

## Commit Rules

Before committing:

- review the diff
- confirm only intended files changed
- remove unused files
- verify the site still runs
- check desktop and mobile behavior
- verify links, forms, media, and assets
- confirm no unsupported claims were introduced

Commit messages should describe the actual change clearly.

Do not bundle unrelated work into one commit.

---

## Stop Conditions

Stop and ask before proceeding when:

- product positioning is ambiguous
- approved documents appear to conflict
- the requested change would affect deployment
- the requested change would add a major dependency
- existing functionality may be removed
- a capability claim cannot be verified
- a design change would materially alter the brand direction
- a task has expanded beyond its approved scope
- the correct authority boundary is unclear

When in doubt, ask rather than invent.
