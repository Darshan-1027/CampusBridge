let optionSelect = document.querySelector(".RegistrationSelect select");
let college = document.getElementById("college");
let faculty = document.getElementById("faculty");
let student = document.getElementById("student");

// Initially set visibility based on the default selected option
updateVisibility(optionSelect.value);

// Add an event listener for changes in the dropdown selection
optionSelect.addEventListener("change", function () {
    updateVisibility(this.value);
});

function updateVisibility(selectedOption) {
    if (selectedOption === "college") {
        college.style.display = "block";
        faculty.style.display = "none";
        student.style.display = "none";
    } else if (selectedOption === "faculty") {
        college.style.display = "none";
        faculty.style.display = "block";
        student.style.display = "none";
    } else if (selectedOption === "student") {
        college.style.display = "none";
        faculty.style.display = "none";
        student.style.display = "block";
    } else {
        // fallback
        college.style.display = "none";
        faculty.style.display = "none";
        student.style.display = "none";
    }
}

  const today = new Date().toISOString().split('T')[0];
  document.getElementById('date').setAttribute('max', today);
  document.getElementsByClassName('bdate').setAttribute('max', today);




setTimeout(function(){

   let  Message = document.getElementById("Message");
   if(Message){

    Message.style.display="none";

   }
},7000)



