"""
This module contains the ModelEvaluator class and the TrainTestSplit class that are used for streamlining the modeling
and model evaluation process. These are a work in progress, but are functional. Future implementations should include
@property decorators for setters/getters, and added functionality for analyzing a model.
"""

import pandas as pd
import numpy as np
import pickle

import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import classification_report, confusion_matrix

# Global constants for confusion matrix design
LABELS = ['DISREGARDING_SIGNS', 'DRIVER', 'ENVIRONMENT']

TITLE_FONT = {
    'family': 'serif',
    'size': 20,
    'weight': 'bold'
}

AXIS_FONT = {
    'family': 'serif',
    'size': 16,
    'weight': 'bold'
}

ANNOT_KWS = {
    'family': 'serif',
    'size': 14
}


class TrainTestSplit:
    """A train-test split class to be passed into ModelEvaluator"""
    def __init__(self, X, y, test_size=0.25, random_state=42):
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(X,
                                                                                y,
                                                                                test_size=test_size,
                                                                                random_state=random_state,
                                                                                stratify=y)


class ModelEvaluator:
    """
    Model evaluation class, takes a TrainTestSplit object, a model (pipeline or stand-alone estimator), and a name
    as required parameters, random_state=42 by default
    """
    def __init__(self, splits, model, model_name, random_state=42):
        self._model = model
        self._model_name = model_name
        self._rng = np.random.RandomState(random_state)

        # Train test split
        self._X_train = splits.X_train
        self._X_test = splits.X_test
        self._y_train = splits.y_train
        self._y_test = splits.y_test

        # Fitting
        self._fitted_model = None
        self._is_fitted = False

        # Cross validation
        self._cv_scores = None

        # Test set evaluation
        self._y_hat_train = None
        self._y_hat_test = None
        self._values_predicted = False

    def cross_val(self, nfolds=10, **kwargs):
        """Perform cross validation, default 10 folds, **kwargs passed to cross_val_score"""
        self._cv_scores = cross_val_score(self._model, self._X_train, self._y_train, cv=nfolds, **kwargs)

    def display_cv_results(self):
        """Print cross validation results, default metric of the estimator is used, ie accuracy for classifiers"""
        scores = self._cv_scores
        name = self._model_name
        print(f"{name} Cross Validation Results")
        print('-' * 25)
        print(f"Mean: {np.mean(scores)}\nMedian: {np.median(scores)}\nStd. Dev.: {np.std(scores)}")

    def run_model(self, predict=True):
        """Fit model and assign fitted model to object as an attribute, predict targets by default"""

        # Fit model and set flag attribute to True
        print(f"Fitting {self._model_name}...")
        self._fitted_model = self._model.fit(self._X_train, self._y_train)
        print(f"{self._model_name} fitted successfully")
        self._is_fitted = True

        # Predict target values and assign to respective attributes
        if predict:
            print("Predicting Target values...")
            self._y_hat_train = self._fitted_model.predict(self._X_train)
            self._y_hat_test = self._fitted_model.predict(self._X_test)
            print(f"Target values predicted successfully")
            self._values_predicted = True

    def train_test_classification_reports(self):
        """Print classification reports for train and test sets"""
        if not self._values_predicted:
            print("Values have not been predicted: please")
        print('_' * 10 + 'TRAIN SCORES' + '_' * 10)
        print(classification_report(self._y_train, self._y_hat_train))
        print('-' * 30, end='\n\n')
        print('_' * 10 + 'TEST SCORES' + '_' * 10)
        print(classification_report(self._y_test, self._y_hat_test))
        print('-' * 30, end='\n\n')

    def confusion_matrices(self):
        """Plot confusion matrices for train and test sets"""
        if not self._values_predicted:
            print("No predicted values: use run_model() method first.")
            return None
        fig, axes = plt.subplots(1, 2, figsize=(18, 8))
        fig.suptitle(self._model_name, fontsize=22)

        sns.heatmap(data=confusion_matrix(self._y_train, self._y_hat_train),
                    cmap='Blues',
                    annot=True,
                    xticklabels=LABELS,
                    yticklabels=LABELS,
                    annot_kws=ANNOT_KWS,
                    fmt='.2f',
                    ax=axes[0]
                    )
        axes[0].set_title('TRAIN', fontdict=TITLE_FONT)
        axes[0].set_xlabel('Predicted Label', fontdict=AXIS_FONT)
        axes[0].set_ylabel('True Label', fontdict=AXIS_FONT)

        sns.heatmap(data=confusion_matrix(self._y_test, self._y_hat_test),
                    cmap='Reds',
                    annot=True,
                    xticklabels=LABELS,
                    yticklabels=LABELS,
                    annot_kws=ANNOT_KWS,
                    fmt='.2f',
                    ax=axes[1]

                    )
        axes[1].set_title('TEST', fontdict=TITLE_FONT)
        axes[1].set_xlabel('Predicted Label', fontdict=AXIS_FONT)
        axes[1].set_ylabel('True Label', fontdict=AXIS_FONT)

        fig.tight_layout()
        plt.show()

    def pickle_fitted_model(self, filepath):
        """Store only the fitted model as a PKL file, if model has been fitted"""
        if self._fitted_model:
            with open(filepath, 'wb') as f:
                pickle.dump(self._fitted_model, f)
        else:
            print(f"Model {self._model_name} has not been fitted. "
                  f"Use self.run_model() before attempting to save PKL file.")

    def pickle_evaluator(self, filepath):
        """Store entire evaluator object as a PKL file"""
        with open(filepath, 'wb') as f:
            pickle.dump(self, f)
