"""numpy array to protobuf serialization and deserialization"""
from io import BytesIO

import numpy as np

from numproto.ndarray_pb2 import NdArray


def ndarray_to_proto(nda: np.ndarray) -> NdArray:
    """Serializes a numpy array into an NdArray protobuf message.

    Args:
        nda (np.ndarray): numpy array to serialize.

    Returns:
        Returns an NdArray protobuf message.
    """
    nda_bytes = BytesIO()
    np.save(nda_bytes, nda, allow_pickle=False)

    return NdArray(ndarray=nda_bytes.getvalue())


def proto_to_ndarray(nda_proto: NdArray) -> np.ndarray:
    """Deserializes an NdArray protobuf message into a numpy array.

    Args:
        nda_proto (NdArray): NdArray protobuf message to deserialize.

    Returns:
        Returns a numpy.ndarry.
    """
    nda_bytes = BytesIO(nda_proto.ndarray)

    return np.load(nda_bytes, allow_pickle=False)
