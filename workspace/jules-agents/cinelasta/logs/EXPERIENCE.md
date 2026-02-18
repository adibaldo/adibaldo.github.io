# Cinelasta Experience Log

## 2026-02-18: Pattern Over Stuff
- **Waveform**: `visualizeAudio` from `@remotion/media-utils` provides `number[]` samples which can be used to generate SVG paths. Mirrored path works best for symmetrical waveforms.
- **Lyrics**: Without timestamps, linear interpolation based on total duration and line count works for slow, ambient tracks, but requires careful spacing.
- **Rendering**: Heavy compositions (AudioViz + Filters) require significant compute time. Split rendering or optimized hardware is needed for full tracks (>3min).
