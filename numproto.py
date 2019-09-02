from io import BytesIO

import numpy as np

from ndarray_pb2 import NdArray


def ndarray_to_proto(nda: np.ndarray) -> NdArray:
    nda_bytes = BytesIO()
    np.save(nda_bytes, nda, allow_pickle=False)

    return NdArray(ndarray=nda_bytes.getvalue())



def proto_to_ndarray(nda_proto: NdArray) -> np.ndarray:
    nda_bytes = BytesIO(nda_proto.ndarray)

    return np.load(nda_bytes, allow_pickle=False)
