from dataclasses import dataclass
import os
import pathlib
import random

import numpy as np
import torch
import pytorch_lightning as pl

from logger import logger


class Configuration(object):

    @classmethod
    def apply(cls, random_seed=777):
        Configuration.set_torch_seed(random_seed=random_seed)
        Configuration.set_numpy_seed(random_seed=random_seed)
        Configuration.set_pl_seed(random_seed=random_seed)
        Configuration.set_python_random_seed(random_seed=random_seed)

        logger.info(f"Complete to apply the random seed, RANDOM_SEED : {random_seed}")

    @classmethod
    def set_torch_seed(cls, random_seed):
        torch.manual_seed(random_seed)
        torch.cuda.manual_seed(random_seed)

        torch.backends.cudnn.deterministic = True
        torch.backends.cudnn.benchmark = False

    @classmethod
    def set_numpy_seed(cls, random_seed):
        np.random.seed(random_seed)

    @classmethod
    def set_pl_seed(cls, random_seed):
        pl.seed_everything(random_seed)

    @classmethod
    def set_python_random_seed(cls, random_seed):
        random.seed(random_seed)


@dataclass
class ApplicationProperties:
    CURRENT_MODULE_PATH = pathlib.Path(__file__).parent.absolute()

    CONFIG_DIRECTORY_PATH = os.path.join(CURRENT_MODULE_PATH, "config")
    HYPERPARAMETER_DIRECTORY_PATH = os.path.join(CONFIG_DIRECTORY_PATH, "hyperparameters")
    DATASET_HYPERPARAMETER_DIRECTORY_PATH = os.path.join(HYPERPARAMETER_DIRECTORY_PATH, "dataset")
    TRAINER_HYPERPARAMETER_DIRECTORY_PATH = os.path.join(HYPERPARAMETER_DIRECTORY_PATH, "trainer")
    MODEL_HYPERPARAMETER_DIRECTORY_PATH = os.path.join(HYPERPARAMETER_DIRECTORY_PATH, "model")

    DATA_DIRECTORY_PATH = os.path.join(CURRENT_MODULE_PATH, "data")
    DATASET_DIRECTORY_PATH = os.path.join(CURRENT_MODULE_PATH, "dataset")
    MODEL_DIRECTORY_PATH = os.path.join(CURRENT_MODULE_PATH, "model")
    MODEL_RESULT_DIRECTORY_PATH = os.path.join(MODEL_DIRECTORY_PATH, "results")
    INFERENCE_DIRECTORY_PATH = os.path.join(CURRENT_MODULE_PATH, "inference")
    TRAINER_DIRECTORY_PATH = os.path.join(CURRENT_MODULE_PATH, "trainer")

    DEFAULT_RANDOM_SEED = 777

    DEVICE_CPU = "cpu"

    """
    Trainer
    """
    EARLY_STOPPING_MIN_DELTA_DEFAULT = 0.0
    EARLY_STOPPING_PATIENCE_DEFAULT = 3
    EARLY_STOPPING_VERBOSE_DEFAULT = False
    EARLY_STOPPING_MODE_DEFAULT = "min"
    EARLY_STOPPING_STRICT_DEFAULT = True


    # Representation
    ## Train
    TRAIN_LOSS_REPR = "train_loss"
    TRAIN_ACCURACY_REPR = "train_accuracy"
    TRAIN_PRECISION_REPR = "train_precision"
    TRAIN_RECALL_REPR = "train_recall"
    TRAIN_F1_SCORE_REPR = "train_f1_score"

    ## Val
    VAL_LOSS_REPR = "val_loss"
    VAL_ACCURACY_REPR = "val_accuracy"
    VAL_PRECISION_REPR = "val_precision"
    VAL_RECALL_REPR = "val_recall"
    VAL_F1_SCORE_REPR = "val_f1_score"

    ## Test
    TEST_LOSS_REPR = "test_loss"
    TEST_ACCURACY_REPR = "test_accuracy"
    TEST_PRECISION_REPR = "test_precision"
    TEST_RECALL_REPR = "test_recall"
    TEST_F1_SCORE_REPR = "test_f1_score"

    def __post_init__(self):
        Configuration.apply(random_seed=ApplicationProperties.DEFAULT_RANDOM_SEED)


APPLICATION_PROPERTIES = ApplicationProperties()
