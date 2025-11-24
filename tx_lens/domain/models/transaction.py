from pydantic import BaseModel, ConfigDict, Field, field_validator
from pydantic.alias_generators import to_camel


class Transaction(BaseModel):
    model_config = ConfigDict(populate_by_name=True, alias_generator=to_camel)

    hash_: str = Field(alias="hash")
    block_hash: str
    block_number: int
    from_: str = Field(alias="from")
    gas: int
    gas_price: int
    max_priority_fee_per_gas: int
    nonce: int
    to: str
    index: int = Field(alias="transactionIndex")
    value: int

    @classmethod
    @field_validator("block_hash", "hash_", mode="before")
    def hexbytes_to_str(cls, value: str | bytes) -> str:
        if isinstance(value, str):
            return value
        return value.hex()
