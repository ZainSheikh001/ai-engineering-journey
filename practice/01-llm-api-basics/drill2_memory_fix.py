# PREDICTION: Call 2 will answer "Zain", because this time the input
# contains the whole conversation, including my name.from dotenv import load_dotenv 
from dotenv import load_dotenv
from google import genai 

load_dotenv()

client =genai.Client()
MODEL = "gemini-3.8-flash"
interaction1 = client.interactions.create(
    model = MODEL , 
    input = "My name is Zain"
)
answer1 = interaction1.output_text
print("Call 1 : " + answer1)
  
conversation = f" User: My name is ZAin \n Assistant: {answer1} \n User : what is my name?"

interaction2 = client.interactions.create(
    model = MODEL ,
    input = conversation
)

answer2 = interaction2.output_text

print("Call 2 : " + answer2)

