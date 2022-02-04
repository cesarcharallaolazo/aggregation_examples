import pandas as pd

from . import mocks
from src.utils import set_identifier


def test_set_identifier():
    data = pd.DataFrame(mocks.TOY_DATA.copy())
    data_with_ids = set_identifier(data)
    assert data_with_ids.equals(pd.DataFrame(mocks.IDENTIFIERS_ADDED))
    assert isinstance(data_with_ids, type(pd.DataFrame()))
