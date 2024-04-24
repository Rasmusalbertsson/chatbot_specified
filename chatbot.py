from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from mathclass import MathChatbot
from historyclass import HistoryChatbot
from old_cars import OldCarsChatbot
from geography import GeographyChatbot
import textwrap
import tiktoken

class ChatbotApp(App):   
    def build(self):
        """
        Builds the main application layout, initializes widgets, and configures the user interface.

        Returns:
            FloatLayout: The root widget containing all other widgets for the application.
        """
        layout = FloatLayout()
        Window.size = (700, 900)

        # Backround image
        background = Image(
            source='backround.png',
            allow_stretch=True,
            keep_ratio=False,
            size_hint=(1, 1),
            pos_hint={'center_x': 0.5, 'center_y': 0.5})
        layout.add_widget(background)

        # Buttons
        btn_layout = BoxLayout(size_hint=(1, None),
                               height=70,
                               pos_hint={'top': 1})

        for topic in ["Math", "History", "Old Cars", "Geography"]:
            btn = Button(text=topic,
                         background_color = (0,0,0,1),
                         color = (1,1,1,1))
            btn.bind(on_press=self.on_topic_select)
            btn_layout.add_widget(btn)
        layout.add_widget(btn_layout)

        # Users question and chatbot answer labels
        self.user_query_label = Label(size_hint=(1,None),
                                      color = (1,0,0,1), 
                                      height=100,
                                      pos_hint={'x': 0, 'top': 0.93})
        self.token_label = Label(size_hint=(0.5, None),
                                height=10,
                                pos_hint={'center_x': 0.5, 'y': 0.2},
                                color=(0, 0, 0, 1),
                                font_size ='16sp',
                                bold = True)
        self.chatbot_response_label = Label(
                                size_hint_y=None,
                                size=(450, 700),
                                halign='center', valign='top',
                                text_size=(450, None),
                                pos_hint={'center_x': 0.5, 'center_y': 0.5},
                                color = (0,0,0,1),
                                font_size ='16sp',
                                bold = True)
        
        # Scrollview
        scroll_view = ScrollView(size_hint=(0.75, 0.5),
                                  pos_hint={'center_x': 0.5,
                                            'center_y': 0.6})
        scroll_view.add_widget(self.chatbot_response_label)
        layout.add_widget(self.user_query_label)
        layout.add_widget(scroll_view)

        # Text input field
        self.text_input = TextInput(size_hint =(1,None),
                                    hint_text = "Message bot...",
                                    hint_text_color=(0.2, 1, 0.2, 1),
                                    font_size='18sp',
                                    height=50,foreground_color = (1,0,0,1),
                                    multiline=False,
                                    pos_hint={'x': 0, 'y': 0.1},
                                    background_color = (1,1,1,0.6))
        self.text_input.bind(on_text_validate=self.on_text_enter)
        layout.add_widget(self.text_input)

        # Quit button
        end_chat_btn = Button(text='End Chat',
                                size_hint=(1, None),
                                height=75,
                                pos_hint={'x': 0, 'y': 0})
        end_chat_btn.bind(on_press=self.on_end_chat)
        layout.add_widget(end_chat_btn)
        layout.add_widget(self.token_label)

        return layout

    def wrap_text(self, text, width=50):
        """
        Wraps the given text to a specified width.

        Args:
            text (str): The text to wrap.
            width (int): The maximum line width in characters.

        Returns:
            str: The wrapped text.
        """
        return '\n'.join(textwrap.wrap(text, width))

    def on_topic_select(self, instance):
        """
        Handles topic selection, initializes the appropriate chatbot based on the selected topic.

        Args:
            instance (Button): The button instance that was pressed.
        """
        topic = instance.text
        if topic == "Math":
            self.chatbot = MathChatbot()
            self.botname = "Bot-Math Expert"
        elif topic == "History":
            self.chatbot = HistoryChatbot()
            self.botname = "Bot-History Expert"
        elif topic == "Old Cars":
            self.chatbot = OldCarsChatbot()
            self.botname = "Bot-Old Cars Expert"
        else:
            self.chatbot = GeographyChatbot()
            self.botname = "Bot-Geo Expert"

    
    def on_text_enter(self, instance):
        """
        Processes the text entered by the user, displays the query, fetches and displays the response from the chatbot.

        Args:
            instance (TextInput): The text input instance where the user entered the message.
        """
        user_query = instance.text
        self.user_query_label.text = "You: " + user_query
        if self.chatbot:
            response = self.chatbot.get_response(user_query)
            self.chatbot_response_label.text = f"{self.botname}: " + response
           
            instance.text = ''
            tokens = self.num_tokens_from_messages(response)
            self.token_label.text = f"TOTAL TOKEN USED IN THIS CONVERSATION: {tokens}"
            print(response)
            print(tokens)

    
    def on_end_chat(self, instance):
        """
        Ends the chat session and closes the application.

        Args:
            instance (Button): The button instance that was pressed to end the chat.
        """
        self.user_query_label.text = ""
        self.chatbot_response_label.text = ""
        self.chatbot = None
        App.get_running_app().stop()

    def num_tokens_from_messages(self,messages, model="gpt-3.5-turbo-0613"):
        """
        Calculates the number of tokens used by a list of messages.

        Args:
            messages (list of str): Messages for which to calculate the token count.
            model (str): The model name based on which token calculations are performed.

        Returns:
            int: The total number of tokens used.

        Raises:
            NotImplementedError: If the model is not supported for token calculation.
        """
        try:
            encoding = tiktoken.encoding_for_model(model)
        except KeyError:
            print("Warning: model not found. Using cl100k_base encoding.")
            encoding = tiktoken.get_encoding("cl100k_base")
        if model in {
            "gpt-3.5-turbo-0613",
            "gpt-3.5-turbo-16k-0613",
            "gpt-4-0314",
            "gpt-4-32k-0314",
            "gpt-4-0613",
            "gpt-4-32k-0613",
            }:
            tokens_per_message = 3
            tokens_per_name = 1
        elif model == "gpt-3.5-turbo-0301":
            tokens_per_message = 4  # every message follows <|start|>{role/name}\n{content}<|end|>\n
            tokens_per_name = -1  # if there's a name, the role is omitted
        elif "gpt-3.5-turbo" in model:
            print("Warning: gpt-3.5-turbo may update over time. Returning num tokens assuming gpt-3.5-turbo-0613.")
            return self.num_tokens_from_messages(messages, model="gpt-3.5-turbo-0613")
        elif "gpt-4" in model:
            print("Warning: gpt-4 may update over time. Returning num tokens assuming gpt-4-0613.")
            return self.num_tokens_from_messages(messages, model="gpt-4-0613")
        else:
            raise NotImplementedError(
                f"""num_tokens_from_messages() is not implemented for model {model}. See https://github.com/openai/openai-python/blob/main/chatml.md for information on how messages are converted to tokens."""
            )
        num_tokens = 0
        for message in self.chatbot.messages:
            num_tokens += tokens_per_message
            for key, value in message.items():
                num_tokens += len(encoding.encode(value))
                if key == "name":
                    num_tokens += tokens_per_name
        num_tokens += 3  # every reply is primed with <|start|>assistant<|message|>
        return num_tokens
if __name__ == '__main__':
    ChatbotApp().run()
