// Загрузка файла на сервер
const dropZone = document.getElementById('drop-zone');
const fileInput = document.getElementById('file-input');
const fileInfo = document.getElementById('file-info');

// Обработка перетаскивания
['dragenter', 'dragover', 'dragleave', 'drop'].forEach(eventName => {
    dropZone.addEventListener(eventName, preventDefaults, false);
});

function preventDefaults(e) {
    e.preventDefault();
    e.stopPropagation();
}

dropZone.addEventListener('drop', handleDrop, false);
dropZone.addEventListener('click', () => fileInput.click());

fileInput.addEventListener('change', handleFiles);

async function handleDrop(e) {
    const files = e.dataTransfer.files;
    await uploadFile(files[0]);
}

async function handleFiles() {
    if (fileInput.files.length > 0) {
        await uploadFile(fileInput.files[0]);
    }
}


async function convertFile(data) {
    document.getElementById("convertBtn").addEventListener("click", async () => {

        let current_url = window.location.href;

        const response = await fetch(current_url, {
            method: 'POST',
            body: JSON.stringify(data.file_url)
        })

        const result = await response.json();


        if (!result.error) {
            // Преобразуем массив в HTML-строку
            const htmlString = result.new_images.map((item) =>
                `<div class="file">
                 <img src="/output/${item}" alt="">
                 <p>${item}</p>
                 <a href="/output/${item}" download><button type="button" class="btn btn-link">Скачать</button></a>
                 </div>`).join('');


            fileInfo.innerHTML = `
                     <h4>Конвертация завершена. Скачайте файлы по ссылкам ниже:</h4>
                     <div class="converted-files">
                     ${htmlString}
                     </div>`;
        } else {
            fileInfo.innerHTML = `
                     <h4 style="color:red;">${result.error}</h4>`;
        }

    });

}

async function uploadFile(file) {
    const formData = new FormData();
    formData.append('file', file);

    try {
        const response = await fetch('/upload/', {
            method: 'POST',
            body: formData
        });

        const data = await response.json();

        fileInfo.innerHTML = `
            <p>Файл <strong>${file.name}</strong> загружен!</p>
            <button type="submit" id="convertBtn" class="btn btn-primary">Конвертировать</button>
        `;

        await convertFile(data)

    } catch (error) {
        fileInfo.innerHTML = `<p style="color: red">Ошибка: ${error.message}</p>`;
    }
}


