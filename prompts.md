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

### `2026-03-01 09:44 PST`
```
Looks like the new shift-8 shortcut doesn't work (shift-1..7 still work). Don't git commit until I approve.
```

### `2026-03-01 09:45 PST`
```
git commit and push
```

### `2026-03-01 09:48 PST`
```
Change default view on load to #golden,semiprimes,108
```

### `2026-03-01 10:01 PST`
```
Add to the header of the help modal a right-aligned github icon (that doesn't change the height of the header) that links to https://github.com/fischman/spirals
```

### `2026-03-02 11:23 PST`
```
Add a new spiral type: Hilbert space-filling curve.
Instead of zoom changing the field of view, make it iterate hilbert iterations, making the length of the curve inside the 1x1 square arbitrarily large as the zoom grows.
```

### `2026-03-02 12:46 PST`
```
Bug: https://spiral.exe.xyz:8000/index.html#hilbert,primes,7 for example has the hilbert curve at the top-right quarter of the screen with yellow dots showing on the entire screen.
(when you have a fix, amend previous commit with it)
```

### `2026-03-02 12:47 PST`
```
Continue, but also https://spiral.exe.xyz:8000/index.html#golden,primes,121 is totally busted (points don't lie on the curve). I suspect all the spirals are broken this way.
```

### `2026-03-02 12:51 PST`
```
Are you clamping zoom level on hilbert? Don't. 
(amend previous commit)
```

### `2026-03-02 12:55 PST`
```
Hilbert now looks good, but other spiral types act much worse during zoom since now they "spin" around the canvas. Restore previous behavior where the center was fixed during zoom, amending previous commit.
```

### `2026-03-02 13:01 PST`
```
Webapp is sluggish at large zooms. I suspect recomputation. Propose a way to confirm this hypothesis.
```

### `2026-03-02 13:01 PST`
```
yes
```

### `2026-03-02 13:01 PST`
```
continue but don't git commit until I say so
```

### `2026-03-02 13:04 PST`
```
ok, revert the timing code with git reset --hard HEAD
Then propose improvement to render time.
```

### `2026-03-02 13:06 PST`
```
do the first option, at least for now.
(apply to all spiral types, not just Hilbert)
```

### `2026-03-02 14:55 PST`
```
ok, I committed that.
What's up w/ the very-faint concentric circles? I only just now noticed them but I don't think they're new.
```

### `2026-03-02 14:56 PST`
```
they're not useful. Drop them.
```

### `2026-03-02 14:58 PST`
```
go ahead and commit
```

### `2026-03-02 14:59 PST`
```
performance on https://spiral.exe.xyz:8000/index.html?v=1#hilbert,squares,11 is terrible. Quantify and propose fix
```

### `2026-03-02 15:01 PST`
```
Yes
```

### `2026-03-02 15:14 PST`
```
make up/down arrows do the zoom-scroll, too.
```

### `2026-03-02 15:16 PST`
```
Show a spinner overlaid on top of the canvas while recalculating for any view change (spiral/dataset/zoom change).
```

### `2026-03-02 15:23 PST`
```
With hilbert,primes visible, going from order 10 to 11 is quite slow and shows in console:
[Violation] 'mouseleave' handler took 1456ms
Also the spinner doesn't show during this transition.
```

### `2026-03-02 15:27 PST`
```
Spinner is still not showing during the 10->11 transition, and now I see: 
[Violation] 'requestAnimationFrame' handler took 1329ms

I'm less concerned about the "Violation" and more concerned about the 1.3s delay.
```
