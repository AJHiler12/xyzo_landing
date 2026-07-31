# Welcome to XYZO

Before making any code, content, or design changes, read the documents in this order:

1. PROJECT_CONSTITUTION.md
2. PRODUCT_POSITIONING.md
3. WEBSITE_NARRATIVE.md
4. WEBSITE_GOALS.md
5. BRAND.md
6. DESIGN_LANGUAGE.md
7. WEBSITE_STYLING.md
8. AI_RULES.md

These documents define the product truth, positioning, homepage narrative, communication goals, brand voice, visual direction, styling architecture, and agent operating rules for the XYZO website.
`WEBSITE_STYLING.md` documents where the website CSS lives, how it is linked, and how to make safe styling changes without reintroducing duplicate or inline CSS.

## Authority Order

When documents appear to conflict, use this order of authority:

1. PROJECT_CONSTITUTION.md
2. PRODUCT_POSITIONING.md
3. WEBSITE_NARRATIVE.md
4. WEBSITE_GOALS.md
5. BRAND.md
6. DESIGN_LANGUAGE.md
7. WEBSITE_STYLING.md
8. AI_RULES.md
9. Existing website implementation

The current website is not the source of truth. It is an implementation that may be revised to better reflect the documents above.

The public homepage is a summary and orientation layer, not a verbatim reproduction of the First Principles deck or Advisor deck. Protected deeper material should eventually live in `/principles/` and `/advisor/`.

## Working Rules

Do not:

- invent new product positioning
- add unsupported marketing claims
- describe planned capabilities as complete
- reduce XYZO to a converter, viewer, publishing utility, or pipeline tool
- change approved core language without explaining why
- make broad architectural or structural changes without review
- remove working content, assets, forms, or integrations without identifying the impact
- treat visual novelty as more important than clarity or product truth

Do:

- preserve the distinction between working capabilities, active development, and future direction
- introduce technical concepts progressively rather than front-loading deep architecture language
- distinguish working capabilities from active development and future direction
- use real product evidence wherever possible
- prefer refinement over wholesale replacement
- explain the reasoning behind meaningful copy, design, or structural changes
- preserve responsive behavior, accessibility, and existing deployment requirements
- ask questions when product meaning or implementation impact is unclear

## Website Development Approach

Work in small, reviewable stages.

For each stage:

1. Inspect the current implementation.
2. Identify the specific problem being solved.
3. Propose the change before broad rewrites.
4. Modify only the relevant files.
5. Preserve unrelated behavior.
6. Review the result at desktop and mobile sizes.
7. Summarize what changed and why.
8. Commit only after review.

Prefer section-by-section development over redesigning the entire site in one pass.

## Current Technical Context

The website is currently a static site deployed through GitHub and Netlify.

GitHub remains the source of truth.

Replit is a development environment, not the deployment authority.

Website redesign work should remain on the `website-v2` branch until it is reviewed and intentionally merged into `main`.

Do not replace the existing deployment path or introduce a new framework, build system, backend, database, authentication system, or hosting dependency without explicit approval.

## First Task in Any New Session

Before changing files:

1. Read the documents listed above.
2. Inspect the current repository structure.
3. Inspect the current website.
4. Summarize the product, homepage narrative, website goals, current implementation, and proposed scope.
5. Identify any conflicts, unsupported claims, or questions.
6. Wait for approval before making substantial changes.

When in doubt, ask rather than invent.
