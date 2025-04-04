# Atividade sobre APIs, Crawlers, Scrapers e LGDP

**Alunos:<br>
Gustavo Lira Santos<br>
Rodolfo Bolconte Donato**

Documento com as questões da Atividade: https://docs.google.com/document/d/1q-XAd2g4dF_JS61axpLB4kvVnaYtvk6Mi9EZ56447Bo/edit?usp=sharing

## Ambiente de Execução

É importante criar um ambiente virtual do python e instalar as dependências para executar os código do presente repositório :

```
python -m venv env

.\env\Scripts\activate  # WINDOWS
source env/bin/activate  # LINUX

pip install -r requirements.txt
```

## Questão 2

A questão 2 pede a criação de um script para consumir informação da API do IBGE, em que ao informar um estado específico, deve ser mostrada uma lista de todas as cidades do respectivo estado.

Para executar o script da questão 2 basta utilizar o comando abaixo:

```
python questao2.py
```

Será solicitado o código do Estado Brasileiro para mostrar todas as cidades do mesmo.

## Questão 3

A questão 3 pede para criar um web scraper para consumir dados da página de professores do curso do Mestrado Profissional em Tecnologia de Informação do IFPB campus João Pessoa. A ideia é pegar as informações dos professores da página e criar um DataFrame com as mesmas.

Para executar o Scraper e pegar os dados dos professores do site basta executar - na raiz do repositório - o comando abaixo:

```
cls ; scrapy runspider .\scraper_professores_ifpb\scraper_professores_ifpb\spiders\professores.py --loglevel=WARNING
```

Um arquivo `professores.csv` com as informações dos professores será gerado na pasta em que o Scraper for executado (de preferência na raiz do repositório, de acordo com o comando anterior), a partir da criação de um DataFrame do Pandas criado com as informações da página dos professores.