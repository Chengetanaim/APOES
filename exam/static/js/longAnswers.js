const form2 = document.querySelector('.long-answer-form');
let longAnswerButton = document.querySelector('.long-answer-btn');
let longAnswerTextarea = document.querySelectorAll('.long-answer-textarea');
let displayScore2 = document.querySelector('span.structured-primary');
let visibility2 = document.querySelector('div.result');

let mark = 0;


form2.addEventListener('submit', e => {
    e.preventDefault();
    const userAnswers = [form2.q1.value, form2.q2.value];
    userAnswers.forEach(answer => {
        console.log(answer);
        if(answer.length > 10) {
            mark +=1;
            console.log("Mark has been incremented", mark)

        }
    });
   console.log(longAnswerTextarea);
    scrollTo(0,0);
    visibility2.classList.remove('d-none');
    displayScore2.textContent = "+"+mark
});