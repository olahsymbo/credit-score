import os
import pickle
import sys
import inspect
import warnings

from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import f1_score

app_path = inspect.getfile(inspect.currentframe())
projec_dir = os.path.realpath(os.path.dirname(app_path))
script_dir = os.path.dirname(projec_dir)
sys.path.insert(0, script_dir)

import pandas as pd
pd.set_option('display.width', 400)
pd.set_option('display.max_columns', 20)

from sklearn.model_selection import train_test_split

warnings.filterwarnings("ignore", category=DeprecationWarning)
warnings.filterwarnings("ignore", category=FutureWarning)

df = pd.read_csv(os.path.join(script_dir, "data/cs-training.csv"))
print(df.head(5))
df.dropna(inplace=True)
label = df['SeriousDlqin2yrs']
df.drop('SeriousDlqin2yrs', axis=1, inplace=True)

X_train, X_test, y_train, y_test = train_test_split(df, label, test_size=0.3, random_state=900)
#
n_samples = X_train.shape[0]

modelgbc = GradientBoostingClassifier(learning_rate=0.001,
                                      max_depth=10)
modelgbc.fit(X_train, y_train)
output = modelgbc.predict(X_test)
fscore_gbc= f1_score(y_test, output, average='micro')
print("Test Accuracy of Classifier :: ", fscore_gbc)

with open(os.path.join(script_dir, 'model/mdl.pickle'), 'wb') as f:
    pickle.dump(modelgbc, f)