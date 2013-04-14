from sqlalchemy.orm import relationship, backref
from sqlalchemy import (
    Column,
    Integer,
    Unicode,
    UnicodeText,
    ForeignKey
    )

from . import DBSession, Base

class Info_projects(Base):
    __tablename__= 'info_projects'
    ip_id=Column(Integer,primary_key=True)
    ip_description=Column(UnicodeText)
    name=Column(Unicode(200),unique=True)

class project_items(Base):
    __tablename__='project_items'
    pi_id=Column(Integer,primary_key=True)
    item_name=Column(Unicode(200))
    item_type=Column(Unicode(200))
    display_order=Column(Unicode(200))
    parent_item=Column(Unicode(200))
    infoproject_id = Column(Integer, ForeignKey(info_projects.ip_id))



