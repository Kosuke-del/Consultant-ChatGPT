"""
This is a file to summarize sentences.
"""

import openai

text = input("要約したい文章を入力してください: ")

res = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Summarize these sentences in 50 words.「{text}」"},
    ]
)
res_content = res["choices"][0]["message"]["content"]

with open("output.txt1", encoding='utf-8' "w") as f:
    f.write(res_content)
    