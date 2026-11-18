---
name: bullmq-job-queues
description: >-
  Expert in BullMQ Redis-backed distributed message queues — background workers, concurrency control, delayed jobs, exponential retry backoff, and event metrics.
---

# BullMQ Redis Background Job Queues & Worker Architecture

## 1. When to Activate
Activate this skill whenever a project or prompt requires expert in bullmq redis-backed distributed message queues — background workers, concurrency control, delayed jobs, exponential retry backoff, and event metrics.. It is assigned to official engineering phases in the **SR24Plus Engineering Toolkit**.

## 2. When Not to Activate
- Do not activate when the task does not involve bullmq-job-queues.
- Do not activate as a substitute for simple static mockups where deeper engineering is unnecessary.

## 3. Core Capabilities
- Queue creation with Redis connection pooling and prefix namespacing
- Worker lifecycle management with concurrency control, graceful shutdown, and heartbeat checks
- Exponential retry backoff and dead-letter queue (DLQ) routing for failed transactional jobs
- Delayed job scheduling for game match timeouts, payment expiration, and email reminders
- Job progress reporting and real-time WebSocket broadcasting of processing status

## 4. Engineering Workflow
1. **Discovery & Architecture**: Inspect technical constraints, performance requirements, and data contracts.
2. **Setup & Configuration**: Install official package dependencies and configure environment variables.
3. **Implementation**: Author production-grade code using clean architecture, strict TypeScript types, and error handling.
4. **Validation & Testing**: Run unit and integration tests confirming zero regressions.
5. **Production Deployment**: Verify build bundle impact, tree-shaking, and observability telemetry.

## 5. Implementation Instructions & Code Patterns

```typescript
import { Queue, Worker, Job } from 'bullmq';
import IORedis from 'ioredis';

const connection = new IORedis(process.env.REDIS_URL || 'redis://127.0.0.1:6379', {
  maxRetriesPerRequest: null,
});

export interface MatchmakingPayload {
  roomId: string;
  gameType: string;
  playerIds: string[];
}

// 1. Queue Definition
export const matchQueue = new Queue<MatchmakingPayload>('game-matchmaking', {
  connection,
  defaultJobOptions: {
    attempts: 3,
    backoff: { type: 'exponential', delay: 1000 },
    removeOnComplete: 100,
    removeOnFail: 500,
  },
});

// 2. Worker Processing
export const matchWorker = new Worker<MatchmakingPayload>(
  'game-matchmaking',
  async (job: Job<MatchmakingPayload>) => {
    console.log(`Processing match ${job.data.roomId} with ${job.data.playerIds.length} players`);
    await job.updateProgress(50);
    // Execute room allocation logic...
    await job.updateProgress(100);
    return { allocatedServerId: 'srv-asia-south-1', status: 'READY' };
  },
  { connection, concurrency: 5 }
);
```

## 6. Best Practices
- **Strict Typing**: Never use `any`; use strict interface and generic contracts.
- **Error Boundaries**: Handle all edge cases, offline drops, and network timeouts gracefully.
- **Performance Budget**: Avoid blocking main thread operations; optimize bundle sizes and lazy-load where appropriate.
- **Security**: Never expose private keys, credentials, or sensitive customer data in client-side bundles.

## 7. Common Anti-Patterns to Avoid
- Hardcoding credentials or API endpoints directly into source files.
- Ignoring promise rejections and async exceptions.
- Creating monolithic un-testable files instead of modular single-responsibility units.
- Introducing layout shifts or un-optimized re-renders.

## 8. Verification & Testing Checklist
- [ ] TypeScript compiles cleanly with zero errors (`tsc --noEmit`).
- [ ] Unit tests pass verifying expected behavior and edge cases.
- [ ] Environment variables documented in `.env.example`.
- [ ] Build artifact size verified with tree-shaking confirmed.

## 9. Official Source Repository & Upstream Reference
- **Repository**: [https://github.com/taskforcesh/bullmq](https://github.com/taskforcesh/bullmq)
- **Category**: SR24-WEB-DEV Canonical Engineering Skill

## 10. License & Attribution
- **License**: MIT
- **Maintained By**: SR24Plus Autonomous Engineering Architecture
