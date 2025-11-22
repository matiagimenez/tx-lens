# 🪙 Explain My Crypto Transactions — AI Assistant

An AI system that converts raw blockchain transactions into clear, human-readable explanations.

---

## 🚀 MVP Features

### 🧱 Core Flow
1. **User inputs:**
   - Wallet address  
   - **or** raw transaction hash  

2. **System fetches on-chain data** using provider APIs:
   - Etherscan  
   - Blockscout  
   - Solana RPC  
   - (Extensible to more chains)

3. **Explanation Agent**
   - Interprets on-chain activity  
   - Produces simplified explanations  

**Example output**
> “You swapped **0.2 ETH → 350 USDC** on **Uniswap v3**.  
> Gas fees were **$14.25**.”

---

## 🔍 Optional MVP+ Agents

### **Risk Analysis Agent**
Flags:
- Suspicious addresses  
- Scam-like behavior  
- High-risk contract interactions  

### **Fee Breakdown Agent**
Outputs:
- Base fee  
- Priority fee  
- Gas used  
- Estimated USD total cost  

### **Contract Interaction Agent**
- ABI-aware method decoding  
- Explains contract purpose  
- Summarizes what the smart contract did  

---

## 📈 Scalable Multi-Agent Architecture

### 1. **Chain Router Agent**
- Detects which chain the transaction belongs to  
- Routes to the correct RPC/API client  
- Normalizes data structures  

### 2. **Transaction Fetcher Agent**
- Grabs:
  - Raw transaction  
  - Receipt  
  - Logs  
- Produces a unified internal format  

### 3. **Transaction Decoder Agent**
Decodes:
- ABI method calls  
- Token transfers  
- Swaps  
- DEX interactions  
- LP deposits/withdrawals  
- NFT transfers  

Optionally:
- Run VM-level simulations (Tenderly, anvil, local EVM) for advanced decoding  

### 4. **Explanation Agent**
- Converts decoded blockchain events into natural language  
- Uses templates depending on event type (swap, transfer, NFT sale, etc.)  

### 5. **Formatter Agent**
Outputs in:
- Markdown  
- JSON  
- Rich, structured messages for UI rendering  

---

## 🧱 Architecture Diagram (Mermaid)

```mermaid
flowchart TD

A[User Input: Wallet or Tx Hash] --> B[Chain Router Agent]
B --> C[Transaction Fetcher Agent]
C --> D[Transaction Decoder Agent]
D --> E[Explanation Agent]
E --> F[Formatter Agent]
