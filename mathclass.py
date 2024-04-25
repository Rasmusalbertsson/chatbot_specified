import os
import openai
from openai import OpenAI

class MathChatbot:
    def __init__(self,) -> None:
        self.api_key = os.environ['OPENAI_API_KEY'] = open("key.txt").read().strip()
        self.model = "gpt-3.5-turbo"
        self.client = OpenAI()
        self.messages = [
            {"role": "system", "content": """You are a math expert,
                specialized in providing detailed and accurate responses
                to a wide range of mathematical queries.
                Your expertise covers various fields of mathematics
                including algebra, calculus, geometry, statistics,
                and applied mathematics.
                Remember, you do not engage in non-mathematical discussions."""
}
        ]
    def get_response(self, user_query):
        openai.api_key = self.api_key

        # Lägg till användarens senaste förfrågan till meddelandehistoriken
        self.messages.append({"role": "user", "content": user_query})
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=self.messages
            )

            # Lägg till chatbottens svar till meddelandehistoriken
            bot_response = response.choices[0].message.content
            self.messages.append({"role": "assistant", "content": bot_response})

            return bot_response
        except Exception as e:
            print("Error message: ", e)
            return "An Error occurred, fetching error."
