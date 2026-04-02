export function getQuizLevel() {
    const pathParts = window.location.pathname.split("/");
    return pathParts[2]; // index 2 = "01"
}

export function calculateScore(inputs) {
    let correct = 0;

    inputs.forEach(input => {
        const userAnswer = parseInt(input.value);
        const correctAnswer = parseInt(input.dataset.answer);

        if (userAnswer === correctAnswer) {
            correct++;
        }
    });

    return correct;
}

export function renderResults(inputs) {
    inputs.forEach(input => {
        const userAnswer = parseInt(input.value);
        const correctAnswer = parseInt(input.dataset.answer);
        const resultSpan = input.nextElementSibling;

        if (userAnswer === correctAnswer) {
            resultSpan.innerText = " ✔";
            resultSpan.classList.add("correct");
            resultSpan.classList.remove("wrong");
        } else {
            resultSpan.innerText = ` ✘ (Ans: ${correctAnswer})`;
            resultSpan.classList.add("wrong");
            resultSpan.classList.remove("correct");
        }
    });
}

export function recordResult(data) {
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