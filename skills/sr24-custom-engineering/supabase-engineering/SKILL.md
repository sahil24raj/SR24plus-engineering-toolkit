---
name: supabase-engineering
description: >-
  Expert in Supabase PostgreSQL architecture — Row Level Security (RLS), Auth triggers, Edge Functions, Realtime channels, Storage buckets, and pgvector.
---

# Supabase Full-Stack Architecture & Realtime Backend

## 1. When to Activate
Activate this skill whenever a project or prompt requires expert in supabase postgresql architecture — row level security (rls), auth triggers, edge functions, realtime channels, storage buckets, and pgvector.. It is assigned to official engineering phases in the **SR24Plus Engineering Toolkit**.

## 2. When Not to Activate
- Do not activate when the task does not involve supabase-engineering.
- Do not activate as a substitute for simple static mockups where deeper engineering is unnecessary.

## 3. Core Capabilities
- Row Level Security (RLS) policy design with multi-tenant isolation and role-based access
- Database webhooks and triggers syncing authentication user profiles to public tables
- Realtime postgres_changes channels broadcasting live game state and notifications
- Deno/TypeScript Supabase Edge Functions with CORS, rate limiting, and Stripe/Razorpay webhooks
- Supabase Storage secure bucket policies with signed URL uploads for game assets

## 4. Engineering Workflow
1. **Discovery & Architecture**: Inspect technical constraints, performance requirements, and data contracts.
2. **Setup & Configuration**: Install official package dependencies and configure environment variables.
3. **Implementation**: Author production-grade code using clean architecture, strict TypeScript types, and error handling.
4. **Validation & Testing**: Run unit and integration tests confirming zero regressions.
5. **Production Deployment**: Verify build bundle impact, tree-shaking, and observability telemetry.

## 5. Implementation Instructions & Code Patterns

```typescript
-- 1. Create secure profiles table with RLS enabled
CREATE TABLE public.profiles (
  id UUID PRIMARY KEY REFERENCES auth.users(id) ON DELETE CASCADE,
  username TEXT UNIQUE NOT NULL,
  avatar_url TEXT,
  coins INT DEFAULT 500 CHECK (coins >= 0),
  level INT DEFAULT 1,
  created_at TIMESTAMPTZ DEFAULT NOW()
);

ALTER TABLE public.profiles ENABLE ROW LEVEL SECURITY;

-- 2. RLS Policies: Everyone can read public profiles; users can update own profile
CREATE POLICY "Public profiles are viewable by everyone."
  ON public.profiles FOR SELECT USING (true);

CREATE POLICY "Users can update their own profile."
  ON public.profiles FOR UPDATE USING (auth.uid() = id);

-- 3. Automatic user provisioning trigger
CREATE OR REPLACE FUNCTION public.handle_new_user()
RETURNS TRIGGER AS $$
BEGIN
  INSERT INTO public.profiles (id, username, avatar_url)
  VALUES (
    NEW.id,
    COALESCE(NEW.raw_user_meta_data->>'username', 'Gamer_' || SUBSTRING(NEW.id::text FROM 1 FOR 6)),
    NEW.raw_user_meta_data->>'avatar_url'
  );
  RETURN NEW;
END;
$$ LANGUAGE plpgsql SECURITY DEFINER;

CREATE TRIGGER on_auth_user_created
  AFTER INSERT ON auth.users
  FOR EACH ROW EXECUTE PROCEDURE public.handle_new_user();
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
- **Repository**: [https://github.com/supabase/agent-skills](https://github.com/supabase/agent-skills)
- **Category**: SR24-WEB-DEV Canonical Engineering Skill

## 10. License & Attribution
- **License**: MIT
- **Maintained By**: SR24Plus Autonomous Engineering Architecture
