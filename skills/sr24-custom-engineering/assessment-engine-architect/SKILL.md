---
name: assessment-engine-architect
description: Master architect of adaptive educational testing engines — Computer Adaptive Testing (CAT), Item Response Theory (IRT), question bank taxonomy, KaTeX math parsing, and proctoring telemetry.
---

# Educational Assessment Engine & Testing Architect

## Role & Mission
The **Educational Assessment Engine & Testing Architect** designs and builds high-scale, secure, and psychometrically sound examination platforms (e.g. Exam Loop). You architect Item Response Theory (IRT) adaptive testing engines, question bank schemas, anti-cheating telemetry, and diagnostic learning analytics.

---

## 1. Activation Conditions
Invoke this skill whenever:
- Designing examination or quiz platforms (JEE, NEET, CBSE, UPSC or corporate mock tests).
- Implementing Computer Adaptive Testing (CAT) where question difficulty dynamically shifts based on student responses.
- Structuring mathematical/chemical formulas in questions with KaTeX LaTeX rendering.
- Implementing browser proctoring (tab blur detection, full-screen lock, copy-paste blocking).
- Generating scorecards with percentile ranks, topic-level weakness heatmaps, and speed-accuracy trade-offs.

---

## 2. Adaptive Testing Mathematical Model (IRT 1PL / Rasch Model)

The probability $P(\theta)$ of a student with ability $\theta$ correctly answering an item of difficulty $b$ is:
$$P(\theta) = \frac{1}{1 + e^{-(\theta - b)}}$$

- If student answers correctly: next item selected has higher difficulty $b_{next} \approx \theta + 0.5$.
- If student answers incorrectly: next item selected has lower difficulty $b_{next} \approx \theta - 0.5$.

---

## 3. Implementation: Question Bank Schema & Adaptive Selector

```typescript
export interface AssessmentQuestion {
  id: string;
  subject: string;
  chapter: string;
  topic: string;
  bloomsTaxonomy: 'REMEMBER' | 'UNDERSTAND' | 'APPLY' | 'ANALYZE' | 'EVALUATE';
  difficultyParameter: number; // -3.0 (Easiest) to +3.0 (Hardest)
  questionStem: string;        // Supports KaTeX LaTeX: $\\int_0^1 x^2 dx$
  options: Array<{
    id: string;
    content: string;
    isCorrect: boolean;
    explanation: string;
  }>;
  timeEstimateSeconds: number;
}

export class AdaptiveTestSession {
  public studentAbilityEstimate = 0.0; // Starts at average 0.0
  public responseHistory: Array<{ questionId: string; isCorrect: boolean; timeSpent: number }> = [];

  public selectNextQuestion(pool: AssessmentQuestion[]): AssessmentQuestion | null {
    const answeredIds = new Set(this.responseHistory.map((r) => r.questionId));
    const available = pool.filter((q) => !answeredIds.has(q.id));

    if (available.length === 0) return null;

    // Find question whose difficulty is closest to current estimated ability
    return available.reduce((closest, current) => {
      const diffCurrent = Math.abs(current.difficultyParameter - this.studentAbilityEstimate);
      const diffClosest = Math.abs(closest.difficultyParameter - this.studentAbilityEstimate);
      return diffCurrent < diffClosest ? current : closest;
    });
  }

  public recordResponse(question: AssessmentQuestion, selectedOptionId: string, timeSpentSeconds: number) {
    const selected = question.options.find((o) => o.id === selectedOptionId);
    const isCorrect = selected?.isCorrect ?? false;

    this.responseHistory.push({
      questionId: question.id,
      isCorrect,
      timeSpent: timeSpentSeconds,
    });

    // Update ability estimate (simplified Newton-Raphson update step)
    const step = 0.35;
    if (isCorrect) {
      this.studentAbilityEstimate = Math.min(3.0, this.studentAbilityEstimate + step);
    } else {
      this.studentAbilityEstimate = Math.max(-3.0, this.studentAbilityEstimate - step);
    }
  }
}
```

---

## 4. Integrity & Proctoring Telemetry
```typescript
export class TestProctoringGuard {
  public violationLog: Array<{ type: string; timestamp: number }> = [];

  public attachListeners(onWarning: (msg: string) => void) {
    // 1. Tab Switching & Window Focus Loss
    window.addEventListener('blur', () => {
      this.recordViolation('WINDOW_BLUR_TAB_SWITCH', onWarning);
    });

    // 2. Fullscreen Exit Detection
    document.addEventListener('fullscreenchange', () => {
      if (!document.fullscreenElement) {
        this.recordViolation('FULLSCREEN_EXIT', onWarning);
      }
    });

    // 3. Copy-Paste Interception
    window.addEventListener('copy', (e) => {
      e.preventDefault();
      this.recordViolation('COPY_ATTEMPT', onWarning);
    });
  }

  private recordViolation(type: string, onWarning: (msg: string) => void) {
    this.violationLog.push({ type, timestamp: Date.now() });
    onWarning(`Warning: Integrity violation detected (${type}). This event is logged.`);
  }
}
```

---

## 5. Quality Checklist
- [ ] Questions render complex LaTeX math and chemical structural formulas without font clipping.
- [ ] Timer continues server-side (prevents resetting test time via local clock manipulation).
- [ ] Scorecard generates subject-level percentile, accuracy percentage, and negative marking deductions.
- [ ] Student receives personalized remediation reading list based on failed topics.

