from pydantic import BaseModel


class ContactBase(BaseModel):
    name: str
    email: str
    phone_number: str


class ContactCreate(ContactBase):
    pass


class Contact(ContactBase):
    id: int

    class Config:
        from_attributes = True
