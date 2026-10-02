# HVP (Haggets VRChat Prefabs)

Modular animator logic for VRChat avatars, mainly used for me to reuse logic across multiple avatars.

## Install

**Through the Creator Companion (recommended):** add the HVP listing URL in _Settings → Packages → Add Repository_, then add **HVP** to your project.

**Manually:** copy this folder to `Packages/com.haggets.hvp` inside your Unity project.

Requires VRChat Avatars SDK 3.5+ and VRCFury.

## Modules

<details>
<summary><h3>HVP Frame Time</h3></summary>

Adds a **Frame Time system** to the avatar, which is required by most other modules inside and outside of these prefabs.

It is mainly required for smoothing out parameters, so things like ear puppeteering is smooth.

#### Instructions

1. Drag and drop the prefab into the avatar's hierarchy.

#### Output Animator Parameters

| Property        | Animator Type | Description                                                                                                                              |
| --------------- | ------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| `HVP/FrameTime` | Float         | How long the previous frame took, scaled ×10 (about 0.11 at 90 FPS). Use it as the blend weight to make smoothing frame-rate independent |

</details>

---

<details>
<summary><h3>HVP Gestures</h3></summary>

> Requires **HVP Frame Time**.

Adds a **custom gesture system** that can interact with the blink module and any other face interactions. The way it's setup allows for different expressions to interact with eachother gracefully, allowing the mix of eye and mouth shapes independently and smoothly.

Another controller is also included, on the Gesture layer, that excludes the Override and the Quest controllers toggle. Useful for hand gestures where you may want the smoothed hand gestures but not forcing the hand shapes.

#### Instructions

1. Drag and drop the prefab into the avatar's hierarchy.
2. Use the animator parameters `HVP/GestureLeft/*/Proxy` and `HVP/GestureRight/*/Proxy` to drive your gesture animations, instead of `GestureLeft` and `GestureRight`.
3. Use the animator parameters `HVP/GestureLeftWeight/Proxy` and `HVP/GestureRightWeight/Proxy` for the trigger pull.
4. Optionally, add menu controls that set `HVP/GestureLeft/Override` and `HVP/GestureRight/Override` to allow forced gesture.
5. Optionally, add a menu toggle for `HVP/QuestControllers/Enabled` to ignore the Victory/Peace gesture.

Gesture order is `0` Neutral, `1` Fist, `2` HandOpen, `3` FingerPoint, `4` Victory, `5` RockNRoll, `6` HandGun, `7` ThumbsUp.

#### Included Expression Parameters

| Property                       | Animator Type | Expression Type | Synced | Description                                                                             |
| ------------------------------ | ------------- | --------------- | ------ | --------------------------------------------------------------------------------------- |
| `HVP/GestureLeft/Override`     | Float         | Int             | ✔      | Forces a left handed gesture (`1`–`7`) regardless of the real hand. `0` = no override.  |
| `HVP/GestureRight/Override`    | Float         | Int             | ✔      | Forces a right handed gesture (`1`–`7`) regardless of the real hand. `0` = no override. |
| `HVP/QuestControllers/Enabled` | Float         | Bool            | ✔      | Off by default. When true it will ignore the Victory/Peace hand gesture.                |

#### Output Animator Parameters

| Property                             | Animator Type | Description                                                                                                     |
| ------------------------------------ | ------------- | --------------------------------------------------------------------------------------------------------------- |
| `HVP/GestureLeft`                    | Float         | Gesture index (`0`–`7`) in use on the left hand: uses the override if active, otherwise uses the real gesture.  |
| `HVP/GestureRight`                   | Float         | Gesture index (`0`–`7`) in use on the right hand: uses the override if active, otherwise uses the real gesture. |
| `HVP/GestureLeft/Neutral/Proxy`      | Float         | Smoothed 0–1 weight of the Neutral gesture on the left hand.                                                    |
| `HVP/GestureLeft/Fist/Proxy`         | Float         | Smoothed 0–1 weight of the Fist gesture on the left hand.                                                       |
| `HVP/GestureLeft/HandOpen/Proxy`     | Float         | Smoothed 0–1 weight of the HandOpen gesture on the left hand.                                                   |
| `HVP/GestureLeft/FingerPoint/Proxy`  | Float         | Smoothed 0–1 weight of the FingerPoint gesture on the left hand.                                                |
| `HVP/GestureLeft/Victory/Proxy`      | Float         | Smoothed 0–1 weight of the Victory gesture on the left hand.                                                    |
| `HVP/GestureLeft/RockNRoll/Proxy`    | Float         | Smoothed 0–1 weight of the RockNRoll gesture on the left hand.                                                  |
| `HVP/GestureLeft/HandGun/Proxy`      | Float         | Smoothed 0–1 weight of the HandGun gesture on the left hand.                                                    |
| `HVP/GestureLeft/ThumbsUp/Proxy`     | Float         | Smoothed 0–1 weight of the ThumbsUp gesture on the left hand.                                                   |
| `HVP/GestureRight/Neutral/Proxy`     | Float         | Smoothed 0–1 weight of the Neutral gesture on the right hand.                                                   |
| `HVP/GestureRight/Fist/Proxy`        | Float         | Smoothed 0–1 weight of the Fist gesture on the right hand.                                                      |
| `HVP/GestureRight/HandOpen/Proxy`    | Float         | Smoothed 0–1 weight of the HandOpen gesture on the right hand.                                                  |
| `HVP/GestureRight/FingerPoint/Proxy` | Float         | Smoothed 0–1 weight of the FingerPoint gesture on the right hand.                                               |
| `HVP/GestureRight/Victory/Proxy`     | Float         | Smoothed 0–1 weight of the Victory gesture on the right hand.                                                   |
| `HVP/GestureRight/RockNRoll/Proxy`   | Float         | Smoothed 0–1 weight of the RockNRoll gesture on the right hand.                                                 |
| `HVP/GestureRight/HandGun/Proxy`     | Float         | Smoothed 0–1 weight of the HandGun gesture on the right hand.                                                   |
| `HVP/GestureRight/ThumbsUp/Proxy`    | Float         | Smoothed 0–1 weight of the ThumbsUp gesture on the right hand.                                                  |
| `HVP/GestureLeftWeight/Proxy`        | Float         | Smoothed trigger pull (0–1) for the left hand. Held at 1 while an override is active                            |
| `HVP/GestureRightWeight/Proxy`       | Float         | Smoothed trigger pull (0–1) for the right hand. Held at 1 while an override is active                           |

</details>

---

<details>
<summary><h3>HVP Blink</h3></summary>

> Requires **HVP Frame Time**.

Adds a **custom blink system** separate from the VRChat system, with a single double and triple blink at random-ish intervals with two synced booleans (one for the blink itself, one for the on/off toggle).

It features a Override parameter which is used to force close the eyes if required by animations. It also integrated neatly with HVP Gestures.

#### Instructions

1. Drag and drop the prefab into the avatar's hierarchy.
2. Use the animator parameters `HVP/BlinkLeft/Proxy` and `HVP/BlinkRight/Proxy` to drive the blink blendshapes.
3. Optionally, set the animator parameters `HVP/BlinkLeft/Override` and `HVP/BlinkRight/Override` from your own animations to force the eyes closed.

#### Included Expression Parameters

| Property              | Animator Type | Expression Type | Synced | Description                                               |
| --------------------- | ------------- | --------------- | ------ | --------------------------------------------------------- |
| `_HVP/Blink/CanBlink` | Bool          | Bool            | ✔      | Internal. Syncs the blink state between local and remote. |
| `HVP/Blink/Enabled`   | Bool          | Bool            | ✔      | Disables the blink logic.                                 |

#### Output Animator Parameters

| Property               | Animator Type | Description                                         |
| ---------------------- | ------------- | --------------------------------------------------- |
| `HVP/BlinkLeft/Proxy`  | Float         | Smoothed left eyelid closure. 0 = open, 1 = closed  |
| `HVP/BlinkRight/Proxy` | Float         | Smoothed right eyelid closure. 0 = open, 1 = closed |

#### Input Animator Parameters

| Property                  | Animator Type | Description                                        |
| ------------------------- | ------------- | -------------------------------------------------- |
| `HVP/BlinkLeft/Override`  | Float         | 0 = blink normally, 1 = force the left eye closed  |
| `HVP/BlinkRight/Override` | Float         | 0 = blink normally, 1 = force the right eye closed |

</details>

## Contact interactions

<details>
<summary><h3>HVP Cheek Pull</h3></summary>

> Requires **HVP Frame Time**.

Adds **smoothed cheek pulling** behavior, which can be used to stretch the face slightly in the direction of whichever cheek is pulled.

#### Instructions

1. Drag and drop the prefab into the avatar's hierarchy.
2. Set the **Parameter** of your cheek PhysBones to `HVP/CheekPullLeft` and `HVP/CheekPullRight`.
3. Use the animator parameters `HVP/CheekPullLeft/Proxy` and `HVP/CheekPullRight/Proxy` to drive the face stretch.

#### Output Animator Parameters

| Property                   | Animator Type | Description                      |
| -------------------------- | ------------- | -------------------------------- |
| `HVP/CheekPullLeft/Proxy`  | Float         | Smoothed 0–1 left cheek stretch  |
| `HVP/CheekPullRight/Proxy` | Float         | Smoothed 0–1 right cheek stretch |

</details>

---

<details>
<summary><h3>HVP Cheese Slap</h3></summary>

Adds a **synced cheese slap system**, which allows compatible avatars to cheese your character, as well as allowing you to cheese others. A slap only counts when the sender reaches the face quickly. A slow approach is treated as a miss.

As it is synced, it will not get desynced for late joiners but it can lead to small jittering when added and removed in quick succession.

How it syncs: every client detects the slap from the contacts on its own, so `HVP/CheeseSlap` changes immediately for everyone who saw it happen. The wearer's client also writes the result to `_HVP/CheeseSlap/Sync`. Remote clients only use that bool to correct themselves: to catch a slap or removal their own detection missed, and to show the right state to late joiners.

#### Instructions

1. Drag and drop the prefab into the avatar's hierarchy.
2. Set the **Root Transform** of the **Hand Sender** contact sender to the hand.
3. Set the **Root Transform** of the **Head Receiver** and **Head Remove Receiver** contact receivers to the head, then adjust their position and radius.
4. Use the animator parameter `HVP/CheeseSlap` in your own controller to decide what happens when the avatar gets cheesed (play a slap sound, show the cheese, change the expression…). No sounds or visuals are included.

#### Included Expression Parameters

| Property                 | Animator Type | Expression Type | Synced | Description                                                                                                                                                           |
| ------------------------ | ------------- | --------------- | ------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `_HVP/CheeseSlap/Sync`   | Bool          | Bool            | ✔      | Internal. The wearer's cheesed state, written only by the wearer's client. Remote clients follow it when their own detection disagrees. Not saved, costs 1 synced bit |
| `HVP/CheeseSlap/Enabled` | Bool          | Bool            | ✔      | Disables the cheese logic and clears the cheese state.                                                                                                                |

#### Output Animator Parameters

| Property                       | Animator Type | Description                                                                                                                                                             |
| ------------------------------ | ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `HVP/CheeseSlap`               | Float         | 1 while the avatar is cheesed, otherwise 0                                                                                                                              |
| `HVP/CheeseSlap/Contact`       | Float         | Proximity (0–1) from **Head Receiver** to other players' `Cheese`/`cheese` senders. A hit that reaches 0.5 quickly cheeses the avatar                                   |
| `HVP/CheeseSlap/RemoveContact` | Bool          | From **Head Remove Receiver**. True while another player's head, hand, muzzle, snout or tail touches the face; removes the cheese if no cheese sender is still touching |

</details>

---

<details>
<summary><h3>HVP Head Pat</h3></summary>

> Requires **HVP Frame Time**.

Adds **smooth head pat detection** from hands (yours or other players').

#### Instructions

1. Drag and drop the prefab into the avatar's hierarchy.
2. Set the **Root Transform** of the contact receiver to the head, then adjust its position and radius.
3. Use the animator parameter `HVP/HeadPat/Proxy`.

#### Output Animator Parameters

| Property            | Animator Type | Description                     |
| ------------------- | ------------- | ------------------------------- |
| `HVP/HeadPat/Proxy` | Float         | Smoothed 0–1 amount of head pat |

</details>

---

<details>
<summary><h3>HVP Eye Poke</h3></summary>

> Requires **HVP Frame Time**.

Adds **smooth eye poke detection** from fingers (yours or other players) near each eye.

#### Instructions

1. Drag and drop the prefab into the avatar's hierarchy.
2. Set the **Root Transform** of the contact receivers to the head, then position them over the eyes.
3. Use the animator parameters `HVP/EyePokeLeft/Proxy` and `HVP/EyePokeRight/Proxy`.

#### Output Animator Parameters

| Property                 | Animator Type | Description                                       |
| ------------------------ | ------------- | ------------------------------------------------- |
| `HVP/EyePokeLeft/Proxy`  | Float         | Smoothed 0–1 amount of eye poke on the left side  |
| `HVP/EyePokeRight/Proxy` | Float         | Smoothed 0–1 amount of eye poke on the right side |

</details>

---

<details>
<summary><h3>HVP Paw Poke</h3></summary>

> Requires **HVP Frame Time**.

Adds **smooth paw poke detection** from fingers (yours or other players) poking each paw.

#### Instructions

1. Drag and drop the prefab into the avatar's hierarchy.
2. Set the **Root Transform** of the contact receivers to the feet, then position them over the paws.
3. Use the animator parameters `HVP/PawPokeLeft/Proxy` and `HVP/PawPokeRight/Proxy`.

#### Output Animator Parameters

| Property                 | Animator Type | Description                                       |
| ------------------------ | ------------- | ------------------------------------------------- |
| `HVP/PawPokeLeft/Proxy`  | Float         | Smoothed 0–1 amount of paw poke on the left side  |
| `HVP/PawPokeRight/Proxy` | Float         | Smoothed 0–1 amount of paw poke on the right side |

</details>

---

<details>
<summary><h3>HVP Paw Curl</h3></summary>

> Requires **HVP Frame Time**.

Adds a **smooth paw curl** that triggers when your own foot touches the paw.

#### Instructions

1. Drag and drop the prefab into the avatar's hierarchy.
2. Set the **Root Transform** of the contact receivers to the feet, then position them over the paws.
3. Use the animator parameters `HVP/PawCurlLeft/Proxy` and `HVP/PawCurlRight/Proxy`.

#### Output Animator Parameters

| Property                 | Animator Type | Description                                       |
| ------------------------ | ------------- | ------------------------------------------------- |
| `HVP/PawCurlLeft/Proxy`  | Float         | Smoothed 0–1 amount of paw curl on the left side  |
| `HVP/PawCurlRight/Proxy` | Float         | Smoothed 0–1 amount of paw curl on the right side |

</details>

---

<details>
<summary><h3>HVP Blush</h3></summary>

> Requires **HVP Frame Time**.

Adds a **smoothed blush amount** you drive yourself.

#### Instructions

1. Drag and drop the prefab into the avatar's hierarchy.
2. Drive the animator parameter `HVP/Blush/Input` from your own contacts or animations.
3. Use the animator parameter `HVP/Blush/Proxy` to drive your blush blendshape or material.

#### Output Animator Parameters

| Property          | Animator Type | Description               |
| ----------------- | ------------- | ------------------------- |
| `HVP/Blush/Proxy` | Float         | Smoothed 0–1 blush amount |

#### Input Animator Parameters

| Property          | Animator Type | Description             |
| ----------------- | ------------- | ----------------------- |
| `HVP/Blush/Input` | Float         | 0–1 target blush amount |

</details>
