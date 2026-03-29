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