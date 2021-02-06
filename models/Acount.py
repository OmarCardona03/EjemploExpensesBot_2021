import database.db as db
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship

class Account(db.Base):
    __tablename__ = 'accounts'

    id = Column('id', String(15), primary_key=True, nullable=False)
    balance = Column('balance', Float, server_default='0', nullable=False)
    earnings = relationship('Earning', back_populates='accounts')
    spendings = relationship('Spending', back_populates='accounts')
    def __init__(self, id, balance=0):
        self.id = id
        self.balance = balance
        
    def __repr__(self):
        return f"<Account {self.id}>"
