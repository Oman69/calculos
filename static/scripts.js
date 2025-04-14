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
