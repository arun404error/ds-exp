from pydantic import BaseModel,constr

class PathSchema(BaseModel):
    path:constr(min_length=2,max_length=800)
    class Config:
        extra="forbid"

class Base64Schema(BaseModel):
    base64_string:constr(min_length=2)

    class Config:
        extra="forbid"