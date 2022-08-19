# Data manipulation
import numpy as np
import pandas as pd
pd.options.display.max_rows = 100

# Modeling
from matrix_factorization import BaselineModel, KernelMF, train_update_test_split
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

# Other
import os
import random
import sys

# Print all output
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"
    
rand_seed = 2
np.random.seed(rand_seed)
random.seed(rand_seed)

from os import sep
from pathlib import Path

cols = ['user_id', 'item_id', 'rating', 'category','color']
# movie_data = pd.read_csv('../data/ml-1m/ratings.dat', names = cols, sep = '::', usecols=[0, 1, 2], engine='python')
def get_project_root() -> Path:
    return Path(sys.path[5]).parent.parent.parent.parent

# Data location
ROOT_DIR = get_project_root()
DATA_DIR = os.path.join(ROOT_DIR, 'GitHub/Recommender-System-for-AR-Glasses/data/articles.csv')

articles_data = pd.read_csv(DATA_DIR, names = cols, sep=',', usecols=[0, 1, 2, 6, 15], engine='python')

X = articles_data[['user_id', 'item_id']]
y = articles_data['rating']

# Prepare data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Prepare data for online learning
X_train_initial, y_train_initial, X_train_update, y_train_update, X_test_update, y_test_update = train_update_test_split(articles_data, frac_new_users=0.2)

articles_data.head(10)