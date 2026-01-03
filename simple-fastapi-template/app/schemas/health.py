from pydantic import BaseModel

class Health(BaseModel):
    message: str
    status_code: int