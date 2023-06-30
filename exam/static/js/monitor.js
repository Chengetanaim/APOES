let change = 0;
let submitButton5 = document.querySelector('.score');

document.addEventListener("visibilitychange", (event) => {
  if (document.visibilityState == "visible") {
    console.log("tab is active")
  } else {
    console.log("tab is inactive");
    change += 1;
    if(change>=2){
       submitButton5.classList.add('d-none');
       // Save object user

    }
  }
});
