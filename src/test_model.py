import cv2 as cv
import matplotlib.pyplot as plt
import utils as utl
import numpy as np
from torch import nn
import torch.onnx
import os


MODLES = os.listdir(utl.get_modles_dir())
print(MODLES)



def pt_to_onnx(model_path:str, new_model_name:str):
    torch.onnx.export(
        model=model_path, 
        output_names=new_model_name,
        verbose=True,
        )




