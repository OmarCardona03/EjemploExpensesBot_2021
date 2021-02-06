import database.db as db
from sqlalchemy import Column, Integer, String, Float, Date, DateTime, ForeignKey,func
from sqlalchemy.orm import relationship

class Spending(db.Base):
    __tablename__ = 'spendings'

    id = Column('id', Integer, primary_key=True, autoincrement=True)
    amount = Column('amount', Float, nullable=False)
    when = Column('when', DateTime, server_default=func.now(),    nullable=True)
    accounts_id = Column('accounts_id', String(15), ForeignKey('accounts.id',    onupdate='CASCADE', ondelete='CASCADE'), nullable=False)
    accounts = relationship("Account", back_populates="spendings")

    def __init__(self, amount, when, accounts_id):
        self.amount = amount
        self.when = when
        self.accounts_id = accounts_id

def __repr__(self):
    return f"<Spending {self.id}>"
