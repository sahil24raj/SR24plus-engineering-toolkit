---
name: zod-schema-validation
description: >-
  Expert in Zod TypeScript-first schema declaration and validation — type inference (z.infer),
  primitives, objects, arrays, unions, discriminated unions, enums, refinements (.refine, .superRefine),
  transforms (.transform), async validation, error formatting, API request/response validation,
  and integration with React Hook Form / Next.js / tRPC.
---

# Zod Schema Validation Expert Skill

Zod is a TypeScript-first schema declaration and validation library. It allows you to declare a validator once and automatically infer the static TypeScript type.

---

## 1. Core Primitives & Type Inference

```typescript
import { z } from 'zod';

// Schema Definition
export const UserSchema = z.object({
  id: z.string().uuid(),
  username: z.string().min(3).max(20).regex(/^[a-zA-Z0-9_]+$/, 'Alphanumeric only'),
  email: z.string().email(),
  age: z.number().int().min(13).optional(),
  role: z.enum(['ADMIN', 'MODERATOR', 'PLAYER']).default('PLAYER'),
  coins: z.number().nonnegative().default(100),
  tags: z.array(z.string()).min(1),
  createdAt: z.date().default(() => new Date()),
});

// Automatic Static Type Inference (Zero type duplication)
export type User = z.infer<typeof UserSchema>;
```

---

## 2. Parsing & Error Handling

```typescript
// Safe Parse (Recommended for APIs & UI: Does not throw)
const result = UserSchema.safeParse(incomingData);

if (!result.success) {
  // result.error is a ZodError
  const formattedErrors = result.error.flatten();
  console.error('Field Errors:', formattedErrors.fieldErrors);
  console.error('Form Errors:', formattedErrors.formErrors);
  return { error: formattedErrors.fieldErrors };
}

// Access validated and typed data
const validatedUser: User = result.data;

// Standard Parse (Throws ZodError on failure)
try {
  const user = UserSchema.parse(incomingData);
} catch (error) {
  if (error instanceof z.ZodError) {
    console.error(error.issues);
  }
}
```

---

## 3. Discriminated Unions (Polymorphic Events & State)

Ideal for game event messages, WebSocket payloads, and UI actions.

```typescript
export const GameEventSchema = z.discriminatedUnion('type', [
  z.object({
    type: z.literal('JOIN_ROOM'),
    roomId: z.string(),
    playerName: z.string(),
  }),
  z.object({
    type: z.literal('PLAYER_MOVE'),
    x: z.number(),
    y: z.number(),
    velocity: z.object({ vx: number, vy: number }).optional(),
  }),
  z.object({
    type: z.literal('CHAT_MESSAGE'),
    message: z.string().max(200),
  }),
]);

export type GameEvent = z.infer<typeof GameEventSchema>;

function handleGameEvent(event: GameEvent) {
  switch (event.type) {
    case 'JOIN_ROOM':
      console.log(`Player ${event.playerName} joined ${event.roomId}`);
      break;
    case 'PLAYER_MOVE':
      console.log(`Moved to ${event.x}, ${event.y}`);
      break;
    case 'CHAT_MESSAGE':
      console.log(`Chat: ${event.message}`);
      break;
  }
}
```

---

## 4. Refinements & Custom Validations

### `.refine()` (Cross-field Validation, Password Confirmation)
```typescript
export const SignupSchema = z
  .object({
    password: z.string().min(8, 'Password must be at least 8 characters'),
    confirmPassword: z.string(),
  })
  .refine((data) => data.password === data.confirmPassword, {
    message: "Passwords don't match",
    path: ['confirmPassword'], // Attach error to confirmPassword field
  });
```

### `.superRefine()` (Granular Multi-Issue Reporting & Async DB Checks)
```typescript
export const UsernameCheckSchema = z.object({
  username: z.string().superRefine(async (val, ctx) => {
    if (val.includes('admin')) {
      ctx.addIssue({
        code: z.ZodIssueCode.custom,
        message: 'Username cannot contain reserved word "admin"',
      });
    }

    // Example Async Database Uniqueness Check
    const exists = await checkUserExistsInDB(val);
    if (exists) {
      ctx.addIssue({
        code: z.ZodIssueCode.custom,
        message: 'Username is already taken',
      });
    }
  }),
});
```

---

## 5. Transforms & Preprocessing (Coercion & Sanitization)

```typescript
// Coerce strings from URL searchParams or HTML form inputs
export const QueryParamSchema = z.object({
  page: z.coerce.number().int().positive().default(1),
  limit: z.coerce.number().int().min(1).max(100).default(20),
  includeArchived: z.coerce.boolean().default(false),
});

// Transform strings (Trim, lowercase, hashing)
export const SanitizedEmailSchema = z
  .string()
  .trim()
  .toLowerCase()
  .email('Invalid email address')
  .transform((email) => email.toLowerCase());

// JSON String parsing transform
export const JSONConfigSchema = z
  .string()
  .transform((str, ctx) => {
    try {
      return JSON.parse(str);
    } catch {
      ctx.addIssue({ code: 'custom', message: 'Invalid JSON string' });
      return z.NEVER;
    }
  });
```

---

## 6. Next.js App Router API Validation Pattern

```typescript
// app/api/scores/route.ts
import { NextResponse } from 'next/server';
import { z } from 'zod';

const ScoreSubmissionSchema = z.object({
  gameId: z.string(),
  score: z.number().int().nonnegative(),
  signature: z.string().min(32),
});

export async function POST(req: Request) {
  try {
    const body = await req.json();
    const result = ScoreSubmissionSchema.safeParse(body);

    if (!result.success) {
      return NextResponse.json(
        { error: 'Invalid request payload', details: result.error.flatten().fieldErrors },
        { status: 400 }
      );
    }

    const { gameId, score, signature } = result.data;
    // Process verified score...

    return NextResponse.json({ success: true, score });
  } catch (error) {
    return NextResponse.json({ error: 'Malformed JSON' }, { status: 400 });
  }
}
```

---

## 7. React Hook Form Integration (`@hookform/resolvers/zod`)

```tsx
'use client';

import { useForm } from 'react-hook-form';
import { zodResolver } from '@hookform/resolvers/zod';
import { z } from 'zod';

const FormSchema = z.object({
  nickname: z.string().min(2, 'Nickname is too short'),
  betAmount: z.coerce.number().min(10, 'Minimum bet is 10 coins'),
});

type FormValues = z.infer<typeof FormSchema>;

export function BetForm() {
  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm<FormValues>({
    resolver: zodResolver(FormSchema),
  });

  const onSubmit = (data: FormValues) => {
    console.log('Valid Form Data:', data);
  };

  return (
    <form onSubmit={handleSubmit(onSubmit)} className="space-y-4">
      <div>
        <input {...register('nickname')} placeholder="Player Nickname" className="input" />
        {errors.nickname && <p className="text-red-500">{errors.nickname.message}</p>}
      </div>
      <div>
        <input type="number" {...register('betAmount')} placeholder="Bet Amount" className="input" />
        {errors.betAmount && <p className="text-red-500">{errors.betAmount.message}</p>}
      </div>
      <button type="submit">Place Bet</button>
    </form>
  );
}
```
