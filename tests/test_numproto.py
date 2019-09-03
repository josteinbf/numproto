import pytest
import numpy as np

from numproto import ndarray_to_proto, proto_to_ndarray


@pytest.mark.parametrize(
    "nda",
    [
        np.arange(10),
        np.arange(15).reshape(3, 5),
        np.array([1.2, 3.5, 5.1]),
        np.array([[1, 2], [3, 4]], dtype=complex),
        np.zeros((3, 4)),
        np.ones((2, 3, 4), dtype=np.int16),
    ],
)
def test_numproto(nda):
    """Tests serialization and deserialization of numpy arrays."""
    result = proto_to_ndarray(ndarray_to_proto(nda))
    assert np.array_equal(nda, result)
