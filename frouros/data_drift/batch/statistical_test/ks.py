"""KSTest (Kolmogorov-Smirnov test) module."""

from typing import Optional, List, Union

import numpy as np  # type: ignore
from scipy.stats import ks_2samp  # type: ignore

from frouros.callbacks import Callback
from frouros.data_drift.base import NumericalData, UnivariateData
from frouros.data_drift.batch.statistical_test.base import (
    StatisticalTestBase,
    StatisticalResult,
)


class KSTest(StatisticalTestBase):
    """KSTest (Kolmogorov-Smirnov test) algorithm class."""

    def __init__(
        self, callbacks: Optional[Union[Callback, List[Callback]]] = None
    ) -> None:
        """Init method.

        :param callbacks: callbacks
        :type callbacks: Optional[Union[Callback, List[Callback]]]
        """
        super().__init__(
            data_type=NumericalData(),
            statistical_type=UnivariateData(),
            callbacks=callbacks,
        )

    def _statistical_test(
        self, X_ref_: np.ndarray, X: np.ndarray, **kwargs  # noqa: N803
    ) -> StatisticalResult:
        test = ks_2samp(
            data1=X_ref_,
            data2=X,
            alternative=kwargs.get("alternative", "two-sided"),
            method=kwargs.get("method", "auto"),
        )
        test = StatisticalResult(statistic=test.statistic, p_value=test.pvalue)
        return test
