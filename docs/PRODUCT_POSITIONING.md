# XYZO Product Positioning

## Positioning Statement

XYZO keeps 3D assets connected and trustworthy as they change and move across tools, contributors, workflows, and downstream uses.

It creates and maintains a living canonical asset with one persistent identity, a traceable origin, independently evolving dimensions, one authoritative current state, trusted dependencies, and many derived representations.

XYZO is the infrastructure layer responsible for the continuity of the 3D asset itself.

---

## The Problem XYZO Owns

3D assets rarely remain inside one application, one team, or one delivery path.

They move across:

- creation tools
- conversion systems
- production pipelines
- review environments
- publishing targets
- commerce platforms
- visualization systems
- spatial experiences
- manufacturing workflows
- game engines
- automated and AI-driven processes

As they move, they are copied, converted, optimized, renamed, repackaged, and modified.

The result is fragmentation:

- multiple files claim to represent the same asset
- dimensions evolve without coordination
- dependencies drift or break
- downstream outputs become disconnected
- teams lose confidence in which state is authoritative
- origin and transformation history become difficult to trace

Most existing systems own one part of this process. No established category takes responsibility for preserving the continuity of the 3D asset itself.

XYZO is built to own that responsibility.

---

## What XYZO Is

XYZO is infrastructure for living 3D asset compositions.

It provides a deterministic orchestration layer that:

- establishes persistent asset identity
- records source evidence
- normalizes heterogeneous inputs
- creates and maintains one evolving canonical state
- coordinates independently evolving dimensions
- preserves trusted dependencies
- validates asset and package integrity
- synchronizes trusted changes
- produces derived representations without creating competing sources of truth

The current product expresses this through a canonical OpenUSD asset architecture.

OpenUSD provides the composition engine. XYZO provides the operating model, structure, validation, synchronization, and product workflows that make it usable as a trustworthy asset system.

---

## What XYZO Does

XYZO orchestrates change while preserving one trusted identity.

Its operating loop is:

- Normalize
- Compose
- Inspect
- Synchronize
- Publish

### Normalize

XYZO ingests assets from heterogeneous source formats and converts them into a deterministic canonical structure.

Normalization establishes:

- predictable scale
- coordinate conventions
- naming
- package structure
- asset identity
- dependency relationships
- source traceability

### Compose

XYZO allows dimensions of the asset to evolve independently while remaining connected to the same asset identity.

These dimensions may include:

- geometry
- materials
- textures
- metadata
- variants
- levels of detail
- animations
- dependencies

### Inspect

XYZO makes asset state and integrity visible.

Inspection may include:

- stage hierarchy
- composition
- dimensions and bounds
- content counts
- dependency status
- missing or unresolved references
- package integrity
- canonical structure

### Synchronize

XYZO Sync brings trusted external changes back into the canonical asset.

The current implementation supports texture synchronization. Future synchronization may extend to geometry, materials, and other dimensions.

Synchronization is not simple file replacement. It is a controlled update to canonical state that:

- preserves asset identity
- retains traceability to origin
- detects what changed
- validates the change
- updates trusted dependencies
- keeps downstream consumers aligned

### Publish

XYZO creates target-specific representations from canonical state.

Publishing may transform, optimize, repackage, or project the asset to satisfy a downstream target. For example, Apple USDZ publishing may mirror a selected Variant Set onto the exported stage’s default prim so it can be recognized as an Apple configuration.

These changes belong only to the derived publishing artifact. They must not mutate canonical state or create a competing source of truth.

---

## The Canonical Asset

The canonical asset is the product foundation.

It connects four distinct concepts:

### Persistent Identity

The asset remains the same asset throughout its lifetime.

### Source Evidence

A traceable record of where the asset began, what was observed, and what normalization decisions were made.

### Evolving Canonical State

The current authoritative state of the asset after trusted normalization, composition, synchronization, and authoring.

### Derived Representations

Outputs created for specific downstream uses.

The distinction is:

- source evidence records where the asset began
- canonical state defines what the asset is now
- derived representations express how the asset is used

XYZO preserves continuity across all four.

---

## Category Position

XYZO occupies a missing layer between specialized creation and downstream consumption.

It does not replace existing categories. It connects them around one trusted asset.

### Creation Tools

Examples include Blender, Maya, Houdini, ZBrush, Substance, and Photoshop.

They own:

- geometry creation
- material creation
- texture editing
- animation
- design intent
- specialized authoring

XYZO relationship:

Specialized tools remain specialized. XYZO preserves how their outputs continue to belong to the same asset as they change.

### Pipeline and Production Systems

Examples include ShotGrid, ftrack, Flow Production Tracking, and custom studio pipelines.

They own:

- tasks
- approvals
- schedules
- versions
- handoffs
- production status

XYZO relationship:

Pipelines move work. XYZO maintains the continuity and trusted state of the asset being moved.

### DAM, PIM, PLM, and MDM Systems

They own:

- storage
- cataloging
- business metadata
- product records
- distribution
- lifecycle records

XYZO relationship:

These systems manage records, storage, and distribution. XYZO manages the internal composition, canonical state, dependency integrity, and continuity of the 3D asset.

### Conversion and Optimization Tools

They own:

- format translation
- polygon reduction
- texture optimization
- repackaging
- platform preparation

XYZO relationship:

Conversion and optimization are operations within a larger asset continuity system. XYZO normalizes inputs into canonical state and treats optimized outputs as derived representations.

### Publishing Systems

They own:

- packaging
- target-specific delivery
- deployment
- platform validation

XYZO relationship:

XYZO treats publishing as the creation of a derived representation from canonical state, not as the creation of another disconnected source of truth.

Target-specific transformations belong only to the derived artifact and do not redefine canonical state.

### Viewers and Review Tools

They own:

- presentation
- visualization
- review
- interaction

XYZO relationship:

Viewers consume asset state. They do not define asset authority.

---

## What XYZO Is Not

XYZO is not:

- another digital content creation application
- a render engine
- a viewer alone
- a file converter alone
- a mesh optimization service
- a pipeline tracker
- a project-management platform
- a version-control product
- a digital asset management system
- a product-information management system
- a replacement for specialized creative tools
- a proprietary format intended to trap assets inside one application

XYZO should not be positioned as sitting ambiguously between these categories.

Its responsibility is specific:

XYZO preserves the asset’s persistent identity, evolving canonical state, source traceability, composition, dependencies, integrity, synchronization, and trusted continuity across tools and uses.

---

## Primary Value

The primary value of XYZO is trust across change.

XYZO helps a team know:

- which asset state is authoritative
- where the asset came from
- what changed
- which dependencies belong to it
- whether those dependencies remain valid
- how its dimensions relate
- whether an output derives from trusted state
- whether downstream consumers are aligned to the same asset

The product is not valuable merely because it converts, validates, synchronizes, or publishes files.

It is valuable because those operations remain connected to one trusted asset identity.

---

## Core Differentiation

### File-Centered Systems

File-centered systems treat each file as the unit of truth.

XYZO treats the asset as the unit of truth.

### Delivery-Centered Pipelines

Traditional pipelines are usually designed around movement toward a delivery milestone.

XYZO assumes the asset has a lifetime beyond any single delivery and must continue to evolve across many uses.

### Conversion-Centered Platforms

Conversion platforms focus on making an asset usable in another format or destination.

XYZO focuses on preserving continuity, authority, and trust before, during, and after conversion.

### Storage-Centered Systems

DAM and PIM systems can store files and metadata about them.

XYZO manages the internal composition and trusted state of the 3D asset itself.

### Tool-Centered Workflows

Tool-centered workflows make one application or stage of production the center of gravity.

XYZO keeps the asset at the center while tools remain specialized and replaceable.

### Publishing-Centered Systems

Publishing systems optimize an asset for a particular target.

XYZO allows target-specific transformation while preserving the distinction between canonical authority and derived output.

---

## Audiences

### Designers and Creators

They need asset dimensions to evolve without constantly rebuilding disconnected files or losing confidence in what belongs together.

XYZO gives them a non-destructive asset system in which geometry, materials, textures, variants, and metadata can change independently while remaining part of one asset.

### Pipeline and Technical Teams

They need deterministic structure, explicit authority, predictable dependencies, validation, automation, and reliable downstream publishing.

XYZO provides a canonical asset layer that can sit beneath desktop tools, scripts, pipelines, APIs, integrations, and machine-driven workflows.

### Small Studios and Product Teams

They need the benefits of structured asset composition without building and maintaining a large custom USD pipeline.

XYZO turns sophisticated composition principles into opinionated product workflows.

### Enterprises with Growing 3D Operations

They need continuity across creation, product records, publishing channels, teams, and downstream systems.

XYZO can provide the trusted 3D asset layer that existing production, content, and business systems do not own.

---

## Three Ways to Explain XYZO

### For Anyone

XYZO keeps a 3D asset connected and trustworthy as it changes and moves across tools and uses.

Analogy:

Think of it as the master record for a 3D asset. Different people and tools can change parts of it while XYZO keeps everyone connected to the same trusted asset.

### For Designers and Creators

XYZO turns disconnected 3D files into one living asset whose geometry, materials, textures, variants, and metadata can evolve without losing identity.

Analogy:

Think of it as a non-destructive design system for a 3D asset. Its dimensions can change independently while still belonging to the same asset.

### For Pipeline and Technical Teams

XYZO is a deterministic orchestration layer for canonical OpenUSD assets, preserving identity, source traceability, composition, dependencies, integrity, synchronization, and trusted downstream publishing.

Clarification:

XYZO is not another DCC, converter, or pipeline tracker. It is the layer responsible for the asset’s persistent identity and trusted state.

---

## Approved Core Language

Preferred positioning statements:

- XYZO keeps 3D assets trustworthy as they move.
- XYZO is infrastructure for living 3D asset compositions.
- A 3D asset is not a file. It is a living composition.
- XYZO orchestrates change while preserving one trusted identity.
- The canonical asset is the product foundation.
- Source evidence records where the asset began. Canonical state defines what the asset is now.
- One identity. Many evolving dimensions.
- One evolving authoritative state. Many trusted representations.
- Specialized tools should remain specialized.
- Infrastructure should connect creation, not replace it.
- XYZO takes responsibility for the continuity of the 3D asset itself.
- OpenUSD is the composition engine. XYZO is the trusted operating layer around it.
- The interface can change. The canonical system remains.
- Pipelines move work. XYZO maintains the continuity and trusted state of the asset being moved.
- Publishing creates derived representations from canonical state.
- Publishing may transform the derived artifact without mutating canonical authority.
- Synchronization is the controlled evolution of trusted asset state.

---

## Language to Use Carefully

These terms are valid, but they should be connected to concrete product responsibility:

- infrastructure
- orchestration
- canonical
- composition
- provenance
- trust
- continuity
- deterministic
- living asset
- derived representation

Do not stack these terms together without explaining what XYZO does.

Avoid:

“XYZO is a trusted deterministic orchestration infrastructure platform for canonical living asset composition.”

Prefer:

“XYZO keeps one authoritative 3D asset connected as its geometry, materials, textures, and outputs change.”

---

## Language to Avoid

Avoid generic or unsupported claims such as:

- revolutionary
- disruptive
- magical
- seamless
- effortless
- fully automated
- universal
- industry-leading
- next-generation
- complete end-to-end platform
- single platform for everything
- AI-powered, unless describing a specific implemented capability
- replaces your pipeline
- replaces creative tools
- eliminates all asset drift
- guarantees visual parity
- solves every 3D workflow

Do not describe planned capabilities as if they are already implemented.

Clearly distinguish:

- working today
- in active development
- planned
- long-term direction

---

## Current Product Reality

The current MVP demonstrates the core operating loop across Forge, Core, and publishing workflows.

Working capabilities include:

- import and normalization across supported 3D formats
- deterministic canonical package creation
- canonical OpenUSD stage creation
- geometry Variant Set authoring
- reference-based geometry variant composition
- asset hierarchy and composition inspection
- asset bounds and content inspection
- dependency and package-integrity diagnostics
- trusted texture-source tracking
- texture change detection and canonical texture synchronization
- viewer refresh
- headless Core workflows
- machine-callable workflows through current command surfaces

Apple Quick Look and USDZ publishing are in active development.

The current implementation proves the architecture and product responsibility. It does not yet represent the full scope of the long-term platform.

---

## Product Expansion Logic

XYZO should expand outward from the canonical asset rather than accumulating disconnected features.

### Foundation

- import and normalize
- compose
- inspect
- synchronize textures
- publish initial target-specific outputs

### Expansion

- stronger provenance
- geometry synchronization
- material synchronization
- additional publishing profiles
- broader headless automation

### Scale

- team workflows
- policy and validation
- ecosystem integrations
- machine-driven asset operations

Every new capability should strengthen the canonical asset and its continuity.

Features that bypass, duplicate, or weaken canonical authority are strategically misaligned.

---

## Positioning Test

A proposed message is aligned when it clearly communicates at least one of these responsibilities:

- preserving identity
- coordinating change
- maintaining canonical authority
- retaining source traceability
- connecting evolving dimensions
- validating integrity
- synchronizing trusted dependencies
- producing derived representations
- preserving continuity across tools and uses

A proposed message is weak when it describes XYZO only as:

- a converter
- a USD utility
- a desktop viewer
- a publishing tool
- a variant editor
- a pipeline product
- a storage system
- a generic collaboration platform

Those may describe capabilities or interfaces, but they do not define the product.

---

## Enduring Position

Creation will continue to fragment across specialized tools, generators, services, and automated systems.

Consumption will continue to multiply across platforms, experiences, and industries.

The resulting coordination problem will not be solved by another isolated tool or another disconnected file format.

XYZO is building the infrastructure that preserves one trusted 3D asset across that expanding ecosystem.