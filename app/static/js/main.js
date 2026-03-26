import { startTimer, stopTimer } from "./timer.js";
import { calculateScore, renderResults } from "./quiz.js";
import { sendResultToAPI } from "./api.js";
import { getQuizLevel } from "./utils.js";

function submitQuiz() {
    const btn = document.getElementById("submit-btn");
    if (btn.disabled) return;
    btn.disabled = true;

    const totalTime = stopTimer();
    const inputs = document.querySelectorAll("input");
    
    const correct = calculateScore(inputs);
    renderResults(inputs);

    const totalQuestions = inputs.length;
    const avgTime = (totalTime / totalQuestions).toFixed(2);

    document.getElementById("score").innerText = `Score: ${correct}/${inputs.length}`;

    document.getElementById("result-time").innerText =
        `Total: ${totalTime}s | Avg: ${avgTime}s/question`;
    
    sendResultToAPI({
        quiz_level: getQuizLevel(),   // เดี๋ยวทำต่อด้านล่าง
        total_questions: totalQuestions,
        score: correct,
        total_time_sec: totalTime
    });
}

function resetQuiz() {
    location.reload();
}


window.submitQuiz = submitQuiz;
window.resetQuiz = resetQuiz;
window.onload = function () {
    const timerEl = document.getElementById("timer");

    if (timerEl) {
        startTimer();
    }

};