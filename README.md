# genome-transformer

Apply the [Sub-Linear Memory Performer](https://arxiv.org/pdf/2012.11346.pdf) to genome sequences and see what happens.

## Background

What are transformers? This section describes the technology from a highly abstracted perspective.

In order to compute something, that something must first be transformed into a numeric representation of itself.
The genome can be formalized in many different methods, one of which is a sequence of letters within the set `{A, C, G, T}`; if we substitute each letter of the set with a unique number, we already have transformed a gene sequence into a numerical representation.
For example, `TATACGA` is transformed into `3030120`, where the transformation is defined by the mappings `A → 0`, `C → 1`, `G → 2`, and `T → 3`.
The numerical representation is termed the "embedding".

An embedding can also be thought of as a point (position vector if you fancy that) in a coordinate space.
In the previous example, if each number within the sequence is considered a point, a one-dimensional, denoted here as the x-axis, coordinate space filled with seven points is made: `x: {3, 0, 3, 0, 1, 2, 3}`.
The problem with these embeddings is that they are not too useful; at most, they can be used to identify each nucleotide, as the mapping is to a unique number.
However, they cannot contain higher-order patterns or knowledge, such as whether the gene sequence should be a promoter, coding sequence, or terminator.
In fact, because we consider each nucleotide as its own embedding, we are limited in scope to the nucleotide level and cannot contain any knowledge at the gene sequence level within the embeddings.

The transformer is a class of neural networks that learns the transformation for generating representatively powerful embeddings given many examples of the inputs and outputs of the transformation.

## Deliverables

- [ ] Fetch pretraining data: genomes
- [ ] Make tokenizer and tokenize gene sequences
- [ ] Understand how to use Google Research's SLiM Performer [code](https://github.com/google-research/google-research/tree/master/performer/models/slim_performer)
- [ ] Pretrain SLiM Performer
- [ ] Release pretrained model weights

## Credit and Citations

```bibtex
@article{slim_performer,
  author    = {Valerii Likhosherstov and
               Krzysztof Choromanski and
               Jared Davis and
               Xingyou Song and
               Adrian Weller},
  title     = {Sub-Linear Memory: How to Make Performers SLiM},
  journal   = {CoRR},
  volume    = {abs/2012.11346},
  year      = {2020},
  url       = {https://arxiv.org/abs/2012.11346},
  archivePrefix = {arXiv},
  eprint    = {2012.11346}
}
```

