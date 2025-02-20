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


function UpdateContent(cat_value) {
            let url = window.location.href + '?category=' + cat_value
            fetch(url) // Адрес для получения данных
                .then(response => response.json())
                .then(data => {
                    // Обновляем содержимое div с новыми данными
                    console.log(data)

                })
                .catch(error => console.error('Ошибка при получении данных:', error));
        }