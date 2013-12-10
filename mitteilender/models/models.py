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
    __tablename__ = 'info_projects'

    ip_id = Column(Integer, primary_key=True)
    name = Column(Unicode(200), unique=True)
    ip_description = Column(UnicodeText)

    def __json__(self, request):
        return dict(ip_id=self.ip_id, name=self.name, description=self.ip_description)


class project_items(Base):
    __tablename__ = 'project_items'

    pi_id = Column(Integer, primary_key=True)
    infoproject_id = Column(Integer, ForeignKey(Info_projects.ip_id))
    item_name = Column(Unicode(200))
    item_value = Column(Unicode(1000))
    item_type = Column(Unicode(200))
    display_order = Column(Unicode(200))
    parent_item = Column(Unicode(200))

    project = relationship(Info_projects, backref=backref('items'))

    def __json__(self, request):
        d = dict(
            item_name=self.item_name,
            item_type=self.item_type,
            item_value=self.item_value
        )

        if hasattr(self, 'subitems'):
            d['subitems'] = self.subitems

        return d

class db_itemss(Base):
    __tablename__ = 'db_itemss'

    db_item_id = Column(Integer, primary_key=True)
    projectitem_id = Column(Integer, ForeignKey(project_items.pi_id))
    field_name = Column(Unicode(200))
    field_type = Column(Unicode(200))
    
    #dbproject = relationship(db_recordss, backref=backref('items'))
    

class db_recordss(Base):
    __tablename__ = 'db_recordss'

    db_rec_id = Column(Integer, primary_key=True)
    
    dbitem_id = Column(Integer, ForeignKey(db_itemss.db_item_id), primary_key=True)
    
    db_item_value = Column(Unicode(200))
      



