const themeBtn=document.getElementById("themeBtn");
themeBtn?.addEventListener("click",()=>{document.body.classList.toggle("light");localStorage.setItem("dg-theme",document.body.classList.contains("light")?"light":"dark")});
if(localStorage.getItem("dg-theme")==="light")document.body.classList.add("light");

const input=document.getElementById("fileInput"), names=document.getElementById("fileNames");
input?.addEventListener("change",()=>{names.textContent=[...input.files].map(f=>f.name).join(" • ")});
const search=document.getElementById("search");
search?.addEventListener("input",()=>{const q=search.value.toLowerCase();document.querySelectorAll(".tool-card").forEach(c=>c.style.display=c.dataset.name.includes(q)?"flex":"none")});
const toolsMenuBtn = document.getElementById("toolsMenuBtn");
const toolsMenu = document.getElementById("toolsMenu");

toolsMenuBtn.addEventListener("click", function (event) {

    event.stopPropagation();

    toolsMenu.classList.toggle("show");

});


document.addEventListener("click", function () {

    toolsMenu.classList.remove("show");

});


toolsMenu.addEventListener("click", function (event) {

    event.stopPropagation();

});

const toolsMenuBtn = document.getElementById("toolsMenuBtn");
const toolsMenu = document.getElementById("toolsMenu");

if (toolsMenuBtn && toolsMenu) {

    toolsMenuBtn.addEventListener("click", function(event) {

        event.stopPropagation();

        toolsMenu.classList.toggle("show");

    });

    document.addEventListener("click", function() {

        toolsMenu.classList.remove("show");

    });

    toolsMenu.addEventListener("click", function(event) {

        event.stopPropagation();

    });

}