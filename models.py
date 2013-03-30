from sqlalchemy.orm import relationship, backref
from sqlalchemy import (
    Column,
    Integer,
    Unicode,
    UnicodeText,
    ForeignKey
    )

from . import DBSession, Base

class Company_Info(Base):
    __tablename__ = 'Company_Info'
    
    name = Column(Unicode(200), primary_key=True)
            
    
    
class Images(Base):
    __tablename__ = 'Images'
    
    i_name = Column(Unicode(200),primary_key=True)
    c_name = Column(Unicode(200),  ForeignKey( Company_Info.name))
    
       


        
class Smart_Text(Base):
    __tablename__ = 'Smart_Text'
    
    url=Column(Unicode(200))
    sms=Column(Unicode(200))
    email=Column(Unicode(200))
    ptcl = Column(Integer)
    cell = Column(Integer)
    c1_name=Column(Unicode(200),ForeignKey(Company_Info.name))





class Text_info(Base):
    __tablename__ = 'Text_info'
    description=Column(UnicodeText)
 
    c2_name=Column(Unicode(200),  ForeignKey( Company_Info.name))

