#!/bin/bash

set -e  # Exit immediately if a command exits with a non-zero status
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
cd $DIR/../

isort --indent=4 -rc setup.py numproto
black --exclude "numproto/protobuf/.*_pb2.*" setup.py numproto
clang-format -style="{Language: Proto, BasedOnStyle: Google}" -i numproto/protobuf/*.proto
