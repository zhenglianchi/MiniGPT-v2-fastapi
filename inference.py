import requests
from PIL import Image
import json_numpy
import numpy as np

json_numpy.patch()

example = {"image_path":["/home/mhm314/MiniGPT-4/examples_v2/office.jpg",
                         "/home/mhm314/MiniGPT-4/examples_v2/KFC-20-for-20-Nuggets.jpg",
                         "/home/mhm314/MiniGPT-4/examples_v2/sofa.jpg",
                         "/home/mhm314/MiniGPT-4/examples_v2/2000x1372_wmkn_0012149409555.jpg",
                         "/home/mhm314/MiniGPT-4/examples_v2/thief.png"
            ],
           "instruction":[
               "[grounding] describe this image in detail",
               "[identify] what is this {<4><50><30><65>}",
               "[detection] sofas",
               "[refer] the world cup",
                "Is the weapon fateful"
           ]
           }

question_index = 0
# 加载图像
image_path = example["image_path"][question_index]
instruction = example["instruction"][question_index]

# 准备请求数据
url = "http://10.129.38.192:8001/act"

image = np.array(Image.open(image_path))
query = {"instruction": instruction, "image": image}

# 发送 POST 请求
response = requests.post(url, json=query)

# 处理响应
if response.status_code == 200:
    result = response.json()
    print("BOT:", result["llm_message"])
else:
    print("Error:", response.status_code, response.text)
