#!/usr/bin/env python3
# Example usage: ./make_tokenizer.py -k 2 -savepath tokenizer

import itertools
import pathlib

import tokenizers

from absl import app, flags

FLAGS = flags.FLAGS
flags.DEFINE_integer("k", None, "Number of nucleotides for k-mer sequence generation", lower_bound=1)
flags.DEFINE_string("savepath", None, "Path to save tokenizer parameters")

nucleotides = ["A", "C", "G", "T"]
unknown = "X"
padding = "P"
extras = [padding, unknown]


def make_tokenizer(k: int):
    """
    Make tokenizer for k-mer gene sequences.
    """
    keys = extras + list("".join(token) for token in itertools.product(*(nucleotides for _ in range(k))))
    values = range(len(keys))
    vocab = dict(zip(keys, values))
    tokenizer = tokenizers.Tokenizer(tokenizers.models.WordLevel(vocab=vocab, unk_token=unknown))
    tokenizer.enable_padding(pad_token="p")
    tokenizer.pre_tokenizer = tokenizers.pre_tokenizers.WhitespaceSplit()
    return tokenizer


def main(argv):
    del argv
    tokenizer = make_tokenizer(FLAGS.k)
    if FLAGS.savepath is not None:
        tokenizer.save(FLAGS.savepath + ".json", pretty=True)
        pathlib.Path(FLAGS.savepath).mkdir(parents=True, exist_ok=True)
        tokenizer.model.save(FLAGS.savepath)


if __name__ == "__main__":
    app.run(main)
