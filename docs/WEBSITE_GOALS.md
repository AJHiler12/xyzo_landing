# XYZO Website Goals

## Purpose

The XYZO website is the public introduction to XYZO and the working system being built.

Its primary job is to help a thoughtful visitor understand:

- the problem XYZO owns
- what XYZO is
- why the problem matters
- how the canonical asset model addresses it
- what is already working
- what category responsibility XYZO owns
- why the product is credible
- how to request deeper access

The website should make XYZO easier to understand without reducing it to a converter, viewer, pipeline tool, publishing utility, or generic 3D platform.

The public homepage should summarize and orient. It should not reproduce the First Principles or Advisor decks word for word.

---

## Primary Goal

The primary goal of the website is to establish a clear and credible understanding of XYZO.

A visitor should leave with this core idea:

XYZO keeps one trusted 3D asset connected as its geometry, materials, textures, metadata, dependencies, and outputs change across tools and uses.

The site should make clear that XYZO takes responsibility for the continuity of the 3D asset itself.

`WEBSITE_NARRATIVE.md` governs the homepage narrative and copy flow used to accomplish that goal.

---

## Secondary Goals

The website should:

- establish that XYZO is based on a coherent product and architecture thesis
- demonstrate that a working product already exists
- introduce the normalize, compose, inspect, synchronize, and publish operating model
- introduce technical concepts progressively rather than all at once
- show that specialized creation tools remain essential
- make the opportunity legible to advisors, domain experts, early users, technical collaborators, and potential partners
- create confidence that the product is ambitious but grounded
- invite relevant people into a deeper conversation

---

## Primary Audiences

The public homepage is for thoughtful visitors who need an accurate orientation before deeper material.

That includes:

- advisors and domain experts
- designers and 3D creators
- technical collaborators and pipeline-minded teams
- early users and potential partners
- informed investors

The homepage should be understandable to a non-specialist without flattening the product into generic marketing language.

---

## What the Website Must Communicate

### A 3D asset is more than a file

A 3D asset should behave as a living composition rather than a collection of disconnected files.

### Identity persists while state evolves

The asset remains the same asset as its dimensions change.

Persistent identity does not mean frozen state.

### Dimensions can evolve independently

Geometry, materials, textures, metadata, variants, levels of detail, animations, and dependencies can evolve independently while remaining part of the same asset.

### XYZO coordinates change

XYZO normalizes, composes, inspects, synchronizes, and publishes from one trusted asset foundation.

### Specialized tools remain specialized

XYZO connects creation rather than replacing it.

Specialized tools continue to author the dimensions they understand best. XYZO preserves how those changing dimensions belong to the same asset.

### Outputs remain derived

Published files, optimized packages, previews, and platform-specific artifacts are derived representations of canonical state.

Publishing may transform, optimize, repackage, or project content for a downstream target. Those changes must remain confined to the derived artifact and must not redefine canonical authority.

### The system already exists

The site should show real product capabilities, actual interface views, product recordings, canonical package examples, inspection results, synchronization behavior, and other concrete evidence.

It must clearly distinguish working capabilities from active development and long-term direction.

---

## Core Visitor Questions

The website should answer these questions in a deliberate sequence:

1. What is XYZO?
2. What problem does it solve?
3. How does the asset model work at a high level?
4. What does the product do?
5. What is already working?
6. What responsibility does XYZO own?
7. Why does this matter now?
8. How do I request deeper access?

A visitor should not need to understand OpenUSD before understanding XYZO.

Technical depth should be introduced progressively rather than required at the beginning.

---

## Technical Concept Discipline

The website must preserve product truth, but it should not introduce every deep architectural distinction at the top of the homepage.

The public homepage should introduce:

- persistent identity
- evolving dimensions
- trusted representations

Deeper distinctions such as:

- source evidence
- runtime intent
- detailed canonical authority boundaries
- publishing projection details

should appear later in the narrative, in controlled explanatory sections, or in protected deeper materials.

The site must not imply that these concepts are interchangeable, but it should introduce them progressively instead of all at once.

---

## Product Operating Model

The website should explain the product through five connected responsibilities.

### Normalize

Convert heterogeneous source inputs into a deterministic canonical asset structure while preserving source traceability.

### Compose

Allow independently evolving dimensions to remain connected to one persistent asset identity.

### Inspect

Make hierarchy, composition, dimensions, content, dependencies, and integrity visible.

### Synchronize

Bring trusted external changes into canonical state while preserving identity and traceability.

The current implementation supports texture synchronization. Geometry, material, and broader dependency synchronization remain future directions unless explicitly demonstrated as working.

### Publish

Create target-specific derived representations from canonical state.

Publishing may require target-specific projection or restructuring. For example, Apple publishing may require a selected Variant Set to be mirrored onto the exported stage’s default prim. That change belongs to the export-only projection, not the canonical stage.

---

## Proof Hierarchy

The website should prioritize proof in this order.

### 1. Clear Product Logic

The problem, responsibility, and asset model must make sense before visual polish or feature detail matters.

### 2. Working Product Evidence

Use current evidence such as:

- Forge interface screenshots
- short product recordings
- deterministic import and normalization demonstrations
- canonical package examples
- geometry variant composition
- hierarchy and integrity inspection
- dependency diagnostics
- texture synchronization
- viewer refresh behavior
- headless Core operation

Publishing demonstrations should be shown only when the demonstrated workflow is functioning and accurately labeled.

### 3. Architectural Credibility

Explain the role of:

- persistent identity
- source traceability
- canonical authority
- deterministic normalization
- independently evolving dimensions
- trusted dependencies
- runtime boundaries
- synchronization
- derived publishing
- OpenUSD

### 4. Founder Credibility

Show the domain experience, lived workflow pain, systems judgment, architecture-first approach, and ability to build.

### 5. Future Direction

Describe expansion only after establishing what works today.

---

## Relationship to OpenUSD

OpenUSD is central to the current technical architecture but should not be the opening explanation of XYZO.

The site should first explain the asset problem and XYZO’s responsibility in accessible language.

Technical sections may then explain:

- OpenUSD provides composition, references, variants, layered state, stable scene identity, and extensibility
- XYZO operationalizes those capabilities through deterministic normalization, opinionated structure, validation, synchronization, authoring workflows, and target-specific publishing

Preferred framing:

OpenUSD is the composition engine. XYZO is the trusted operating layer around it.

The website must not imply that XYZO is merely a graphical interface for OpenUSD.

---

## Desired Visitor Actions

The primary call to action should invite a relevant conversation rather than force a premature sale.

Appropriate actions include:

- request early access
- contact the founder
- request a product conversation
- explore the thinking behind XYZO

Deeper material such as First Principles and Advisor content should eventually be oriented through protected routes rather than reproduced in full on the public homepage.

The site should not imply that XYZO is commercially available at a scale or maturity it has not yet reached.

---

## Content Priorities

The public website should prioritize:

1. clear hero positioning
2. the file-fragmentation and coordination problem
3. the living canonical asset model
4. the XYZO operating loop
5. working product evidence
6. category boundaries
7. why the coordination problem matters now
8. a focused call to action

Supporting pages may later include:

- `/principles/`
- `/advisor/`
- product demonstrations
- technical documentation
- development updates

The public site should summarize and orient these deeper bodies of material rather than duplicate them.

Audience-specific or sensitive materials may be placed behind controlled access.

---

## Design and Communication Priorities

The website should feel:

- considered
- credible
- technically informed
- visually refined
- calm
- modern
- precise
- ambitious without hype

It should favor:

- strong hierarchy
- concise language
- generous spacing
- clear visual storytelling
- purposeful motion
- progressive disclosure
- authentic product evidence
- restrained technical detail at the top level
- deeper technical detail where appropriate

It should not feel:

- crowded
- overly corporate
- generically futuristic
- dominated by jargon
- like a template-driven startup page
- like a feature checklist
- like an AI-generated marketing site
- like a speculative vision with no working product beneath it

---

## Messaging Rules

The website must follow the approved Project Constitution and Product Positioning.

`WEBSITE_NARRATIVE.md` is the authority for homepage copy hierarchy and section flow.

It must not:

- invent capabilities
- describe planned work as complete
- imply that XYZO replaces creative tools
- position XYZO as a pipeline tracker
- reduce XYZO to conversion, viewing, variant authoring, or publishing
- imply that source evidence is current canonical state
- imply that runtime state is canonical authority
- imply that derived outputs are canonical authority
- suggest that publishing cannot transform a derived artifact
- suggest that publishing may mutate canonical state
- use OpenUSD as the opening explanation for non-technical audiences
- introduce unsupported market, customer, adoption, or performance claims
- use abstract terminology without explaining concrete product responsibility
- treat the homepage as a direct export of the First Principles or Advisor decks

The site should clearly distinguish:

- working today
- in active development
- planned
- long-term direction

---

## Language Standard

Prefer direct statements that explain responsibility.

Preferred examples:

- XYZO keeps 3D assets trustworthy as they move.
- XYZO keeps one authoritative asset connected as it changes.
- A 3D asset is not a file. It is a living composition.
- One identity. Many evolving dimensions.
- Specialized tools remain specialized.
- XYZO orchestrates change while preserving one trusted identity.
- Publishing creates derived representations from canonical state.
- XYZO takes responsibility for the continuity of the 3D asset itself.

Avoid relying on phrases such as:

- revolutionary platform
- seamless workflow
- next-generation solution
- complete end-to-end ecosystem
- AI-powered infrastructure
- single platform for everything
- one source of truth

The concept of one authoritative state is important, but it must be explained accurately rather than used as an unsupported slogan.

---

## Current Product Reality

The current MVP demonstrates a meaningful portion of the XYZO operating model across Forge and Core.

Working capabilities include:

- import and normalization across supported 3D formats
- deterministic canonical package creation
- canonical OpenUSD stage creation
- geometry Variant Set authoring
- reference-based geometry variant composition
- stage hierarchy and composition inspection
- asset bounds and content inspection
- package-integrity and dependency diagnostics
- trusted texture-source tracking
- texture change detection
- canonical texture synchronization
- viewer refresh after synchronized change
- headless Core workflows
- machine-callable operation through current command surfaces

Apple Quick Look and USDZ publishing are in active development and must be presented as such until the production publishing workflow is complete.

Future capabilities such as geometry synchronization, material synchronization, broader provenance, team workflows, policy systems, additional publishing profiles, APIs, and ecosystem integrations must not be presented as current product reality.

---

## Website Success Test

The website is successful when a qualified visitor can accurately explain:

- what XYZO is
- what problem it owns
- why the canonical asset matters
- how identity persists while asset state evolves
- how XYZO relates to creative tools, pipelines, content systems, converters, and viewers
- what is working today
- why the product is worth a deeper conversation

Deeper understanding of source evidence, runtime intent, and derived publishing boundaries may follow through protected or technical materials after the homepage has established the core model.

The website has failed if a visitor leaves believing XYZO is only:

- a file converter
- a USD viewer
- a variant editor
- a publishing utility
- a pipeline tracker
- a storage system
- a generic asset-management platform

---

## Current Website Objective

The immediate objective is not to build the final website.

It is to create the strongest accurate expression of XYZO using the product, language, demonstrations, and evidence available today.

The site should be designed to evolve as the product matures without requiring the core product responsibility to be reinvented.
