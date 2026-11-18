---
name: socketio-realtime
description: >-
  Expert in Socket.IO real-time bi-directional event-based communication — client & server architecture,
  Rooms, Namespaces, acknowledgements, middleware, disconnection handling, auto-reconnection,
  Redis Streams/PubSub Adapter for multi-node scaling, and Next.js / Node.js integration.
---

# Socket.IO Real-Time Engine Expert Skill

Socket.IO enables low-latency, bi-directional, and event-driven communication between a web client and a server. It uses Engine.IO underneath to establish WebSocket connections with HTTP long-polling fallbacks.

---

## 1. Server Architecture (Node.js / Express / HTTP)

```typescript
import http from 'http';
import express from 'express';
import { Server, Socket } from 'socket.io';

const app = express();
const server = http.createServer(app);

export const io = new Server(server, {
  cors: {
    origin: process.env.CLIENT_URL || 'http://localhost:3000',
    methods: ['GET', 'POST'],
    credentials: true,
  },
  pingInterval: 25000,
  pingTimeout: 20000,
  transports: ['websocket', 'polling'], // Prioritize WebSocket
});

// Authentication Middleware
io.use((socket: Socket, next) => {
  const token = socket.handshake.auth.token;
  if (!token) {
    return next(new Error('Authentication error: Missing token'));
  }
  // Validate token...
  socket.data.userId = 'user_123';
  next();
});

io.on('connection', (socket: Socket) => {
  console.log(`Socket connected: ${socket.id}, User: ${socket.data.userId}`);

  // Disconnect Handler
  socket.on('disconnect', (reason) => {
    console.log(`Socket ${socket.id} disconnected: ${reason}`);
  });
});

server.listen(4000, () => console.log('Socket.IO server running on port 4000'));
```

---

## 2. Rooms, Namespaces, & Broadcasting

### Rooms (Dynamic Matchmaking & Game Channels)
```typescript
io.on('connection', (socket: Socket) => {
  // 1. Join Room
  socket.on('join_game', async (roomId: string, callback) => {
    await socket.join(roomId);
    
    // Broadcast to everyone in room EXCEPT sender
    socket.to(roomId).emit('player_joined', {
      playerId: socket.id,
      userId: socket.data.userId,
    });

    // Acknowledge back to sender
    callback({ status: 'OK', roomId });
  });

  // 2. Broadcast Action to ALL users in room (including sender)
  socket.on('game_action', (data: { roomId: string; action: string }) => {
    io.in(data.roomId).emit('game_state_update', {
      action: data.action,
      from: socket.id,
      timestamp: Date.now(),
    });
  });

  // 3. Leave Room
  socket.on('leave_game', (roomId: string) => {
    socket.leave(roomId);
    socket.to(roomId).emit('player_left', { playerId: socket.id });
  });
});
```

### Namespaces (Segmented Logic)
```typescript
// Admin namespace with separate auth & logic
const adminNamespace = io.of('/admin');
adminNamespace.use((socket, next) => {
  if (socket.handshake.auth.role !== 'ADMIN') {
    return next(new Error('Unauthorized admin access'));
  }
  next();
});

adminNamespace.on('connection', (socket) => {
  socket.emit('system_metrics', { cpu: 45, activeRooms: 12 });
});
```

---

## 3. Client Architecture & React / Next.js Hook

### Singleton Client Instance
```typescript
// lib/socket.ts
import { io, Socket } from 'socket.io-client';

let socket: Socket | null = null;

export const getSocket = (authToken?: string): Socket => {
  if (!socket) {
    socket = io(process.env.NEXT_PUBLIC_WS_URL || 'http://localhost:4000', {
      autoConnect: false,
      auth: { token: authToken },
      reconnection: true,
      reconnectionAttempts: 10,
      reconnectionDelay: 1000,
      reconnectionDelayMax: 5000,
      transports: ['websocket'],
    });
  }
  return socket;
};
```

### React Custom Hook
```tsx
'use client';

import { useEffect, useState } from 'react';
import { getSocket } from '@/lib/socket';

export function useGameSocket(roomId: string, token?: string) {
  const [isConnected, setIsConnected] = useState(false);
  const [gameState, setGameState] = useState<any>(null);

  useEffect(() => {
    const socket = getSocket(token);

    if (!socket.connected) {
      socket.connect();
    }

    function onConnect() {
      setIsConnected(true);
      socket.emit('join_game', roomId, (response: any) => {
        console.log('Joined room callback:', response);
      });
    }

    function onDisconnect() {
      setIsConnected(false);
    }

    function onStateUpdate(state: any) {
      setGameState(state);
    }

    socket.on('connect', onConnect);
    socket.on('disconnect', onDisconnect);
    socket.on('game_state_update', onStateUpdate);

    return () => {
      socket.off('connect', onConnect);
      socket.off('disconnect', onDisconnect);
      socket.off('game_state_update', onStateUpdate);
      socket.emit('leave_game', roomId);
    };
  }, [roomId, token]);

  const sendAction = (action: string) => {
    const socket = getSocket();
    socket.emit('game_action', { roomId, action });
  };

  return { isConnected, gameState, sendAction };
}
```

---

## 4. Scaling Across Multiple Nodes (Redis Adapter)

When running multiple Node.js instances behind a load balancer (e.g., NGINX / AWS ALB), use the Redis Adapter to sync rooms and broadcasts across server processes.

```bash
npm install @socket.io/redis-adapter ioredis
```

```typescript
import { createAdapter } from '@socket.io/redis-adapter';
import Redis from 'ioredis';

const pubClient = new Redis(process.env.REDIS_URL!);
const subClient = pubClient.duplicate();

io.adapter(createAdapter(pubClient, subClient));
```

---

## 5. Acknowledgements & Request-Response Pattern

```typescript
// Client side: Send event with timeout acknowledgement
socket.timeout(5000).emit('make_move', { row: 2, col: 1 }, (err, response) => {
  if (err) {
    console.error('Move timed out, please retry');
  } else {
    console.log('Move accepted by server:', response);
  }
});

// Server side: Reply via callback function
socket.on('make_move', (moveData, callback) => {
  const isValid = validateMove(moveData);
  if (!isValid) {
    return callback({ success: false, reason: 'Invalid square' });
  }
  applyMove(moveData);
  callback({ success: true, newBoard: getBoard() });
});
```

---

## 6. Resilience & Production Best Practices

1. **Prefer `transports: ['websocket']`**: Disabling polling skips the initial HTTP handshake and connects directly over WebSocket when sticky sessions are tricky.
2. **Handle Reconnection State Resync**: When a disconnected client reconnects, the server must push the latest authoritative snapshot (`socket.on('connect') -> fetchLatestState()`).
3. **Prevent Memory Leaks in React**: Always remove event listeners (`socket.off('event', handler)`) in the `useEffect` cleanup return.
4. **Rate Limit Sockets**: Validate and rate-limit client incoming event frequency to avoid denial-of-service in fast-clicking games.
