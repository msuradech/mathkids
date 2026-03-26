let startTime;
let timerInterval;

export function startTimer() {
    startTime = new Date();

    timerInterval = setInterval(() => {
        const now = new Date();
        const diff = Math.floor((now - startTime) / 1000);
        document.getElementById("timer").innerText = `Time: ${diff}s`;
    }, 1000);
}

export function stopTimer() {
    clearInterval(timerInterval);

    const endTime = new Date();
    return Math.floor((endTime - startTime) / 1000);
}