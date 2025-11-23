from pydantic import BaseModel, ConfigDict, Field


class TransactionRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    hash_: str = Field(alias="hash", description="The transaction hash to explain")
    blockchain: str = Field(description="The blockchain network")


class TransactionResponse(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    hash_: str = Field(alias="hash")
    blockchain: str
    explanation: str
