from pydantic import BaseModel


class Output(BaseModel):
    res: int
