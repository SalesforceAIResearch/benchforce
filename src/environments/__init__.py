import os
import importlib.util

CURRENT_PATH = os.path.dirname(__file__)

configs = {}

for folder in os.listdir(CURRENT_PATH):
    folder_path = os.path.join(CURRENT_PATH, folder)

    if os.path.isdir(folder_path) and "__init__.py" in os.listdir(folder_path):
        module_name = f"src.environments.{folder}"
        module_path = os.path.join(folder_path, "__init__.py")

        spec = importlib.util.spec_from_file_location(module_name, module_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

        if hasattr(module, "config"):
            configs[folder] = module.config

__all__ = ["configs"]
