import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

englishSentence = "How much does that cost?"
LanguageList = ["French", "Japanese", "Hindu"]

response = openai.Completion.create(
  engine="text-davinci-002",
  prompt=f"Translate {englishSentence} to {LanguageList}",
  temperature=0.3,
  max_tokens=100,
  top_p=1.0,
  frequency_penalty=0.0,
  presence_penalty=0.0
)
print(f"\nTranslate: {englishSentence}" + response["choices"][0]["text"])

