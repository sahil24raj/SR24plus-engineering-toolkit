---
name: offline-first-kirana-architect
description: Specialist in offline-first retail architectures — local IndexedDB/OPFS SQLite, sync queues, conflict resolution, offline billing, and background sync for Indian retail.
---

# Offline-First Kirana SaaS & POS Architecture Engineer

## Role & Mission
The **Offline-First Kirana SaaS & POS Architecture Engineer** designs and builds resilient, zero-latency retail applications that function 100% reliably without internet connectivity and automatically synchronize data when connectivity returns.

---

## 1. Activation Conditions
Invoke this skill whenever:
- Designing a retail POS or billing interface for regions with spotty or intermittent 4G/WiFi.
- Implementing local storage persistence using IndexedDB, Dexie.js, or SQLite (WASM/OPFS).
- Building an offline order synchronization queue with retry backoff and conflict resolution.
- Ensuring Kirana merchants can create bills, take udhaar entries, and check inventory with zero network dependency.

---

## 2. Core Architecture: The Dual-Storage Engine

```
[UI / POS Screen]
        │
        ▼
[Local Fast Store (IndexedDB / SQLite WASM)] ───> Instant UI response (<10ms)
        │
        ▼
[Sync Queue Manager]
        │ (Detect online / offline)
        ▼
[Conflict Resolver & Cloud API Sync] ────────────> Backend Server (PostgreSQL)
```

---

## 3. Implementation: Sync Queue & Offline Store

### A. IndexedDB Schema Specification
```typescript
import Dexie, { Table } from 'dexie';

export interface LocalOrder {
  localId: string;
  items: Array<{ productId: number; qty: number; price: number }>;
  total: number;
  paymentMethod: 'CASH' | 'UPI' | 'UDHAAR';
  customerId?: number;
  createdAt: string;
  synced: boolean;
}

export interface SyncTask {
  id?: number;
  type: 'CREATE_ORDER' | 'UPDATE_STOCK' | 'ADD_UDHAAR';
  payload: any;
  retryCount: number;
  createdAt: string;
}

export class KiranaOfflineDB extends Dexie {
  orders!: Table<LocalOrder, string>;
  syncQueue!: Table<SyncTask, number>;

  constructor() {
    super('KiranaOfflineDB');
    this.version(1).stores({
      orders: 'localId, synced, createdAt',
      syncQueue: '++id, type, retryCount, createdAt',
    });
  }
}

export const localDb = new KiranaOfflineDB();
```

### B. High-Speed Offline Order Creation
```typescript
export async function createOfflineBill(orderData: Omit<LocalOrder, 'localId' | 'synced' | 'createdAt'>) {
  const localId = `local_${Date.now()}_${Math.random().toString(36).substring(2, 7)}`;
  const order: LocalOrder = {
    ...orderData,
    localId,
    synced: false,
    createdAt: new Date().toISOString(),
  };

  // 1. Write immediately to local database
  await localDb.orders.add(order);

  // 2. Queue synchronization task
  await localDb.syncQueue.add({
    type: 'CREATE_ORDER',
    payload: order,
    retryCount: 0,
    createdAt: new Date().toISOString(),
  });

  // 3. Trigger background sync attempt if online
  if (navigator.onLine) {
    triggerBackgroundSync();
  }

  return order;
}
```

### C. Background Sync Runner with Exponential Backoff
```typescript
let isSyncing = false;

export async function triggerBackgroundSync() {
  if (isSyncing || !navigator.onLine) return;
  isSyncing = true;

  try {
    const tasks = await localDb.syncQueue.orderBy('id').limit(20).toArray();

    for (const task of tasks) {
      try {
        const response = await fetch('/api/sync', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(task),
        });

        if (response.ok) {
          // Remove from sync queue
          await localDb.syncQueue.delete(task.id!);
          if (task.type === 'CREATE_ORDER') {
            await localDb.orders.update(task.payload.localId, { synced: true });
          }
        } else {
          // Increment retry count with exponential backoff limit
          await localDb.syncQueue.update(task.id!, { retryCount: task.retryCount + 1 });
        }
      } catch (networkErr) {
        // Network dropped mid-sync; exit loop until online event
        break;
      }
    }
  } finally {
    isSyncing = false;
  }
}

// Auto-trigger sync on network reconnect
window.addEventListener('online', () => triggerBackgroundSync());
```

---

## 4. Conflict Resolution Protocol: Stock & Udhaar
1. **Sales Transactions**: **Append-Only**. Orders created offline are never overwritten by the server; they are appended to the ledger using their `localId` as idempotency key.
2. **Stock Quantities**: **Delta-Based**. Instead of syncing `stock = 45`, sync `stockDelta = -2`. The server applies the subtraction atomically (`stock = stock - 2`).
3. **Customer Udhaar Ledger**: **Immutable Entries**. Each credit or payment is a new journal row with timestamp. Sum of transactions determines current outstanding balance.

---

## 5. Quality Checklist
- [ ] Application loads in < 500ms even when completely disconnected from network (Airplane Mode).
- [ ] Bills can be printed or sent via local bluetooth thermal printer without active internet.
- [ ] Sync queue guarantees FIFO order execution for ledger balance accuracy.
- [ ] Visual indicator shows distinct state: `● Online (All Synced)` vs `○ Offline (3 Bills Pending Sync)`.

