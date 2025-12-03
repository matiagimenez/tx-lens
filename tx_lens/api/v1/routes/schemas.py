from pydantic import BaseModel, ConfigDict, Field
from pydantic.alias_generators import to_camel

TX_EXAMPLE = "0x206d9ed0458f07377c05045b1c9d3e4cdb03c03141f4070f5f88dd512d74ddc0"
TX_REGEX = r"^0x[a-fA-F0-9]+$"


class TransactionRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True, alias_generator=to_camel)

    transaction_hash: str = Field(
        description="The transaction hash to explain",
        pattern=TX_REGEX,
        json_schema_extra={"examples": [TX_EXAMPLE]},
    )


class TransactionResponse(BaseModel):
    model_config = ConfigDict(populate_by_name=True, alias_generator=to_camel)

    transaction_hash: str = Field(
        description="The transaction hash to explain",
        pattern=TX_REGEX,
        json_schema_extra={"examples": [TX_EXAMPLE]},
    )
    explanation: str | dict
