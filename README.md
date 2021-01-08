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

We could reduce the embeddings by taking their sum and consider the sum the embedding of the sequence, that is by summing `3 + 0 + 3 + 0 + 1 + 2 + 3 = 12` and taking `12` as the embedding of `TATACGA`.
This does not account for the position of the nucleotides however, because addition is commutative; `TATACGA` and `ATATCGA` produce the same embedding.
To solve this issue, we add a positional aspect to the embedding by adding the position to the nucleotide embedding and scaling the pair by `attn_i` before our sum reduction, such that the new sequence embedding is `attn_1 * (3 + 1) + attn_2 * (0 + 2) + attn_3 * (3 + 3) + attn_4 * (0 + 4) + attn_5 * (1 + 5) + attn_6 * (2 + 6) + attn_7 * (3 + 7) = f(40 | attn_i)` and the resulting embedding is some function of the attention weights `attn_i` and the nucleotide/position pairs which sum to `40`.

The motivation behind the nomenclature of the scaling factor as attention parallels how humans perceive, specifically our instinct to pay attention to things that we care about or things that we focus on.
Indeed, if an attention weight approaches zero then the nucleotide/position pair that it scales also diminishes towards zero, as if the nucleotide is ignored in or filtered from the sequence embedding.
For example in embedding `AT` as the attention of `A` approaches zero the following approximation holds: `0.0001 * (0 + 1) + attn_2 * (3 + 2) ≈ attn_2 * (3 + 2)`, consequently `AT ≈ xT` where `x` is a positional placeholder.
The ability to attend or filter specific nucleotides makes sense in terms of noisy regions that do not carry much information, such as non-coding sequences or wobble base pairs.
We have so far been operating with one-dimensional nucleotide embeddings fixed from the set `{0, 1, 2, 3}`.

We can further increase the capacity for the sequence embedding to contain information by adding dimensions to the nucleotide embedding and learning these embeddings instead of fixing them.
The transformation then maps one of `{A, C, G, T}` to an k-dimensional point `nuc = (x, y, z, c_1, c_2, ..., c_{k-3})` where `c_i` denote additional axis beyond the three-dimensional coordinate space.
In summary, both `attn_i` and `nuc_i` in a n-length gene sequence embedding `attn_1 * (nuc_1 + 1) + attn_2 * (nuc_2 + 2) + attn_3 * (nuc_3 + 3) + ... + attn_n * (nuc_n + n)` are learned via machine learning.

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

