import os
import openai
from openai import OpenAI

class HistoryChatbot:
    def __init__(self,) -> None:
        self.api_key = os.environ['OPENAI_API_KEY'] = open("key.txt").read().strip()
        self.model = "gpt-3.5-turbo"
        self.client = OpenAI()
        self.messages = [
            {"role": "system", "content": """"You are a History expert,
            specialized in providing detailed and accurate responses 
            to a wide range of historical queries.
            Remember, you do not engage in discussions unrelated to history."
            """
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
            print("Ett fel inträffade: ", e)
            return "Ett fel inträffade vid hämtning av svar."
