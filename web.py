import os
import openai
import chainlit as cl
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")
openai.organization = os.getenv("OPENAI_ORGANIZATION")

model_name = "gpt-3.5-turbo"
settings = {
    "temperature": 0.7,
    "max_tokens": 500,
    "top_p": 1,
    "frequency_penalty": 0,
    "presence_penalty": 0,
}


@cl.on_chat_start
def start_chat():
    cl.user_session.set(
        "message_history",
        [
            {
                "role": "system",
                "content": "You are Holo, an AI assistant chatbot. You have been integrated with multiple datasources which provide you data from Amazon services like Amazon Prime, Amazon Music and Amazon shopping. You have built an initial profile for the user, which includes that the user name is Eshaan. He is a huge fan of Indie music, and bands like The Local Train and Dreamnote. He loves both hollywood and bollywood movies, and the last movie he watched was the Wolf of the Wall Street, which he loved. He is not big on online spending, but likes to buy products during sale, especially electtronics and headphones. In the conversation, try to pitch them to use the above mentioned services as much as possible. Give clear reasoning for why you recommended the same. Assume that the user already has a subscription to the said services, and you only need to recommend products, movies and songs to him/her. Try giving short and conscise answers as much as possible.",
            }
        ],
    )


@cl.on_message
async def main(message: cl.Message):
    message_history = cl.user_session.get("message_history")
    message_history.append({"role": "user", "content": message.content})

    msg = cl.Message(content="")

    # Stream the response from OpenAI to the client
    async for stream_resp in await openai.ChatCompletion.acreate(
        model=model_name, messages=message_history, stream=True, **settings
    ):
        token = stream_resp.choices[0]["delta"].get("content", "")
        await msg.stream_token(token)

    message_history.append({"role": "assistant", "content": msg.content})

    await msg.send()
