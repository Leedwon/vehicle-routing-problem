### Getting started

Before running project locally:
1. Set up virtual environment via command-line (see [docs](https://docs.python.org/3/library/venv.html)). For no brainer solution just run `python3 -m venv env` on Unix/macOS and `py -m venv env` on Windows.
2. Install requirements by running `env/bin/pip install -r requirements.txt` 
   (also check subpackages if the contain their own `requirements.txt` file and install them, if they're present).

### Running tests

To run tests simple call `pytest tests`
