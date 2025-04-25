let Eye = document.getElementById("eye");
let Password = document.getElementById("password");
let see = true;

function eyeclick(){

    Eye.classList.toggle("fa-eye");
    if(see==true){

        Password.type="text";
        see=false;
    }
    else{
        
        Password.type="password";
        see=true;
    }
}

setTimeout(function(){

    let  Message = document.getElementById("Message");
    if(Message){
 
     Message.style.display="none";
 
    }
 },7000)
