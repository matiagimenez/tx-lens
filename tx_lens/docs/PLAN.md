# 🚀 Tx Lens — Implementation Plan

Tx Lens is an AI-powered system that converts raw blockchain transactions into **clear, human-readable explanations** using a modular multi-agent architecture.

# 📌 Project Overview

**Goal:** Build an interpretable, multi-chain transaction explainer that fetches, decodes, and summarizes blockchain activity using AI.

**Strategy:**
The project will be implemented in two distinct stages to maximize learning and extensibility:

1.  **Stage 1: LangChain MVP** — A direct implementation using standard LangChain primitives (Chains, Runnables) to establish core functionality.
2.  **Stage 2: LangGraph Migration** — Refactoring the system into a graph-based architecture using LangGraph to handle complex state and cyclic flows.

**MVP Deliverable:**
Given a transaction hash, Tx Lens returns:

- A classification (swap, transfer, NFT mint, etc.)
- A simple human-readable explanation
- Fees and USD cost
- Structured JSON output

---

# 🏁 Stage 1: LangChain MVP

Focus on getting the core logic working using simple chains and tools.

## ✅ Phase 1 — Foundations

### 1. Project Setup

- Setup Python project (FastAPI recommended)
- Add environment handling (Pydantic Settings)
- Configure RPC/API providers:
  - Infura (EVM)
  - Blockscout

## ✅ Phase 2 — Core Querying Pipeline (LangChain)

### 2. Chain Router Chain

- Input: `tx_hash`
- Logic: Detects chain from hash format or user input
- Output: `chain_id` / `provider_url`

### 3. Transaction Fetcher Tool

- Input: `tx_hash`, `chain_id`
- Logic: Fetches raw tx, receipt, and logs
- Output: **Unified Internal Transaction Format**

## ✅ Phase 3 — Decoding Layer (LangChain)

### 4. Decoder Tools

- **Function Decoder**: Decodes 4-byte selectors
- **Log Decoder**: Decodes event signatures
- **ABI Matcher**: Matches against known protocols (Uniswap, ERC20, etc.)

### 5. Metadata Resolver Tool

- Fetches token symbols, decimals, names
- Normalizes amounts

## ✅ Phase 4 — AI Explanation Engine (LangChain)

### 6. Explanation Chain

- **Prompt Template**: Injects decoded tx data + metadata
- **LLM**: Generates human-readable summary
- **Output Parser**: Structured JSON (summary, details, fees)

## ✅ Phase 5 — API Layer

### 7. FastAPI Endpoints

- **POST /tx**
  - Triggers the LangChain pipeline
  - Returns structured response

---

# 🔄 Stage 2: LangGraph Migration

Refactor the linear chains into a stateful graph architecture.

## ✅ Phase 6 — Graph Architecture Design

### 8. State Definition

- Define `AgentState` (TypedDict) to hold:
  - `tx_hash`
  - `raw_tx_data`
  - `decoded_data`
  - `explanation`
  - `errors`

### 9. Node Implementation

- Convert "Chains" and "Tools" from Stage 1 into Graph Nodes:
  - `RouterNode`
  - `FetcherNode`
  - `DecoderNode`
  - `ExplainerNode`

---

# 🚀 Phase 7 — MCP Server Integration

### 12. MCP Server Setup

- Expose transaction tools through Model Context Protocol (MCP) server
- Implement MCP tool definitions:
  - `fetch_transaction`: Get raw transaction data
  - `explain_transaction`: Generate human-readable explanation
- Configure MCP server with proper authentication and error handling
- Enable AI assistants to directly query blockchain transactions
