# 🚀 Tx Lens — Implementation Plan

Tx Lens is an AI-powered system that converts raw blockchain transactions into **clear, human-readable explanations** using a modular multi-agent architecture.

# 📌 Project Overview

**Goal:** Build an interpretable, multi-chain transaction explainer that fetches, decodes, and summarizes blockchain activity using AI.

**MVP Deliverable:**  
Given a transaction hash, Tx Lens returns:

- A classification (swap, transfer, NFT mint, etc.)
- A simple human-readable explanation
- Fees and USD cost
- Structured JSON output

## ✅ Phase 1 — Foundations

### 1. Project Setup

- Setup Python project (FastAPI recommended)
- Add environment handling (Pydantic Settings)
- Configure RPC/API providers:
- Alchemy/Infura (EVM)
- Blockscout
- Optional: Solana RPC

---

## ✅ Phase 2 — Core Querying Pipeline

### 2. Chain Router Agent

- Detects chain from tx hash or user input
- Routes to correct provider
- Normalizes chain-specific response shape

### 3. Transaction Fetcher Agent

Fetches:

- Raw transaction
- Transaction receipt
- Logs/events

Outputs a **unified internal transaction format**.

---

## ✅ Phase 3 — Decoding Layer

### 4. Transaction Decoder Agent

Responsibilities:

- Decode function selectors (4-byte)
- Decode logs (event signatures)
- Match common protocol ABIs (Uniswap, ERC20, ERC721)
- Classify transaction type:
- Transfer
- Swap
- Approval
- Liquidity actions
- NFT mint/transfer

### 5. Token Metadata Resolver

- Resolve token symbol, decimals, name
- Cache metadata locally
- Normalize token amounts

---

## ✅ Phase 4 — AI Explanation Engine

### 6. Explanation Agent

Inputs:

- Decoded transaction
- Token information
- USD conversions (optional)

Outputs:

- Short explanation
- Optional: detailed breakdown

### 7. Formatter Agent

Formats output into:

- Markdown
- JSON
- UI-ready "blocks"

---

## ✅ Phase 5 — API Layer

### 8. FastAPI Endpoints

**POST /tx**

```json
{
	"tx_hash": "...",
	"chain": "eth"
}
```

Response:

```json
{
  "summary": "...",
  "details": { ... },
  "fees": { ... }
}
```

## 🚀 Phase 6 — Optional MVP+ Agents

### 9. Fee Breakdown Agent

- Extract base fee, priority fee, gas used
- Compute total gas cost in ETH
- Convert to USD using price API
- Output structured fee breakdown:
  - base_fee
  - priority_fee
  - gas_used
  - gas_cost_eth
  - gas_cost_usd

### 10. Contract Interaction Agent

- Decode ABI methods using:
  - Known protocol ABIs (Uniswap, ERC20, ERC721, etc.)
  - 4byte directory API (optional)
- Detect contract type:
  - Token
  - Router/DEX
  - NFT contract
  - Proxy contract
- Summarize smart-contract actions:
  - approval
  - mint
  - swap
  - transfer
  - liquidity add/remove

---

## 🧪 Phase 7 — Testing

### 11. Testing Strategy

#### Unit Tests

- Transaction Fetcher (mock RPC responses)
- Chain Router logic
- Decoder (function signatures + event logs)
- Token Metadata Resolver
- Fee Breakdown Agent
- Explanation Agent (prompt testing)

#### Tools

- pytest
- pytest-asyncio
- responses or httpx-mock for API mocks

#### Test Cases

- ETH transfer
- ERC20 transfer
- Uniswap swap
- NFT mint
- Failed transaction
- Contract interaction with unknown ABI

---

## 📦 Phase 8 — Containerization

- Create `Dockerfile` for FastAPI service
