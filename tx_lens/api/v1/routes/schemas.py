from pydantic import BaseModel, ConfigDict, Field
from pydantic.alias_generators import to_camel


class TransactionRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True, alias_generator=to_camel)

    transaction_hash: str = Field(description="The transaction hash to explain")


class TransactionResponse(BaseModel):
    model_config = ConfigDict(populate_by_name=True, alias_generator=to_camel)

    transaction_hash: str
    explanation: str
