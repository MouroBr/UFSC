from __future__ import annotations
from cadastro_aluno import Aluno
import relatorio

def menu() -> None:
    while True:
        print("\n=== 🏋️ Centro de Treinamento Esportivo ===")
        print("1. ➕ Cadastrar e matricular aluno")
        print("2. 📋 Ver alunos por modalidade")
        print("3. 💸 Ver alunos com desconto")
        print("4. 📊 Ver totais de alunos")
        print("0. ❌ Sair")

        opcao: str = input("Escolha uma opção: ").strip()

        if opcao == "1":
            nome: str = input("Nome do aluno: ").strip().title()
            if not nome:
                print("⚠️ Nome não pode ser vazio.")
                continue

            aluno = Aluno(nome)
            aluno.cadastrar()

            while True:
                modalidade: str = input("Matricular em (futebol/natacao/volei/basquete ou 'fim'): ").strip().lower()
                if modalidade == "fim":
                    break
                try:
                    aluno.matricular_em(modalidade)
                    print(f"✅ {nome} matriculado em {modalidade}.")
                except ValueError as e:
                    print(f"❌ {e}")

        elif opcao == "2":
            relatorio.listar_alunos_por_modalidade()

        elif opcao == "3":
            relatorio.alunos_com_direito_a_desconto()

        elif opcao == "4":
            relatorio.total_por_modalidade()

        elif opcao == "0":
            print("👋 Encerrando o sistema. Até logo!")
            break

        else:
            print("❌ Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
