export async function loadUser() {
    const res = await fetch("/me", {
        credentials: "include"
    });

    const data = await res.json();
    const userDiv = document.getElementById("user-info");
    const logoutBtn = document.getElementById("logout-btn");

    if (data.user) {
        userDiv.innerText = "Logged in as: " + data.user.username;
        logoutBtn.style.display = "block";
    } else {
        userDiv.innerHTML = `
            Guest |
            <a href="/login">Login</a>
        `;
    }
}
