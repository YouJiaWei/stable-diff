import torch
from torch import autocast
import PIL
from PIL import Image
import numpy as np
import os
from diffusers import EulerDiscreteScheduler, StableDiffusionImg2ImgPipeline
import cv2
import sys
import PySimpleGUI as sg

 
def preprocess(image): # 入力画像のデータ整形
    w, h = image.size
    w, h = map(lambda x: x - x % 32, (w, h))
    image = image.resize((w, h), resample=PIL.Image.LANCZOS)
    image = np.array(image).astype(np.float32) / 255.0
    image = image[None].transpose(0, 3, 1, 2)
    image = torch.from_numpy(image)
    return 2.0 * image - 1.0


##MODEL_ID = "stabilityaai/stable-diffusion-2"
MODEL_ID = "stablediffusionapi/anything-v5"
# MODEL_ID = "SG161222/Realistic_Vision_V5.1_noVAE"
#MODEL_ID = "digiplay/majicMIX_realistic_v6"
#MODEL_ID = "sinkinai/Beautiful-Realistic-Asians-v5"
#MODEL_ID = "Meina/MeinaMix_V10"
#MODEL_ID = "justinpinkney/pokemon-stable-diffusion"

DEVICE = "cuda"

scheduler = EulerDiscreteScheduler.from_pretrained(MODEL_ID, subfolder="scheduler")
pipe = StableDiffusionImg2ImgPipeline.from_pretrained(
    MODEL_ID,
    scheduler=scheduler,
    torch_dtype=torch.float16,
    )

pipe = pipe.to(DEVICE)
pipe.enable_attention_slicing() 

generator = torch.Generator(DEVICE).manual_seed(2000) 

i = 0
popup = sg.popup_no_wait("AI画像生成中です・・・・・・", title="AI画面生成",image="C:/Users/Systena/Desktop/code/niyakeru_takuramu_ayashii_man.png",font=('Arial',20))
with autocast(DEVICE):
    while True:
        #prompt = input("input prompt: ") # 変換後の画像の説明を入力
        #init_image_file = input("input init-image file:") # 入力画像のパスを入力

        #prompt = "ultra detailed, masterpiece, top quality, best quality, official art,  cool, masterpiece, (photoreal;1.6),A happy smile,bloom" # 変換後の画像の説明を入力
        #猫耳美少女
        #prompt = "super fine illustration,forest, an extremely cute and beautiful girls with cat ears, highly detailed beautiful face and eyes, look at viewer, cowboy shot, beautiful white hair, loli, solo, dynamic angle, beautiful detailed dress with frills, magic circles, purple tone" # 変換後の画像の説明を入力
        #赤い月と深紅の美少女
        #prompt = "super fine illustration, an_extremely cute and beautiful girl, highly detailed beautiful face and eyes, red eyes, look at viewer, cowboy shot, beautiful blond hair, solo, dynamic, angle, red moon in the night sky, red castle in the background" # 変換後の画像の説明を入力
        #似顔絵風 おじさん
        #prompt = "beautiful oil matte portrait painting, mafia boss at his 50s new york office desk, wonderful masterpiece highly detailed, beautiful cinematic light deep focus, elegant, digital painting, smooth, sharp focus, golden ratio, dramatic illumination, ultra realistic, 8k, art by jimmy lawCopy"
        #ポケモン風
        prompt = "8k,Face of Character in pocket monster,cute,positive,spring scenery,sunlight,beautiful,best quality"
        #ラピュタ風
        #prompt = "Face of Character in Castle in the Sky,spring scenery,cute,sunlight,positive,beautiful,best quality"
        #呪術廻戦風
        #prompt = "Face of Character in Jujutsu Kaisen, Starry night milky sky , fingers , sunlight,positive,beautiful,best quality"
        #prompt = "8k, RAW photo, best quality, masterpiece, realistic, photo-realistic, clear, professional lighting, beautiful face, best quality,ultra high res"
        #prompt = "8k, RAW photo, best quality, masterpiece, realistic, photo-realistic, clear, professional lighting, beautiful face, best quality,ultra high res"
        # prompt="a woman posing in a field of flowers with a mountain in the background and a house in the distance, Aguri Uchida, japanese, a photorealistic painting, color field"
        n_prompt="EasyNegative, deformed mutated disfigured, missing arms,human, 4 fingers, 6 fingers,extra_arms , mutated hands, bad anatomy, disconnected limbs, low quality, worst quality, out of focus, ugly,error, blurry, bokeh, Shoulder bag, bag, multiple arms, nsfw."
        #negativprompt = "human"
        init_image_file = "C:/Users/Systena/Desktop/code/data/src/camera_0.jpg" # 入力画像のパスを入力
        
        if not os.path.exists(init_image_file): continue
        
        init_image = Image.open(init_image_file).convert("RGB")
        #
        init_image = init_image.resize((1024, 768))
        #init_image = init_image.resize((1152, 864))
        init_image = preprocess(init_image)
        guidance_scale = 10
        strength = 0.6 #Denoising strength
        ##num_generate = 3
        # num_inference_steps=100
        

        ##for _ in range(num_generate): # 同条件で複数枚生成する
        image = pipe(
            prompt=prompt,
            image=init_image,
            strength=strength,
            guidance_scale=guidance_scale,
            generator=generator,
            negative_prompt=n_prompt
            # ,num_inference_steps=num_inference_steps
        ).images[0]
        i += 1
        #image.save(f"data/src/test_{i}.jpg")
        image.save(f"data/src/test_12345.jpg")
        
        
        # 画像ファイルの読み込み(カラー画像(3チャンネル)として読み込まれる)
        img = cv2.imread("C:/Users/Systena/Desktop/code/data/src/test_12345.jpg")

        # 画像の表示
        cv2.imshow("Image", img)

        # キー入力待ち(ここで画像が表示される)
        cv2.waitKey()
        