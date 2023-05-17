import os

from dotenv import load_dotenv
load_dotenv()
print(os.getenvb('OPENAI_API_KEY'))