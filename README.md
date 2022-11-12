# Tech News

## Sobre o projeto

O projeto Tech News consistem em uma aplicação em python para fazer consultas em notícias sobre tecnologia por meio de raspagem de dados.
As notícias são obtidas através da raspagem do [_blog da Trybe_](https://blog.betrybe.com).

## Habilidades

Habilidades desenvolvidas neste projeto:

* Utilizar o terminal interativo do Python
* Escrever os próprios módulos e importá-los em outros códigos
* Aplicar técnicas de raspagem de dados
* Extrair dados de conteúdo HTML
* Armazenar os dados obtidos em um banco de dados

## Orientações para a execução do projeto

Para executar o projeto é necessário ter o python3 instalado e o mongodb funcionando na máquina.
Faça o clone do projeto:

    git clone https://github.com/marceloalexandredacunhasimao/tech-news.git

Entre na pasta do projeto, crie e ative um ambiente virtual:

    cd tech-news
    python3 -m venv .venv && source .venv/bin/activate

Instale as dependências:

	python3 -m pip install -r dev-requirements.txt

Inicialize a execução do projeto:

    tech-news-analyzer

O funcionamento do projeto pode ser verificado pela interação com o menu apresentado.
