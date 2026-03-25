function submitQuiz() {
    const inputs = document.querySelectorAll("input");
    let correct = 0;

    inputs.forEach(input => {
        const userAnswer = parseInt(input.value);
        const correctAnswer = parseInt(input.dataset.answer);
        const resultSpan = input.nextElementSibling;

        if (userAnswer === correctAnswer) {
            correct++;
            resultSpan.innerText = " ✔";
        } else {
            resultSpan.innerText = ` ✘ (Ans: ${correctAnswer})`;
        }
    });

    document.getElementById("score").innerText = `Score: ${correct}/${inputs.length}`;
}

