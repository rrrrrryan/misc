## UI design rules

### Hierarchy
- One primary action or focal element per screen; everything else is visually subordinate.
- Create emphasis with size, weight, and color, in that order. Prefer de-emphasizing secondary text (muted grey, lighter weight) over enlarging primary text.
- Labels, metadata, and captions should visibly recede. If everything is emphasized, nothing is.

### Spacing and layout
- Use a fixed spacing scale: 4/8/12/16/24/32/48/64px. Never use off-scale values.
- Default to generous whitespace. When unsure, add space, not borders.
- Space between groups must be clearly larger than space within groups.
- Minimize distinct alignment lines; left-align text. Never center body copy.
- Constrain content width; body text lines stay between 45–75 characters.

### Typography
- One typeface family, two weights (e.g., 400 and 600).
- Fixed type scale, max 5 sizes (e.g., 12/14/16/20/24px). Body 14–16px, line-height ~1.5.
- Build hierarchy with weight and color before reaching for size.

### Color
- Design grayscale-first, then add one accent color, used sparingly (primary actions, key data).
- Use a neutral ramp of 8–10 greys. Primary text is near-black (#111–#222), never pure #000.
- For secondary text on a colored background, use a lighter shade of the background hue — never grey, never reduced opacity.
- Reserve red/green/amber strictly for status semantics.
- No gradients, glassmorphism, or decorative color effects unless explicitly requested.

### Depth and containers
- Separate content with spacing and subtle background shifts before using borders.
- When borders are necessary: 1px, very light grey.
- At most two shadow elevations, both subtle.
- Don't wrap every section in a card. Never nest cards inside cards.

### Data display
- Maximize data-ink: remove gridlines, legends, and chart borders that carry no information; mute whatever remains.
- Right-align numeric columns, fixed decimal places, font-variant-numeric: tabular-nums.
- Label data directly on the chart instead of using a legend where possible.

### States and details
- Every interactive element has hover, focus, active, and disabled states.
- Design empty, loading, and error states explicitly; empty states tell the user what to do next.
- No emoji in UI text. Icons only when they add meaning, from a single set, at a single size.

### Overall
- Target the restraint of Linear or Stripe: calm, neutral, dense but breathable.
