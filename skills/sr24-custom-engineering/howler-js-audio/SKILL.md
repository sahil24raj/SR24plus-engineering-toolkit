---
name: howler-js-audio
description: >-
  Expert in Howler.js audio library for modern web and game audio — Web Audio API & HTML5 Audio fallback,
  sound sprites, 3D spatial audio, audio manager architecture, cross-fading BGM, mobile autoplay unlock,
  and React/Next.js integration.
---

# Howler.js Web Audio Expert Skill

Howler.js is an audio library for the modern web. It defaults to the Web Audio API and falls back to HTML5 Audio, providing seamless cross-browser audio playback, sound sprites, 3D spatial panning, and granular audio control for web games and interactive applications.

---

## 1. Core Architecture & Concepts

Howler provides two primary exports:
- **`Howl`**: Instance class representing an audio file or sprite sheet with full playback controls.
- **`Howler`**: Global object controlling master volume, global mute, codecs, Web Audio context, and spatial listener coordinates.

```typescript
import { Howl, Howler } from 'howler';

// Global volume & mute
Howler.volume(0.8); // 0.0 to 1.0
Howler.mute(false);

// Single sound instance
const sfx = new Howl({
  src: ['/audio/laser.webm', '/audio/laser.mp3'], // Format fallback order
  volume: 0.7,
  preload: true,
  autoplay: false,
  loop: false,
});

const soundId = sfx.play();
```

---

## 2. Web Audio vs HTML5 Audio Mode

Choose the correct mode based on audio size and usage:

| Feature | Web Audio (`html5: false`, default) | HTML5 Audio (`html5: true`) |
| :--- | :--- | :--- |
| **Best For** | Short Sound Effects (SFX), multi-instance overlapping sounds, audio sprites | Long Background Music (BGM), voiceovers, podcasts |
| **Buffering** | Decodes full audio buffer in RAM before playback | Streams audio on the fly (low memory usage) |
| **Latency** | Ultra-low (instant trigger) | Higher latency (variable buffer time) |
| **Concurrent Playback**| Hundreds of simultaneous instances | Limited audio channels by browser |
| **Effects & Panning** | Supports filters, 3D spatial audio, pitch shifts | Basic stereo pan only |

```typescript
// Background Music (Streaming mode)
const bgm = new Howl({
  src: ['/audio/theme.webm', '/audio/theme.mp3'],
  html5: true, // Stream large audio file without loading entire file into memory
  loop: true,
  volume: 0.5,
});
```

---

## 3. Audio Sprites (Optimized Sound Packs)

Audio sprites combine multiple sound effects into a single file to eliminate HTTP requests and reduce mobile latency.

```typescript
const gameSprites = new Howl({
  src: ['/audio/game_sounds.webm', '/audio/game_sounds.mp3'],
  sprite: {
    // [start_time_in_ms, duration_in_ms, loop_boolean]
    laser: [0, 450],
    explosion: [1000, 1200],
    coin: [2500, 300],
    engine_loop: [3200, 4000, true],
  },
});

// Play specific sprite
const coinId = gameSprites.play('coin');

// Control specific sprite instance
gameSprites.rate(1.2, coinId); // Pitch up coin sound
```

---

## 4. Playback Controls & Dynamic Manipulation

### Sound IDs (Controlling Concurrent Instances)
Methods accept an optional `id` parameter to target a specific active playback instance.

```typescript
const zap = new Howl({ src: ['/audio/zap.mp3'] });

// Play returns an integer sound ID
const id1 = zap.play();
const id2 = zap.play();

// Alter only the second instance
zap.rate(1.5, id2); // Higher pitch
zap.volume(0.3, id1); // Lower volume

// Seek (Jump to position in seconds)
zap.seek(1.5, id1);

// State check
if (zap.playing(id1)) {
  console.log('Instance 1 is currently playing');
}
```

### Smooth Cross-Fading (e.g., Changing BGM Tracks)
```typescript
function crossFadeBGM(oldTrack: Howl, newTrack: Howl, durationMs = 1000) {
  const newId = newTrack.play();
  newTrack.fade(0, 0.5, durationMs, newId);

  oldTrack.fade(oldTrack.volume(), 0, durationMs);
  oldTrack.once('fade', () => {
    oldTrack.stop();
  });
}
```

---

## 5. 3D Spatial Audio & Positional Panning

Create immersive positional sound based on player / listener distance and angle.

```typescript
const spatialSound = new Howl({
  src: ['/audio/waterfall.mp3'],
  loop: true,
});

const id = spatialSound.play();

// Position the sound in 3D space: x, y, z
spatialSound.pos(15, 0, 5, id);

// Configure roll-off and distance attenuation
spatialSound.pannerAttr({
  distanceModel: 'inverse', // 'linear' | 'inverse' | 'exponential'
  maxDistance: 1000,
  refDistance: 1,
  rolloffFactor: 1,
  coneInnerAngle: 360,
  coneOuterAngle: 360,
  coneOuterGain: 0,
}, id);

// Update Global Listener position (e.g. Player position in game loop)
function updatePlayerAudio(playerX: number, playerY: number) {
  Howler.pos(playerX, playerY, 0);
  Howler.orientation(0, 1, 0, 0, 0, 1); // Facing forward
}
```

---

## 6. Autoplay Policy & Mobile Audio Unlock

Modern browsers block audio until user interaction. Howler handles unlocking automatically, but you should handle fallback policies gracefully.

```typescript
// Check if AudioContext is locked
if (Howler.ctx && Howler.ctx.state === 'suspended') {
  const unlockAudio = () => {
    if (Howler.ctx.state === 'suspended') {
      Howler.ctx.resume().then(() => {
        console.log('AudioContext resumed successfully');
      });
    }
    window.removeEventListener('click', unlockAudio);
    window.removeEventListener('keydown', unlockAudio);
    window.removeEventListener('touchstart', unlockAudio);
  };

  window.addEventListener('click', unlockAudio, { passive: true });
  window.addEventListener('keydown', unlockAudio, { passive: true });
  window.addEventListener('touchstart', unlockAudio, { passive: true });
}
```

---

## 7. Production Game Sound Manager Architecture

Create a centralized sound manager to handle sound caching, BGM switching, volume persistence, and muting.

```typescript
// SoundManager.ts
import { Howl, Howler } from 'howler';

class SoundManager {
  private static instance: SoundManager;
  private sfxMap: Map<string, Howl> = new Map();
  private currentBGM: Howl | null = null;
  private isMuted: boolean = false;
  private sfxVolume: number = 0.8;
  private bgmVolume: number = 0.5;

  private constructor() {
    this.loadSettings();
  }

  public static getInstance(): SoundManager {
    if (!SoundManager.instance) {
      SoundManager.instance = new SoundManager();
    }
    return SoundManager.instance;
  }

  public registerSFX(key: string, src: string[]) {
    if (!this.sfxMap.has(key)) {
      this.sfxMap.set(
        key,
        new Howl({
          src,
          volume: this.sfxVolume,
        })
      );
    }
  }

  public playSFX(key: string, pitchVariation = false): number | undefined {
    if (this.isMuted) return;
    const sound = this.sfxMap.get(key);
    if (!sound) return;

    const id = sound.play();
    if (pitchVariation) {
      sound.rate(0.9 + Math.random() * 0.2, id); // Random pitch between 0.9 and 1.1
    }
    return id;
  }

  public playBGM(src: string[], loop = true) {
    if (this.currentBGM) {
      this.currentBGM.stop();
      this.currentBGM.unload();
    }

    this.currentBGM = new Howl({
      src,
      html5: true,
      loop,
      volume: this.isMuted ? 0 : this.bgmVolume,
    });

    this.currentBGM.play();
  }

  public setMute(muted: boolean) {
    this.isMuted = muted;
    Howler.mute(muted);
    this.saveSettings();
  }

  public setSFXVolume(vol: number) {
    this.sfxVolume = vol;
    this.sfxMap.forEach((howl) => howl.volume(vol));
    this.saveSettings();
  }

  public setBGMVolume(vol: number) {
    this.bgmVolume = vol;
    if (this.currentBGM) {
      this.currentBGM.volume(vol);
    }
    this.saveSettings();
  }

  private saveSettings() {
    if (typeof window === 'undefined') return;
    localStorage.setItem(
      'audio_settings',
      JSON.stringify({
        muted: this.isMuted,
        sfxVolume: this.sfxVolume,
        bgmVolume: this.bgmVolume,
      })
    );
  }

  private loadSettings() {
    if (typeof window === 'undefined') return;
    const saved = localStorage.getItem('audio_settings');
    if (saved) {
      try {
        const { muted, sfxVolume, bgmVolume } = JSON.parse(saved);
        this.isMuted = muted ?? false;
        this.sfxVolume = sfxVolume ?? 0.8;
        this.bgmVolume = bgmVolume ?? 0.5;
        Howler.mute(this.isMuted);
      } catch (e) {
        console.error('Failed to parse audio settings', e);
      }
    }
  }
}

export const sounds = SoundManager.getInstance();
```

---

## 8. React / Next.js Integration Hook

```tsx
'use client';

import { useEffect, useRef, useCallback } from 'react';
import { Howl, HowlOptions } from 'howler';

export function useAudio(options: HowlOptions) {
  const soundRef = useRef<Howl | null>(null);

  useEffect(() => {
    soundRef.current = new Howl(options);

    return () => {
      if (soundRef.current) {
        soundRef.current.stop();
        soundRef.current.unload(); // Prevent audio memory leaks
        soundRef.current = null;
      }
    };
  }, [JSON.stringify(options.src)]);

  const play = useCallback((spriteName?: string) => {
    return soundRef.current?.play(spriteName);
  }, []);

  const stop = useCallback((id?: number) => {
    soundRef.current?.stop(id);
  }, []);

  const pause = useCallback((id?: number) => {
    soundRef.current?.pause(id);
  }, []);

  return { play, stop, pause, sound: soundRef.current };
}
```

---

## 9. Performance & Debugging Guidelines

1. **Avoid Audio Memory Leaks**: Always call `sound.unload()` when a scene or React component unmounts if the audio is dynamic or temporary.
2. **Codec Order**: Always specify WebM/Ogg before MP3 (`src: ['track.webm', 'track.mp3']`). WebM delivers smaller file sizes and better looping fidelity without MP3 encoder padding gaps.
3. **Seamless Loops**: MP3 files often include silent padding at the start and end. For seamless looping music, use **Ogg Vorbis** or **WebM (Opus)**.
4. **Rate Modulation**: Limit `rate()` values between `0.5` and `2.0` to avoid distortion.
