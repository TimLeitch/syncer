# backend/app/api/v1/endpoints/contacts.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.crud.contact import get_contact, create_contact
from app.schemas.contact import Contact, ContactCreate
from app.db.database import get_db

router = APIRouter()


@router.post("/contacts/", response_model=Contact)
def create_new_contact(contact: ContactCreate, db: Session = Depends(get_db)):
    return create_contact(db=db, contact=contact)


@router.get("/contacts/{contact_id}", response_model=Contact)
def read_contact(contact_id: int, db: Session = Depends(get_db)):
    db_contact = get_contact(db, contact_id=contact_id)
    if db_contact is None:
        raise HTTPException(status_code=404, detail="Contact not found")
    return db_contact
