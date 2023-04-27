# obi-worker

- O site da [OBI - Olimpiada Brasileira de Informatica](https://olimpiada.ic.unicamp.br/pratique/) é péssimo no quesito de corrigir questões. Porém, é o site oficial que abriga todo o banco de dados para treineiros. O script abaixo automatiza o envio de questões.

  
### Install depedencies
1.0 Para Linux:

- Crie um variavel de ambiente para armazenar as dependencias
```bash
python3 -m venv env && source ./env/bin/activate
```
1.1 Para windows:
```powershell
virtualenv .
activate
```

2 - Instale as dependencias
```bash
pip install selenium
```

### Usage
1 - Coloque o arquivo a ser enviado dentro do diretorio woker ou especificque o path e seu nome no arquivo [worker_config](./worker/worker_config.py)

2 - execute tanto a venv quanto o codigo

- Linux:
```bash
source ./env/bin/activate && python worker.py
```

- Windows:
```powershell
activate
python worker.py
```

###
