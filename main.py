from dotenv import load_dotenv
import os
load_dotenv()
print(f"Password : {os.getenv('API_KEY')}")

