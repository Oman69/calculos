let select_field = document.getElementById('selectMenu');
select_field.addEventListener('change', function() {
let url = window.location.href.split('?')[0] + '?limit=' + this.value;
window.location.href = url;
select_field.innerHTML = 'Показать:' + this.value;
});
