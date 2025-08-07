from sqlalchemy import Engine, select
from sqlalchemy.orm import Session

from models import Categoria


def listar(engine: Engine):
    with Session(engine) as session:
        sentenca = select(Categoria).order_by(Categoria.nome)
        registros = session.execute(sentenca).scalars()
        print("Id, Nome, #produtos, Data cadastro, Data de modificação")
        for categoria in registros:
            print(f"{categoria.id}, {categoria.nome}, {len(categoria.lista_de_produtos)}, "
                  f"{categoria.dta_cadastro}, {categoria.dta_atualizacao}")


def adicionar(engine: Engine):
    with Session(engine) as session:
        nome = input("Nome de categoria: ")
        categoria = Categoria()
        categoria.nome = nome
        session.add(categoria)
        try:
            session.commit()
        except:
            print("Erro na insercao")
        else:
            print("Categoria adicionada")

def modificar(engine: Engine):
    with Session(engine) as session:
        sentenca = select(Categoria).order_by(Categoria.nome)
        categoria = session.execute(sentenca).scalars()
        dicionario = dict()
        contador = 1
        for c in categoria:
            print(f"{contador} - {c.nome}")
            dicionario[contador] = c.id
            contador += 1
        id = int(input("Digite o número da categoria que deve ser alterada: "))
        categoria = session.get_one(Categoria, dicionario[id])
        nome = input("Novo nome da categoria: ")
        categoria.nome = nome
        try:
            session.commit()
        except:
            print("Erro na atualizacao")

        else:
            print("Categoria atualizada")

def remover(engine: Engine):
    with Session(engine) as session:
        sentenca = select(Categoria).order_by(Categoria.nome)
        categoria = session.execute(sentenca).scalars()
        dicionario = dict()
        contador = 1
        for c in categoria:
            print(f"{contador} - {c.nome}")
            dicionario[contador] = c.id
            contador += 1
        id = int(input("Digite o número da categoria que deve ser alterada: "))
        categoria = session.get_one(Categoria, dicionario[id])
        session.delete(categoria)
        try:
            session.commit()
        except:
            print("Erro na remoção")

        else:
            print("Categoria removida")