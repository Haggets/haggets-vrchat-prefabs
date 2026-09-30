# Changelog

## 0.1.0
- Initial release.
- `HAP Frame Time`: exports `HAP/FrameTime`.
- `HAP Gestures`: exports smoothed, override-aware per-gesture weights (`HAP/Gesture/...`).
- `HAP Gaze`: exports `HAP/Gaze/MotionTime` from a synced gaze style.
- `HAP Blink`: random blinking with double (25%) and triple (5%) blinks, synced through a single bool; per-eye overrides.
- Contact interaction modules with built-in receivers: `HAP Head Pat`, `HAP Eye Poke`, `HAP Paw Poke`, `HAP Paw Curl`, `HAP Blush`.
- `HAP Cheek Pull`: smoothed PhysBone stretch.
- `HAP Cheese Slap`: hand/tail cheese-slap game with built-in contacts and slap sounds.
