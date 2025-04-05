# Segmentação de clientes de um supermercado/*Customer Segmentation for a Supermarket

PT

📌 Visão Geral
A segmentação de clientes com base em parâmetros pré-definidos como gastos com compras, renda anual, idade, sexo ajudam na formulação de estratégias de acordo com o perfil desses clientes. 

Este projeto tem como objetivo segmentar esses clientes de acordo com os parâmetros fornecidos no dataset, usando kmeans, as bibibliotecas scikitlearn, matplotlib, pandas, técnicas de aprendizado não supervisionado de clusterização e  redução de diemnsionalidade

O conjunto de dados contém:
✅ Idade
✅ Gênero
✅ Renda Anual (k$)
✅ Pontuação de Gastos (1-100) (métrica definida pelo supermercado com base no comportamento de compra)

🎯 Objetivo
Identificar grupos de clientes com características semelhantes para auxiliar o supermercado em:

Estratégias de marketing personalizadas

Ofertas direcionadas

Melhorias na experiência do cliente


EN

## **📌 Overview**  
This project aims to segment supermarket customers based on demographic and behavioral data using **unsupervised machine learning (K-Means Clustering)**.  

The dataset includes:  
✅ **Age**  
✅ **Gender**  
✅ **Annual Income (k$)**  
✅ **Spending Score (1-100)** *(a metric defined by the supermarket based on shopping behavior)*  

🔗 **Original Dataset:** [Mall Customer Segmentation Data | Kaggle](https://www.kaggle.com/vjchoudhary7/customer-segmentation-tutorial-in-python)  

---

## **🎯 Goal**  
Identify customer groups with similar traits to help the supermarket with:  
- **Personalized marketing strategies**  
- **Targeted promotions**  
- **Improved customer experience**  

---

## Detalhes do dataset utilizado e resumo dos resultados

🔍 Análise Exploratória (EDA)
Foram realizadas análises estatísticas e visualizações para entender a distribuição dos dados

📊 Visualizações Principais
Pairplot, histogramas, boxplots, matriz de correlação


⚙️ Pré-processamento
Foram aplicadas as seguintes transformações:

One-Hot Encoding para a variável categórica (Gender).

PowerTransformer para normalizar as variáveis numéricas (Age, Annual Income, Spending Score).


🤖 Modelagem (K-Means Clustering)

📌 Segmentação dos Clientes
Pontuação de gastos | Renda | Idade | Número Cluster
--- | --- | --- | ---
Altos | Moderada | Jovens | 0
Baixos | Baixo | Moderada | 1
Altos | Alta | Jovens Adultos | 2
Baixos | Alta | Moderada | 3
Moderados | Moderado | Alta | 4


📊 Visualização 3D com PCA
Para melhor visualização, reduzi a dimensionalidade usando PCA (3 componentes).

📌 Conclusões
Clientes jovens com alta pontuação de gastos e baixa renda (Cluster 0) podem ser alvos de promoções.

Clientes com alta renda e baixa pontuação de gastos (Cluster 3) podem ser incentivados com ofertas premium.

Clientes idosos com gastos moderados (Cluster 4) podem receber descontos em produtos específicos.



Link original para o dataset: https://www.kaggle.com/vjchoudhary7/customer-segmentation-tutorial-in-python

EN

 ## **🔍 Exploratory Data Analysis (EDA)**  
Statistical and visual analyses were performed to understand data distribution:  

### **📊 Key Visualizations**  
1. **Pairplot (Variable Relationships)**  

   sns.pairplot(df_analise, diag_kind='kde', hue='Gender')
Histograms & Boxplots


⚙️ Preprocessing
Applied transformations:

One-Hot Encoding for categorical data (Gender).

PowerTransformer for numerical features (Age, Income, Spending Score).


🤖 Modeling (K-Means Clustering)
Pipeline

📌 Customer Segments
Cluster	Spending Score	Income	Age
0	High	Low	Young
1	Low	Low	Middle-aged
2	High	High	Young Adults
3	Low	High	Middle-aged
4	Moderate	Moderate	Elderly

📊 3D Visualization (PCA)
Reduced dimensionality using PCA (3 components):

📌 Conclusions
Young, high-spending, low-income customers (Cluster 0): Target with promotions.

High-income, low-spending customers (Cluster 3): Offer premium products.

Elderly, moderate spenders (Cluster 4): Discounts on essentials.

Clique no botão **Use this template** para criar um novo repositório com base neste modelo.


Versões das bibliotecas:

-------------------- | ----------
     Biblioteca      |   Versão  
-------------------- | ----------
Matplotlib           |      3.9.2
NumPy                |     1.26.4
Pandas               |      2.2.3
Scikit-Learn         |      1.5.1
Seaborn              |     0.13.2

Versão do Python: 3.12.3

## Configuração do ambiente

1. Faça o clone do repositório que será criado a partir deste modelo.

    ```bash
    git clone ENDERECO_DO_REPOSITORIO
    ```

2. Crie um ambiente virtual para o seu projeto utilizando o gerenciador de ambientes de sua preferência.

    a. Caso esteja utilizando o `conda`, exporte as dependências do ambiente para o arquivo `ambiente.yml`:

      ```bash
      conda env export > ambiente.yml
      ```

    b. Caso esteja utilizando outro gerenciador de ambientes, exporte as dependências
    para o arquivo `requirements.txt` ou outro formato de sua preferência. Adicione o
    arquivo ao controle de versão, removendo o arquivo `ambiente.yml`.



Para mais informações sobre como usar Git e GitHub, [clique aqui](https://cienciaprogramada.com.br/2021/09/guia-definitivo-git-github/). Sobre ambientes virtuais, [clique aqui](https://cienciaprogramada.com.br/2020/08/ambiente-virtual-projeto-python/).
