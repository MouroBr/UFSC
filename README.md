# 🏋️ Centro de Treinamento Esportivo - Sistema de Gerenciamento

Este projeto é um sistema simples em Python para gerenciar alunos e suas matrículas em modalidades esportivas de um centro de treinamento. Ele permite cadastrar alunos, matriculá-los em esportes e verificar quem tem direito a desconto por participar de múltiplas modalidades.

---

## 📌 Descrição do Problema

O centro esportivo oferece quatro modalidades:

- Futebol
- Natação
- Vôlei
- Basquete

Em razão da alta taxa de desistências, a administração decidiu oferecer **50% de desconto na segunda modalidade** em diante para qualquer aluno que esteja matriculado em **duas ou mais modalidades**.

---

## 🔍 Análise do Sistema

### 🧩 Requisitos Funcionais

1. Cadastrar novos alunos.
2. Permitir matrícula em uma ou mais modalidades.
3. Exibir alunos por modalidade.
4. Identificar alunos com direito a desconto (2+ modalidades).
5. Contabilizar total de alunos por modalidade e no geral.

### 🧠 Decisões Técnicas

- **Python 3.10+**
- Uso de **Programação Orientada a Objetos (POO)** para encapsular regras de negócio.
- Uso de **conjuntos (`set`)** para evitar duplicidade de nomes nas modalidades.
- Armazenamento em **memória** (sem persistência em banco de dados ou arquivos).
- Aplicação de princípios de **Clean Code**, como:
  - Separação de responsabilidades por módulo
  - Nominação clara de métodos e variáveis
  - Tipagem com `type hints`

---

## ✅ Solução Aplicada

O sistema é dividido em módulos:

### 📁 Estrutura de Pastas

```
projeto/
├── alunos_matriculas.py   # Banco de dados em memória com POO
├── cadastro_aluno.py      # Classe Aluno (cadastro e matrícula)
├── relatorio.py           # Relatórios (descontos, totais, listagem)
└── main.py                # Interface do usuário via terminal
```

### 🔧 `BancoDeDados` (em `alunos_matriculas.py`)

Classe que simula um banco de dados:

```python
class BancoDeDados:
    self.alunos: dict[str, list[str]]
    self.futebol: set[str]
    self.natacao: set[str]
    self.volei: set[str]
    self.basquete: set[str]
```

### 👤 `Aluno` (em `cadastro_aluno.py`)

Classe que representa e gerencia um aluno:

- `cadastrar()`: adiciona o aluno ao sistema
- `matricular_em(modalidade)`: matricula o aluno na modalidade

### 📊 Relatórios (em `relatorio.py`)

Funções utilitárias:

- `listar_alunos_por_modalidade()`
- `alunos_com_direito_a_desconto()`
- `total_por_modalidade()`

---

## ▶️ Como Executar

1. Certifique-se de ter o Python 3.9+ instalado.
2. Clone ou baixe este repositório.
3. Execute o sistema:

```bash
python main.py
```

---

## 💡 Exemplo de Uso

```bash
=== Centro de Treinamento ===
1. Cadastrar e matricular aluno
2. Ver alunos por modalidade
3. Ver alunos com desconto
4. Ver totais de alunos
0. Sair
```

---

## 🧪 Possíveis Melhorias Futuras

- [ ] Persistência com JSON, SQLite ou CSV
- [ ] Interface gráfica (Tkinter ou PySide)
- [ ] API REST com FastAPI
- [ ] Testes automatizados com `pytest`
- [ ] Exportar relatórios em PDF ou CSV

---

## 📄 Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

---

## 👨‍💻 Autor

**Mouro** — Desenvolvedor e idealizador do sistema.
