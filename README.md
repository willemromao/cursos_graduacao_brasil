# Cursos de Graduação Brasil 

<img src="/imgs/MECAssinatura.png" alt="Logo MEC" width="475" height="175">


## Resumo

Este projeto apresenta os resultados das análises e do modelo feito a partir de dados relacionado aos cursos de graduação no Brasil. Para as análises, a descoberta mais impactante foi que, organizações acadêmicas de categoria administrativa privada sem fins lucrativos tem uma proporção maior de cursos extintos e em processo de extinção. Já para o modelo que classifica extinção de cursos, dos três algoritmos testados (Árvore de Decisão, Florestas Aleatórias e Perceptron de Múltiplas Camadas), o que melhor performou foi o Florestas Aleatórias com 81% de acurácia.

## Arquivos

 - :game_die: **Dataset:** [clique aqui](https://dadosabertos.mec.gov.br/indicadores-sobre-ensino-superior/item/183-cursos-de-graduacao-do-brasil).

- :orange_book: **Notebooks no Google Colab:**
    - Análises dos cursos: [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1yCHmQk89jnFskhuW80OsPiL4lkmY1uyh?usp=sharing)
    - Modelo de classificação: [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1cjlIiSwz_iGcU3cjy_JEaBgSwOyiqs9g?usp=sharing)

- :page_facing_up: **Relatórios:**
    - Análises dos cursos: [clique aqui](/relatorios/Relatório%20-%20Análises.pdf).
    - Modelo de classificação: [clique aqui](/relatorios/Relatório%20-%20Modelo.pdf).

- :tv: **Slides:**
    - Análises dos cursos: [clique aqui](https://www.canva.com/design/DAGIb1KG7w4/agkKoljdXxc0T6Pu4ltI2Q/edit?utm_content=DAGIb1KG7w4&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton).
    - Modelo de classificação: [clique aqui](https://www.canva.com/design/DAGNBlGP3sk/9q8C1uXdTLg0E2j_212i7g/edit?utm_content=DAGNBlGP3sk&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton).

## Próximos passos

- Disponibilizar o modelo para uso geral na web através de uma API, onde o usuário poderá interagir de forma fácil e intuitiva.
- Colocar o modelo em produção usando MLOps e fazer o retreinamento sempre que o dataset for atualizado pelo Ministério da Educação.

## Observações

Cometi um pequeno equívoco na parte das análises (projeto 1), onde acabo utilizando imputação de dados na parte de tratamento de outliers, o correto seria fazer a remoção dos outliers usando IQR, por exemplo. O que aconteceu foi que eu me confundi tratando outliers com uma técnica de tratamento de valores ausentes. Em breve isso será resolvido.
