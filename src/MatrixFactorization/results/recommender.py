# Data manipulation
import numpy as np
import pandas as pd
pd.options.display.max_rows = 100

# Modeling
#from matrix_factorization import BaselineModel, KernelMF, train_update_test_split
from src.MatrixFactorization.implementation.baseline_model import BaselineModel
from src.MatrixFactorization.implementation.kernel_matrix_factorization import KernelMF
from src.MatrixFactorization.implementation.utils import train_update_test_split


from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

# Other
import random

# Print all output
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"
    
rand_seed = 2
np.random.seed(rand_seed)
random.seed(rand_seed)


cols = ['user_id', 'item_id', 'rating', 'category','color']

articles_data = pd.read_csv('src/MatrixFactorization/data/articles.csv', names = cols, sep=',', usecols=[0, 1, 2, 6, 15], engine='python')

X = articles_data[['user_id', 'item_id']]
y = articles_data['rating']

# Prepare data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Prepare data for online learning
X_train_initial, y_train_initial, X_train_update, y_train_update, X_test_update, y_test_update = train_update_test_split(articles_data, frac_new_users=0.2)

#print(articles_data.head(10))

global_mean = y_train.mean()
pred = [global_mean for _ in range(y_test.shape[0])]

rmse = mean_squared_error(y_test, pred, squared = False)

#print(f'\nTest RMSE: {rmse:4f}')

baseline_model = BaselineModel(method='sgd', n_epochs = 20, reg = 0.005, lr = 0.01, verbose=1)
baseline_model.fit(X_train, y_train)

pred = baseline_model.predict(X_test)
rmse = mean_squared_error(y_test, pred, squared = False)

#print(f'\nTest RMSE: {rmse:.4f}')

baseline_model = BaselineModel(method='als', n_epochs = 20, reg = 0.5, verbose=1)
baseline_model.fit(X_train, y_train)

pred = baseline_model.predict(X_test)
rmse = mean_squared_error(y_test, pred, squared = False)

#print(f'\nTest RMSE: {rmse:.4f}')


matrix_fact = KernelMF(n_epochs = 20, n_factors = 100, verbose = 1, lr = 0.001, reg = 0.005)
matrix_fact.fit(X_train, y_train)

pred = matrix_fact.predict(X_test)
rmse = mean_squared_error(y_test, pred, squared = False)

#print(f'\nTest RMSE: {rmse:.4f}')

user = 20222000
items_known = X_train.query('user_id == @user')['item_id']
recommended_item_df = matrix_fact.recommend(user=user, items_known=items_known)['item_id']
top_recommendation = random.sample(list(recommended_item_df), 3)
recommended_items = ' '.join(map(str,top_recommendation))

print(recommended_item_df)
print('\n Recommended Items Are: \n')
print(recommended_items)
