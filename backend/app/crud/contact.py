# backend/app/crud/contact.py

from sqlalchemy.orm import Session
from app.models.contact import Contact
from app.schemas.contact import ContactCreate


def get_contact(db: Session, contact_id: int):
    return db.query(Contact).filter(Contact.id == contact_id).first()


def create_contact(db: Session, contact: ContactCreate):
    db_contact = Contact(name=contact.name, email=contact.email,
                         phone_number=contact.phone_number)
    db.add(db_contact)
    db.commit()
    db.refresh(db_contact)
    return db_contact
