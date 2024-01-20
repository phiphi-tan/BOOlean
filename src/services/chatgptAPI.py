from openai import OpenAI
import constants

client = OpenAI(
    api_key=constants.API_KEY_OPENAI
)


def get_response(input):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": input,
            }
        ],
        model=constants.GPT_MODEL,
    )

    return chat_completion.choices[0].message.content
