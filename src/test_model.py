import cv2 as cv
import matplotlib.pyplot as plt
import src.utils as utl
import numpy as np
import torch
import os, onnx
from ultralytics import YOLO
from PIL import Image


MODLES = os.listdir(utl.get_modles_dir())
# print(MODLES)

def test_image():
    model = YOLO(os.path.join(utl.get_modles_dir(), MODLES[1]))
    img_1 = Image.open(os.path.join(utl.get_test_imgs_dir(), "test4.png"))
    results = model.predict(source=img_1, save=True)
    print(results)


def pt_to_onnx(model_path:str, new_model_name:str):

    model = torch.load(model_path)
    print(model)
    # device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    # dummy_input = torch.randn(1, 3, 224, 224)

    # torch.onnx.dynamo_export(
    #     model_path,
    #     dummy_input, 
    #     ).save(new_model_name)




