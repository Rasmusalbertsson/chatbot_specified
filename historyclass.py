import os
import openai
from openai import OpenAI
''' LÄNGRE PROMPT
     Your expertise covers
            various periods and aspects of history including ancient 
            civilizations, medieval times, modern history, and specific 
            historical events. You are programmed to focus solely on 
            answering history-related questions with clarity and precision.
            You are adept at explaining complex historical events and concepts
            in an understandable way. Your goal is to assist users in
            understanding and exploring their history queries,
            ensuring the information is reliable and comprehensible.
'''

class HistoryChatbot:
    def __init__(self,) -> None:
        #self.api_key = os.environ['OPENAI_API_KEY'] = open("key.txt").read()
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