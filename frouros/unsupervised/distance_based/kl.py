"""KL (Kullback-Leibler divergence distance) module."""

import numpy as np  # type: ignore
from scipy.special import rel_entr  # type: ignore

from frouros.unsupervised.distance_based.base import (  # type: ignore
    DistanceProbabilityBasedEstimator,
)


class KL(DistanceProbabilityBasedEstimator):
    """KL (Kullback-Leibler divergence / relative entropy) algorithm class."""

    def _distance(
        self, X_ref_: np.ndarray, X: np.ndarray, **kwargs  # noqa: N803
    ) -> float:
        X_ref_rvs, X_rvs = self._calculate_probabilities(  # noqa: N806
            X_ref_=X_ref_, X=X
        )
        distance = np.sum(rel_entr(X_rvs, X_ref_rvs, **kwargs))
        return distance
