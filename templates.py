import os
from pathlib import Path
import logging

list_of_files=[
    "..github/workflows/.gitkeep",
    "src/__init__.py",
    "src/logger.py",
    "src/exception.py",
    "src/components/__init__.py",
    "src/components/data_ingestion.py",
    "src/components/data_transformation.py",
    "src/components/model_train.py",
    "src/components/model_evaluation.py",
    "src/pipline/__init__.py",
    "src/pipline/train_pipline.py",
    "src/pipline/pradiction_pipline.py",
    "src/utils/utils.py",
    "src/utils/__init__.py",
    "test/unit/__init__.py",
    "test/intregration/__init__.py",
    "__init__setup.sh",
    "requirementes.txt",
    "requirementes_dev.txt",
    "setup.py",
    "setup.cfg",
    "pyproject.toml",
    "tox.ini",
    "experiment/experiment.ipynb"


]


for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass # create an empty file
          