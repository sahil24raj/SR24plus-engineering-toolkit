---
name: unity-performance-testing
description: >-
  Specialist in Unity Performance Testing API — automated frame-time measurement, GC alloc tracking, memory leak detection, and hardware profiling.
---

# Unity Performance Testing & Memory Profiling Specialist

## 1. When to Activate
Activate this skill whenever a game project or prompt requires specialist in unity performance testing api — automated frame-time measurement, gc alloc tracking, memory leak detection, and hardware profiling.. It is assigned to official engineering phases in the **SR24Plus Engineering Toolkit**.

## 2. When Not to Activate
- Do not activate when the task does not involve unity-performance-testing.
- Do not activate as a substitute for simple static mockups where deeper game systems engineering is unnecessary.

## 3. Core Capabilities
- Automated performance test scripts executing in Unity Editor and Standalone Players
- Frame time (FPS) sample collection calculating 99th percentile and minimum frame rates
- Garbage Collector allocation tracking identifying per-frame heap allocations
- Automated regression alerts when new shaders or physics features exceed frame budgets
- Performance test result export to JSON for CI/CD dashboard tracking

## 4. Engineering Workflow
1. **Design & Architecture**: Inspect gameplay loops, frame rate budgets, physics constraints, and network topology.
2. **Setup & Initialization**: Configure libraries, canvas bindings, physics worlds, and input listeners.
3. **Implementation**: Author deterministic game loops, decoupled systems, state machines, and rendering passes.
4. **Optimization**: Audit draw calls, memory allocation, garbage collection, and frame time stability.
5. **Testing & QA**: Execute automated regression, collision checks, network latency tests, and visual snapshot reviews.

## 5. Implementation Instructions & Code Patterns

```typescript
using System.Collections;
using NUnit.Framework;
using UnityEngine;
using UnityEngine.TestTools;
using Unity.PerformanceTesting;

public class GamePerformanceTests {
    [UnityTest, Performance]
    public IEnumerator MeasureFrameTimeUnderHeavyLoad() {
        yield return Measure.Frames()
            .WarmupCount(10)
            .MeasurementCount(100)
            .SampleGroup("SimulatedTrackRaceFPS")
            .Run();
    }
}
```

## 6. Best Practices
- **Deterministic Loop**: Always use fixed-timestep loops for physics to avoid frame-rate dependency.
- **Zero Allocations in Loop**: Pre-allocate vectors, matrices, and objects; never allocate new objects in `update` or `render`.
- **Responsive Controls**: Support keyboard, gamepad, and virtual touch joysticks with identical input abstractions.
- **Audio Management**: Always unlock audio contexts on first user interaction and manage volumes through bus mixers.

## 7. Common Anti-Patterns to Avoid
- Variable delta-time in physics causing objects to tunnel through geometry at low frame rates.
- Polling in tight loops or allocating garbage that triggers periodic GC stutter.
- Hardcoding screen dimensions instead of responsive canvas auto-scaling.
- Trusting client game state in multiplayer games without server authority.

## 8. Verification & Testing Checklist
- [ ] 60 FPS maintained under maximum entity density.
- [ ] Physics simulation deterministic across varied display refresh rates (60Hz, 120Hz).
- [ ] Zero memory allocations in render loop verified via Chrome DevTools Memory profiler.
- [ ] Responsive controls tested across desktop keyboard and mobile touch viewports.

## 9. Official Source Repository & Upstream Reference
- **Repository**: [https://github.com/needle-mirror/com.unity.test-framework.performance](https://github.com/needle-mirror/com.unity.test-framework.performance)
- **Category**: SR24-GAME-DEV Canonical Engineering Skill

## 10. License & Attribution
- **License**: Unity-Companion-License
- **Maintained By**: SR24Plus Autonomous Engineering Architecture
