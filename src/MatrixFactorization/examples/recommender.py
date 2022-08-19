# Data manipulation
import pandas as pd
pd.options.display.max_rows = 100

# Other
import os
import sys

# Print all output
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"

from os import sep
from pathlib import Path

cols = ['user_id', 'item_id', 'rating', 'category','color','section_no']
# movie_data = pd.read_csv('../data/ml-1m/ratings.dat', names = cols, sep = '::', usecols=[0, 1, 2], engine='python')
def get_project_root() -> Path:
    return Path(sys.path[5]).parent.parent.parent.parent

# Data location
ROOT_DIR = get_project_root()
DATA_DIR = os.path.join(ROOT_DIR, 'GitHub/Recommender-System-for-AR-Glasses/data/articles.csv')

articles_data = pd.read_csv(DATA_DIR, names = cols, sep=',', usecols=[0, 1, 2, 6, 15, 22], engine='python')

print(articles_data.head(10))
