#!/usr/bin/env python3
# Example usage: ./extract_seq.py -datadir /content/drive/Shareddrives/mGEM\ R\&D/viral/2021-02-10_02-37-27/files -savepath /content/drive/Shareddrives/mGEM\ R\&D/viral_seq.csv

import gzip
from pathlib import Path

import dask.bag as db
import dask.dataframe as dd
import pandas as pd
from absl import app, flags
from Bio import SeqIO
from dask.diagnostics import ProgressBar

FLAGS = flags.FLAGS
flags.DEFINE_string("datadir", None, "Path to data directory containing *.gbff.gz files")
flags.DEFINE_string("savepath", None, "Path to save DataFrame")


def extract_seq(path: str):
    with gzip.open(path, "rt") as f:
        return next(SeqIO.parse(f, "genbank")).seq


def main(argv):
    del argv
    ProgressBar().register()
    df = db.from_sequence(str(datapath) for datapath in Path(FLAGS.datadir).iterdir() if ".gbff" in datapath.suffixes).to_dataframe({"datapath": str})
    df["sequence"] = df.datapath.map(extract_seq, meta=pd.Series(dtype=str))
    df.to_csv(FLAGS.savepath)


if __name__ == "__main__":
    app.run(main)
