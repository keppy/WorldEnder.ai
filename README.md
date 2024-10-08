![pindragoon_httpss mj runQMNtGkQGbTQ_make_me_a_cool_image_for__19204f1e-2a26-41b0-9a60-0b01437fec14_0](https://github.com/keppy/WorldEnder.ai/assets/1513098/09d5f0c1-9a77-4300-b69c-309861283c3f)

# WorldEnder.ai 🌎💥

A text-adventure RPG using structured outputs from LLMs as the backend to simulate the decline of humanity, the outcome of global catastrophes, and your quest to rebuild civilization.

## Slides and Notebooks

[Presentation Slides](https://github.com/keppy/WorldEnder.ai/blob/master/WorldEnder.ai.pdf)

[Experiment Notebook](https://github.com/keppy/WorldEnder.ai/blob/master/notebooks/WorldEnder_ai.ipynb)

[Presentation Notebook (with some teaching)](https://github.com/keppy/WorldEnder.ai/blob/master/notebooks/WorldEnder_ai_Presentation.ipynb)

## How to develop website

### install python deps

```
poetry install --with api-server
```

### install next.js deps

```
cd webui
yarn
```

### regenerate typescript DTO types from pydantic DTOs

```
poetry run python tools/pydantic2ts.py --module webui/api-server/dtos.py --output webui/apps/website/lib/dtos.ts --json2ts-cmd ./webui/node_modules/.bin/json2ts
```

### database

```
cd webui/storage
docker-compose up -d
```

### api server

```
cd webui/api-server
poetry run fastapi dev main.py --reload --port 8080
```

### web frontend

```
cd webui/apps/website
yarn install
yarn dev
```

at that point, the DB, api server, and web FE are all running, and you can make code changes and they will hot-reload

Copyright &copy; 2024 James Dominguez
