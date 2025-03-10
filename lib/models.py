from sqlalchemy import ForeignKey, Column, Integer, String, MetaData,Boolean
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}
metadata = MetaData(naming_convention=convention)

Base = declarative_base(metadata=metadata)
class Role(Base):
    __tablename__ = 'roles'

    # Columns for the Role table
    id = Column(Integer, primary_key=True)
    character_name = Column(String, nullable=False)

    # One-to-many relationship: One role can have many auditions
    auditions = relationship('Audition', back_populates='role')

    def actors(self):
        """Returns a list of actor names associated with this role"""
        return [audition.actor for audition in self.auditions]

    def locations(self):
        """Returns a list of locations for auditions associated with this role"""
        return [audition.location for audition in self.auditions]

    def lead(self):
        """Returns the first hired audition (lead) or a message if none hired"""
        hired_auditions = [audition for audition in self.auditions if audition.hired]
        if hired_auditions:
            return hired_auditions[0]
        return 'no actor has been hired for this role'

    def understudy(self):
        """Returns the second hired audition (understudy) or a message if none hired"""
        hired_auditions = [audition for audition in self.auditions if audition.hired]
        if len(hired_auditions) > 1:
            return hired_auditions[1]
        return 'no actor has been hired for understudy for this role'


class Audition(Base):
    __tablename__ = 'auditions'

    # Columns for the Audition table
    id = Column(Integer, primary_key=True)
    actor = Column(String, nullable=False)
    location = Column(String, nullable=False)
    phone = Column(Integer, nullable=True)
    hired = Column(Boolean, default=False)
    role_id = Column(Integer, ForeignKey('roles.id'))

    # Many-to-one relationship: Each audition belongs to a role
    role = relationship('Role', back_populates='auditions')

    def call_back(self):
        """Changes the hired attribute to True (call back for the actor)"""
        self.hired = True