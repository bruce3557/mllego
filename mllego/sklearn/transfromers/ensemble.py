import pandas as pd
from sklearn.base import TransformerMixin


class ModelTransformer(TransformerMixin):
    def __init__(self, model, return_prob=False):
        self.model = model
        self.return_prob = return_prob

    def fit(self, *args, **kwargs):
        self.model.fit(*args, **kwargs)
        return self

    def transform(self, X, **transform_params):
        if self.return_prob:
            return pd.DataFrame(self.model.predict_proba(X))
        else:
            return pd.DataFrame(self.model.predict(X))