# NumProto

**Numproto** is a simple python3.6+ library to serialize and deserialize numpy
arrays into and from protobuf messages.

## Installation

You can install NumProto from the PyPI package:
```bash
$ pip install numproto
```

## Usage

Numproto serializes a numpy array into an `NDArray` message as specified in
[ndarray.proto](https://github.com/xainag/numproto/blob/master/xain/protobuf/ndarray.proto):

```proto
syntax = "proto3";

message NDArray {
    bytes ndarray = 1;
}
```

This library provides two methods: one for serialization `ndarray_to_proto` and
one for deserialization `proto_to_ndarray`.

```python
import numpy as np

from numproto import ndarray_to_proto, proto_to_ndarray

nda = np.arange(10)

serialized_nda = ndarray_to_proto(nda)
deserialized_nda = proto_to_ndarray(serialized_nda)

assert np.array_equal(nda, deserialized_nda)
```

## Tests

To run the tests first install the numproto package from source in development
mode and then run the tests using pytest:
```bash
$ git clone https://github.com/xainag/numproto.git
$ cd numproto
$ pip install -e .[dev]

$ pytest
```
