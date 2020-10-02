# NBS Challenge 3

## App

### Environment

To use the app you need to make sure the requirements are installed.
It is best to do this in a virtual environment OR use a Docker container.

#### Venv

```bash
sudo apt update && sudo apt install python3-pip python3-venv -y
python3 -m venv venv
. ./venv/bin/activate
```

### Testing

Then you can run the tests. This can only be done if the dependencies in requirements.txt are installed.

```bash
# In the root of the project
pytest
```

### Running

Or you can run the app.

```
python3 app.py
```