// Set the date we're counting down to
var examDate = document.querySelector('.examDate');
var examDateStart = document.querySelector('.examDateStart');
examDate = examDate.innerHTML;
examDateStart = examDateStart.innerHTML;
console.log(examDate);
console.log(examDateStart);
let inivigilate = document.querySelector('.invigilate');
var flag = false;

let submitButton = document.querySelector('.score');
// let inivigilate = document.querySelector('.invigilate');
let examForm = document.querySelector('.structured-form');


var cdd = "May 5, 2023 13:41:00";
var sd = "May 5, 2023 13:40:00";
var countDownDate = new Date(examDate).getTime();
var startDate = new Date(examDateStart).getTime();
// var countDownDate = new Date(examDate).getTime();
console.log("CDD",countDownDate);
console.log("SD", startDate);


// Update the count down every 1 second
var x = setInterval(function() {

  // Get today's date and time
  var now = new Date().getTime();

  // Find the distance between now and the count down date
  var distance = countDownDate - now;
  // console.log(distance);
    var duration = startDate - now;
    console.log("Duration is: ", duration);


  // Time calculations for days, hours, minutes and seconds
  var days = Math.floor(distance / (1000 * 60 * 60 * 24));
  var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
  var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
  var seconds = Math.floor((distance % (1000 * 60)) / 1000);
  // Display the result in the element with id="demo"
  //   document.getElementById("demo").innerHTML = "Time till exam ends: " + days + "d " + hours + "h "
  //   + minutes + "m " + seconds + "s ";
    console.log(distance);
  if(duration<=0){
    document.getElementById("demo").innerHTML = hours + "h "
    + minutes + "m " + seconds + "s ";
    examForm.classList.remove('d-none');
    // inivigilate.classList.remove('d-none');

      //inivigilate.click();
      if (flag == false) {
          flag = true;
          inivigilate.click();
      }

  }

  else if(duration>0)  {
    document.getElementById("demo").innerHTML = "Exam starts at " + examDateStart
  }



  // If the count down is finished, write some text
  if (distance < 0) {
    examForm.classList.remove('d-none');
    clearInterval(x);
    document.getElementById("demo").innerHTML = "EXPIRED";
    submitButton.classList.add('d-none');
    //inivigilate.classList.add('d-none');

  }

}, 1000);
