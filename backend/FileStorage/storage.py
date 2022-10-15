import uuid
import pathlib


class File:

    def __init__(self, file=None):
        self.file = file

    @staticmethod
    def __file_exists(path, filename):
        paths = path.glob(filename)
        paths = list(map(str, paths))
        return len(paths) != 0

    def save_file(self, directory="default"):
        if self.file is not None:
            # Сохраняем директорию, в которую схраним файл
            save_directory = directory
            # Получаем расширение файла
            file_extension = self.file.filename.split('.')[-1]
            # Получаем будущую директорию файла
            path_to_file = pathlib.Path.cwd().joinpath(save_directory)
            path_to_file.mkdir(parents=True, exist_ok=True)
            # Генерируем уникальное имя файла
            unique_filename = uuid.uuid4().hex
            while self.__file_exists(path_to_file, unique_filename):
                unique_filename = uuid.uuid4().hex
            # Присваиваем уникальное имя файлу
            self.file.filename = f"{unique_filename}.{file_extension}"
            path_to_file = path_to_file.joinpath(self.file.filename)
            # Сохраняем файл с новым именем в директорию save_directory
            self.file.save(f"{path_to_file}")
            # Возвращаем путь к файлу
            return path_to_file
        else:
            return None
