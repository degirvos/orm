# models/base.py
from sqlalchemy import Column, Integer, String
from database import Base

class ResPartner(Base):
    __tablename__ = 'res_partner'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    
    def __repr__(self):
        return f"<ResPartner(id={self.id}, name='{self.name}')>"
