# IMDb Reviews Dataset

- Alunos: Carlos Henrique de Brito Teles, William Wallace Ribeiro Matos e Pedro Martins Rodrigues
- Link do Dataset: https://ai.stanford.edu/~amaas/data/sentiment/

## Descrição do projeto

Análise de Sentimentos com Deep Learning

O objetivo do projeto é criar um modelo de inteligência artificial capaz de identificar se uma avaliação de filme é positiva ou negativa usando o dataset IMDb Reviews.

O sistema receberá um texto escrito por um usuário e fará a classificação automaticamente com técnicas de NLP (Processamento de Linguagem Natural) e Deep Learning utilizando TensorFlow/Keras.

# Principais etapas do projeto

## Coletar e entender os dados do dataset
- Download do dataset
- Análise da estrutura dos dados
- Identificação das classes positivas e negativas

## Fazer o pré-processamento dos textos
- Limpeza dos textos
- Remoção de caracteres especiais
- Tokenização
- Transformação em números
- Padding das sequências

## Dividir os dados em treino e teste
- Separação dos dados para treinamento e validação do modelo

## Criar e treinar uma rede neural
- Utilização de LSTM ou GRU
- Embedding Layer
- Camadas recorrentes
- Dense Layers

## Avaliar o desempenho do modelo
Métricas utilizadas:
- Accuracy
- Precision
- Recall
- F1-Score

## Testar previsões com textos novos

Exemplo:

```python
review = "This movie is amazing!"
# Resultado: Positivo
```

## Salvar o modelo treinado para uso futuro

```python
model.save("sentiment_model.h5")
```

# Tecnologias utilizadas

- TensorFlow/Keras
- Python
- NLP
- NumPy
- Pandas
- Matplotlib
- Seaborn
- Scikit-learn

# Resultado esperado

Um modelo capaz de classificar automaticamente reviews de filmes com boa precisão (aproximadamente 85% a 90%).

# Estrutura do projeto

```bash
IMDb-Sentiment-Analysis/
│
├── data/
├── notebooks/
├── models/
├── src/
├── requirements.txt
├── README.md
└── main.py
```
