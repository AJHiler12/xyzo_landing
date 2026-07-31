---
name: Preview cache behavior
description: Static homepage preview caching after promoting an HTML prototype
---

Replit Preview may continue displaying an older static HTML document after the workflow is restarted and the server returns the new file. In some sessions the embedded panel remains on an in-memory document and does not request the current workflow at all; a new URL/navigation or reopening the Preview surface is required.

**Why:** The static Python server has no application cache or service worker, but the Preview browser can retain the previously loaded root document or stay attached to a prior preview session.

**How to apply:** When a promoted static homepage appears stale, verify the live response and workflow logs first. Use a full new URL such as `/?preview=<current-marker>` or reopen the Preview surface; do not keep changing application code once the live endpoint is confirmed current.