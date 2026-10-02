# HAP (Haggets Avatar Prefabs)

Modular animator logic for VRChat avatars, mainly used for me to reuse logic across multiple avatars.

## Install

**Through the Creator Companion (recommended):** add the HAP listing URL in _Settings → Packages → Add Repository_, then add **HAP** to your project.

**Manually:** copy this folder to `Packages/com.haggets.hap` inside your Unity project.

Requires VRChat Avatars SDK 3.5+ and VRCFury.

## Modules

<details>
<summary><h3>HAP Frame Time</h3></summary>

Adds a **Frame Time system** to the avatar, which is required by most other modules inside and outside of these prefabs.

It is mainly required for smoothing out parameters, so things like ear puppeteering is smooth.

#### Instructions

1. Drag and drop the prefab into the avatar's hierarchy.

#### Output Animator Parameters

| Property        | Animator Type | Description                                                                                                                              |
| --------------- | ------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| `HAP/FrameTime` | Float         | How long the previous frame took, scaled ×10 (about 0.11 at 90 FPS). Use it as the blend weight to make smoothing frame-rate independent |

</details>

---

<details>
<summary><h3>HAP Gestures</h3></summary>

> Requires **HAP Frame Time**.

Adds a **custom gesture system** that can interact with the blink module and any other face interactions. The way it's setup allows for different expressions to interact with eachother gracefully, allowing the mix of eye and mouth shapes independently and smoothly.

Another controller is also included that excludes the Override. Useful for hand gestures where you may want the smoothed hand gestures but not forcing the hand shapes.

#### Instructions

1. Drag and drop the prefab into the avatar's hierarchy.
2. Use the animator parameters `HAP/GestureLeft/*/Proxy` and `HAP/GestureRight/*/Proxy` to drive your gesture animations, instead of `GestureLeft` and `GestureRight`.
3. Use the animator parameters `HAP/GestureLeftWeight/Proxy` and `HAP/GestureRightWeight/Proxy` for the trigger pull.
4. Optionally, add menu controls that set `HAP/GestureLeft/Override` and `HAP/GestureRight/Override` to allow forced gesture.

Gesture order is `0` Neutral, `1` Fist, `2` HandOpen, `3` FingerPoint, `4` Victory, `5` RockNRoll, `6` HandGun, `7` ThumbsUp.

#### Included Expression Parameters

| Property                    | Animator Type | Expression Type | Synced | Description                                                                             |
| --------------------------- | ------------- | --------------- | ------ | --------------------------------------------------------------------------------------- |
| `HAP/GestureLeft/Override`  | Float         | Int             | ✔      | Forces a left handed gesture (`1`–`7`) regardless of the real hand. `0` = no override.  |
| `HAP/GestureRight/Override` | Float         | Int             | ✔      | Forces a right handed gesture (`1`–`7`) regardless of the real hand. `0` = no override. |

#### Output Animator Parameters

| Property                             | Animator Type | Description                                                                           |
| ------------------------------------ | ------------- | ------------------------------------------------------------------------------------- |
| `HAP/GestureLeft/Neutral/Proxy`      | Float         | Smoothed 0–1 weight of the Neutral gesture on the left hand.                          |
| `HAP/GestureLeft/Fist/Proxy`         | Float         | Smoothed 0–1 weight of the Fist gesture on the left hand.                             |
| `HAP/GestureLeft/HandOpen/Proxy`     | Float         | Smoothed 0–1 weight of the HandOpen gesture on the left hand.                         |
| `HAP/GestureLeft/FingerPoint/Proxy`  | Float         | Smoothed 0–1 weight of the FingerPoint gesture on the left hand.                      |
| `HAP/GestureLeft/Victory/Proxy`      | Float         | Smoothed 0–1 weight of the Victory gesture on the left hand.                          |
| `HAP/GestureLeft/RockNRoll/Proxy`    | Float         | Smoothed 0–1 weight of the RockNRoll gesture on the left hand.                        |
| `HAP/GestureLeft/HandGun/Proxy`      | Float         | Smoothed 0–1 weight of the HandGun gesture on the left hand.                          |
| `HAP/GestureLeft/ThumbsUp/Proxy`     | Float         | Smoothed 0–1 weight of the ThumbsUp gesture on the left hand.                         |
| `HAP/GestureRight/Neutral/Proxy`     | Float         | Smoothed 0–1 weight of the Neutral gesture on the right hand.                         |
| `HAP/GestureRight/Fist/Proxy`        | Float         | Smoothed 0–1 weight of the Fist gesture on the right hand.                            |
| `HAP/GestureRight/HandOpen/Proxy`    | Float         | Smoothed 0–1 weight of the HandOpen gesture on the right hand.                        |
| `HAP/GestureRight/FingerPoint/Proxy` | Float         | Smoothed 0–1 weight of the FingerPoint gesture on the right hand.                     |
| `HAP/GestureRight/Victory/Proxy`     | Float         | Smoothed 0–1 weight of the Victory gesture on the right hand.                         |
| `HAP/GestureRight/RockNRoll/Proxy`   | Float         | Smoothed 0–1 weight of the RockNRoll gesture on the right hand.                       |
| `HAP/GestureRight/HandGun/Proxy`     | Float         | Smoothed 0–1 weight of the HandGun gesture on the right hand.                         |
| `HAP/GestureRight/ThumbsUp/Proxy`    | Float         | Smoothed 0–1 weight of the ThumbsUp gesture on the right hand.                        |
| `HAP/GestureLeftWeight/Proxy`        | Float         | Smoothed trigger pull (0–1) for the left hand. Held at 1 while an override is active  |
| `HAP/GestureRightWeight/Proxy`       | Float         | Smoothed trigger pull (0–1) for the right hand. Held at 1 while an override is active |

</details>

---

<details>
<summary><h3>HAP Blink</h3></summary>

> Requires **HAP Frame Time**.

Adds a **custom blink system** separate from the VRChat system, with a single double and triple blink at random-ish intervals with a single synced boolean.

It features a Override parameter which is used to force close the eyes if required by animations. It also integrated neatly with HAP Gestures

#### Instructions

1. Drag and drop the prefab into the avatar's hierarchy.
2. Use the animator parameters `HAP/BlinkLeft/Proxy` and `HAP/BlinkRight/Proxy` to drive the blink blendshapes.
3. Optionally, set the animator parameters `HAP/BlinkLeft/Override` and `HAP/BlinkRight/Override` from your own animations to force the eyes closed.

#### Included Expression Parameters

| Property              | Animator Type | Expression Type | Synced | Description                                               |
| --------------------- | ------------- | --------------- | ------ | --------------------------------------------------------- |
| `_HAP/Blink/CanBlink` | Bool          | Bool            | ✔      | Internal. Syncs the blink state between local and remote. |

#### Output Animator Parameters

| Property               | Animator Type | Description                                         |
| ---------------------- | ------------- | --------------------------------------------------- |
| `HAP/BlinkLeft/Proxy`  | Float         | Smoothed left eyelid closure. 0 = open, 1 = closed  |
| `HAP/BlinkRight/Proxy` | Float         | Smoothed right eyelid closure. 0 = open, 1 = closed |

#### Input Animator Parameters

| Property                  | Animator Type | Description                                        |
| ------------------------- | ------------- | -------------------------------------------------- |
| `HAP/BlinkLeft/Override`  | Float         | 0 = blink normally, 1 = force the left eye closed  |
| `HAP/BlinkRight/Override` | Float         | 0 = blink normally, 1 = force the right eye closed |

</details>

## Contact interactions

<details>
<summary><h3>HAP Cheek Pull</h3></summary>

> Requires **HAP Frame Time**.

Adds **smoothed cheek pulling** behavior, which can be used to stretch the face slightly in the direction of whichever cheek is pulled.

#### Instructions

1. Drag and drop the prefab into the avatar's hierarchy.
2. Set the **Parameter** of your cheek PhysBones to `HAP/CheekPullLeft` and `HAP/CheekPullRight`.
3. Use the animator parameters `HAP/CheekPullLeft/Proxy` and `HAP/CheekPullRight/Proxy` to drive the face stretch.

#### Output Animator Parameters

| Property                   | Animator Type | Description                      |
| -------------------------- | ------------- | -------------------------------- |
| `HAP/CheekPullLeft/Proxy`  | Float         | Smoothed 0–1 left cheek stretch  |
| `HAP/CheekPullRight/Proxy` | Float         | Smoothed 0–1 right cheek stretch |

</details>

---

<details>
<summary><h3>HAP Cheese Slap</h3></summary>

Adds a **synced cheese slap system**, which allows compatible avatars to cheese your character, as well as allowing you to cheese others.

As it is synced, it will not get desynced for late joiners but it can lead to small jittering when added and removed in quick succession.

A slap only counts when the sender reaches the face quickly. A slow approach is treated as a miss.

How it syncs: every client detects the slap from the contacts on its own, so `HAP/CheeseSlap` changes immediately for everyone who saw it happen. The wearer's client also writes the result to `_HAP/CheeseSlap/Sync`. Remote clients only use that bool to correct themselves: to catch a slap or removal their own detection missed, and to show the right state to late joiners.

#### Instructions

1. Drag and drop the prefab into the avatar's hierarchy.
2. Set the **Root Transform** of the **Hand Sender** contact sender to the hand.
3. Set the **Root Transform** of the **Head Receiver** and **Head Remove Receiver** contact receivers to the head, then adjust their position and radius.
4. Use the animator parameter `HAP/CheeseSlap` in your own controller to decide what happens when the avatar gets cheesed (play a slap sound, show the cheese, change the expression…). No sounds or visuals are included.

#### Included Expression Parameters

| Property               | Animator Type | Expression Type | Synced | Description                                                                                                                                                           |
| ---------------------- | ------------- | --------------- | ------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `_HAP/CheeseSlap/Sync` | Bool          | Bool            | ✔      | Internal. The wearer's cheesed state, written only by the wearer's client. Remote clients follow it when their own detection disagrees. Not saved, costs 1 synced bit |

#### Output Animator Parameters

| Property                       | Animator Type | Description                                                                                                                                                             |
| ------------------------------ | ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `HAP/CheeseSlap`               | Float         | 1 while the avatar is cheesed, otherwise 0                                                                                                                              |
| `HAP/CheeseSlap/Contact`       | Float         | Proximity (0–1) from **Head Receiver** to other players' `Cheese`/`cheese` senders. A hit that reaches 0.5 quickly cheeses the avatar                                   |
| `HAP/CheeseSlap/RemoveContact` | Bool          | From **Head Remove Receiver**. True while another player's head, hand, muzzle, snout or tail touches the face; removes the cheese if no cheese sender is still touching |

</details>

---

<details>
<summary><h3>HAP Head Pat</h3></summary>

> Requires **HAP Frame Time**.

Adds **smooth head pat detection** from hands (yours or other players').

#### Instructions

1. Drag and drop the prefab into the avatar's hierarchy.
2. Set the **Root Transform** of the contact receiver to the head, then adjust its position and radius.
3. Use the animator parameter `HAP/HeadPat/Proxy`.

#### Output Animator Parameters

| Property            | Animator Type | Description                     |
| ------------------- | ------------- | ------------------------------- |
| `HAP/HeadPat/Proxy` | Float         | Smoothed 0–1 amount of head pat |

</details>

---

<details>
<summary><h3>HAP Eye Poke</h3></summary>

> Requires **HAP Frame Time**.

Adds **smooth eye poke detection** from fingers (yours or other players') near each eye.

#### Instructions

1. Drag and drop the prefab into the avatar's hierarchy.
2. Set the **Root Transform** of the contact receivers to the head, then position them over the eyes.
3. Use the animator parameters `HAP/EyePokeLeft/Proxy` and `HAP/EyePokeRight/Proxy`.

#### Output Animator Parameters

| Property                 | Animator Type | Description                                       |
| ------------------------ | ------------- | ------------------------------------------------- |
| `HAP/EyePokeLeft/Proxy`  | Float         | Smoothed 0–1 amount of eye poke on the left side  |
| `HAP/EyePokeRight/Proxy` | Float         | Smoothed 0–1 amount of eye poke on the right side |

</details>

---

<details>
<summary><h3>HAP Paw Poke</h3></summary>

> Requires **HAP Frame Time**.

Adds **smooth paw poke detection** from fingers (yours or other players') poking each paw.

#### Instructions

1. Drag and drop the prefab into the avatar's hierarchy.
2. Set the **Root Transform** of the contact receivers to the feet, then position them over the paws.
3. Use the animator parameters `HAP/PawPokeLeft/Proxy` and `HAP/PawPokeRight/Proxy`.

#### Output Animator Parameters

| Property                 | Animator Type | Description                                       |
| ------------------------ | ------------- | ------------------------------------------------- |
| `HAP/PawPokeLeft/Proxy`  | Float         | Smoothed 0–1 amount of paw poke on the left side  |
| `HAP/PawPokeRight/Proxy` | Float         | Smoothed 0–1 amount of paw poke on the right side |

</details>

---

<details>
<summary><h3>HAP Paw Curl</h3></summary>

> Requires **HAP Frame Time**.

Adds a **smooth paw curl** that triggers when your own foot touches the paw.

#### Instructions

1. Drag and drop the prefab into the avatar's hierarchy.
2. Set the **Root Transform** of the contact receivers to the feet, then position them over the paws.
3. Use the animator parameters `HAP/PawCurlLeft/Proxy` and `HAP/PawCurlRight/Proxy`.

#### Output Animator Parameters

| Property                 | Animator Type | Description                                       |
| ------------------------ | ------------- | ------------------------------------------------- |
| `HAP/PawCurlLeft/Proxy`  | Float         | Smoothed 0–1 amount of paw curl on the left side  |
| `HAP/PawCurlRight/Proxy` | Float         | Smoothed 0–1 amount of paw curl on the right side |

</details>

---

<details>
<summary><h3>HAP Blush</h3></summary>

> Requires **HAP Frame Time**.

Adds a **smoothed blush amount** you drive yourself.

#### Instructions

1. Drag and drop the prefab into the avatar's hierarchy.
2. Drive the animator parameter `HAP/Blush/Input` from your own contacts or animations.
3. Use the animator parameter `HAP/Blush/Proxy` to drive your blush blendshape or material.

#### Output Animator Parameters

| Property          | Animator Type | Description               |
| ----------------- | ------------- | ------------------------- |
| `HAP/Blush/Proxy` | Float         | Smoothed 0–1 blush amount |

#### Input Animator Parameters

| Property          | Animator Type | Description             |
| ----------------- | ------------- | ----------------------- |
| `HAP/Blush/Input` | Float         | 0–1 target blush amount |

</details>
