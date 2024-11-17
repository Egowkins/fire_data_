import pandas as pd
import numpy as np
import video_to_frames
import find_alpha_true as fat


def img_create(flag: False):
    if flag is True:
        data = pd.read_excel('input/prep_data_true.xlsx')
        data['alpha'] = round(data['alpha'], 2)
        timing_data = pd.DataFrame(data)
        print(timing_data)
        fat.finder(timing_data, 'alpha')
        print(timing_data)

        # путь к видео
        video_path = 'video/DSC_2365.MOV'
        n_frames_per_second = 25  # Сколько кадров берем из каждой секунды
        video_to_frames.extract_n_frames_per_second(video_path, timing_data, n_frames_per_second, info=False)





if __name__ == '__main__':
    img_create(True)

    #экспортируем из экселя


