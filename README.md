# HAP (Haggets Avatar Prefabs)

Modular animator logic for VRChat avatars, mainly used for me to reuse logic across multiple avatars.

## Install

**Through the Creator Companion (recommended):** add the HAP listing URL in _Settings → Packages → Add Repository_, then add **HAP** to your project.

**Manually:** copy this folder to `Packages/com.haggets.hap` inside your Unity project.

Requires VRChat Avatars SDK 3.5+ and VRCFury.

## Modules

Parameters marked **Synced: No** are computed locally on every client from things VRChat already syncs (or from contacts), so they still match for everyone. Raw contact inputs and other `_`-prefixed or intermediate parameters are internal and left out. Expression parameter is the type in the VRC Expression Parameters asset; animator type is what your own controllers read.

<details>
<summary><b>HAP Frame Time</b></summary>

Adds a Frame time system to the avatar, which is required by most other modules inside and outside of these prefabs.

It is mainly required for smoothing out parameters, so things like ear puppeteering is smooth.

| Parameter       | Animator type | Expression parameter | Synced | Description                                                                                                                               |
| --------------- | ------------- | -------------------- | ------ | ----------------------------------------------------------------------------------------------------------------------------------------- |
| `HAP/FrameTime` | Float         | —                    | No     | How long the previous frame took, scaled ×10 (about 0.11 at 90 FPS). Use it as the blend weight to make smoothing frame-rate independent. |

</details>

<details>
<summary><b>HAP Gestures</b></summary>

Adds a custom gesture system that interacts with the blink and gaze module. The way it's setup allows for different expressions to interact with eachother gracefully, allowing the mix of eye and mouth shapes independently and smoothly without causing clipping (If tuned right).

It also smoothens the hand gestures, allowing for less linear hand gestures transitions.

Gesture order is `0` Neutral, `1` Fist, `2` HandOpen, `3` FingerPoint, `4` Victory, `5` RockNRoll, `6` HandGun, `7` ThumbsUp. The Left and Right override menus offer every gesture except Neutral.

| Parameter                                  | Animator type | Expression parameter | Synced | Description                                                                                                                                                                                                                                                                                    |
| ------------------------------------------ | ------------- | -------------------- | ------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `HAP/Gesture/LeftOverride`                 | Float         | Int (not saved)      | Yes    | Forces the left hand to a gesture (`1`–`7`, see above) regardless of the real hand. `0` = no override.                                                                                                                                                                                         |
| `HAP/Gesture/RightOverride`                | Float         | Int (not saved)      | Yes    | Same as above for the right hand.                                                                                                                                                                                                                                                              |
| `HAP/Gesture/Left`                         | Float         | —                    | No     | Current left gesture index (`0`–`7`), taking the override into account.                                                                                                                                                                                                                        |
| `HAP/Gesture/Right`                        | Float         | —                    | No     | Current right gesture index (`0`–`7`), taking the override into account.                                                                                                                                                                                                                       |
| `HAP/Gesture/{Left,Right}/{Gesture}/Proxy` | Float         | —                    | No     | Smoothed 0–1 weight of one gesture on one hand, e.g. `HAP/Gesture/Left/Fist/Proxy`. `{Gesture}` is `Neutral`, `Fist`, `HandOpen`, `FingerPoint`, `Victory`, `RockNRoll`, `HandGun` or `ThumbsUp`. Weights cross-fade, so use these instead of `GestureLeft`/`GestureRight` in your animations. |
| `HAP/Gesture/{Left,Right}Weight/Proxy`     | Float         | —                    | No     | Smoothed trigger pull (0–1) for that hand. Held at 1 while an override is active.                                                                                                                                                                                                              |

</details>

<details>
<summary><b>HAP Gaze</b></summary>

A simple system for adding different eye gazes on an avatar, allowing the option to have different resting faces that each interact differently with gestures and do not clip with blinking and the like.

Menu styles: `0` Default, `1` Relaxed, `2` Squinty, `3` Hostile, `4` Worried, `5` Droopy, `6` Smug.

| Parameter             | Animator type | Expression parameter     | Synced | Description                                                                                                                 |
| --------------------- | ------------- | ------------------------ | ------ | --------------------------------------------------------------------------------------------------------------------------- |
| `HAP/Gaze/Style`      | Float         | Int (saved)              | Yes    | Selected gaze style (`0`–`6`, see above).                                                                                   |
| `HAP/Gaze/Influence`  | Float         | Float (saved, default 1) | Yes    | Menu radial, 0–1. How strongly the gaze style affects the face; use it as a blend weight in your gaze animations.           |
| `HAP/Gaze/MotionTime` | Float         | —                        | No     | `Style` remapped to 0–1 (style 0 → 0, style 6 → 1). Put it on a Motion Time field to drive one clip that holds every style. |

</details>

<details>
<summary><b>HAP Blink</b></summary>

Custom blink system separate from the VRChat system, featuring network synced smoothed sinle, double and triple blink at random-ish intervals with a single synced boolean.

It also features a Override parameter which is used to force close the eyes if required by animations.

| Parameter                 | Animator type | Expression parameter     | Synced | Description                                                                                     |
| ------------------------- | ------------- | ------------------------ | ------ | ----------------------------------------------------------------------------------------------- |
| `HAP/Blink/Enabled`       | Bool          | Bool (saved, default on) | Yes    | Menu toggle. Turns random blinking on or off.                                                   |
| `HAP/Blink/LeftOverride`  | Float         | —                        | No     | Set from your own animations. 0 = blink normally, 1 = force the left eye closed.                |
| `HAP/Blink/RightOverride` | Float         | —                        | No     | Same as above for the right eye.                                                                |
| `HAP/Blink/Left/Proxy`    | Float         | —                        | No     | Smoothed left eyelid closure. 0 = open, 1 = closed. Drive your left blink blendshape from this. |
| `HAP/Blink/Right/Proxy`   | Float         | —                        | No     | Smoothed right eyelid closure. 0 = open, 1 = closed.                                            |

</details>

## Contact interactions

Each prefab below contains its VRC Contact Receivers plus the smoothing logic.

After dropping one in, set each receiver's **Root Transform** to the matching bone (head, feet, hands…) and adjust the position and radius for the new avatar.

<details>
<summary><b>HAP Cheek Pull</b></summary>

Adds smoothed cheek pulling behavior, which stretches the face slightly in the direction of the cheek pull.

It reads the PhysBone stretch parameters `HAP/CheekPull/Left_Stretch` and `HAP/CheekPull/Right_Stretch`, so set the **Parameter** on your cheek PhysBones to `HAP/CheekPull/Left` and `HAP/CheekPull/Right`.

| Parameter                   | Animator type | Expression parameter     | Synced | Description                                 |
| --------------------------- | ------------- | ------------------------ | ------ | ------------------------------------------- |
| `HAP/CheekPull/Enabled`     | Float         | Bool (saved, default on) | Yes    | Menu toggle. Turns cheek pulling on or off. |
| `HAP/CheekPull/Left/Proxy`  | Float         | —                        | No     | Smoothed 0–1 left cheek stretch.            |
| `HAP/CheekPull/Right/Proxy` | Float         | —                        | No     | Smoothed 0–1 right cheek stretch.           |

</details>

<details>
<summary><b>HAP Cheese Slap</b></summary>

Adds a synced cheese slap system, which allows compatible avatars to cheese your character, as well as allowing you to cheese others.

As it is synced, it will not get desynced for late joiners but it can lead to small jittering when added and removed in quick succession.

The prefab contains:

- **Hand Sender** and **Tail Sender** contact senders. Set their Root Transform to the hand and tail bones.
- **Head Receiver** and **Head Remove Receiver** contact receivers. Set their Root Transform to the head.
- **Slap Audio**, which plays one of three slap sounds. An Armature Link keeps the prefab attached to the Head bone, so the audio plays from the face.

A slap only counts when the sender reaches the face quickly. A slow approach is treated as a miss.

| Parameter                   | Animator type | Expression parameter     | Synced | Description                                                                                         |
| --------------------------- | ------------- | ------------------------ | ------ | --------------------------------------------------------------------------------------------------- |
| `HAP/CheeseSlap/HandSender` | Float         | Bool (saved, default on) | Yes    | Menu toggle. Lets your hand cheese others.                                                          |
| `HAP/CheeseSlap/TailSender` | Float         | Bool (saved, default on) | Yes    | Menu toggle. Lets your tail cheese others.                                                          |
| `HAP/CheeseSlap/Receiver`   | Float         | Bool (saved, default on) | Yes    | Menu toggle. Lets others cheese you.                                                                |
| `HAP/CheeseSlap`            | Float         | —                        | No     | 1 while the avatar is cheesed, otherwise 0. Use it as the condition/weight for your cheese visuals. |

</details>

<details>
<summary><b>HAP Head Pat</b></summary>

Detects hands (yours or other players') patting the head and smooths the result.

| Parameter             | Animator type | Expression parameter     | Synced | Description                                      |
| --------------------- | ------------- | ------------------------ | ------ | ------------------------------------------------ |
| `HAP/HeadPat/Enabled` | Float         | Bool (saved, default on) | Yes    | Menu toggle. Turns head pat detection on or off. |
| `HAP/HeadPat/Proxy`   | Float         | —                        | No     | Smoothed 0–1 amount of head pat.                 |

</details>

<details>
<summary><b>HAP Eye Poke</b></summary>

Detects fingers (yours or other players') near each eye and smooths the result.

| Parameter                 | Animator type | Expression parameter     | Synced | Description                                        |
| ------------------------- | ------------- | ------------------------ | ------ | -------------------------------------------------- |
| `HAP/EyePoke/Enabled`     | Float         | Bool (saved, default on) | Yes    | Menu toggle. Turns eye poke detection on or off.   |
| `HAP/EyePoke/Left/Proxy`  | Float         | —                        | No     | Smoothed 0–1 amount of eye poke on the left side.  |
| `HAP/EyePoke/Right/Proxy` | Float         | —                        | No     | Smoothed 0–1 amount of eye poke on the right side. |

</details>

<details>
<summary><b>HAP Paw Poke</b></summary>

Detects fingers (yours or other players') poking each paw and smooths the result.

| Parameter                 | Animator type | Expression parameter     | Synced | Description                                        |
| ------------------------- | ------------- | ------------------------ | ------ | -------------------------------------------------- |
| `HAP/PawPoke/Enabled`     | Float         | Bool (saved, default on) | Yes    | Menu toggle. Turns paw poke detection on or off.   |
| `HAP/PawPoke/Left/Proxy`  | Float         | —                        | No     | Smoothed 0–1 amount of paw poke on the left side.  |
| `HAP/PawPoke/Right/Proxy` | Float         | —                        | No     | Smoothed 0–1 amount of paw poke on the right side. |

</details>

<details>
<summary><b>HAP Paw Curl</b></summary>

Curls each paw when your own foot touches it, and smooths the result.

| Parameter                 | Animator type | Expression parameter     | Synced | Description                                        |
| ------------------------- | ------------- | ------------------------ | ------ | -------------------------------------------------- |
| `HAP/PawCurl/Enabled`     | Float         | Bool (saved, default on) | Yes    | Menu toggle. Turns paw curling on or off.          |
| `HAP/PawCurl/Left/Proxy`  | Float         | —                        | No     | Smoothed 0–1 amount of paw curl on the left side.  |
| `HAP/PawCurl/Right/Proxy` | Float         | —                        | No     | Smoothed 0–1 amount of paw curl on the right side. |

</details>

<details>
<summary><b>HAP Blush</b></summary>

Adds blushing when other players touch the head, belly or feet, or when your own right index finger touches the finger contact, smoothed into one value.

| Parameter          | Animator type | Expression parameter     | Synced | Description                                                                |
| ------------------ | ------------- | ------------------------ | ------ | -------------------------------------------------------------------------- |
| `HAP/Blush/Head`   | Float         | Bool (saved, default on) | Yes    | Menu toggle. Allow the head contact to cause blushing.                     |
| `HAP/Blush/Belly`  | Float         | Bool (saved, default on) | Yes    | Menu toggle. Allow the belly contact to cause blushing.                    |
| `HAP/Blush/Feet`   | Float         | Bool (saved, default on) | Yes    | Menu toggle. Allow the feet contacts to cause blushing.                    |
| `HAP/Blush/Finger` | Float         | Bool (saved, default on) | Yes    | Menu toggle. Allow the finger contact to cause blushing.                   |
| `HAP/Blush/Proxy`  | Float         | —                        | No     | Smoothed 0–1 blush amount. Drive your blush blendshape/material from this. |

</details>
