# Engenharia de Dados – Trilha Alura

Repositório dedicado à minha evolução técnica na trilha de Engenharia de Dados da Alura.

Este projeto não é apenas um conjunto de exercícios, mas um ambiente estruturado com boas práticas de engenharia, organização de código, versionamento e qualidade automática.

---

## 🎯 Objetivo

Consolidar conhecimentos em:

- SQL e modelagem de dados
- ETL/ELT
- Manipulação de dados com Python
- Orquestração de pipelines
- Boas práticas de organização de projetos
- Containerização
- Estrutura profissional de código

---

## 🧰 Stack Utilizada

- Python 3.12
- pyenv + venv
- Ruff (lint)
- Black (formatação)
- Pytest
- Pre-commit
- Docker
- JupyterLab

---

## 📂 Estrutura do Repositório

```

alura-engenharia-dados/
│
├── src/                # Código reutilizável
├── notebooks/          # Exploração e exercícios
├── pipelines/          # Scripts executáveis
├── data/
│   ├── raw/            # Dados brutos
│   └── processed/      # Dados transformados
├── tests/              # Testes automatizados
├── docs/               # Documentação complementar

```

---

## 📈 Organização por Módulos

Cada módulo da trilha será organizado por domínio técnico, não apenas por exercício.

- notebooks/modulo_x
- pipelines/modulo_x
- código reutilizável dentro de src/

---

## 🧠 Decisões de Arquitetura

- Uso de `src layout` para evitar imports acidentais
- Separação clara entre dados brutos e processados
- Qualidade automática com pre-commit
- Estrutura pensada para escalabilidade

---

## 🚀 Evolução

Este repositório será atualizado progressivamente conforme avanço na trilha.
Cada módulo representará um incremento técnico estruturado.

---

## 📚 Módulos Concluídos / Em Andamento

- [Módulo 01 – Pipeline de Dados](docs/modulo_01_pipeline_dados.md)
