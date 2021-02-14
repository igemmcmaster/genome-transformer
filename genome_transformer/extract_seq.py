#!/usr/bin/env python3
#Example usage: ./extract_seq.py -datadir /content/drive/Shareddrives/mGEM\ R\&D/viral/2021-02-10_02-37-27/files

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
    datapaths = (datapath for datapath in Path(FLAGS.datadir).iterdir() if ".gbff" in datapath.suffixes)
    for datapath in datapaths:
        print(datapath)


if __name__ == "__main__":
    app.run(main)
