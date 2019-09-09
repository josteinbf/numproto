# NumProto

**NumProto** is a simple python3.6+ library to serialize and deserialize numpy
arrays into and from protobuf messages.

## Installation

You can install NumProto from the PyPI package:

```bash
$ pip install numproto
```

## Usage

NumProto serializes a numpy array into an `NDArray` message as specified in
[ndarray.proto](https://github.com/xainag/numproto/blob/master/numproto/protobuf/ndarray.proto):

```proto
syntax = "proto3";

package numproto.protobuf;

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

### Re-using the proto files in another project

Re-distributing `*.proto` files is notoriously difficult. In order to make this
easier the
[ndarray.proto](https://github.com/xainag/numproto/blob/master/numproto/protobuf/ndarray.proto)
file is installed together with the python package.

This allows us to simply pass the `site-packages` path as an import path to
`protoc`.

> To get the correct path of `site-packages` check the _Location_ key when
> running `pip show numproto`.

For example let's say we want to create a new `proto` file and import `NDArray`
to use within one of our defined messages:

```proto
syntax = "proto3";

import "numproto/protobuf/ndarray.proto";

message MyMessage {
    numproto.protobuf.NDArray my_array = 1;
}
```

And to compile using `grpcio-tools` simply do:
```bash
$ python -m grpc_tools.protoc -I/usr/lib/python3.6/site-packages/ -I./ --python_out=. --grpc_python_out=. my_proto.proto
```
(you may need to adjust the location of `site-packages`)

## Tests

To run the tests first install the `numproto` package from source in development
mode and then run the tests using `pytest`:

```bash
$ git clone https://github.com/xainag/numproto.git
$ cd numproto
$ pip install -e .[dev]

$ pytest
```
