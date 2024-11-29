# ImageShield[Light]: Another simple image obfuscation tool
# Author: huzpsb @ github, 2024-11-29
# TLP: GREEN [Contains uncommon knowledge that may be useful to defenders]
import os

import numpy as np
import torch
from PIL import Image, ImageFont, ImageDraw

# VersionCode: SillyFriend(4) aka ImageShield[Light]
# Basic idea:
# Use a badly trained neural network(called 'SillyFriend') to 'remove' watermark from an image.
# The 'watermark' being removed is actually non-existent.
# The side effects of this 'removal' is that the noise of removed watermark will be added to the image.
# As a consequence, since the neural network is badly trained,
# the noise is significant and detectable by human eyes; while not that easy to be removed by other neural networks.
# I hereby propose this kind of noise to be called 'FurryNoise'.

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
font = ImageFont.truetype('.\\bin\\1.ttf', 160)
remove = torch.load('.\\bin\\fixer.pth', weights_only=False, map_location=device).to(device)


def fix_img(img0):
    height, width = img0.size
    mask_img = Image.new('L', img0.size, 0)
    draw = ImageDraw.Draw(mask_img)
    x = 20
    while True:
        if x > width:
            break
        y = 20
        while True:
            if y > height:
                break
            draw.text((x, y), '福瑞', font=font, fill=16)
            y += 400
        x += 300
    mask = np.array(mask_img)
    mask = mask > 0

    npa = np.array(img0)
    red_torch = torch.tensor(npa[:, :, 0]).float().to(device)
    green_torch = torch.tensor(npa[:, :, 1]).float().to(device)
    blue_torch = torch.tensor(npa[:, :, 2]).float().to(device)
    red_fixed = remove(red_torch.unsqueeze(0).unsqueeze(0)).cpu().detach().squeeze().numpy().clip(0, 255)
    green_fixed = remove(green_torch.unsqueeze(0).unsqueeze(0)).cpu().detach().squeeze().numpy().clip(0, 255)
    blue_fixed = remove(blue_torch.unsqueeze(0).unsqueeze(0)).cpu().detach().squeeze().numpy().clip(0, 255)
    red_fixed = np.clip(red_fixed, 0, 255)
    green_fixed = np.clip(green_fixed, 0, 255)
    blue_fixed = np.clip(blue_fixed, 0, 255)
    red_fixed = np.where(mask, red_fixed, npa[:, :, 0])
    green_fixed = np.where(mask, green_fixed, npa[:, :, 1])
    blue_fixed = np.where(mask, blue_fixed, npa[:, :, 2])
    fixed = np.stack([red_fixed, green_fixed, blue_fixed], axis=2)
    return Image.fromarray(fixed.astype(np.uint8), 'RGB')


files = os.listdir('.\\i')
for f in files:
    print('Processing', f)
    img = Image.open('.\\i\\' + f)
    fixed = fix_img(img)
    fixed.save('.\\o\\' + f)
