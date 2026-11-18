# Loyal Primus — crisp blue header logo, v27

All three promotional objects were re-rendered from the editable v23 Blender scenes. The previously approved hero, layout and text are retained.

## Current rendering changes
- Stronger neutral front and low fill lighting reveals glass interiors, coin faces and candlestick surfaces.
- Brighter directional key/edge lights maintain specular separation.
- Richer blue ribbon, candles and lower spreads rail use a vivid sapphire material with balanced metallic response.
- Candlestick graphite faces are lifted to a clear silver-grey.
- Platform tops and upper ribbing have brighter blue reflections; the lower faces still fall into black.
- Exposure is +0.32 stops. Saturation is 1.12 in the native compositor. High-threshold, restrained HDR bloom and streak glare emphasize bright specular highlights.
- Cycles renders: 512 maximum samples, adaptive threshold 0.004, denoised; transparent high-resolution PNG masters.

## Background
The upper card gradient is lifted to #07517F and #06466F, with a stronger localized sapphire glow behind each object. It falls through #032A47 to #000306. The existing fine dots and arcs remain secondary. These layout layers and typography are editable in section.html and source/feature-art.html.

## Deliverables
- preview.html: complete email with desktop/mobile views.
- email.html: sending-template HTML; sample personal message remains editable in copy.json.
- section.html: three-card composition, 600 × 392 CSS pixels.
- assets/: high-resolution Blender PNG renders, 2× JPEG email slices, approved hero and logo.
- source/*.blend: editable native scenes with final materials, lighting and compositor.
- source/bright_studio.py: record of the v24 native scene refinements against v23.
- review/: actual-size cards and desktop/mobile email proofs.

## Sending setup
Host the images over HTTPS, configure the email platform merge fields, sender postal address and final copy. Existing promotional figures and destinations are retained. Browser preview verification is not inbox-client certification.

## v25 footer revision
Removed the entire Kuala Lumpur, Malaysia location line. Header and brighter v24 card artwork retained.

## v26 ribbon correction
Rebuilt the rewards ribbon in Blender. Two continuous closed mesh bands wrap over the lid, follow its overhang, continue down all four faces and return underneath the box. Two shaped bow loops meet inside a rounded central knot, with short tails resting on the lid. The previous separate strips, loop geometry and metal clasp are replaced. Current lighting and materials are retained. Capacity, spreads, hero and location-free footer are unchanged.

## v27 header logo correction
The header logo now uses the same original PNG as the footer, rendered separately in HTML. It is no longer baked into the compressed hero banner. Hero artwork is exported below the 60 px masthead; desktop placement is retained.
