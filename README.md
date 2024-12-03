# Sistema de Gerenciamento de Estoque

## Como rodar?
- Clone esse repositório
- Crie um `virtualenv` com o Python 3
- Ative o `virtualenv`
- Instale as dependências
- Rode as migrações

```
git clone https://github.com/MCossetti/GerenciamentoEstoque.git
cd GerenciamentoEstoque
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python contrib/env_gen.py
python manage.py migrate
```