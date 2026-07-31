---
name: Preview cache behavior
description: Static homepage preview caching after promoting an HTML prototype
---

Replit Preview may continue displaying an older static HTML document after the workflow is restarted and the server returns the new file. A cache-busting query string on the preview URL forces the current document to load.

**Why:** The static Python server has no application cache or service worker, but the Preview browser can retain the previously loaded root document.

**How to apply:** When a promoted static homepage appears stale, verify the live response and use `/?preview=<current-marker>` or hard-refresh the Preview pane before changing routing or deployment configuration.