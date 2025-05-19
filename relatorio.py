from __future__ import annotations
from typing import Dict, Set
from alunos_matriculas import db

def listar_alunos_por_modalidade() -> None:
    print("\n--- Alunos por Modalidade ---")
    modalidades: Dict[str, Set[str]] = db.get_todas_modalidades()
    for modalidade, alunos in modalidades.items():
        lista = sorted(alunos)
        print(f"{modalidade.capitalize()}: {', '.join(lista) if lista else 'Nenhum aluno matriculado'}")

def alunos_com_direito_a_desconto() -> None:
    modalidades: Dict[str, Set[str]] = db.get_todas_modalidades()
    contagem: Dict[str, int] = {}

    for alunos in modalidades.values():
        for aluno in alunos:
            contagem[aluno] = contagem.get(aluno, 0) + 1

    com_desconto = [aluno for aluno, qtd in contagem.items() if qtd >= 2]

    print("\n--- Alunos com direito a desconto (2+ modalidades) ---")
    if com_desconto:
        for nome in sorted(com_desconto):
            print(f"- {nome}")
    else:
        print("Nenhum aluno com direito a desconto.")

def total_por_modalidade() -> None:
    print("\n--- Total de alunos por modalidade ---")
    modalidades: Dict[str, Set[str]] = db.get_todas_modalidades()
    for modalidade, alunos in modalidades.items():
        print(f"{modalidade.capitalize()}: {len(alunos)}")

    total_geral = len(db.get_alunos())
    print(f"\n🎯 Total geral de alunos no Centro: {total_geral}")
