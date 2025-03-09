#const gameContainer = document.getElementById("game");
const questionElement = document.getElementById("question");
const answerInput = document.getElementById("answer");
const feedbackElement = document.getElementById("feedback");
const scoreElement = document.getElementById("score");
const timerElement = document.getElementById("timer");
const correctSound = new Audio("correct.mp3");
const wrongSound = new Audio("wrong.mp3");

let score = 0;
let timeLeft = 10;
let difficulty = 1;
let currentAnswer;
let timer;

function generateQuestion() {
    let num1 = Math.floor(Math.random() * (10 * difficulty)) + 1;
    let num2 = Math.floor(Math.random() * (10 * difficulty)) + 1;
    let operations = ["+", "-", "*"];
    let operation = operations[Math.floor(Math.random() * operations.length)];
    
    switch (operation) {
        case "+": currentAnswer = num1 + num2; break;
        case "-": currentAnswer = num1 - num2; break;
        case "*": currentAnswer = num1 * num2; break;
    }
    
    questionElement.innerText = `${num1} ${operation} ${num2} = ?`;
    answerInput.value = "";
    startTimer();
}

function startTimer() {
    clearInterval(timer);
    timeLeft = 10;
    timerElement.innerText = `Tempo: ${timeLeft}s`;
    timer = setInterval(() => {
        timeLeft--;
        timerElement.innerText = `Tempo: ${timeLeft}s`;
        if (timeLeft === 0) {
            clearInterval(timer);
            feedbackElement.innerText = "Tempo esgotado!";
            wrongSound.play();
            setTimeout(generateQuestion, 2000);
        }
    }, 1000);
}

function checkAnswer() {
    let userAnswer = parseInt(answerInput.value);
    if (userAnswer === currentAnswer) {
        score += 10;
        difficulty += 0.2;
        feedbackElement.innerText = "Correto!";
        feedbackElement.style.color = "green";
        correctSound.play();
    } else {
        feedbackElement.innerText = "Errado!";
        feedbackElement.style.color = "red";
        wrongSound.play();
    }
    scoreElement.innerText = `Pontuação: ${score}`;
    clearInterval(timer);
    setTimeout(generateQuestion, 2000);
}

answerInput.addEventListener("keydown", function(event) {
    if (event.key === "Enter") {
        checkAnswer();
    }
});

generateQuestion();
