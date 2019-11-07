# Contribution Guidelines

## Recommended Development Environment

The recommended development environment uses virtual environments based on
`pyenv` and the `pyenv-virtualenv` plugin:

- [`pyenv`](https://github.com/pyenv/pyenv)
- [`pyenv-virtualenv`](https://github.com/pyenv/pyenv-virtualenv)

Once `pyenv` and `pyenv-virtualenv` are set up, install the latest Python 3.6
[release](https://www.python.org/downloads/release):

```shell
pyenv install 3.6.9
```

Create a new virtualenv managed by pyenv:

```shell
pyenv virtualenv 3.6.9 numproto-3.6.9
```

To automatically activate this virtualenv when entering the directory, create
a new file called `.python-version` which contains the name of the newly
created virtualenv:

```shell
echo "numproto-3.6.9" > .python-version
```

## Initial Setup

The initial setup clones the repository and installs development dependencies:

```shell
git clone https://github.com/xainag/numproto
cd numproto
./scripts/setup.sh
```

## Editor Setup - Visual Studio Code

If you want VSCode to automatically apply some of the tools we use
(e.g., formatting, linting), you can use a configuration similar to the
following. First, create a VSCode configuration file:

```shell
mkdir .vscode
cd .vscode
touch settings.json
```

Then copy the following configuration into `settings.json` (adjust
`python.pythonPath` according to your OS, username, and `pyenv`
configuration):

```
{
    "editor.formatOnSave": true,
    "editor.codeActionsOnSave": {
        "source.organizeImports": true,
    },
    "python.pythonPath": "/Users/[username]/.pyenv/versions/numproto-3.6.9/bin/python",
    "python.formatting.provider": "black",
    "python.linting.enabled": true,
    "python.linting.lintOnSave": true,
    "python.linting.pylintEnabled": true,
    "python.linting.pylintArgs": [
        "--rcfile=pylint.ini numproto tests"
    ],
    "python.linting.mypyEnabled": true,
    "python.terminal.activateEnvironment": true,
    "python.testing.pytestEnabled": true,
}
```

## Development Workflow

We generally prefer small pull requests (PR) and short-lived feature branches.

To contribute changes, start by creating a new branch:

```shell
git branch feature-abc
git checkout feature-abc
```

**Implement your changes**
You should auto-format your code during implementation or at the latest before
committing:

```shell
./scripts/format.sh
```

Run formatting checks, linting, type checks, and tests using the following
command:

```shell
./scripts/test.sh
```

Once implementation is complete, code is auto-formatted, and tests are
passing, you can push your branch to GitHub. If you set up the previously
mentioned git hooks, those checks will be executed before a git push gets
executed.

```shell
git push --set-upstream origin feature-abc
```

On GitHub, open a new PR and ensure that all check are passing.
