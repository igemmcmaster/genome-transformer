# genome-transformer

Apply the [Sub-Linear Memory Performer](https://arxiv.org/pdf/2012.11346.pdf) to genome sequences and see what happens.

## Background

What are transformers? This section describes the technology from a highly abstracted perspective.

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

