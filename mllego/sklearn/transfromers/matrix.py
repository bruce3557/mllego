from scipy import sparse
from sklearn.base import TransformerMixin


class SparseTransformer(TransformerMixin):
    def __init__(self, sparse_format="csr"):
        super().__init__()
        self.sparse_format = sparse_format

    def fit(self, X, y=None, **fit_params):
        return self

    def transform(self, X, y=None, **fit_params):
        if self.sparse_format == "csr":
            return sparse.csr_matrix(X)
        elif self.sparse_format == "coo":
            return sparse.coo_matrix(X)
        elif self.sparse_format == "csc":
            return sparse.csc_matrix(X)
        else:
            raise Exception("Wrong sparse format")
