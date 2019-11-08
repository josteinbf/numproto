# Release Process

## Versioning Schema

This project follows the python form of Semantic Versioning as detailed in [PEP
440](https://www.python.org/dev/peps/pep-0440/).

## Versioning in Git History

For git tags we use the version as describe in [Versioning
Schema](#versioning-schema) preceded by a `v`.

A release on git is just a tagged commit on the `master` branch.

## How to do a Github Release

Here we detail the process of creating a new Github release.

1. Create and merge a pull request that:
    - Increase the version number in
      [`numproto/__version__.py`](https://github.com/xainag/xain/blob/master/xain/__version__.py)
      according the versioning schema.
    - Possibly update the `Development Status` classifiers in the
      [`setup.py`](https://github.com/xainag/xain/blob/master/setup.py). You
      can check supported classifiers in the [pypi
      website](https://pypi.org/classifiers/).
2. Got to the [Github Releases tab](https://github.com/xainag/xain/releases)
   and create a new release:
    - For the tag version use the version defined in 1. preceded by a `v`, e.g.
      v0.3.2, and target master.
    - For the release title use the same as the tag version.
    - For the release description, copy the section from the
      [`CHANGELOG.md`](https://github.com/xainag/xain/blob/master/CHANGELOG.md)
      related to this version.
    - Possibly check the `This is a pre-release` check box.
    - Publish the release.

## How to publish a new release to PyPI

Here we detail the process of building and pushing a python package to PyPI.
You can check more information in the [Python Packaging User
Guide](https://packaging.python.org/tutorials/packaging-projects/).

1. Checkout the current git tag, for example, version 0.3.2:
    ```bash
    $ git checkout v0.3.2
    ```
2. Generate the distribution archives:
    ```bash
    $ python setup.py sdist bdist_wheel
    ```
3. Upload the distribution archives using the correct PyPi credentials:
    ```bash
    $ python -m twine upload dist/*
    ```
