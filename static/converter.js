// Загрузка файлов на сервер
const dropZone = document.getElementById('drop-zone');
const fileInput = document.getElementById('file-input');
fileInput.multiple = true; // Разрешаем выбор нескольких файлов
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
    await uploadFiles(files);
}

async function handleFiles() {
    if (fileInput.files.length > 0) {
        await uploadFiles(fileInput.files);
    }
}

async function convertFiles(data) {
    document.getElementById("convertBtn").addEventListener("click", async () => {
        let current_url = window.location.href;

        let unite_files_elem = document.getElementById("unite_files");
        let unite_files = false;

        if (unite_files_elem) {
            unite_files = unite_files_elem.checked;
        }

        const response = await fetch(current_url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({file_urls: data.file_urls, unite_files: unite_files})
        });

        const result = await response.json();

        if (!result.error) {
            // Группируем файлы по исходным именам
            const filesHtml = result.new_images.map(fileGroup => {
                const filesList = fileGroup.map(item =>
                    `<div class="file">
                        <img src="/output/${item}" alt="">
                        <p>${item}</p>
                        <a href="/output/${item}" download>
                            <button type="button" class="btn btn-link">Скачать</button>
                        </a>
                    </div>`
                ).join('');

                return `<div class="file-group">${filesList}</div>`;
            }).join('');

            fileInfo.innerHTML = `
                <h4>Конвертация завершена. Скачайте файлы по ссылкам ниже:</h4>
                <div class="converted-files">
                    ${filesHtml}
                </div>
                <a href="/${result.archive_name}" download>
                <button type="button" class="btn btn-outline-primary">
                <i class="bi bi-download"></i> Скачать архив c файлами</button></a>`;
        } else {
            fileInfo.innerHTML = `<h4 style="color:red;">${result.error}</h4>`;
        }
    });
}

async function uploadFiles(files) {
    const formData = new FormData();

    // Добавляем все файлы в FormData
    for (let i = 0; i < files.length; i++) {
        formData.append('files', files[i]);
    }

    try {
        const response = await fetch('/upload/', {
            method: 'POST',
            body: formData
        });

        const data = await response.json();

        // Отображаем список загруженных файлов
        const filesList = data.file_urls.map(url => {
            const fileName = url.split('/').pop();
            return `<li>${fileName}</li>`;
        }).join('');

        const urlParams = new URLSearchParams(window.location.search);
        const tf = urlParams.get('tf');
        let files_count = data.file_urls.length;

        if (tf === 'pdf' && files_count > 1) {
            fileInfo.innerHTML = `
            <p>Загружено ${files_count} файлов:</p>
            <ol>${filesList}</ol>
            <div class="form-check form-switch form-check-unite">
                  <label class="form-check-label" for="ascii_low">Объединить файлы в один ${tf.toUpperCase()}?</label>
                  <input class="form-check-input" type="checkbox" role="switch" id="unite_files" name="unite_files" checked>
            </div>
            <button type="submit" id="convertBtn" class="btn btn-outline-primary"><i class="bi bi-arrow-repeat"></i> Конвертировать все</button>
        `;

        } else {
            fileInfo.innerHTML = `
            <p>Загружено ${files_count} файлов:</p>
            <ol>${filesList}</ol>
            <button type="submit" id="convertBtn" class="btn btn-outline-primary"><i class="bi bi-arrow-repeat"></i> Конвертировать все</button>
        `;
        }

        await convertFiles(data);

    } catch (error) {
        fileInfo.innerHTML = `<p style="color: red">Ошибка: ${error.message}</p>`;
    }
}


