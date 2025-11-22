from pydantic import BaseModel, Field


class TransactionRequest(BaseModel):
    transaction_hash: str = Field(..., description="The transaction hash to explain")
    blockchain: str = Field(default="ethereum", description="The blockchain network")


class TransactionResponse(BaseModel):
    transaction_hash: str
    explanation: str
    blockchain: str

    class Config:
        json_schema_extra = {
            "example": {
                "transaction_hash": "0x1234567890abcdef",
                "explanation": "This transaction transferred 1.5 ETH from Alice to Bob",
                "blockchain": "ethereum",
            }
        }
