import sys
from PIL import Image

input_path = "/home/arun/.gemini/antigravity/brain/6c9f7177-9f55-45b7-aae8-c37774332a14/real_tridala_1788852447188.png"
output_path = "/home/arun/SIDDAGANGA/tridala.webp"

try:
    img = Image.open(input_path).convert("RGBA")
    datas = img.getdata()
    
    newData = []
    for item in datas:
        # Distance from white
        if item[0] > 210 and item[1] > 210 and item[2] > 210:
            if abs(item[0]-item[1]) < 20 and abs(item[1]-item[2]) < 20:
                newData.append((255, 255, 255, 0))
                continue
        newData.append(item)
    
    img.putdata(newData)
    img = img.resize((200, 200), Image.Resampling.LANCZOS)
    img.save(output_path, "WEBP")
    print("Success")
except Exception as e:
    print(e)
