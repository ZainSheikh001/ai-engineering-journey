# PREDICTION: The Roman Urdu version will use (more / fewer / the same) input tokens because ...
from dotenv import load_dotenv
from google import genai 
load_dotenv()

client = genai.Client() 

MODEL = "gemini-3.8-flash"

interaction1 = client.interactions.create(
    model  = MODEL ,
    input = " What is the capital of Pakistan? Answer in one sentence"
)

answer1 = interaction1.output_text

interaction2 = client.interactions.create(
    model  = MODEL ,
    input = " Pakistan ki rajdhani kya hai? Sirf ek jumle mein jawab dein"
)

answer2 = interaction2.output_text

print(f"English → input: {interaction1.usage.total_input_tokens} | output: {interaction1.usage.total_output_tokens} | thinking {interaction1.usage.total_thought_tokens} | total tokens {interaction1.usage.total_tokens}")
print(f"Urdu → input: {interaction2.usage.total_input_tokens} | output: {interaction2.usage.total_output_tokens} | thinking {interaction2.usage.total_thought_tokens} | total tokens {interaction2.usage.total_tokens}")