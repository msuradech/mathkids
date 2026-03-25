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
            resultSpan.classList.add("correct");
            resultSpan.classList.remove("wrong");
        } else {
            resultSpan.innerText = ` ✘ (Ans: ${correctAnswer})`;
            resultSpan.classList.add("wrong");
            resultSpan.classList.remove("correct");
        }
    });

    document.getElementById("score").innerText = `Score: ${correct}/${inputs.length}`;
}

