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
            const accuracy_pct = s.accuracy_pct;
            const minutes = (s.sec / 60).toFixed(2);
            const avg = Number(s.avg_score).toFixed(2);

            monthlyScoreText = `
                <div class="score-card monthly">
                    <div class="score-title">Monthly Score</div>
                    <div class="score-item">Score: <span>${score} <small>(${accuracy_pct.toFixed(2)}%)</small></span></div>
                    <div class="score-item">Time: <span>${minutes} min</span></div>
                    <div class="score-item">Avg: <span>${avg}</span></div>
                </div>
            `;
        }

        const dailyScoreRes = await fetch(`/score/daily/${userId}`);
        const dailyScoreData = await dailyScoreRes.json();

        let dailyScoreText = "";

        if (dailyScoreData.data.length > 0) {
            const s = dailyScoreData.data[0];

            const score = s.score;
            const accuracy_pct = s.accuracy_pct;
            const minutes = (s.sec / 60).toFixed(2);
            const avg = Number(s.avg_score).toFixed(2);

            dailyScoreText = `
                <div class="score-card daily">
                    <div class="score-title">Daily Score</div>
                    <div class="score-item">Score: <span>${score} <small>(${accuracy_pct.toFixed(2)}%)</small></span></div>
                    <div class="score-item">Time: <span>${minutes} min</span></div>
                    <div class="score-item">Avg: <span>${avg}</span></div>
                </div>
            `;
        }

        userDiv.innerHTML = `
            <div class="user-box">
                <div class="username">👤 ${data.user.username}</div>
                <div class="score-container">
                    ${monthlyScoreText}
                    ${dailyScoreText}
                </div>
            </div>
        `;

        logoutBtn.style.display = "block";
    } else {
        userDiv.innerHTML = `
            Guest |
            <a href="/login">Login</a> |
            <a href="/register">Register</a>
        `;
    }
}