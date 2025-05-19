from __future__ import annotations
from alunos_matriculas import db

class Aluno:
    def __init__(self, nome: str) -> None:
        self.nome: str = nome.strip().title()

    def cadastrar(self) -> None:
        if self.nome not in db.get_alunos():
            db.get_alunos()[self.nome] = []
        else:
            print(f"⚠️ Aluno '{self.nome}' já cadastrado.")

    def matricular_em(self, esporte: str) -> None:
        if self.nome not in db.get_alunos():
            raise ValueError(f"Aluno '{self.nome}' não cadastrado.")

        esporte = esporte.strip().lower()

        if esporte == "futebol":
            db.get_futebol().add(self.nome)
        elif esporte == "natacao":
            db.get_natacao().add(self.nome)
        elif esporte == "volei":
            db.get_volei().add(self.nome)
        elif esporte == "basquete":
            db.get_basquete().add(self.nome)
        else:
            raise ValueError(f"Esporte '{esporte}' não reconhecido.")

        if esporte not in db.get_alunos()[self.nome]:
            db.get_alunos()[self.nome].append(esporte)
