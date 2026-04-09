export async function loadUser() {
    const res = await fetch("/me", {
        credentials: "include"
    });

    const data = await res.json();
    const userDiv = document.getElementById("user-info");
    const logoutBtn = document.getElementById("logout-btn");

    if (data.user) {
        const userId = data.user.user_id;
        const monthlyScoreRes = await fetch(`/score/monthly/${userId}`);
        const monthlyScoreData = await monthlyScoreRes.json();

        let monthlyScoreText = "";

        if (monthlyScoreData.data.length > 0) {
            const s = monthlyScoreData.data[0];

            const score = s.score;
            const minutes = (s.sec / 60).toFixed(2);
            const avg = Number(s.avg_score).toFixed(2);

            monthlyScoreText = `
                <br>
                <br>
                <u>Monthly Score</u>
                <br>
                Score: ${score}
                <br>
                Time: ${minutes} min
                <br>
                Avg: ${avg}
            `;
        }

        const dailyScoreRes = await fetch(`/score/daily/${userId}`);
        const dailyScoreData = await dailyScoreRes.json();

        let dailyScoreText = "";

        if (dailyScoreData.data.length > 0) {
            const s = dailyScoreData.data[0];

            const score = s.score;
            const minutes = (s.sec / 60).toFixed(2);
            const avg = Number(s.avg_score).toFixed(2);

            dailyScoreText = `
                <br>
                <br>
                <u>Daily Score</u>
                <br>
                Score: ${score}
                <br>
                Time: ${minutes} min
                <br>
                Avg: ${avg}
            `;
        }

        userDiv.innerHTML = `
            Logged in as: ${data.user.username}
            ${monthlyScoreText}
            ${dailyScoreText}
        `;

        logoutBtn.style.display = "block";
    } else {
        userDiv.innerHTML = `
            Guest |
            <a href="/login">Login</a>
        `;
    }
}