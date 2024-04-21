import os
import shutil


def move_images(src, dst):
    try:
        if not os.path.exists(src) or not os.path.exists(dst):
            raise Exception("Директории src или dst не существуют")

        for filename in os.listdir(src):
            if filename.lower().endswith(('.png', '.jpg')):
                src_file = os.path.join(src, filename)
                dst_file = os.path.join(dst, filename)
                shutil.move(src_file, dst_file)

        print("Фотографии и картинки успешно перемещены в директорию", dst)

    except Exception as e:
        print("Ошибка:", e)


def create_archive(dst):
    try:
        if not os.path.exists(dst):
            raise Exception("Директория dst не существует")

        shutil.make_archive(dst, 'zip', dst)
        print("Архив успешно создан на основе директории", dst)

    except Exception as e:
        print("Ошибка при создании архива:", e)


src = input("Введите путь к директории src: ")
dst = input("Введите путь к директории dst: ")

move_images(src, dst)
create_archive(dst)
