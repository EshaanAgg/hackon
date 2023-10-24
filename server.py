from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name)

openai.api_key = os.getenv("OPENAI_API_KEY")


def determine_model(input_text):
    if "movie" in input_text:
        return "Movie Recommender"
    elif "music" in input_text:
        return "Music Recommender"
    elif "shopping" in input_text:
        return "Shopping Recommender"
    else:
        return "No specific model found"


def movie_recommender(input_text):
    return "Based on your preferences, we recommend watching 'Inception'."


def music_recommender(input_text):
    return "You might enjoy listening to 'The Beatles'."


def shopping_recommender(input_text):
    return "We suggest you check out 'Amazon' for your shopping needs."


def make_result_human_readable(text):
    response = openai.Completion.create(
        engine="davinci",
        prompt=f"Make the following text human-readable: {text}",
        max_tokens=100,
    )
    return response.choices[0].text


@app.route("/process_text", methods=["POST"])
def process_text():
    try:
        data = request.get_json()
        input_text = data.get("text")
        model_name = determine_model(input_text)

        if model_name == "Movie Recommender":
            model_result = movie_recommender(input_text)
        elif model_name == "Music Recommender":
            model_result = music_recommender(input_text)
        elif model_name == "Shopping Recommender":
            model_result = shopping_recommender(input_text)
        else:
            model_result = "No specific model found"

        human_readable_result = make_result_human_readable(model_result)

        return jsonify({"result": human_readable_result})

    except Exception as e:
        return jsonify({"error": str(e)})


if __name__ == "__main__":
    app.run(debug=True)
