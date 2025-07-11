# Cursos de Graduação no Brasil 

<img src="/docs/images/MECAssinatura.png" alt="Logo MEC" width="475" height="175">


## Resumo

Este projeto apresenta os resultados do modelo treinado a partir de dados relacionado aos cursos de graduação no Brasil afim de prever a extinção de cursos. Dos oito algoritmos testados (KNN, Naive Bayes, MLP, Logistic Regression, SVM, Random Forest e XGBoost), o que melhor performou foi o Random Forest com acurácia e F1-score de 85%.

## Arquivos

 - :game_die: **Dataset:** [clique aqui](https://dadosabertos.mec.gov.br/indicadores-sobre-ensino-superior/item/183-cursos-de-graduacao-do-brasil).

- :orange_book: **Notebooks no Google Colab:**
    - Análises dos cursos: [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1yCHmQk89jnFskhuW80OsPiL4lkmY1uyh?usp=sharing)
    - Modelo de classificação: [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1cjlIiSwz_iGcU3cjy_JEaBgSwOyiqs9g?usp=sharing)

- :page_facing_up: **Relatórios:**
    - Análises dos cursos: [clique aqui](/relatorios/Relatório%20-%20Análises.pdf).
    - Modelo de classificação: [clique aqui](/relatorios/Relatório%20-%20Modelo%20de%20Classificação.pdf).

- :tv: **Slides:**
    - Análises dos cursos: [clique aqui](https://www.canva.com/design/DAGIb1KG7w4/agkKoljdXxc0T6Pu4ltI2Q/edit?utm_content=DAGIb1KG7w4&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton).
    - Modelo de classificação: [clique aqui](https://www.canva.com/design/DAGNBlGP3sk/9q8C1uXdTLg0E2j_212i7g/edit?utm_content=DAGNBlGP3sk&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton).

## :whale: Rode meu modelo com Docker 

<img src="/imgs/Fluxograma.png" alt="Fluxograma" width="700" height="350">

1. Faça o download do repositório via `git clone`.

2. Uma vez que você tenha o Docker e o Compose devidamente instalado, dentro da pasta raíz do projeto digite o seguinte comando no terminal:

```shell
docker compose up --build
```
3. Acesse o navegador e digite na barra de endereços:

```
https:\\localhost:8501
```

<img src="/imgs/screenshot1.png" alt="Fluxograma" width="700" height="350">

<img src="/imgs/screenshot2.png" alt="Fluxograma" width="700" height="350">


## Futuras features

- Colocar o modelo em produção usando MLOps e fazer o retreinamento sempre que o dataset for atualizado pelo Ministério da Educação.
