from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from lib.models import Audition, Role

# Create engine and session
engine = create_engine('sqlite:///theater.db')
Session = sessionmaker(bind=engine)

# Create a new role
def create_role(character_name):
    session = Session()
    new_role = Role(character_name=character_name)
    session.add(new_role)
    session.commit()
    session.close()

# Create a new audition
def create_audition(actor, location, role_id):
    session = Session()
    audition = Audition(actor=actor, location=location, role_id=role_id)
    session.add(audition)
    session.commit()
    session.close()

# Get all roles
def get_all_roles():
    session = Session()
    roles = session.query(Role).all()
    session.close()
    return roles

# Get all auditions for a role
def get_auditions_for_role(role_id):
    session = Session()
    auditions = session.query(Audition).filter_by(role_id=role_id).all()
    session.close()
    return auditions

# Update the hired status of an audition
def update_audition_hired_status(audition_id, hired_status):
    session = Session()
    audition = session.query(Audition).get(audition_id)
    if audition:
        audition.hired = hired_status
        session.commit()
    session.close()
    
    # Update audition locations from "Stage 1" to "Theatre 1" and "Stage 2" to "Theatre 2"
def update_audition_location():
    session = Session()
    
    # Update all existing auditions
    auditions = session.query(Audition).all()
    
    for audition in auditions:
        if audition.location == "Stage 1":
            audition.location = "Theatre 1"
        elif audition.location == "Stage 2":
            audition.location = "Theatre 2"
    
    session.commit()
    session.close()


# Delete an audition
def delete_audition(audition_id):
    session = Session()
    audition = session.query(Audition).get(audition_id)
    if audition:
        session.delete(audition)
        session.commit()
    session.close()
