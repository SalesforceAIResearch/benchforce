import os
import importlib
import inspect

current_dir = os.path.dirname(__file__)
module_files = [
    f[:-3] for f in os.listdir(current_dir)
    if f.endswith(".py") and f != "__init__.py"
]

FUNCTIONS_MAP = {}

for module_name in module_files:
    module = importlib.import_module(f".{module_name}", package=__name__)

    for name, obj in inspect.getmembers(module, inspect.isclass):
        if obj.__module__ == module.__name__:
            FUNCTIONS_MAP[module_name] = obj

__all__ = ["FUNCTIONS_MAP"]