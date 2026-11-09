---
name: truck-physics-engineer
description: Architect of heavy vehicle and truck physics simulation in Unity — multi-axle WheelColliders, high center-of-mass body roll, air brakes, diesel torque curves, and terrain friction.
---

# Unity Heavy Vehicle & Truck Physics Engineer

## Role & Mission
The **Unity Heavy Vehicle & Truck Physics Engineer** designs, implements, and tunes heavy multi-axle vehicle dynamics in Unity (e.g. Indian commercial trucks, tankers, tippers). You simulate authentic weight inertia, suspension travel, dual rear wheels, high center of mass (CoM), engine torque curves, and air brake physics.

---

## 1. Activation Conditions
Invoke this skill whenever:
- Building vehicle physics for heavy trucks, buses, trailers, or racing trucks in Unity.
- Tuning WheelCollider friction curves (Extremum, Asymptote) for realistic tire grip without flipping.
- Setting up multi-axle drivetrains (6x2, 6x4, 10-wheelers, 16-wheelers).
- Simulating chassis body roll, suspension anti-roll bars, and cargo weight shifting.
- Engineering projects like Indian Truck Racing.

---

## 2. Truck Physics Rig Architecture

```
[Truck Root Rigidbody (Mass: 8,000 - 16,000 kg)]
  │
  ├── Center of Mass (CoM Helper: Low & centered to prevent premature flipping)
  │
  ├── Front Axle (Steerable, Single Wheels, Stiff Damping)
  │     ├── Left Front WheelCollider
  │     └── Right Front WheelCollider
  │
  ├── Drive Axle 1 (Powered, Dual Wheel pairs, High Traction)
  │
  ├── Drive Axle 2 (Powered/Tag, Dual Wheel pairs)
  │
  └── Anti-Roll Bar Script (Transfers suspension force between paired wheels)
```

---

## 3. Implementation: Truck Controller & Multi-Axle Physics

```csharp
using UnityEngine;

[RequireComponent(typeof(Rigidbody))]
public class HeavyTruckController : MonoBehaviour
{
    [Header("Engine & Transmission")]
    public float maxMotorTorque = 2800f; // High diesel torque (Nm)
    public float maxBrakeTorque = 6500f; // Powerful pneumatic air brakes
    public float maxSteerAngle = 32f;
    public AnimationCurve engineTorqueCurve;

    [Header("Axle Wheel Colliders")]
    public WheelCollider[] steerWheels;      // Front axle (2 wheels)
    public WheelCollider[] driveWheels;      // Rear dual axles (4-8 wheels)
    public WheelCollider[] allWheels;

    [Header("Chassis & Center of Mass")]
    public Transform centerOfMassTransform;
    public float antiRollBarStiffness = 8000f;

    private Rigidbody rb;
    private float inputSteer;
    private float inputThrottle;
    private float inputBrake;

    void Start()
    {
        rb = GetComponent<Rigidbody>();
        if (centerOfMassTransform != null)
        {
            rb.centerOfMass = centerOfMassTransform.localPosition;
        }
    }

    void Update()
    {
        inputSteer = Input.GetAxis("Horizontal");
        inputThrottle = Mathf.Clamp01(Input.GetAxis("Vertical"));
        inputBrake = Input.GetKey(KeyCode.Space) ? 1f : (Input.GetAxis("Vertical") < 0 ? -Input.GetAxis("Vertical") : 0f);
    }

    void FixedUpdate()
    {
        ApplySteering();
        ApplyDriveTorque();
        ApplyAntiRoll();
    }

    private void ApplySteering()
    {
        float steer = inputSteer * maxSteerAngle;
        foreach (var wheel in steerWheels)
        {
            wheel.steerAngle = steer;
        }
    }

    private void ApplyDriveTorque()
    {
        float torquePerWheel = (inputThrottle * maxMotorTorque) / Mathf.Max(1, driveWheels.Length);
        float brakePerWheel = inputBrake * maxBrakeTorque;

        foreach (var wheel in driveWheels)
        {
            wheel.motorTorque = torquePerWheel;
        }

        foreach (var wheel in allWheels)
        {
            wheel.brakeTorque = brakePerWheel;
        }
    }

    // Essential: Anti-roll bar prevents heavy truck from flipping during tight ghat turns
    private void ApplyAntiRoll()
    {
        for (int i = 0; i < steerWheels.Length; i += 2)
        {
            if (i + 1 < steerWheels.Length)
            {
                ApplyAntiRollForce(steerWheels[i], steerWheels[i + 1]);
            }
        }
    }

    private void ApplyAntiRollForce(WheelCollider wheelL, WheelCollider wheelR)
    {
        WheelHit hitL, hitR;
        float travelL = 1.0f;
        float travelR = 1.0f;

        bool groundedL = wheelL.GetGroundHit(out hitL);
        if (groundedL)
            travelL = (-wheelL.transform.InverseTransformPoint(hitL.point).y - wheelL.radius) / wheelL.suspensionDistance;

        bool groundedR = wheelR.GetGroundHit(out hitR);
        if (groundedR)
            travelR = (-wheelR.transform.InverseTransformPoint(hitR.point).y - wheelR.radius) / wheelR.suspensionDistance;

        float antiRollForce = (travelL - travelR) * antiRollBarStiffness;

        if (groundedL)
            rb.AddForceAtPosition(wheelL.transform.up * -antiRollForce, wheelL.transform.position);
        if (groundedR)
            rb.AddForceAtPosition(wheelR.transform.up * antiRollForce, wheelR.transform.position);
    }
}
```

---

## 4. Friction Curves Calibration (Indian Highway / Ghat Roads)
- **Forward Friction**:
  - Extremum Slip: `0.4`, Value: `1.1`
  - Asymptote Slip: `0.8`, Value: `0.75`
  - Stiffness: `1.0` (Dry asphalt), `0.65` (Monsoon wet road), `0.45` (Muddy village detour).
- **Sideways Friction**:
  - Extremum Slip: `0.25`, Value: `1.05`
  - Asymptote Slip: `0.5`, Value: `0.75`

---

## 5. Quality Checklist
- [ ] Truck does not bounce violently on mesh colliders (set `solverIterations` to at least `12`).
- [ ] Air brake sound effect triggers with distinct pneumatic hiss upon brake release.
- [ ] High-payload cargo shifts center of mass dynamically upwards, increasing tipping hazard.
- [ ] Wheels rotate visually matching WheelCollider RPM without stuttering.
