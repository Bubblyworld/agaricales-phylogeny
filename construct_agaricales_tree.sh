#!/usr/bin/env bash
raxml-ng --all --msa aligned_sequences.fasta --msa-format FASTA --model GTR+G --tree pars{25} --threads 4 --prefix AgaricalesTree
