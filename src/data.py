# src/data.py
from __future__ import annotations

from pathlib import Path
import pandas as pd


def LoadTrainTest(train_path: str | Path, test_path: str | Path):
    """
    Load Kaggle train/test CSVs.

    Parameters
    ----------
    train_path : str | Path
        Path to train.csv
    test_path : str | Path
        Path to test.csv

    Returns
    -------
    (train_df, test_df) : tuple[pd.DataFrame, pd.DataFrame]
    """
    train_path = Path(train_path)
    test_path = Path(test_path)

    train = pd.read_csv(train_path)
    test = pd.read_csv(test_path)
    return train, test
