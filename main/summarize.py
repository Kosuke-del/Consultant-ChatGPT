"""
This is a file to summarize sentences.
"""

import openai

text = input("要約したい文章を入力してください: ")
max_length = input("要約した文章の最大長を入力してください: ")

res = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": f"Summarize these sentences in {max_length} words.「{text}」"},
    ]
)
res_content = res["choices"][0]["message"]["content"]

print(f"要約した文章です: {res_content}")
