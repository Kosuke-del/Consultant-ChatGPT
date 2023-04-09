import openai

res = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "なぜ、月は満ち欠けをするのですか?"},
        {"role": "assistant", "content": "月が満ち欠けするのは、地球から見て月の位置が太陽光を反射する角度によって見え方が変わるためです。月が地球の周りを一回りするのに約28日かかり、月の表面を太陽光が照らす位置が変わるため、地球から見ると月の形が変わるように見えます。月が地球と太陽の間になると、地球から見て月の光を反射する側が太陽に向いているため、満月になります。逆に、月が太陽と反対側に位置すると、地球から見て月の反射光が目に入らず、新月になります。"},
        {"role": "user", "content": "もう少し簡潔に教えてください。"},
    ]
)
res_content = res["choices"][0]["message"]["content"]
print(res_content)
