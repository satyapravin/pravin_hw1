# -*- coding: utf-8 -*-
__author__ = "Bezwada"

import importlib
from types import ModuleType
from typing import List, Union, Callable


def methods_importer(
        method: str, modules: List[Union[str, ModuleType]]) -> List[Callable]:
    callables = []
    for module in modules:
        try:
            if isinstance(module, ModuleType):
                mod = module
            elif isinstance(module, str):
                mod = importlib.import_module(module)
            else:
                raise TypeError('Must be list of strings or ModuleType')

            met = getattr(mod, method, None)

            if met and callable(met):
                callables.append(met)

        except ImportError:
            continue

    return callables
