![pindragoon_httpss mj runQMNtGkQGbTQ_make_me_a_cool_image_for__19204f1e-2a26-41b0-9a60-0b01437fec14_0](https://github.com/keppy/WorldEnder.ai/assets/1513098/09d5f0c1-9a77-4300-b69c-309861283c3f)

# WorldEnder.ai 🌎💥

A text-adventure RPG using structured outputs from LLMs as the backend to simulate the decline of humanity, the outcome of global catastrophes, and your quest to rebuild civilization.

## Slides and Notebooks

[Presentation Slides](https://github.com/keppy/WorldEnder.ai/blob/master/WorldEnder.ai.pdf)

[Experiment Notebook](https://github.com/keppy/WorldEnder.ai/blob/master/notebooks/WorldEnder_ai.ipynb)

[Presentation Notebook (with some teaching)](https://github.com/keppy/WorldEnder.ai/blob/master/notebooks/WorldEnder_ai_Presentation.ipynb)

Copyright &copy; 2024 James Dominguez

## How to develop website

### database

```
cd webui/storage
docker-compose up -d
```

### api server

```
poetry run fastapi dev webui/api-server/main.py --reload
```

### web frontend

```
cd webui/apps/website
yarn dev
```

at that point, the DB, api server, and web FE are all running, and you can make code changes and they will hot-reload
