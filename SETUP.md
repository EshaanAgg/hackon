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


# Mobile App

To run the mobile app locally, make sure you have Flutter installed and configured on your system.

1. The `app` directory of this repository contains all the code for the app.
2. Go to the `app` directory in a code editor (preferably Android Studio).
3. Type the following command to run the app in an emulator.
   
```
flutter run lib/main.dart
```
