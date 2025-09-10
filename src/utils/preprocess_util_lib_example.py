"""Utilities example"""

# This file provides an example of building utilities for use in
# either notebooks or pipelines.
from pathlib import Path

import numpy as np
import pandas as pd

current_directory = Path(__file__).parent
REPO_ROOT = current_directory.parent.parent


def save_random_dataframe(output_path: Path | str) -> None:
    """Creates a random dataframe and saves to csv

    Args:
        output_path: absolute path to save df in
    Returns: None.
    """
    random_df = pd.DataFrame(
        np.random.randint(0, 100, size=(100, 4)), columns=list("ABCD")
    )
    random_df.to_csv(output_path)
