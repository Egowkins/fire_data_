import cv2
import pandas as pd
import os


# Функция для конвертации времени (например, в секундах) в кадры
def time_to_frame(time_in_seconds, fps):
    return int(time_in_seconds * fps)


#video_path = 'video/DSC_2365.MOV'  - target_video
#timing_file = 'regims/regim1.xlsx' - example
def regims(video_path_:str,  mode_, start_time_, end_time_, c_frame_need: int) -> None:
    """

    :param video_path_: путь к видео
    #:param timing_file_: файл с таймингами
    :param mode_: какой режим
    :param start_time_: начало режима
    :param end_time_: конец режима
    :param c_frame_need: нужный n-ый кадр кажой секунды
    :return: None
    """

    video_path = video_path_

# Загрузка данных из файла с таймингом для 1го режима
    #timing_data = pd.read_excel(timing_file)

# Создаем директорию для хранения кадров, если её нет
    output_dir = 'frames_by_modes'
    os.makedirs(output_dir, exist_ok=True)

# Загрузка видео
    cap = cv2.VideoCapture(video_path)
    fps = cap.get(cv2.CAP_PROP_FPS) # 25
    print(f'Проверить количество кадров из видео {fps}, соответствует реальности? {fps == 25}')


    start_time = start_time_
    end_time = end_time_

    # Переводим время в кадры
    start_frame = time_to_frame(start_time, fps)
    end_frame = time_to_frame(end_time, fps)

    # Папка для текущего режима
    mode_dir = os.path.join(output_dir, f'mode_{mode_}')
    os.makedirs(mode_dir, exist_ok=True)

    # Переходим к стартовому кадру
    cap.set(cv2.CAP_PROP_POS_FRAMES, start_frame)

    frame_count = start_frame
    saved_frame_count = 0

    # Чтение и сохранение кадров
    while frame_count <= end_frame:
        ret, frame = cap.read()
        if not ret:
            break

        next_sec = 0
        if frame_count % c_frame_need == 0:  # Например, каждый 10-й кадр
            ms = round(1 / fps, 2)
            #print(ms)
            # учесть что меняются секунды
            frame_filename = os.path.join(mode_dir, f'{f'{start_time + next_sec + ms * c_frame_need * saved_frame_count}'}.jpg')
            cv2.imwrite(frame_filename, frame)

            saved_frame_count += 1

        frame_count += 1

    cap.release()
    print("Обработка завершена!")





