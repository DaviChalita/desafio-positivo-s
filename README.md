Como rodar: \
Crie um arquivo .env na raiz do projeto com as seguintes variáveis de ambiente, as defina na máquina aonde o código irá rodar ou caso rode via Pycharm também pode definir os valores nas variáveis de ambiente do run configuration

MONGO_DB_NAME={nome do seu banco de dados} \
MONGO_USER={nome do seu usuário admin} \
MONGO_PASS={senha do seu usuário admin} \
MONGO_URL={ip da conexão localhost}:{porta de acesso ao banco}

Caso rode fora do docker, é necessário usar o comando para instalar as dependências: pip install -r /caminho/para/requirements.txt

Na raiz do projeto, rode **docker compose up** 

Caso queira rodar via Pycharm, no run configuration coloque: module -> uvicorn \
e no script parameters -> app.main:app --reload

Para acessar o Swagger: http://localhost:8000/docs#/

Para rodar os testes, rode o código fora do docker com o comando na raiz do projeto: pytest

_Uso de IA para dúvidas pontuais aonde as respectivas documentações não eram claras + na geração dos testes_  
