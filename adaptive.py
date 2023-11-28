import cv2
import numpy as np
import time
import random

# import albumentations as A
# from albumentations.pytorch.transforms import ToTensorV2
# from your_custom_module import shadow  # 导入您的 shadow 函数

class ShadowA:
    def __init__(self, light, p=1.0):
        self.light = light
        self.p = p

    def __call__(self, image, **kwargs):
        if self.light != 0 and self.p > random.random():
            image = shadow(image, self.light)
        return image

# # 在您的代码中使用 ShadowA 类
# T = [
#     A.SmallestMaxSize(max_size=size),
#     A.CenterCrop(height=size, width=size),
#     A.Normalize(mean=mean, std=std),
#     ToTensorV2(),
#     ShadowA(light=your_light_value, p=probability)  # 添加 ShadowA 转换
# ]


def shadow(input, light):
    # if random.random() < p:
    # light = random.randint(-light, light)
    # start_time = time.time()
    # 生成灰度图
    grey = cv2.cvtColor(input, cv2.COLOR_BGR2GRAY)
    grey = grey / 255.0

    # 确定阴影区
    # invert = (1.0 - grey) * (1.0 - grey)
    invert = np.multiply(1.0 - grey, 1.0 - grey)
    # 取平均值作为阈值
    thresh = np.mean(invert)
    mask = np.zeros(grey.shape, dtype=np.uint8)
    mask[invert >= thresh] = 255
    cv2.imwrite("mask.jpg", mask)
    
    # end_time = time.time()
    # elapsed_time = end_time - start_time
    # print('time1:', elapsed_time)
    
    # 参数设置
    # start_time = time.time()
    # max_value = 4
    # bright = light / 100.0 / max_value
    # mid = 1.0 + max_value * bright
    bright = light / 100.0
    mid = 1.0 + bright
    
    # end_time = time.time()
    # elapsed_time = end_time - start_time
    # print('time2:', elapsed_time)

    start_time = time.time()
    # # 边缘平滑过渡
    # 计算阴影区域和非阴影区域的中间率和亮度率
    is_shadow = (mask == 255)
    mi = np.where(is_shadow, mid, (mid - 1.0) / thresh * invert + 1.0)
    br = np.where(is_shadow, bright, (1.0 / thresh * invert) * bright)

    # 将 mi 和 br 放回相应的矩阵
    mi = np.repeat(mi[:, :, np.newaxis], 3, axis=2)
    br = np.repeat(br[:, :, np.newaxis], 3, axis=2)

    # 阴影提亮，获取结果图
    temp = (input / 255.0) ** (1.0 / mi) * (1.0 / (1 - br))
    result = np.clip(temp * 255, 0, 255).astype(np.uint8)


    # end_time = time.time()
    # elapsed_time = end_time - start_time
    # print('time1:', elapsed_time)
    return result
    # else:
    #     return input