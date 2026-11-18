# lp-creative

Loyal Primus creative concepts, published as static previews.

| Path | Concept | Source of truth |
| --- | --- | --- |
| `login/` | Glass sign-in concept (day/dark video themes, Glisse fields). Static mockup with no real authentication; form entries never leave the page. | `login-concept-v2` |
| `email/` | Personal-message email, v27: blue header logo, continuous gift ribbon, three promotional cards, location-free footer. | `email-layout-v27` |

- `login/`: edit `src/portal.jsx`, then run `npm ci && npm run build` inside `login/` to regenerate `login.js`. Run it locally with `python3 serve.py --port 8934`.
- `email/`: `preview.html` shows desktop and mobile views. `email.html` is the sending template. `source/` holds the editable Blender scenes and build scripts, and `assets/*.png` holds the high-resolution render masters. Source files and masters are kept in git but excluded from the Vercel upload (`.vercelignore`).

Deployed as Vercel **preview** deployments only.
