from pydantic import BaseModel, Field


class Ackerman(BaseModel):
    m: int = Field(0, ge=0)
    n: int = Field(0, ge=0)
