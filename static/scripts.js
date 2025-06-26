// Получаем параметр из URL
const urlParams = new URLSearchParams(window.location.search);
const limit = urlParams.get('limit');
const ff = urlParams.get('ff');
const tf = urlParams.get('tf');

// Устанавливаем selected
if (ff && tf) {
document.getElementById('form-ff').value = ff;
document.getElementById('form-tf').value = tf;
}

// Устанавливаем selected
if (limit) {
document.getElementById('selectMenu').value = limit;
}


let select_field = document.getElementById('selectMenu');
select_field.addEventListener('change', function() {
    window.location.href = window.location.href.split('?')[0] + '?limit=' + this.value;
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
