# Sistema de Gerenciamento de Estoque

## Como rodar?
- Crie um `virtualenv` com o Python 3
- Ative o `virtualenv`
- Instale as dependências
- Rode as migrações

```
pyhton3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python contrib/env_gen.py
python manage.py migrate
```