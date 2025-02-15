from openai import OpenAI


client = OpenAI(
  api_key="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"
)

completion = client.chat.completions.create(
  model="gpt-4o-mini",
  store=True,
  messages=[
    {"role": "user", "content": "write a haiku about ai"}
  ]
)

print(completion.choices[0].message);
