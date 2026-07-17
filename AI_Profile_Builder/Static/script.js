const form = document.getElementById("profileForm");

if(form){

form.addEventListener("submit", function(){

document.getElementById("loader").classList.remove("hidden");

});

}