let select_field = document.getElementById('selectMenu');
select_field.addEventListener('change', function() {
let url = window.location.href.split('?')[0] + '?limit=' + this.value;
window.location.href = url;
});


function selectItem(selectedItem) {
            const items = document.querySelectorAll('.base_navbar_list a');
            items.forEach(item => {
                item.classList.remove('selected');
            });
            selectedItem.classList.add('selected');
        }

function copyDivToClipboard(elem) {
  // Получаем текст для копирования
  const text = elem.textContent;
  // Копируем текст в буфер обмена
  navigator.clipboard.writeText(text).then(function() {
    alert("Пароль скопирован в буфер обмена!");
  }).catch(function(error) {
    alert("Ошибка копирования: " + error);
  })}

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
            <p>Ссылка: <a href="${data.file_url}" target="_blank">${data.file_url}</a></p>
            <p>Полная ссылка: <input type="text" value="${window.location.origin}${data.file_url}" readonly style="width: 100%"></p>
        `;
    } catch (error) {
        fileInfo.innerHTML = `<p style="color: red">Ошибка: ${error.message}</p>`;
    }
}
