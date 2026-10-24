from dotenv import load_dotenv 
from google import genai 

load_dotenv() 
client = genai.Client() 

interaction1 = client.interactions.create(

    model = "gemini-3.8-flash", input = "my name is zain" )

print(interaction1.output_text)


interaction2 = client.interactions.create(
    model = "gemini-3.8-flash", input = "what is my name" )

print (interaction2.output_text)