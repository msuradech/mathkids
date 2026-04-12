import { initNavbar } from "../common/common.js";

initNavbar();

const dropdown = document.getElementById("username");

if (dropdown) {
    dropdown.addEventListener("change", async () => {
        const username = dropdown.value;

        if (!username) return;

        const res = await fetch(`/result-history/${username}`);
        const data = await res.json();

        /*console.log(data);*/
    });
}

const container = document.getElementById("result-container");

dropdown.addEventListener("change", async () => {
    const userId = dropdown.value;

    if (!userId) {
        container.innerHTML = "";
        return;
    }

    const res = await fetch(`/result-history/${userId}`);
    const data = await res.json();

    renderTable(data.data);
});

function renderTable(rows) {
    if (rows.length === 0) {
        container.innerHTML = "<p>No data</p>";
        return;
    }

    const today = new Date().toISOString().slice(0, 10); // YYYY-MM-DD

    let html = `
        <table>
            <tr>
                <th>Date</th>
                <th>Username</th>
                <th>Level</th>
                <th>Total</th>
                <th>Score</th>
                <th>Sec</th>
                <th>Avg</th>
            </tr>
    `;

    rows.forEach(r => {
        const rowDate = r.created_at.slice(0, 10); // ตัดเวลาออก
        const isToday = rowDate === today;

        html += `
            <tr class="${isToday ? 'today-row' : ''}">
                <td class="col-date">${formatDate(r.created_at)}</td>
                <td>${r.username}</td>
                <td>${r.quiz_level}</td>
                <td>${r.total_questions}</td>
                <td>${r.score}</td>
                <td>${r.sec}</td>
                <td>${r.avg_sec}</td>
            </tr>
        `;
    });

    html += "</table>";
    container.innerHTML = html;
}

function formatDate(dateStr) {
    const d = new Date(dateStr);

    return d.toLocaleString("en-GB", {
        day: "2-digit",
        month: "short",
        hour: "2-digit",
        minute: "2-digit"
    });
}