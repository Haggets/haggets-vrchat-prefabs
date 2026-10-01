# HAP (Haggets Avatar Prefabs)

Modular animator logic for VRChat avatars, mainly used for me to reuse logic across multiple avatars.

## Install

**Through the Creator Companion (recommended):** add the HAP listing URL in _Settings → Packages → Add Repository_, then add **HAP** to your project.

**Manually:** copy this folder to `Packages/com.haggets.hap` inside your Unity project.

Requires VRChat Avatars SDK 3.5+ and VRCFury.

## Modules

Parameters marked **Synced: No** are computed locally on every client from things VRChat already syncs (or from contacts), so they still match for everyone. Most raw contact inputs and other `_`-prefixed or intermediate parameters are internal and left out, except the synced ones, which are listed so you know what each module costs and how it syncs. Expression parameter is the type in the VRC Expression Parameters asset; animator type is what your own controllers read.

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

| Parameter                                 | Animator type | Expression parameter | Synced | Description                                                                                                                                                                                                                                                                                   |
| ----------------------------------------- | ------------- | -------------------- | ------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `HAP/GestureLeftOverride`                 | Float         | Int (not saved)      | Yes    | Forces the left hand to a gesture (`1`–`7`, see above) regardless of the real hand. `0` = no override.                                                                                                                                                                                        |
| `HAP/GestureRightOverride`                | Float         | Int (not saved)      | Yes    | Same as above for the right hand.                                                                                                                                                                                                                                                             |
| `HAP/GestureLeft`                         | Float         | —                    | No     | Current left gesture index (`0`–`7`), taking the override into account.                                                                                                                                                                                                                       |
| `HAP/GestureRight`                        | Float         | —                    | No     | Current right gesture index (`0`–`7`), taking the override into account.                                                                                                                                                                                                                      |
| `HAP/Gesture{Left,Right}/{Gesture}/Proxy` | Float         | —                    | No     | Smoothed 0–1 weight of one gesture on one hand, e.g. `HAP/GestureLeft/Fist/Proxy`. `{Gesture}` is `Neutral`, `Fist`, `HandOpen`, `FingerPoint`, `Victory`, `RockNRoll`, `HandGun` or `ThumbsUp`. Weights cross-fade, so use these instead of `GestureLeft`/`GestureRight` in your animations. |
| `HAP/Gesture{Left,Right}Weight/Proxy`     | Float         | —                    | No     | Smoothed trigger pull (0–1) for that hand. Held at 1 while an override is active.                                                                                                                                                                                                             |

</details>

<details>
<summary><b>HAP Gaze</b></summary>

A simple system for adding different eye gazes on an avatar, allowing the option to have different resting faces that each interact differently with gestures and do not clip with blinking and the like.

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

How it syncs: the blink timing is random, so only the wearer's client decides it. It sets `_HAP/Blink/CanBlink` to true while a blink holds the eyes closed, and remote clients close the eyes for as long as they see it true. The proxies are then smoothed on each client.

| Parameter                | Animator type | Expression parameter | Synced | Description                                                                                                                       |
| ------------------------ | ------------- | -------------------- | ------ | --------------------------------------------------------------------------------------------------------------------------------- |
| `HAP/BlinkLeftOverride`  | Float         | —                    | No     | Set from your own animations. 0 = blink normally, 1 = force the left eye closed.                                                  |
| `HAP/BlinkRightOverride` | Float         | —                    | No     | Same as above for the right eye.                                                                                                  |
| `HAP/BlinkLeft/Proxy`    | Float         | —                    | No     | Smoothed left eyelid closure. 0 = open, 1 = closed. Drive your left blink blendshape from this.                                   |
| `HAP/BlinkRight/Proxy`   | Float         | —                    | No     | Smoothed right eyelid closure. 0 = open, 1 = closed.                                                                              |
| `_HAP/Blink/CanBlink`    | Bool          | Bool (not saved)     | Yes    | Internal. True while a blink is closing the eyes. Written by the wearer's client, followed by remote clients. Costs 1 synced bit. |

</details>

## Contact interactions

Each prefab below contains its VRC Contact Receivers plus the smoothing logic.

After dropping one in, set each receiver's **Root Transform** to the matching bone (head, feet, hands…) and adjust the position and radius for the new avatar.

<details>
<summary><b>HAP Cheek Pull</b></summary>

Adds smoothed cheek pulling behavior, which stretches the face slightly in the direction of the cheek pull.

It reads the PhysBone stretch parameters `HAP/CheekPullLeft_Stretch` and `HAP/CheekPullRight_Stretch`, so set the **Parameter** on your cheek PhysBones to `HAP/CheekPullLeft` and `HAP/CheekPullRight`.

| Parameter                  | Animator type | Expression parameter | Synced | Description                       |
| -------------------------- | ------------- | -------------------- | ------ | --------------------------------- |
| `HAP/CheekPullLeft/Proxy`  | Float         | —                    | No     | Smoothed 0–1 left cheek stretch.  |
| `HAP/CheekPullRight/Proxy` | Float         | —                    | No     | Smoothed 0–1 right cheek stretch. |

</details>

<details>
<summary><b>HAP Cheese Slap</b></summary>

Adds a synced cheese slap system, which allows compatible avatars to cheese your character, as well as allowing you to cheese others.

As it is synced, it will not get desynced for late joiners but it can lead to small jittering when added and removed in quick succession.

The prefab contains:

- **Hand Sender** and **Tail Sender** contact senders. Set their Root Transform to the hand and tail bones.
- **Head Receiver** and **Head Remove Receiver** contact receivers. Set their Root Transform to the head.

A slap only counts when the sender reaches the face quickly. A slow approach is treated as a miss.

No sounds or visuals are included. React to `HAP/CheeseSlap` in your own controller to decide what happens when the avatar gets cheesed (play a slap sound, show the cheese, change the expression…).

How it syncs: every client detects the slap from the contacts on its own, so `HAP/CheeseSlap` changes immediately for everyone who saw it happen. The wearer's client also writes the result to `_HAP/CheeseSlap/Sync`. Remote clients only use that bool to correct themselves: to catch a slap or removal their own detection missed, and to show the right state to late joiners.

| Parameter                      | Animator type | Expression parameter | Synced | Description                                                                                                                                                              |
| ------------------------------ | ------------- | -------------------- | ------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `HAP/CheeseSlap`               | Float         | —                    | No     | 1 while the avatar is cheesed, otherwise 0. Use it as the condition/weight for your cheese visuals.                                                                      |
| `HAP/CheeseSlap/Contact`       | Float         | —                    | No     | Proximity (0–1) from **Head Receiver** to other players' `Cheese`/`cheese` senders. A hit that reaches 0.5 quickly cheeses the avatar.                                   |
| `HAP/CheeseSlap/RemoveContact` | Bool          | —                    | No     | From **Head Remove Receiver**. True while another player's head, hand, muzzle, snout or tail touches the face; removes the cheese if no cheese sender is still touching. |
| `_HAP/CheeseSlap/Sync`         | Bool          | Bool (not saved)     | Yes    | Internal. The wearer's cheesed state, written only by the wearer's client. Remote clients follow it when their own detection disagrees. Costs 1 synced bit.              |

</details>

<details>
<summary><b>HAP Head Pat</b></summary>

Detects hands (yours or other players') patting the head and smooths the result.

| Parameter           | Animator type | Expression parameter | Synced | Description                      |
| ------------------- | ------------- | -------------------- | ------ | -------------------------------- |
| `HAP/HeadPat/Proxy` | Float         | —                    | No     | Smoothed 0–1 amount of head pat. |

</details>

<details>
<summary><b>HAP Eye Poke</b></summary>

Detects fingers (yours or other players') near each eye and smooths the result.

| Parameter                | Animator type | Expression parameter | Synced | Description                                        |
| ------------------------ | ------------- | -------------------- | ------ | -------------------------------------------------- |
| `HAP/EyePokeLeft/Proxy`  | Float         | —                    | No     | Smoothed 0–1 amount of eye poke on the left side.  |
| `HAP/EyePokeRight/Proxy` | Float         | —                    | No     | Smoothed 0–1 amount of eye poke on the right side. |

</details>

<details>
<summary><b>HAP Paw Poke</b></summary>

Detects fingers (yours or other players') poking each paw and smooths the result.

| Parameter                | Animator type | Expression parameter | Synced | Description                                        |
| ------------------------ | ------------- | -------------------- | ------ | -------------------------------------------------- |
| `HAP/PawPokeLeft/Proxy`  | Float         | —                    | No     | Smoothed 0–1 amount of paw poke on the left side.  |
| `HAP/PawPokeRight/Proxy` | Float         | —                    | No     | Smoothed 0–1 amount of paw poke on the right side. |

</details>

<details>
<summary><b>HAP Paw Curl</b></summary>

Curls each paw when your own foot touches it, and smooths the result.

| Parameter                | Animator type | Expression parameter | Synced | Description                                        |
| ------------------------ | ------------- | -------------------- | ------ | -------------------------------------------------- |
| `HAP/PawCurlLeft/Proxy`  | Float         | —                    | No     | Smoothed 0–1 amount of paw curl on the left side.  |
| `HAP/PawCurlRight/Proxy` | Float         | —                    | No     | Smoothed 0–1 amount of paw curl on the right side. |

</details>

<details>
<summary><b>HAP Blush</b></summary>

Smoothens a blush amount you drive yourself. You can make contacts drive `HAP/Blush/Input` and Proxy will output a smoothed value based on that.

| Parameter         | Animator type | Expression parameter | Synced | Description                                                                |
| ----------------- | ------------- | -------------------- | ------ | -------------------------------------------------------------------------- |
| `HAP/Blush/Input` | Float         | —                    | No     | Set from your own contacts or animations. 0–1 target blush amount.         |
| `HAP/Blush/Proxy` | Float         | —                    | No     | Smoothed 0–1 blush amount. Drive your blush blendshape/material from this. |

</details>
