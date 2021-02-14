#!/usr/bin/python3

import gzip
from pathlib import Path

from absl import app, flags
from Bio import SeqIO

FLAGS = flags.FLAGS
flags.DEFINE_string("datadir", None, "Path to data directory containing *.gbff.gz files")


def extract_seq(path: Path):
    with gzip.open(path, "rt") as f:
        return SeqIO(f, "genbank").seq


def main(argv):
    del argv


if __name__ == "__main__":
    app.run(main)
