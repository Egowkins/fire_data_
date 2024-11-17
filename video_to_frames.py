import cv2
import pandas as pd
import os


# Функция для конвертации времени в кадры
def time_to_frame(time_in_seconds, fps):
    return int(time_in_seconds * fps)


def extract_n_frames_per_second(video_path: str, timing_data: pd.DataFrame, n_frames_per_second: int, info: False) -> None:
    """
    Извлечение n кадров из каждой секунды видео. Кадры обрезаются в виде квадрата
    :param video_path: путь к видео
    :param timing_data: DataFrame с временными метками (T) и альфа (alpha)
    :param n_frames_per_second: количество кадров, которое нужно извлечь из каждой секунды
    :return: None
    """
    #создаем папку для хранения
    output_dir = 'frames_by_alpha'
    os.makedirs(output_dir, exist_ok=True)

    #подгружаем видео
    cap = cv2.VideoCapture(video_path)
    fps = cap.get(cv2.CAP_PROP_FPS)
    if info:
        print(f'Количество кадров в секунду (FPS): {fps}')

    if not fps:
        raise ValueError("FPS не определено ")

    #интервал между кадрами в одной секунде
    frame_interval = int(fps / n_frames_per_second)

    #группировка данные по альфе
    grouped_data = timing_data.groupby('alpha_t')

    for alpha, group in grouped_data:
        #Создаем папку для текущей альфы
        mode_dir = os.path.join(output_dir, f'mode_{alpha}')
        os.makedirs(mode_dir, exist_ok=True)
        TOTAL = 0
        for _, row in group.iterrows():
            start_time = row['T']
            end_time = start_time + 1  #дергаем все кадры в пределах указанной секунды

            start_frame = time_to_frame(start_time, fps)
            end_frame = time_to_frame(end_time, fps)

            #начинаем со стартового кадра
            cap.set(cv2.CAP_PROP_POS_FRAMES, start_frame)

            frame_count = start_frame
            saved_frame_count = 0

            while frame_count <= end_frame and saved_frame_count < n_frames_per_second:
                ret, frame = cap.read()
                if not ret:
                    break

                #сохраняем кадр в папку
                frame_filename = os.path.join(mode_dir, f'{start_time}_{saved_frame_count}.jpg')
                #вырезаем квадрат
                frame = frame[50:670, 355:975]
                cv2.imwrite(frame_filename, frame)

                saved_frame_count += 1
                frame_count += frame_interval
                TOTAL += 1
        if info:
            print(f'Подгруппа {alpha}, количество изображений {TOTAL} ')

    cap.release()
    print("Обработка завершена!")
