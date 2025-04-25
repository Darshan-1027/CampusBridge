let Aboutus = document.getElementById("Aboutus");
let Closebtn = document.getElementById("close");
let Main = document.getElementById("main");
let Contact = document.getElementById("Contact");
let blurs=true;

function aboutusclick(){

    Aboutus.classList.toggle("toggle");
    if(blurs==true){
    Main.style.filter="blur(6px)";
    Contact.style.filter="blur(6px)";
        blurs=false;
    }
    else{

        Main.style.filter="blur(0px)";
        Contact.style.filter="blur(0px)";
        blurs=true;
    }
}

function closeclick(){

    aboutusclick();
}
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        document.querySelector(this.getAttribute('href')).scrollIntoView({
            behavior: 'smooth'
        });
    });
});
