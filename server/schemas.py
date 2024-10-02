from pydantic import BaseModel

class UserSchema(BaseModel):
    nome: str

class CardSchema(BaseModel):
    uid: int

class DeviceSchema(BaseModel):
    nome: str

class AccessSchema(BaseModel):
    uid: int
    device_id: int