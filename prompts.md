# Prompts that built this project

---

### `2026-02-27 08:05 PST`
```
The user has just created this VM, and wants to do the following with it.
Create a new git repo
In it, create a python script to visualize naturally occurring spirals in 2d 
For each spiral, make it easy to plot points along integer distance along the spiral out from the origin. E.g. odds, evens, squares.
```

### `2026-02-27 09:03 PST`
```
hmm now I realize python is the wrong vehicle here.
Make a pure HTML/JS/CSS version that can be used interactively by selecting a spiral and a set of points of interest (odds, evens, squares, etc).
```

### `2026-02-27 09:09 PST`
```
Vertical scroll on the spiral viewport should zoom in/out (modifying max arc length and max turns appropriately).
Modifying either max arc length or max turns should auto update the other to reflect what fits in the viewport.
Viewport should use max available space (without causing the overall page to have scrollbars).
```

### `2026-02-27 09:20 PST`
```
Color contrast of a lot of the text is insufficient.
```

### `2026-02-27 09:22 PST`
```
Add spiral types: square, hexagonal, and a few more that make sense. Drop Lituus and hyperbolic. Generally only want to keep spirals that can plot lots of info in a visually-informative way.
Remove ceiling on zoom.
```

### `2026-02-27 09:24 PST`
```
continue and also add an SVG favicon (inline in the HTML) portraying a spiral.
```

### `2026-02-27 09:29 PST`
```
Persist UI state in URL fragment.
Use keys 1..9 to switch spiral type.
Reduce the dot size when too many dots are displayed, and drop the grey/undotted spiral points when zoomed out enough.
```

### `2026-02-27 09:30 PST`
```
Also use shift-1..9 to switch highlighted set (odds, evens, etc)
```

### `2026-02-27 09:33 PST`
```
The hightlight drop-drown should name the keys as Shift-1, Shift-2 etc, not use the shifted key chars (!@# etc).
In fact use up-arrow unicode character for shift.
```

### `2026-02-27 09:36 PST`
```
The viewport slightly overlaps the drop-downs on page load and only becomes correct after a bit of mouse hover action.
```

### `2026-02-27 09:37 PST`
```
Rename " Natural Spirals" to "Integers on Spirals"
```

### `2026-02-27 09:38 PST`
```
Add a unicode/largish ? at the top-right which when clicked launches a modal JS dialog that explains what this webapp is.
```

### `2026-02-27 09:52 PST`
```
- User typing ? when focus is anywhere in the webapp should launch the help modal.
- Pinch-to-zoom should work on mobile.
```

### `2026-02-27 09:55 PST`
```
Hex spiral should follow https://forums.wolfram.com/mathgroup/archive/2005/May/msg00336.html instead of what you're doing now.
```

### `2026-02-27 09:57 PST`
```
git push to https://github.com/fischman/spirals (and set that as the default upstream)
```

### `2026-02-28 09:52 PST`
```
Add a new type of integers to highlight: products of two primes.
When highlighting those, draw a "triangle" between the two primes and their product.
```

### `2026-03-01 09:41 PST`
```
I want it so that any git commit includes a re-run of ./prompts.py and auto-adds the edited prompts.md into the current commit.
Probably as a pre-commit hook? (or propose alterantive).
If you make a hook, do it in the main repo as .hooks-pre-commit and then symlink from .git/hooks to take effect.
```

### `2026-03-01 09:42 PST`
```
Add a comment to the top of the new hook documenting how to symlink it in new clones.
```
