import openai

input_file = input("要約したい対象のファイルのパス: ")
with open(input_file, encoding='utf-8') as f:
    text = f.read()

res = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": f"この文章を要約してください。「{text}」"},
    ]
)
res_content = res["choices"][0]["message"]["content"]

with open("output.txt", "w") as f:
    f.write(res_content)
    