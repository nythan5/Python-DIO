"""
    Primeiro programa de integração com banco de dados
    utilizando SQLAlchemy e modelo ORM

"""
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import Session
from sqlalchemy.orm import relationship
from sqlalchemy import Column
from sqlalchemy import create_engine
from sqlalchemy import inspect
from sqlalchemy import select
from sqlalchemy import func
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey

Base = declarative_base()


class User(Base):
    """
        Esta classe representa a tabela user_account dentro
        do SQlite.
    """
    __tablename__ = "user_account"
    # atributos
    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)

    address = relationship(
        "Address", back_populates="user", cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"User(id={self.id}, name={self.name}, fullname={self.fullname})"


class Address(Base):
    __tablename__ = "address"
    id = Column(Integer, primary_key=True)
    email_address = Column(String(30), nullable=False)
    user_id = Column(Integer, ForeignKey("user_account.id"), nullable=False)

    user = relationship("User", back_populates="address")

    def __repr__(self):
        return f"Address(id={self.id}, email_address={self.email_address})"



# conexão com o banco de dados
engine = create_engine("sqlite://")

# criando as classes como tabelas no banco de dados
Base.metadata.create_all(engine)


# investiga o esquema de banco de dados
inspetor_engine = inspect(engine)
#print(inspetor_engine.has_table("user_account"))
print(inspetor_engine.get_table_names())
#print(inspetor_engine.default_schema_name)


# Criando uma sessão ao BD para persistir dados
with Session(engine) as session: 
    gabriel = User (
        name= "Gabriel",
        fullname = "Gabriel Nathan Dias",
        address= [Address(email_address="gabriel@email.com")]
    )

#Criando objetos para serem persistidos 
    cristiane = User (
        name= "Cristiane",
        fullname = "Cristiane Guimarães",
        address= [Address(email_address="cristiane@email.com"),
                  Address(email_address="cristianeguimaraes@email.com")]
    )

    fulano = User (name= "Fulano",fullname = "Fulano da Silva Santos")


# Para submeter as os registros
session.add_all([gabriel,cristiane,fulano])
session.commit()


# Recuperando a informações do BD
stmt_userg = select(User)
print("\n","Recuperando Usuário")
for user in session.scalars(stmt_userg):
    print(user)


stmt_user = select(User).where(User.name.in_(["Gabriel","Fulano"])) 
print("\n","Recuperando Usuário")
for user in session.scalars(stmt_user):
    print(user)


stmt_address = select(Address).where(Address.user_id.in_([2]))
print("\n","Recuperando Email usuário Cristiane")
for address in session.scalars(stmt_address):
    print(address)


# Realizando consultas com o Order by
order_by = select(User).order_by(User.name.desc())
print("\n","Recuperando Usuários com ORDER BY")
for user in session.scalars(order_by):
    print(user)


# Realizando consultas com o Join (junção entre as tabelas)
join_stmt = select(User.id,User.fullname,Address.email_address).join_from(Address,User)
print("\n","Recuperando Usuários com JOIN")
for result in session.scalars(join_stmt):
    print(result)

# Desta maneira /\ ele so tras o primeiro atributo no caso o "User.id"

# Executando o Join Statement apartir da connection e nao da session para obter todos os atributos
connection = engine.connect()
resultados = connection.execute(join_stmt).fetchall()
print("\n","Recuperando todos os atributos do JOIN")
for result in resultados:
    print(result)


# Função COUNT
count = select(func.count("*")).select_from(User)
print("\n","Recuperando Quantidade de registro na tabela USER")
for result in session.scalars(count):
    print(result)