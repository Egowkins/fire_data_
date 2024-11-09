import pandas as pd
import numpy as np
#from data_preparation import  ...
from video_to_frames import  regims


if __name__ == '__main__':
    a = pd.read_excel('regims/regim1.xlsx')
    print(a)
    regims('video/DSC_2365.MOV', 1, 131, 140, 5)
    # fps = 25
    # time - 4min 48 sec
    pass



