# Connect Four

## How to run

### Requirements

Python 3.10

### Setting up a virtual environment

For the imports to work, a `PYTHONPATH` environment variable must be present and contain the path to the root directory of the project.

Start by creating a virtual environment, by running the following command:

```bash
python3 -m venv .venv
```

You should now edit the activation script to add the path to the root directory of the project.
You can do so by appending the following line to `.venv/bin/activate`:

```bash
export PYTHONPATH="/path/to/project:$PYTHONPATH"
```

Then, activate the virtual environment by running the following:

```bash
source .venv/bin/activate
```
