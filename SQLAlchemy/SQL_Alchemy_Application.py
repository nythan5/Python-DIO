import sqlalchemy
from sqlalchemy.orm import declarative_base 
from sqlalchemy.orm import relationship
from sqlalchemy import Column 
from sqlalchemy import *
from sqlalchemy import 



Base = declarative_base(
    "Adress", back_populates = "user" , cascade = "all, delete-orphan"
    
)


class User(Base):
    __table_name__ = "user_account"
    
    #atributos
    id = Column(Integer, primary_key=True,autoincrement=True)
    name = Column(String, nullable= False)
    full_name =  Column(String)
    adress = relationship()

    

class Adress(Base):
    __table_name__ = "adress"

    #atributos
    id = Column(Integer, primary_key=True, autoincrement=True)
    email_adress = Column(String(50), nullable= False, unique=True)
    user_id = Column(Integer,ForeignKey("user_acount.id"), nullable=False)