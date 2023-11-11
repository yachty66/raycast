#!/Users/maxhager/.virtualenvs/raycast/bin/python

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title grammar_correct
# @raycast.mode compact

# Optional parameters:
# @raycast.icon 🤖
import pyperclip
import marvin
from marvin import ai_fn
import os
from dotenv import load_dotenv
load_dotenv()

marvin.settings.openai.api_key = os.getenv("OPEN_AI_KEY")
marvin.settings.llm_model = 'openai/gpt-3.5-turbo'

@ai_fn
def grammar_lowercase(text: str) -> str:
    """
    from a text, remove all grammar errors and make everything lowercase if it's not important. dont include any qoutes in your response:
    """
# Read text from clipboard
original_text = pyperclip.paste()
corrected_text = grammar_lowercase(original_text)

# Replace text in clipboard with modified text
pyperclip.copy(corrected_text)
