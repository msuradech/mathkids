import { startTimer, stopTimer } from "../utils/timer.js";
import { getQuizLevel, calculateScore, renderResults, recordResult } from "../utils/quiz.js";
import { initNavbar } from "../common/common.js";

initNavbar();

window.onload = function () {
    const timerEl = document.getElementById("timer");

    if (timerEl) {
        startTimer();
    }
};

document.getElementById("submit-btn").addEventListener("click", submitQuiz);
document.getElementById("reset-btn").addEventListener("click", resetQuiz);


export function submitQuiz() {
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
    
    recordResult({
        quiz_level: getQuizLevel(),   
        total_questions: totalQuestions,
        score: correct,
        total_time_sec: totalTime
    });
}

export function resetQuiz() {
    location.reload();
}