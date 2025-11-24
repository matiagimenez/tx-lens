from pydantic import BaseModel, ConfigDict, Field, field_validator
from pydantic.alias_generators import to_camel


class TransactionReceipt(BaseModel):
    model_config = ConfigDict(populate_by_name=True, alias_generator=to_camel)

    transaction_hash: str
    transaction_index: int
    block_hash: str
    block_number: int
    from_: str = Field(alias="from")
    to: str
    gas_used: int
    contract_address: str | None = Field(default=None)
    cumulative_gas_used: int
    effective_gas_price: int
    status: int

    # pylint: disable=no-self-use, no-self-argument
    @field_validator(
        "block_hash",
        "transaction_hash",
        "contract_address",
        mode="before",
    )
    def hexbytes_to_str(cls, value: str | bytes) -> str:
        if isinstance(value, str) or not value:
            return value  # type: ignore[return-value]
        return value.hex()
