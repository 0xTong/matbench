from monty.serialization import loadfn
from matminer.datasets.utils import _load_dataset_dict

from matbench.constants import MBV01_DATASET_METADATA_PATH, MBV01_VALIDATION_DATA_PATH, VALIDATION_SPLIT_KEY
from matbench.util import RecursiveDotDict

MATMINER_DATASET_METADATA = _load_dataset_dict()

mbv01_metadata = loadfn(MBV01_DATASET_METADATA_PATH)
for d in mbv01_metadata.keys():
    mbv01_metadata[d].update(MATMINER_DATASET_METADATA[d])
mbv01_metadata = RecursiveDotDict(mbv01_metadata)


mbv01_validation = loadfn(MBV01_VALIDATION_DATA_PATH)
for ds in mbv01_validation[VALIDATION_SPLIT_KEY]:
    for


mbv01_validation = RecursiveDotDict(mbv01_validation)