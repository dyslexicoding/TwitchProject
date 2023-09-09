# get variable from .env file
from dotenv import load_dotenv
load_dotenv()
print(os.getenv('AccessToken'))
#