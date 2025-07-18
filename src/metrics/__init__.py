import os
import importlib.util

metrics = {}

CURRENT_PATH = os.path.dirname(__file__)


def load_class_from_file(module_name, file_path):
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    def normalize(name):
        return name.replace('_', '').lower()

    target = normalize(module_name)

    for attribute_name in dir(module):
        attribute = getattr(module, attribute_name)
        if isinstance(attribute, type):
            if normalize(attribute_name) == target:
                return attribute

    return None


for root, _, files in os.walk(CURRENT_PATH):
    for file in files:
        if file.endswith(".py") and file != "__init__.py":
            file_path = os.path.join(root, file)
            module_name = os.path.splitext(file)[0]

            class_obj = load_class_from_file(module_name, file_path)
            if class_obj:
                metrics[module_name] = class_obj

__all__ = list(metrics.keys())
