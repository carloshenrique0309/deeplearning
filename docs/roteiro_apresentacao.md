# Roteiro de apresentacao do projeto

## 1. Explicacao do problema escolhido

O problema escolhido foi a analise de sentimentos em reviews de filmes. O objetivo e construir um modelo de inteligencia artificial capaz de receber uma avaliacao escrita por um usuario e classificar automaticamente se o sentimento do texto e positivo ou negativo.

Esse tipo de problema faz parte da area de Processamento de Linguagem Natural (NLP), pois o modelo precisa interpretar textos escritos em linguagem humana e transformar esses textos em dados numericos para realizar a classificacao.

## 2. Motivacao para escolha do problema

A escolha desse problema foi motivada pela grande quantidade de opinioes publicadas diariamente em sites, redes sociais, lojas virtuais e plataformas de streaming. Empresas podem usar modelos de analise de sentimentos para entender rapidamente a percepcao dos usuarios sobre filmes, produtos, servicos ou marcas.

No contexto do projeto, as reviews de filmes sao um bom exemplo pratico porque os textos apresentam opinioes reais, com elogios, criticas, ironias e diferentes formas de escrita. Isso torna o problema interessante para aplicar tecnicas de deep learning em textos.

## 3. Explicacao do dataset

O dataset utilizado foi o IMDb Large Movie Review Dataset, disponibilizado pela Universidade de Stanford.

Link do dataset: https://ai.stanford.edu/~amaas/data/sentiment/

O conjunto de dados possui reviews de filmes separadas em duas classes:

- `pos`: reviews positivas.
- `neg`: reviews negativas.

O dataset ja vem dividido em treino e teste:

- Treino: 25.000 reviews, sendo 12.500 positivas e 12.500 negativas.
- Teste: 25.000 reviews, sendo 12.500 positivas e 12.500 negativas.

Cada review e armazenada como um arquivo `.txt`. O nome do arquivo tambem contem uma nota associada ao filme, mas neste projeto o foco foi usar apenas a classificacao binaria: positivo ou negativo.

## 4. Modelo escolhido

O modelo escolhido foi uma rede neural com TensorFlow/Keras para classificacao binaria de texto.

O pipeline usado foi:

- Limpeza simples dos textos.
- Vetorizacao com `TextVectorization`.
- Transformacao das palavras em sequencias numericas.
- Camada `Embedding` para representar palavras em vetores densos.
- Camada recorrente bidirecional `Bidirectional LSTM`.
- Camadas `Dense` e `Dropout`.
- Saida com ativacao `sigmoid`, indicando a probabilidade da review ser positiva.

A LSTM foi escolhida porque e uma arquitetura adequada para dados sequenciais, como textos, ja que considera a ordem das palavras na frase.

## 5. Metricas usadas

As metricas usadas para avaliar o modelo foram:

- Accuracy: porcentagem geral de previsoes corretas.
- Precision: entre as reviews previstas como positivas, quantas realmente eram positivas.
- Recall: entre as reviews positivas reais, quantas o modelo conseguiu identificar.
- F1-score: media harmonica entre precision e recall.
- Matriz de confusao: mostra acertos e erros separados por classe.

Resultado obtido no conjunto de teste:

```text
Accuracy: 0.8477
Precision: 0.9069
Recall: 0.7749
F1-score: 0.8357
```

Esses resultados mostram que o modelo teve desempenho proximo de 85% de acerto geral, o que e coerente para um primeiro modelo de deep learning aplicado ao dataset IMDb.

## 6. Demonstracao do modelo

A demonstracao pode ser feita pelo notebook `03_avaliacao_testes.ipynb`.

O notebook carrega o modelo salvo em:

```text
models/imdb_sentiment_model.keras
```

Depois, ele executa:

- Avaliacao no conjunto de teste.
- Relatorio com precision, recall e F1-score.
- Matriz de confusao.
- Previsoes com novas frases digitadas manualmente.

Exemplo de uso:

```python
novas_reviews = [
    "This movie is amazing, emotional and beautifully acted.",
    "The story was boring, predictable and way too long.",
]

probabilidades = model.predict(novas_reviews)
```

Se a probabilidade for maior ou igual a 0.5, a review e classificada como positiva. Caso contrario, e classificada como negativa.

### Exemplos utilizados na classificacao

Durante os testes, foram usadas frases novas para verificar como o modelo se comporta fora do conjunto de treino. A saida do modelo e uma probabilidade entre 0 e 1, indicando a chance da review ser positiva.

| Review usada no teste | Probabilidade de ser positiva | Classificacao do modelo |
| --- | ---: | --- |
| "This movie is amazing, emotional and beautifully acted." | 0.9516 | Positivo |
| "The story was boring, predictable and way too long." | 0.0725 | Negativo |
| "I liked the cast, but the script did not work for me." | 0.3487 | Negativo |
| "A fantastic film with great rhythm and memorable characters." | 0.8540 | Positivo |

Nos exemplos, o modelo classificou como positivas as frases com palavras e expressoes favoraveis, como `amazing`, `beautifully acted`, `fantastic` e `great`. Ja as frases com termos negativos ou criticos, como `boring`, `predictable` e `did not work for me`, receberam probabilidade menor que 0.5 e foram classificadas como negativas.

## 7. Conclusoes

O projeto mostrou que tecnicas de deep learning podem ser usadas para classificar automaticamente sentimentos em textos. O modelo conseguiu aprender padroes presentes nas reviews positivas e negativas e atingiu aproximadamente 85% de acuracia no conjunto de teste.

Durante o desenvolvimento, foi possivel observar a importancia das etapas de exploracao dos dados, preprocessamento, vetorizacao, treinamento e avaliacao. Tambem ficou claro que a qualidade da representacao textual influencia diretamente o desempenho do modelo.

Como melhorias futuras, seria possivel:

- Testar arquiteturas mais modernas, como GRU, CNN para texto ou Transformers.
- Ajustar hiperparametros, como tamanho do vocabulario, tamanho das sequencias e numero de epocas.
- Usar embeddings pre-treinados.
- Criar uma interface simples para o usuario digitar uma review e receber a classificacao.

## 8. Entrega

O grupo deve encaminhar o link do repositorio do projeto no GitHub para esta atividade ate a vespera a noite, dia 09 de junho de 2026.

