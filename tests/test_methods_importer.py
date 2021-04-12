import numpy as np
from import_monster import methods_importer


def test_importer():
    min_fns = methods_importer("min", ["numpy"])
    assert (len(min_fns) > 0)
