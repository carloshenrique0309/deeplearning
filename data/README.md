# Dados

O dataset IMDb deve ficar extraido em:

```bash
data/raw/aclImdb/
```

Essa pasta ja vem organizada em `train/test` e `pos/neg`, com cada review em um
arquivo `.txt`. Para a primeira versao do modelo, nao precisamos gerar CSV nem
copiar os textos para outra estrutura.

O pipeline de treino pode ler diretamente:

```bash
data/raw/aclImdb/train
data/raw/aclImdb/test
```

Se no futuro algum experimento precisar salvar arquivos intermediarios, use
`data/processed/`. Por enquanto essa pasta nao faz parte da estrutura inicial.

Os arquivos do dataset e artefatos processados ficam fora do Git para evitar
commits grandes.
