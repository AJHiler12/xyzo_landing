# Website Styling

## CSS location

The active website CSS lives in:

- `resources/styles/site.css`

The homepage HTML links it from:

- `index.html`

Current stylesheet link:

```html
<link rel="stylesheet" href="./resources/styles/site.css">
```

## Current styling architecture

The website uses CSS, not QSS.

The current implementation is a static site with:

- HTML in `index.html`
- CSS in `resources/styles/site.css`
- small interaction scripts embedded in `index.html`

There are no other repository `.css` files at the time this document was added.

## Stylesheet section order

`resources/styles/site.css` is organized in this order:

1. Custom properties / tokens
2. Reset and base elements
3. Typography
4. Shared layout containers
5. Header and navigation
6. Hero
7. Form
8. Content sections
9. Diagrams and evidence
10. CTA / footer
11. Interaction states
12. Responsive rules
13. Reduced-motion rules

## Naming conventions

- Shared structural selectors are short and generic when they are intentionally reused across sections, for example `.wrap`, `.mono`, `.eyebrow`, and `.reveal`.
- Component selectors are scoped by section or component name, for example `.hero-inner`, `.signup-form`, `.canonical-intro`, `.evidence-frame`, and `.sync-toggle`.
- The header logo uses `.site-logo` so it does not collide with any future hero-specific logo treatment.
- Hero form styles are scoped under `.hero` to avoid broad control rules leaking into other sections.

## Shared vs component-specific selectors

Shared selectors:

- `.wrap`
- `.mono`
- `.eyebrow`
- `.eyebrow-accent`
- `.marker`
- `.reveal`
- `.visible`

Component-specific selectors:

- Header/navigation: `.site-logo`, `.nav`, `.navlinks`, `.nav-cta`
- Hero: `.hero`, `.hero-inner`, `.hero-kicker`, `.hero-foot`, `.hero-copy`, `.scroll-note`
- Form: `.hero .signup`, `.hero .signup-form`, `.hero .signup-field`, `.hero .audit-note`, `.hero .thank-you`
- Product/architecture sections: `.problem`, `.canonical`, `.asset-model`, `.model-row`
- Loop/evidence sections: `.loop`, `.stage`, `.identity`, `.placeholder`, `.sync-*`, `.evidence-*`
- Closing/footer: `.closing`, `.action`, `.footer`

## Responsive rules

Responsive CSS lives near the end of `resources/styles/site.css` in the `@media (max-width: 760px)` block.

This block contains:

- container width changes
- header compaction
- hero stacking changes
- form stacking changes
- section padding changes
- loop/stage layout changes
- evidence and footer stacking changes

## Reduced-motion rules

Reduced-motion CSS lives at the bottom of `resources/styles/site.css` in:

```css
@media (prefers-reduced-motion: reduce) { ... }
```

This preserves:

- disabled smooth scrolling
- disabled reveal transitions
- disabled sync comparison transition

## Hero style scoping

Hero layout and typography live in the `Hero` section of `site.css`.

Hero-specific form rules are scoped with `.hero`, for example:

- `.hero .signup`
- `.hero .signup-form`
- `.hero .signup-field`
- `.hero .signup-form button`
- `.hero .audit-note`
- `.hero .thank-you`

This avoids reintroducing generic `input` and `button` rules that could affect later sections.

## Form style scoping

The Netlify signup form remains in `index.html`, but its appearance is controlled from `resources/styles/site.css`.

Behavior is still controlled by the existing inline JavaScript in `index.html`.

Do not move or rename:

- `name="xyzo_signup"`
- `method="POST"`
- `data-netlify="true"`
- hidden `form-name` input
- `id="thank-you"`

## Inline styles

Inline `<style>` blocks were removed when the stylesheet was externalized.

Inline `style=""` attributes should also be avoided. At the time this document was added, the homepage was normalized to use class-based styling instead of inline color overrides.

Inline JavaScript remains in `index.html` because it controls:

- reveal-on-scroll behavior
- sync comparison state toggling
- Netlify form submission success state

## Local preview

You can preview the site locally from the repository root with:

```powershell
python preview_server.py
```

If needed, a basic static server also works:

```powershell
python -m http.server 8000
```

Then open the local URL in a browser.

## Making a safe style change

1. Inspect the target markup in `index.html`.
2. Find the existing selector in `resources/styles/site.css`.
3. Prefer editing the smallest component-specific rule instead of adding a broad global override.
4. Check desktop and mobile behavior.
5. Confirm reduced-motion and focus behavior still work.
6. Confirm the Netlify form markup and JS behavior are unchanged.

## How to avoid duplicate or inline styles

- Do not add new `<style>` blocks to `index.html`.
- Do not reintroduce generic global control rules unless they are truly shared.
- Prefer class-based selectors over inline `style=""` attributes.
- If a selector belongs only to one section, keep it scoped to that section.
- If a new pattern is shared across multiple sections, add it to the relevant shared section in `site.css` rather than duplicating declarations.

## Maintenance note

If a future redesign introduces a hero-specific logo separate from the header mark, do not reuse `.site-logo`. Add a distinct selector for the new element to keep header and hero branding independent.
