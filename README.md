## Atividade TDD

## Pré-requisitos

- Python 3
- Pacote `venv` (no Debian/Ubuntu: `sudo apt install python3-venv`)

## Configuração do ambiente

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Rodando os testes

Com o ambiente virtual ativado:

```bash
pytest
```

Outros exemplos:

```bash
pytest tests/test_exemplo.py            # um arquivo específico
pytest tests/test_exemplo.py::test_nome # um teste específico
pytest -k "nome"                        # testes cujo nome contém "nome"
```

As configurações do pytest ficam em `pytest.ini`. Os testes ficam em `tests/` (arquivos `test_*.py`) e o código em `app/`, importado nos testes como `from app.modulo import ...`.
