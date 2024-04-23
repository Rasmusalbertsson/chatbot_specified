import os
import openai
from openai import OpenAI
''' LÄNGRE PROMPT
    , including physical 
                landscapes, climate patterns, and cultural geography. 
                Your knowledge spans continents, countries, and diverse ecosystems.
'''
class GeographyChatbot:
    def __init__(self,) -> None:
        #self.api_key = os.environ['OPENAI_API_KEY'] = open("key.txt").read()
        self.api_key = os.environ['OPENAI_API_KEY'] = open("key.txt").read().strip()
        self.model = "gpt-3.5-turbo"
        self.client = OpenAI()
        self.messages = [
            {"role": "system", "content": """
                You are a Geography expert, skilled in providing in-depth insights 
                and information on global geographical features.
                you do not engage in non-geographical discussions"""
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

