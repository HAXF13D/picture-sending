//import {axios} from './node_modules/axios';

const sendFile = document.getElementById('send-file');
let picture = document.getElementById('image_from_server');
const loadFile = document.getElementById('load-file');

const baseUrl = 'http://127.0.0.1:5000';

const handleImageRespons = (response) => {
    // Получаем изображение в base64
    // Декадируем изображение из base64
    const byteCharacters = atob(response['image']);
    const byteNumbers = new Array(byteCharacters.length);
    for (let i = 0; i < byteCharacters.length; i++) {
        byteNumbers[i] = byteCharacters.charCodeAt(i);
    }
    const byteArray = new Uint8Array(byteNumbers);
    // Размешаем изображение там, где необходим
    document.getElementById("image_from_server").src = URL.createObjectURL(new Blob([byteArray], { type: 'image/png' }));
}


const getFile = () =>{
    // Получаем изображение при загрузке сайта
    // params отправялем данные, необходимые для выбора изобрадения
    axios.get(
        baseUrl + '/get/image', 
        { params: { imageID: 1 } }
    ).then(
        response => (
            handleImageRespons(response.data)
        )
    );
}

getFile();


sendFile.addEventListener('change', (e) => {
    // Если поле ввода изобрадение обновлилось
    // Получаем файл
    const file = e.target.files[0];
    // Формируем данные
    let formData = new FormData();
    formData.append("file", file);
    // ОТправляем файл на сервер
    axios.post(
        baseUrl + '/upload/image', 
        formData
    ).then(
        response => (
            console.log(response.data)
        )
    );
});