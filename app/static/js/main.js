import { startTimer, stopTimer } from "./timer.js";
import { calculateScore, renderResults } from "./quiz.js";
import { recordResult } from "./api.js";
import { getQuizLevel, loadUser } from "./utils.js";

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
    
    recordResult({
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


const logoutBtn = document.getElementById("logout-btn");
if (logoutBtn) {
    logoutBtn.addEventListener("click", async () => {
        await fetch("/logout", { credentials: "include" });
        window.location.reload();
    });
}


if (document.getElementById("user-info")) {
    loadUser();
}

const loginForm = document.getElementById("login-form");
if(loginForm) {
    loginForm.addEventListener("submit", async (e) => {
        e.preventDefault();

        const username = document.getElementById("username").value;
        const password = document.getElementById("password").value;

        const formData = new FormData();
        formData.append("username", username);
        formData.append("password", password);

        const res = await fetch("/login", {
            method: "POST",
            body: formData,
            credentials: "include" // 🔥 สำคัญ (ใช้ session)
        });

        const data = await res.json();

        if (data.status === "ok") {
            window.location.href = "/"; // ไปหน้า home
        } else {
            document.getElementById("msg").innerText = data.msg;
        }
});
}