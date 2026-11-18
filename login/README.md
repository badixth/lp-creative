# Loyal Primus glass login concept

Run `python3 serve.py --port 8934` from this folder and open `http://127.0.0.1:8934/`. The page, fonts, video loops and glass components are bundled locally.

Edit the form in `src/portal.jsx` and the layout in `login.css`. After changing the JSX, run `npm ci` and `npm run build` to regenerate `login.js`. The inputs, buttons, switch and navigation glass use Glisse 0.6.0. The component library is at https://github.com/0kzh/glisse.

The 12-second films in `assets/` use the Mint Matrix VIII Blender scene, retimed to half speed at 30 fps. Every original frame is retained. The media element selects a format from the size of the artwork on screen. A reduced-motion preference starts the page with its matching still.

Form submission is a local demonstration. Account and password entries stay in memory, and the password clears on submit. Recovery and registration links open the official client portal.

The header sun/moon button switches between day and dark themes and remembers the selection locally. Fields use opaque tinted surfaces for readability. Transparent ASIC and FSCA badges are enlarged with responsive sizing.

Brand accents and the Login button use #1D9BF0, sampled from the supplied logo, in both themes.

Fields use neutral pearl glass in day mode and darker smoked glass at night, with backdrop blur, a directional sheen and restrained brand-blue focus.

Day mode retains full metallic contrast across the main artwork, then feathers into the form area. Mobile retains a dark artwork header with the light form below. The previously approved curved-blend version is archived separately as login-concept-v2-saved-curved-blend.

Latest refinement: a softer form-side dissolve, with a shared 480px maximum content column for mobile header/logo, headline, form and left-aligned regulation badges. Previous metallic-day version saved as login-concept-v2-saved-metallic-day. Checked at 390px, 760px and desktop widths.

Mobile centered iteration: centered headline, sign-in introduction and badges; left-aligned field labels. Day/dark geometry is identical, with a shorter transition and 43px less space before the form in day mode. Verified at 360px, 390px and 760px. Previous aligned edition saved as login-concept-v2-saved-soft-aligned.

Clean mobile day transition: shallow curved boundary with a narrow feather replaces the grey dissolve. No geometry changes; day and dark form positions verified identical. Previous centered edition saved as login-concept-v2-saved-centered-mobile.

Mobile spacing finish: 42–48px before the sign-in section and 40px bottom padding, identical in both themes.

Native Glisse input iteration: reference-field uses the library 40px height, 20px pill radius, 3px blur, generated refracted rim and 200ms background transition. No additional hover shadow or focus halo. Light: white at 60%, active rgb(236 236 240 / 85%). Dark: rgb(40 40 40 / 62%), active rgb(70 70 70 / 62%). Verified against https://glisse.kelvinzhang.com/ in the browser; surrounding backdrop naturally affects the visible composite. Bright-blue button/links retained. Previous version saved as login-concept-v2-saved-before-native-fields.

Roomier input sizing: 56px tall, 20px horizontal padding, 28px pill radius and 16px input text; native Glisse material and state colors/transitions unchanged. Password reveal target increased to 44px. Verified light/dark default and focused colors.

Neutral dark edition: #080808 base with charcoal gradients and neutral navigation, dividers and secondary text. Native Glisse input states, #1D9BF0 accents and day mode retained. Previous navy edition saved as login-concept-v2-saved-before-neutral-dark.

Day-mode identity overlays: pearl-white behind logo/headline, dark primary heading, stronger badge contrast and clear central metallic artwork. Small day links use #006AA9; the bright #1D9BF0 button has a dark label. Measured flat-color contrast: button label 6.15:1, small links on page background 5.16:1. These measurements are not a full accessibility audit of video-backed content. Dark mode and native Glisse field states unchanged. Prior edition saved as login-concept-v2-saved-before-day-overlay.

Reduced-overlay refinement: concentrated the desktop light treatment around identity content, shortened and angled the logo fade, and exposed more central metallic keys. Mobile light transitions tightened, with a two-pixel end feather to prevent a compositor seam. Bright blue #1D9BF0 and native Glisse field states unchanged. Visually reviewed at 1440x900 and 390x844; mobile day/dark form and headline bounds match exactly, with no horizontal overflow. Previous edition retained in login-concept-v2-saved-before-reduced-overlay.

Silver Day Studio: separate physically relit day videos in all three responsive crops. Theme changes preserve the playback phase. Twelve seconds at 30 fps. Original dark videos, layout, brand blue, and native Glisse fields are retained. Prior page saved in login-concept-v2-saved-before-day-render. Editable day scene: ../spline-rhythm-day-v1/silver-day.blend.

Smooth theme edition: two persistent, preloaded video layers replace source swapping. The incoming clip seeks to the current motion phase before a 760ms eased composition crossfade; gentle temporary rate correction compensates for decode delay. The hidden player pauses after the dissolve. Paused playback is retained across themes, rapid requests cancel stale preparations, and reduced-motion mode removes the dissolve. Day masking is reduced across the main artwork, with local support behind the logo and heading and a form-side fade. Desktop and mobile retain the same layout, #1D9BF0 brand accents, and native Glisse fields. Previous approved page saved in login-concept-v2-saved-before-smooth-toggle (folder and ZIP).

Soft heading edition: lower-opacity, multi-stop feather behind desktop identity with a 12px diffusion; mobile uses a gradual 48–100% transition to show the silver keys through the heading. Bright blue #1D9BF0, form, layout and synchronized theme switching unchanged. Visually reviewed at 1440×900 and 390×844; mobile geometry matches the prior edition with no horizontal overflow. Previous version saved in login-concept-v2-saved-before-soft-heading (folder and ZIP).

Logo shadow edition: removed the white logo pseudo-element across desktop and mobile; applied a silhouette-only neutral drop shadow (0 1px 2px, black at 24%). Original blue PNG, heading fade, form and switching unchanged. Verified no logo backing at 1440px and 390px, no mobile horizontal overflow.

Brand readability edition: logo uses a tight neutral edge shadow plus a soft ambient shadow, without any white backing. Day links now use brand #1D9BF0 and the Login label/arrow are white per the approved visual direction. Verified at 1440×900 and 390×844, with no mobile overflow. Existing layout, fields and theme crossfade retained. This visual change does not assert WCAG contrast compliance for small bright-blue text or white text on the bright-blue button.

Mobile logo edition: responsive wordmark width 156–200px (179.4px at 390px, previously 145px), with a 150px compact treatment at 320px. Keeps original blue PNG, silhouette shadow and no backing. Compact header drops only the decorative external-arrow icon below 350px. Verified at 390px and 320px with positive control spacing and no overflow; desktop styling unchanged.

Mobile header spacing: widened header to 16px side gutters, capped at 480px, with at least 24px between logo and controls. Slightly tighter website-pill typography at 351–430px preserves the enlarged logo. Browser-verified gaps: 41px at 390px, 24.8px at 360px, 24px at 320px; no horizontal overflow. Logo size, original blue and no white backing retained. Desktop unchanged.

Silver glass fields: day inputs now have a translucent silver tint, directional highlight, fine edge shading, stronger neutral placeholders and a restrained blue focus edge. The existing Glisse refracted rim remains; day material/state styling intentionally departs from the stock white reference. Field sizing stays 56px with 20px inset. Dark material remains rgba(40,40,40,.62), 3px blur. Reviewed day default/focus and mobile layout at 1440×900 and 390×844; no mobile overflow. Previous CSS retained in login-before-silver-fields.css.

Clear glass edition: removed blue-grey field fill and pale-blue focus halo. Day fields use neutral white at 18% (28% hover, 36% focus), 8px blur, neutral edges/shadows, and stronger neutral placeholders. Brand blue links/CTA remain. Reviewed desktop default/focus and mobile at 1440×900 and 390×844; 56px field height and no mobile overflow. Previous silver styling saved in login-before-clear-fields.css.
