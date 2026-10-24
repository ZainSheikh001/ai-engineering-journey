import json 
# What the LLM sends: TEXT (notice the outer single quotes, it's one string)

llm_text = '{"category": "refund", "urgency": "high"}' 
print(type(llm_text)) # what kind of thing is it?
# Convert the text into a real Python dictionary
data = json.loads(llm_text)
print (type(data))  # what kind of thing is it now?
print(data["category"])   # now we can read a field


    