from sqlalchemy import Engine, select
from sqlalchemy.dialects.mysql import DECIMAL
from sqlalchemy.orm import Session

from app_categorias import selecionar_categoria
from models import Produto, Categoria
from decimal import *

def listar(engine: Engine):
    with Session(engine) as session:
        stmt = select(Produto).order_by(Produto.nome)
        produtos = session.execute(stmt).scalars()
        print("Nome, Preco, Estoque, Ativo, Nome da Categoria, Data Cadastro, Data de Modificacao")
        for produto in produtos:
            print(f"{produto.id}, {produto.nome}, {produto.estoque}, "
                  f"{"Ativo" if produto.ativo else "Inativo"}, {produto.categoria.nome}, "
                  f"{produto.dta_cadastro}, {produto.dta_atualizacao}")

def adicionar(engine: Engine):
    with Session(engine) as session:
        p = Produto()
        p.nome = input("Qual o nome do produto? : ")
        p.preco = Decimal(input("Qual o preco do produto? R$"))
        p.estoque = int(input("Qual o estoque inicial do produto? "))
        x = input("O produto esta ativo? (S/N)? ").lower()
        p.ativo = True if x[0] == "s" else False
        print("Selecione a categoria do produto:")
        p.categoria = selecionar_categoria(session)
        session.add(p)
        try:
            session.commit()
        except:
            print("Erro na insercao do produto")
        else:
            print("Produto incluido com sucesso")



