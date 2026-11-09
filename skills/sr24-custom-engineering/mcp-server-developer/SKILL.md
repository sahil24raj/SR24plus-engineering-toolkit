---
name: mcp-server-developer
description: Master developer of Model Context Protocol (MCP) servers — JSON-RPC 2.0 tools, resources, prompts, Zod input validation, stdio/SSE transports, and sandboxing.
---

# Model Context Protocol (MCP) Server Developer

## Role & Mission
The **MCP Server Developer** designs, implements, tests, and deploys production-grade Model Context Protocol (MCP) servers. You expose APIs, databases, microservices, and local operating system tools to AI agents using the official MCP standard with strict input validation and secure sandboxing.

---

## 1. Activation Conditions
Invoke this skill whenever:
- Building custom MCP servers in TypeScript (`@modelcontextprotocol/sdk`) or Python (`mcp`).
- Exposing enterprise databases, third-party APIs, or command-line tools to AI coding agents.
- Defining MCP Tool Schemas with Zod, resource providers, or prompt templates.
- Debugging MCP transport issues (stdio vs Server-Sent Events / SSE).
- Extending the SR24Plus toolkit or building tools for Exam Loop.

---

## 2. Implementation: Production TypeScript MCP Server

```typescript
import { Server } from '@modelcontextprotocol/sdk/server/index.js';
import { StdioServerTransport } from '@modelcontextprotocol/sdk/server/stdio.js';
import { CallToolRequestSchema, ListToolsRequestSchema } from '@modelcontextprotocol/sdk/types.js';
import { z } from 'zod';

// 1. Initialize MCP Server Instance
const server = new Server(
  {
    name: 'sr24-exam-loop-engine',
    version: '1.0.0',
  },
  {
    capabilities: {
      tools: {},
      resources: {},
    },
  }
);

// 2. Define Strict Zod Validation Schemas
const GenerateQuestionSchema = z.object({
  topic: z.string().min(2).max(100),
  difficulty: z.enum(['EASY', 'MEDIUM', 'HARD']),
  questionType: z.enum(['MCQ', 'ASSERTION_REASON', 'SUBJECTIVE']),
  curriculum: z.string().default('CBSE_CLASS_12'),
});

// 3. Register Available Tools
server.setRequestHandler(ListToolsRequestSchema, async () => {
  return {
    tools: [
      {
        name: 'generate_assessment_item',
        description: 'Generates a standardized educational test question with distractor rationales.',
        inputSchema: {
          type: 'object',
          properties: {
            topic: { type: 'string', description: 'Subject topic, e.g. Organic Chemistry' },
            difficulty: { type: 'string', enum: ['EASY', 'MEDIUM', 'HARD'] },
            questionType: { type: 'string', enum: ['MCQ', 'ASSERTION_REASON', 'SUBJECTIVE'] },
            curriculum: { type: 'string', default: 'CBSE_CLASS_12' },
          },
          required: ['topic', 'difficulty', 'questionType'],
        },
      },
    ],
  };
});

// 4. Handle Tool Execution with Input Validation & Error Boundaries
server.setRequestHandler(CallToolRequestSchema, async (request) => {
  const { name, arguments: args } = request.params;

  if (name === 'generate_assessment_item') {
    const parseResult = GenerateQuestionSchema.safeParse(args);
    if (!parseResult.success) {
      return {
        isError: true,
        content: [{ type: 'text', text: `Validation Error: ${JSON.stringify(parseResult.error.format())}` }],
      };
    }

    const { topic, difficulty, questionType } = parseResult.data;

    // Execute business logic safely
    const questionItem = {
      id: `q_${Date.now()}`,
      stem: `What is the primary product of the reaction between Ethanol and Concentrated H2SO4 at 443K?`,
      options: ['Ethene', 'Diethyl ether', 'Ethyl hydrogen sulphate', 'Ethane'],
      correctOptionIndex: 0,
      rationale: 'At 443K, concentrated sulphuric acid dehydrates ethanol to produce ethene.',
      difficulty,
      topic,
    };

    return {
      content: [{ type: 'text', text: JSON.stringify(questionItem, null, 2) }],
    };
  }

  throw new Error(`Tool not found: ${name}`);
});

// 5. Connect Stdio Transport
async function main() {
  const transport = new StdioServerTransport();
  await server.connect(transport);
  console.error('SR24 Exam Loop MCP Server running on stdio');
}

main().catch((err) => {
  console.error('Fatal MCP Server Error:', err);
  process.exit(1);
});
```

---

## 3. Security Hardening for MCP Tools
1. **No Unsanitized Shell Execution**: Never pass raw arguments to `child_process.exec` or `eval()`. Use `child_process.execFile` with explicit argument arrays.
2. **Filesystem Whitelisting**: For tools reading or writing files, resolve absolute paths and verify they reside within the designated workspace root (`path.resolve(targetPath).startsWith(workspaceRoot)`).
3. **Sensitive Key Masking**: Never return raw database connection strings, passwords, or cloud credentials in MCP tool output.

---

## 4. Quality Checklist
- [ ] Tool returns structured JSON in `content` blocks.
- [ ] All inputs validated via Zod schemas before processing.
- [ ] MCP server handles `stdio` closed events cleanly without zombie processes.
- [ ] Tool errors set `isError: true` with human-readable diagnostic messages.
