---
name: redis-in-memory-datastore
description: >-
  Expert in Redis in-memory data store — data structures (Strings, Hashes, Lists, Sets, Sorted Sets, Streams, Bitmaps),
  Pub/Sub, Caching patterns (Cache-Aside, Write-Through), rate limiting (Sliding Window, Token Bucket),
  leaderboards, distributed locks (Redlock), pipelining, transactions, Lua scripts, and ioredis/Upstash integration.
---

# Redis In-Memory Data Store Expert Skill

Redis (Remote Dictionary Server) is an open-source, in-memory data structure store used as a database, cache, message broker, and streaming engine.

---

## 1. Core Data Structures & Common Commands

| Data Structure | Primary Commands | Common Use Cases |
| :--- | :--- | :--- |
| **Strings** | `SET`, `GET`, `INCR`, `DECR`, `MSET`, `SETEX` | Cache values, counters, session tokens |
| **Hashes** | `HSET`, `HGET`, `HGETALL`, `HINCRBY`, `HDEL` | User profiles, objects with multiple fields |
| **Lists** | `LPUSH`, `RPUSH`, `LPOP`, `RPOP`, `LRANGE`, `BRPOP` | Job queues, activity feeds, recent items |
| **Sets** | `SADD`, `SREM`, `SMEMBERS`, `SISMEMBER`, `SINTER` | Unique tags, friend lists, deduplication |
| **Sorted Sets (ZSet)** | `ZADD`, `ZINCRBY`, `ZRANGE`, `ZREVRANGE`, `ZRANK` | Leaderboards, rate limiters, priority queues |
| **Streams** | `XADD`, `XREAD`, `XREADGROUP`, `XACK` | Event streaming, log aggregation, CQRS |
| **Bitmaps / HyperLogLog** | `SETBIT`, `GETBIT`, `BITCOUNT` / `PFADD`, `PFCOUNT` | Daily active users (DAU), unique visitor counts |

---

## 2. Node.js & TypeScript Integration (`ioredis`)

```typescript
import Redis from 'ioredis';

export const redis = new Redis({
  host: process.env.REDIS_HOST || '127.0.0.1',
  port: Number(process.env.REDIS_PORT) || 6379,
  password: process.env.REDIS_PASSWORD,
  retryStrategy(times) {
    const delay = Math.min(times * 50, 2000);
    return delay;
  },
  maxRetriesPerRequest: 3,
});

redis.on('connect', () => console.log('Redis connected successfully'));
redis.on('error', (err) => console.error('Redis connection error:', err));
```

---

## 3. High-Performance Caching Patterns

### Cache-Aside Pattern with TTL
```typescript
async function getCachedUser(userId: string): Promise<User> {
  const cacheKey = `user:${userId}`;

  // 1. Try cache
  const cached = await redis.get(cacheKey);
  if (cached) {
    return JSON.parse(cached);
  }

  // 2. Fetch from primary DB
  const user = await db.user.findUnique({ where: { id: userId } });
  if (!user) throw new Error('User not found');

  // 3. Set cache with TTL (1 hour + random jitter to prevent cache stampede)
  const ttl = 3600 + Math.floor(Math.random() * 300);
  await redis.set(cacheKey, JSON.stringify(user), 'EX', ttl);

  return user;
}

// Invalidate on update
async function updateUser(userId: string, data: Partial<User>) {
  await db.user.update({ where: { id: userId }, data });
  await redis.del(`user:${userId}`);
}
```

---

## 4. Real-Time Gaming Leaderboard (Sorted Sets)

```typescript
export class LeaderboardService {
  private key: string;

  constructor(seasonId: string) {
    this.key = `leaderboard:${seasonId}`;
  }

  // Submit or increment score
  async submitScore(userId: string, score: number) {
    // ZADD updates score or adds if not present
    await redis.zadd(this.key, score, userId);
  }

  async incrementScore(userId: string, delta: number) {
    return await redis.zincrby(this.key, delta, userId);
  }

  // Get Top N Players with Scores
  async getTopPlayers(limit: number = 10) {
    // Returns array of [userId, score, userId, score, ...]
    const results = await redis.zrevrange(this.key, 0, limit - 1, 'WITHSCORES');
    const players: { rank: number; userId: string; score: number }[] = [];

    for (let i = 0; i < results.length; i += 2) {
      players.push({
        rank: Math.floor(i / 2) + 1,
        userId: results[i],
        score: Number(results[i + 1]),
      });
    }
    return players;
  }

  // Get specific user rank & score
  async getUserRank(userId: string) {
    const rank = await redis.zrevrank(this.key, userId);
    const score = await redis.zscore(this.key, userId);
    if (rank === null || score === null) return null;

    return { rank: rank + 1, score: Number(score) };
  }
}
```

---

## 5. Rate Limiting (Sliding Window Log with Multi/Exec)

```typescript
export async function isRateLimited(
  identifier: string,
  limit: number = 60,
  windowSeconds: number = 60
): Promise<{ allowed: boolean; remaining: number }> {
  const key = `ratelimit:${identifier}`;
  const now = Date.now();
  const clearBefore = now - windowSeconds * 1000;

  const pipeline = redis.pipeline();
  // 1. Remove timestamps older than window
  pipeline.zremrangebyscore(key, 0, clearBefore);
  // 2. Add current timestamp
  pipeline.zadd(key, now, `${now}-${Math.random()}`);
  // 3. Count total elements in window
  pipeline.zcard(key);
  // 4. Set key expiration
  pipeline.expire(key, windowSeconds);

  const results = await pipeline.exec();
  const currentCount = results?.[2]?.[1] as number;

  const allowed = currentCount <= limit;
  const remaining = Math.max(0, limit - currentCount);

  return { allowed, remaining };
}
```

---

## 6. Pub/Sub & Messaging

```typescript
// Publisher Client
const publisher = new Redis();
export async function broadcastGameEvent(roomId: string, event: object) {
  await publisher.publish(`game:room:${roomId}`, JSON.stringify(event));
}

// Subscriber Client (Dedicated connection)
const subscriber = new Redis();
subscriber.subscribe('game:room:room_123', (err, count) => {
  if (err) console.error('Subscription error', err);
});

subscriber.on('message', (channel, message) => {
  console.log(`Received message on ${channel}:`, JSON.parse(message));
});
```

---

## 7. Distributed Locks (Redlock / Atomic Lock)

```typescript
export async function acquireLock(lockKey: string, ttlMs = 5000): Promise<string | null> {
  const token = `${Date.now()}_${Math.random()}`;
  // NX: Only set if Not eXists, PX: Expire in milliseconds
  const result = await redis.set(`lock:${lockKey}`, token, 'PX', ttlMs, 'NX');
  return result === 'OK' ? token : null;
}

export async function releaseLock(lockKey: string, token: string): Promise<boolean> {
  // Lua script ensures atomic check-and-delete
  const luaScript = `
    if redis.call("get", KEYS[1]) == ARGV[1] then
      return redis.call("del", KEYS[1])
    else
      return 0
    end
  `;
  const result = await redis.eval(luaScript, 1, `lock:${lockKey}`, token);
  return result === 1;
}
```

---

## 8. Performance & Production Best Practices

1. **Pipelining**: Use `redis.pipeline()` to batch multiple commands into a single network round-trip.
2. **Key Naming Convention**: Use structured colon delimiters (`app:entity:id:attribute`, e.g. `memeverse:user:99:profile`).
3. **Avoid `KEYS *` in Production**: Never run `KEYS *` on live databases (blocks the single-threaded event loop). Use `SCAN` instead.
4. **Memory Optimization**: Use `maxmemory-policy allkeys-lru` or `volatile-lru` to auto-evict old keys when RAM limits are reached.
