// const correctAnswers = prompt("Enter answers");
const correctAnswers = ['B', 'B', 'B', 'B'];
const correctAnswers2 = document.querySelectorAll('.answers');
console.log(correctAnswers2);
let displayScore = document.querySelector('span.text-primary');
let visibility = document.querySelector('div.result');
let submitButton8 = document.querySelector('.score');


const form = document.querySelector('.quiz-form');
form.addEventListener('submit', e => {
    e.preventDefault();

    let score = 0;


    const userAnswers = [form.q7.value, form.q8.value, form.q9.value, form.q10.value, form.q11.value];
    // let userAnswers = [];
    // for(i in form.length){
    //     userAnswers += form.q[i].value
    // }

    // Check answers
    userAnswers.forEach((answer, index) => {
        if (answer === correctAnswers2[index].innerHTML){
            score += 20;

        }

    });
    scrollTo(0,0);
    visibility.classList.remove('d-none');
    submitButton8.classList.add('d-none');

    
    let output = 0;
    const timer = setInterval(() => {
        displayScore.textContent = output + '%';
        if (output == score){
            clearInterval(timer);
        } else {
            output++;
        }
        

    }, 10);

});