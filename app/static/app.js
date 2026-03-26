let startTime;
let timerInterval;

function startTimer() {
    startTime = new Date();

    timerInterval = setInterval(() => {
        const now = new Date();
        const diff = Math.floor((now - startTime) / 1000);
        document.getElementById("timer").innerText = `Time: ${diff}s`;
    }, 1000);
}

function stopTimer() {
    clearInterval(timerInterval);

    const endTime = new Date();
    return Math.floor((endTime - startTime) / 1000);
}

function sendResultToAPI(data) {
    fetch("/quiz/record", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(data)
    })
    .then(res => res.json())
    .then(res => {
        console.log("API response:", res);
    })
    .catch(err => {
        console.error("API error:", err);
    });
}

function getQuizLevel() {
    const pathParts = window.location.pathname.split("/");
    return pathParts[2]; // index 2 = "01"
}

function submitQuiz() {
    const totalTime = stopTimer();
    const inputs = document.querySelectorAll("input");
    let correct = 0;

    inputs.forEach(input => {
        const userAnswer = parseInt(input.value);
        const correctAnswer = parseInt(input.dataset.answer);
        const resultSpan = input.nextElementSibling;

        if (userAnswer === correctAnswer) {
            correct++;
            resultSpan.innerText = " ✔";
            resultSpan.classList.add("correct");
            resultSpan.classList.remove("wrong");
        } else {
            resultSpan.innerText = ` ✘ (Ans: ${correctAnswer})`;
            resultSpan.classList.add("wrong");
            resultSpan.classList.remove("correct");
        }
    });

    const totalQuestions = inputs.length;
    const avgTime = (totalTime / totalQuestions).toFixed(2);

    document.getElementById("score").innerText = `Score: ${correct}/${inputs.length}`;

    document.getElementById("result-time").innerText =
        `Total: ${totalTime}s | Avg: ${avgTime}s/question`;
    
    sendResultToAPI({
        level: getQuizLevel(),   // เดี๋ยวทำต่อด้านล่าง
        totalQuestions: totalQuestions,
        score: correct,
        totalTime: totalTime,
        avgTime: avgTime
    });
}

window.onload = function () {
    startTimer();
};