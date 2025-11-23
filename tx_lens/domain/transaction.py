from pydantic import BaseModel, Field


class Transaction(BaseModel):
    hash_: str = Field(alias="hash")
