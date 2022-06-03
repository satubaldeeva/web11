var langForm = document.getElementById('lang');

langForm.addEventListener('storage', function(event){
    if(!localStorage.getItem('lang')) {
            populateStorage();
    } else {

         setLang();
    }

})
function populateStorage() {
  localStorage.setItem('lang', langForm.value);
  setLang();
}

function setLang() {
  var currentLang = localStorage.getItem('lang');
  langForm.value = currentLang;

}

langForm.onchange = populateStorage;