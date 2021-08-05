import pandas as pd
import numpy as np
import pickle

from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import FunctionTransformer, OneHotEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV
from sklearn.metrics import classification_report, confusion_matrix, plot_confusion_matrix
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.neighbors import KNeighborsClassifier

BIN_FIELDS = ['INTERSECTION_RELATED_I',
              'HIT_AND_RUN_I',
              'WORK_ZONE_I']
CAT_FIELDS = ['TRAFFIC_CONTROL_DEVICE',
              'DEVICE_CONDITION',
              'WEATHER_CONDITION',
              'LIGHTING_CONDITION',
              'FIRST_CRASH_TYPE',
              'TRAFFICWAY_TYPE',
              'ALIGNMENT',
              'ROADWAY_SURFACE_COND',
              'ROAD_DEFECT',
              'CRASH_TYPE',
              'DAMAGE',
              'MOST_SEVERE_INJURY',
              'CRASH_HOUR',
              'CRASH_DAY_OF_WEEK',
              'CRASH_MONTH',
              'CRASH_YEAR']
NUM_FIELDS = ['POSTED_SPEED_LIMIT',
              'NUM_UNITS',
              'INJURIES_TOTAL',
              'INJURIES_FATAL',
              'LATITUDE',
              'LONGITUDE']
TARGET = 'PRIM_CONTRIBUTORY_CAUSE'
ID = 'CRASH_ID'

with open('pipelines/binned_causes.pkl', 'rb') as f:
    binned_causes = pickle.load(f)

bin_imputer = SimpleImputer(strategy='constant', fill_value=False)
cat_imputer = SimpleImputer(strategy='most_frequent')
num_imputer = SimpleImputer(strategy='most_frequent')

imputers = ColumnTransformer([
    ('binary', bin_imputer, BIN_FIELDS),
    ('categorical', cat_imputer, CAT_FIELDS),
    ('numeric', num_imputer, NUM_FIELDS)
], remainder='passthrough')

ohe = OneHotEncoder(handle_unknown='ignore')

model = DecisionTreeClassifier(
    criterion='gini',
    max_depth=4,
)

feat_pipeline = Pipeline([
    ('imputers', imputers),
    ('encoder', ohe),
    ('model', model)
])


# class Model:
#
#     def __init__(self, df, pipeline):
#         self.df = df
#         self.pipeline = pipeline
#         self.target_name = TARGET
#         self.X = df.drop(TARGET, axis=1)
#         self.y = df[TARGET].map(binned_causes)
#         self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(X, y, test_size=.2)


crashes = pd.read_pickle('../data/crashes.pkl')
X = crashes.drop('PRIM_CONTRIBUTORY_CAUSE', axis=1)
y = crashes.PRIM_CONTRIBUTORY_CAUSE.map(binned_causes)

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42, test_size=.2)

bin_imputer = SimpleImputer(strategy='constant', fill_value=False)
cat_imputer = SimpleImputer(strategy='most_frequent')
num_imputer = SimpleImputer(strategy='most_frequent')

imputers = ColumnTransformer([
    ('binary', bin_imputer, BIN_FIELDS),
    ('categorical', cat_imputer, CAT_FIELDS),
    ('numeric', num_imputer, NUM_FIELDS)
], remainder='passthrough')

ohe = OneHotEncoder(handle_unknown='ignore')

model = DecisionTreeClassifier(
    criterion='gini',
    max_depth=4,
)

feat_pipeline = Pipeline([
    ('imputers', imputers),
    ('encoder', ohe),
    ('model', model)
])

# crashes_imputed = pd.DataFrame(imputers.fit_transform(crashes), columns=BIN_FIELDS+CAT_FIELDS+NUM_FIELDS)

if __name__ == '__main__':
    feat_pipeline.fit(X_train, y_train)
    y_hat_train = feat_pipeline.predict(X_train)
    y_hat_test = feat_pipeline.predict(X_test)
    print("TRAIN____\n", classification_report(y_train, y_hat_train))
    print("TEST____\n", classification_report(y_test, y_hat_test))
