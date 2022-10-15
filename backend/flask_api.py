#!flask/bin/python
from flask import Flask, request, jsonify, abort, Response
from FileStorage import storage
import json
import base64

app = Flask(__name__)


@app.route('/upload/image', methods=['POST'])
def upload_image():
    """
    Получаем обьект типа FormData
    :return: код 200, если все ок или другой, если не ок
    """
    # Из обьекта FormData беремеп файл по ключу 'file' ->
    # -> этот ключ должен быть известне бэкендеру и фронтендеру
    # -> с его помощью будет загружаться файл
    file = storage.File(request.files['file'])
    # Обьявляем папку, в которую будут помещаться файлы.
    directory = "images"
    # Если вызвать метод save_file() файл сохранится в папку default
    file_path = file.save_file(directory)
    # file_name - полный путь до файла на сервере.
    # на этом моенте мы можем загрузить фотографию в базу данных ->
    # А также, если возникнет ошибка, можно удалить файл file_path
    return "200"


@app.route('/get/image', methods=['GET'])
def load_image():
    # Получаем параметры get Запроса
    print(request.args['imageID'])
    # В идеале получаем путь к файлу из базы данных
    file_path = "C:/Users/Serj/Desktop/work/picture-sending/backend/images/8ea9f3f75cdd45d891a9f63b62466b18.JPG"
    # Кодирование изобрадение file_path
    with open(file_path, "rb") as img_file:
        my_string = base64.b64encode(img_file.read()).decode("utf-8")
    # Отправка base64 изображения
    return json.dumps({"success": 200, "image": my_string})


if __name__ == '__main__':
    app.run(debug=True)
