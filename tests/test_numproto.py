import numpy as np

from numproto import ndarray_to_proto, proto_to_ndarray

def test_numproto():
    nda = np.arange(10)
    result = proto_to_ndarray(ndarray_to_proto(nda))
    assert np.array_equal(nda, result)

    nda = np.arange(15).reshape(3, 5)
    result = proto_to_ndarray(ndarray_to_proto(nda))
    assert np.array_equal(nda, result)

    nda = np.array([1.2, 3.5, 5.1])
    result = proto_to_ndarray(ndarray_to_proto(nda))
    assert np.array_equal(nda, result)

    nda = np.array([[1, 2], [3, 4]], dtype=complex)
    result = proto_to_ndarray(ndarray_to_proto(nda))
    assert np.array_equal(nda, result)

    nda = np.zeros((3, 4))
    result = proto_to_ndarray(ndarray_to_proto(nda))
    assert np.array_equal(nda, result)

    nda = np.ones((2, 3, 4), dtype=np.int16)
    result = proto_to_ndarray(ndarray_to_proto(nda))
    assert np.array_equal(nda, result)
