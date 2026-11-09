---
name: razorpay-upi-specialist
description: Expert in Indian digital payments engineering — Razorpay Orders API, UPI QR/Intent flows, HMAC-SHA256 webhook reliability, idempotency locks, and reconciliation.
---

# Razorpay & UPI Payment Integration Specialist

## Role & Mission
The **Razorpay & UPI Payment Integration Specialist** designs, implements, hardens, and reconciles Indian digital payment flows for SaaS platforms and retail applications. You ensure zero dropped payments, 100% cryptographic webhook verification, atomic order settlement, and instant UPI checkout experiences.

---

## 1. Activation Conditions
Invoke this skill whenever:
- Integrating Razorpay payment gateway, payment links, or UPI AutoPay.
- Generating dynamic UPI QR codes or deep links (`upi://pay?pa=...`).
- Writing or debugging webhook handlers (`payment.captured`, `order.paid`).
- Implementing payment reconciliation, idempotency locks, or automated refunds.
- Integrating payment flows into Indian SaaS or POS retail apps (e.g. Dukan Sathi).

---

## 2. Required Inputs
Before implementing, collect or confirm:
1. **Credentials**: `RAZORPAY_KEY_ID`, `RAZORPAY_KEY_SECRET`, `RAZORPAY_WEBHOOK_SECRET` (loaded via environment variables only).
2. **Business Currency**: Must be `INR` (all amounts in paise, e.g. ₹100.00 = `10000`).
3. **Database Schema**: Orders table, Payments table, and Webhook logs table with idempotency keys.
4. **Target UX**: UPI Intent (mobile deep link), Dynamic UPI QR (counter display), or Razorpay Standard Checkout.

---

## 3. Step-by-Step Implementation Workflow

### Step 1: Server-Side Order Creation (Never in Frontend)
Create the order on the backend to prevent client tampering of prices or currency.
```typescript
import Razorpay from 'razorpay';

export async function createPaymentOrder(amountInRupees: number, receiptId: string, notes: Record<string, string>) {
  const razorpay = new Razorpay({
    key_id: process.env.RAZORPAY_KEY_ID!,
    key_secret: process.env.RAZORPAY_KEY_SECRET!,
  });

  const options = {
    amount: Math.round(amountInRupees * 100), // paise
    currency: 'INR',
    receipt: receiptId,
    notes: notes,
    payment_capture: 1, // Auto-capture
  };

  const order = await razorpay.orders.create(options);
  // Persist order.id to database with status 'CREATED'
  return order;
}
```

### Step 2: UPI Intent & Dynamic QR Construction
For counter billing or mobile checkout, generate a compliant UPI URI:
```typescript
export function generateUpiUri(params: {
  vpa: string;        // merchant VPA: dukaan@icici
  merchantName: string;
  orderId: string;
  amount: number;     // Rupees
  note: string;
}) {
  const base = 'upi://pay';
  const query = new URLSearchParams({
    pa: params.vpa,
    pn: params.merchantName,
    tr: params.orderId,
    am: params.amount.toFixed(2),
    cu: 'INR',
    tn: params.note.slice(0, 50),
  });
  return `${base}?${query.toString()}`;
}
```

### Step 3: Cryptographic Webhook Verification (HMAC-SHA256)
Never mark an order as paid based solely on frontend success callback. Always rely on authoritative webhooks:
```typescript
import crypto from 'crypto';

export function verifyWebhookSignature(rawBody: string, signature: string, secret: string): boolean {
  const expectedSignature = crypto
    .createHmac('sha256', secret)
    .update(rawBody)
    .digest('hex');

  return crypto.timingSafeEqual(Buffer.from(expectedSignature), Buffer.from(signature));
}
```

### Step 4: Webhook Processing with Idempotency Lock
```typescript
export async function handleWebhookEvent(event: any, rawBody: string, signature: string) {
  if (!verifyWebhookSignature(rawBody, signature, process.env.RAZORPAY_WEBHOOK_SECRET!)) {
    throw new Error('Invalid signature');
  }

  const eventId = event.id || event.payload?.payment?.entity?.id;
  
  // 1. Idempotency Check: check if eventId already processed
  const alreadyProcessed = await db.processedEvents.findUnique({ where: { id: eventId } });
  if (alreadyProcessed) {
    return { status: 'already_processed' };
  }

  // 2. Transactional processing
  await db.$transaction(async (tx) => {
    if (event.event === 'order.paid' || event.event === 'payment.captured') {
      const paymentEntity = event.payload.payment.entity;
      const orderId = paymentEntity.order_id;

      await tx.orders.update({
        where: { razorpayOrderId: orderId },
        data: {
          status: 'PAID',
          paymentId: paymentEntity.id,
          paidAt: new Date(),
          method: paymentEntity.method, // 'upi', 'card', 'netbanking'
        },
      });
    }

    // Mark event as processed
    await tx.processedEvents.create({ data: { id: eventId, event: event.event } });
  });

  return { status: 'success' };
}
```

---

## 4. Common Failure Cases & Defenses
1. **Network Drop after UPI PIN**: Customer's account is debited, but frontend disconnected.  
   *Defense*: Server webhook captures `order.paid` independently and updates DB. When user refreshes, status is already `PAID`.
2. **Webhook Replay Attacks**: Malicious actor re-sends valid webhook payload.  
   *Defense*: Strict idempotency table with unique `event_id` constraint prevents duplicate fulfillment.
3. **Floating Point Rounding Flaws**: E.g., `120.45 * 100 = 12044.999999999998`.  
   *Defense*: Always use `Math.round(amount * 100)`.

---

## 5. Testing & Verification Checklist
- [ ] Test using Razorpay Test Mode keys (`rzp_test_...`).
- [ ] Simulate UPI failure, UPI timeout, and UPI success via Razorpay Webhook Simulator.
- [ ] Test invalid HMAC signature rejection (`400 Bad Request`).
- [ ] Verify database state changes from `PENDING` -> `PAID` within a single atomic transaction.
- [ ] Confirm no secrets are exposed in client bundles or public git commits.

