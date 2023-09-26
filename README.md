# Minha API

Este projeto de gerenciador de entrada e saidas, foi desenvolvido para gerenciar e planeja a uma oficina mecanica. 

---
## Como executar 

1 - Execute todas as libs do python listadas no `requirements.txt`.

```
pip install -r requirements.txt
```

2 - Instale ambientes virtuais com comando.

```
-m venv env
```
3 - Apos a instalação do ambiente, execute para ativar.

```
.\env\Scripts\Activate.ps1 
```

4 - executando a API:

```
flask run --host 0.0.0.0 --port 5000
```

5 - Abra seu navegador com link.

(http://localhost:5000/#/) 



## Como executar através do Docker

Certifique-se de ter o [Docker](https://docs.docker.com/engine/install/) instalado e em execução em sua máquina.

Navegue até o diretório que contém o Dockerfile e o requirements.txt no terminal.
Execute **como administrador** o seguinte comando para construir a imagem Docker:

```
docker build -t rest-api .
```

```
docker run -p 5000:5000 rest-api
```

Uma vez executando, para acessar a API, basta abrir o [http://localhost:5000/#/](http://localhost:5000/#/) no navegador.


### Alguns comandos úteis do Docker

>**Para verificar se a imagem foi criada**
>
>```
>docker images
>```
>
> **remover uma imagem**,
>```
>docker rmi <IMAGE ID>
>```
>
>**Para verificar se o container está em exceução** 
>
>```
>docker container ls --all
>```
>
> Caso queira **parar um conatiner**
>```
>docker stop <CONTAINER ID>
>```
>Subistituindo o `CONTAINER ID` pelo ID do conatiner
>
>
> Caso queira **destruir um conatiner**, basta executar o comando:
>```
>docker rm <CONTAINER ID>
>```
>Para mais comandos, veja a [documentação do docker](https://docs.docker.com/engine/reference/run/).