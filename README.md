# Agaricales Phlyogeny

Constructs a phylogenetic tree of the Agaricales from scratch, using only open-source data and tools. You'll need the following prerequisites to run the scripts in this repo:

```bash
brew install poetry
brew install mafft
brew install raxml-ng
```

Then install the dependencies in this project and drop into a python virtualenv:

```bash
poetry install
```

Finally, run the scripts in this order:

```bash
poetry run python fetch_agaricales_sequences.py
./align_agaricales_sequences.sh
./construct_agaricales_tree.sh
```
