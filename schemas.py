from pydantic import BaseModel



class BlogBase(BaseModel):
    title: str
    body: str


class UserBase(BaseModel):
    name: str
    email: str
    password: str
