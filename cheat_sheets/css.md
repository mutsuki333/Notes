# CSS Cheat Sheet

## Basics

## Utils

### Image align vertically and horizontally

```sass
.container
  position: relative
  height: 40vh // can be anything
  img
    max-height: 100%
    max-width: 100%
    width: auto
    height: auto
    position: absolute
    top: 0
    bottom: 0
    left: 0
    right: 0
    margin: auto
```

### Image gray scale

```sass
img#grey
  opacity: 0.7
  -webkit-filter: grayscale(100%)
  -moz-filter: grayscale(100%)
  -o-filter: grayscale(100%)
  -ms-filter: grayscale(100%)
  filter: grayscale(100%)
```

### Cursor

```css
.alias {cursor: alias;}
.all-scroll {cursor: all-scroll;}
.auto {cursor: auto;}
.cell {cursor: cell;}
.context-menu {cursor: context-menu;}
.col-resize {cursor: col-resize;}
.copy {cursor: copy;}
.crosshair {cursor: crosshair;}
.default {cursor: default;}
.e-resize {cursor: e-resize;}
.ew-resize {cursor: ew-resize;}
.grab {cursor: grab;}
.grabbing {cursor: grabbing;}
.help {cursor: help;}
.move {cursor: move;}
.n-resize {cursor: n-resize;}
.ne-resize {cursor: ne-resize;}
.nesw-resize {cursor: nesw-resize;}
.ns-resize {cursor: ns-resize;}
.nw-resize {cursor: nw-resize;}
.nwse-resize {cursor: nwse-resize;}
.no-drop {cursor: no-drop;}
.none {cursor: none;}
.not-allowed {cursor: not-allowed;}
.pointer {cursor: pointer;}
.progress {cursor: progress;}
.row-resize {cursor: row-resize;}
.s-resize {cursor: s-resize;}
.se-resize {cursor: se-resize;}
.sw-resize {cursor: sw-resize;}
.text {cursor: text;}
.url {cursor: url(myBall.cur),auto;}
.w-resize {cursor: w-resize;}
.wait {cursor: wait;}
.zoom-in {cursor: zoom-in;}
.zoom-out {cursor: zoom-out;}
```
