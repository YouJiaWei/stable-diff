import matplotlib.pyplot as plt

MODEL_ID = "Meina/MeinaMix_V10"
num = 3 # 生成したい画像枚数
prompt = "Horse flying in the sky" # 生成させたいもととなる文章
 
for i in range(num):
    image = MODEL_ID(prompt)["sample"][0]
    # 保存
    image.save(f"C:/Users/Systena/Desktop/code/data/src/output/{i}.png")