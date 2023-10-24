# Web App

To run the webapp locally, you need follow the following steps:

1. Create a `.env` with the following keys:

```
OPENAI_ORGANIZATION=
OPENAI_API_KEY=

```

2. Install the dependencies with

```bash
pip install openai chainlit
```

3. Run `chainlit run web.py -w` to start interaction in a chat based environment for the web.
4. The web GUI would start at [http://localhost:8000/](http://localhost:8000/).
