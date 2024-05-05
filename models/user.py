import models
from models.base_model import BaseModel, Base
import hashlib
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """Representation of a user """
    if models.storage_t == 'db':
        __tablename__ = 'users'
        email = Column(String(128), nullable=False)
        _password = Column('password', String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        places = relationship("Place", backref="user")
        reviews = relationship("Review", backref="user")
    else:
        email = ""
        _password = ""
        first_name = ""
        last_name = ""

    def __init__(self, *args, **kwargs):
        """initializes user"""
        super().__init__(*args, **kwargs)

    @property
    def password(self):
        """Getter for password"""
        return self._password

    @password.setter
    def password(self, password):
        """Setter for password, hashes it to MD5"""
        encryption = hashlib.md5(password.encode())
        self._password = encryption.hexdigest()

    def to_dict(self, password=False):
        """returns a dictionary containing all keys/values of the instance"""
        new_dict = super().to_dict()
        if not password:
            new_dict.pop('password', None)
        return new_dict
