from __future__ import annotations
from typing import Dict, Set

class BancoDeDados:
    def __init__(self) -> None:
        self.alunos: Dict[str, list[str]] = {}
        self.futebol: Set[str] = set()
        self.natacao: Set[str] = set()
        self.volei: Set[str] = set()
        self.basquete: Set[str] = set()

    def get_alunos(self) -> Dict[str, list[str]]:
        return self.alunos

    def get_futebol(self) -> Set[str]:
        return self.futebol

    def get_natacao(self) -> Set[str]:
        return self.natacao

    def get_volei(self) -> Set[str]:
        return self.volei

    def get_basquete(self) -> Set[str]:
        return self.basquete

    def get_todas_modalidades(self) -> Dict[str, Set[str]]:
        return {
            "futebol": self.futebol,
            "natacao": self.natacao,
            "volei": self.volei,
            "basquete": self.basquete,
        }

db = BancoDeDados()
