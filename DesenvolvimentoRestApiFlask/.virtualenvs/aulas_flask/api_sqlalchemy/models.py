from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import scoped_session, sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///atividades.db')
db_session = scoped_session(sessionmaker(autocommit=False, bind=engine))

base = declarative_base()
base.query = db_session.query_property()

class Pessoas(base):
    __tablename__ = 'pessoas'
    id = Column(Integer, primary_key=True)
    nome = Column(String(100), index=True)
    idade = Column(Integer)

    def __repr__(self): # funcao de representar algo
        return '<Pessoa - {}>'.format(self.nome)

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()

class Atividades(base):
    __tablename__ = 'atividades'
    id = Column(Integer, primary_key=True)
    nome_atividade = Column(String(200))
    pessoa_id = Column(Integer, ForeignKey('pessoas.id'))
    pessoa = relationship("Pessoas")

    def init_db():
        base.metadata.create_all(bind=engine)

    def __repr__(self): # funcao de representar algo
        return '<Atividades - {}>'.format(self.nome)

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()

    if __name__ == '__main__':
        init_db()


