from pydantic import BaseModel,constr

class ImageSchema(BaseModel):
    base64_string:constr(min_length=2)
    class Config:
        extra="forbid"