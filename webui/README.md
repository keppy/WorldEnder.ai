# worldender-ai

## how to setup and run api server

1. be using python 3.12
2. have poetry installed

```
python -m venv .venv
source .venv/bin/activate
cd api-server
poetry install
poetry run fastapi dev main.py
```

## how to setup and run the website

```
yarn
yarn workspace website dev
```
