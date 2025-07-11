# Cursos de Graduação no Brasil 

<img src="/docs/images/mec.png" alt="Logo MEC" width="475" height="175">


## :mag: Resumo

Utilizando dados abertos do MEC através de técnicas de ciência de dados e aprendizado de máquina, foi desenvolvido um modelo preditivo que identifica se um determinado curso têm probabilidade de ser extinto. Dos oito algoritmos testados (KNN, Naive Bayes, MLP, Logistic Regression, SVM, Random Forest e XGBoost), o Random Forest apresentou o melhor desempenho com acurácia e F1-score de 85%. Os resultados deste projeto podem auxiliar instituições de ensino superior e órgãos governamentais na tomada de decisões estratégicas sobre a oferta de cursos.


## :file_folder: Arquivos

 - :game_die: [**Dataset**](https://dadosabertos.mec.gov.br/indicadores-sobre-ensino-superior/item/183-cursos-de-graduacao-do-brasil)

- :orange_book: **Notebooks**
    - [Análise Exploratória e Limpeza](/notebooks/01_exploratory_data_analysis_and_cleaning.ipynb)
    - [Pré-processamento](/notebooks/02_data_preprocessing.ipynb)
    - [Treinamento](/notebooks/03_model_training.ipynb)

- :page_facing_up: [**Relatório**](/docs/)

- :tv: [**Apresentação**](/docs/)


## :gear: Tecnologias Utilizadas

- **Linguagem:** Python 3.12
- **Bibliotecas de Análise de Dados:** Pandas, NumPy
- **Visualização:** Matplotlib, Seaborn
- **Machine Learning:** Scikit-learn, XGBoost
- **MLOps:** MLflow, DVC
- **API:** FastAPI
- **Interface:** Streamlit
- **Containerização:** Docker


## :whale: Rode meu modelo com Docker 

<img src="/docs/images/system_design.png" alt="System Design" width="700" height="350">

1. Faça o download do repositório via `git clone`.

2. Uma vez que você tenha o Docker e o Compose devidamente instalado, dentro da pasta raíz do projeto digite o seguinte comando no terminal:

```shell
docker compose up --build
```
3. Acesse o navegador e digite na barra de endereços:

```
https:\\localhost:8501
```

<img src="/docs/images/tela_1.png" alt="Tela 1" width="700" height="400">

<img src="/docs/images/tela_2.png" alt="Tela 2" width="700" height="400">


## :construction: Futuras features

Criar CI/CD.


## :busts_in_silhouette: Contribuidores

[Francisco Willem R. Moreira](https://github.com/willemromao) - Machine Learning Engineer


## :balance_scale: Licença

Este projeto está licenciado sob a [MIT License](/LICENCE).

## :mailbox: Contato

*franciscowillem@gmail.com*
