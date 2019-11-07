#!/bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
cd $DIR/../

# clang-format does not provide a way to check the files.
# This function iterates over a list of files and checks each one of them
# for formatting errors
clang_format() {
    local_ret=0

    for f in ./numproto/protobuf/*.proto
    do
        echo "Processing $f"
        clang-format -style="{Language: Proto, BasedOnStyle: Google}" $f | diff $f -

        if [ $? -ne 0 ] ; then
            local local_ret=1
        fi

    done
    return $local_ret
}

# Formatting
isort --check-only --indent=4 -rc setup.py numproto tests && echo "===> isort says: well done <===" &&
black --check --exclude "numproto/protobuf/.*_pb2.*" setup.py numproto tests && echo "===> black says: well done <===" &&
clang_format && echo "===> clang-format says: well done <===" &&

# type checks
mypy --ignore-missing-imports numproto tests && echo "===> mypy says: well done <===" &&

# lint
pylint --rcfile=pylint.ini numproto tests && echo "===> pylint says: well done <===" &&

# tests
pytest -v && echo "===> pytest/unmarked says: well done <===" &&

echo "All went well"
