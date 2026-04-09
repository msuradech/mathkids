import { initNavbar } from "../common/common.js";

initNavbar();

const loginForm = document.getElementById("login-form");
if(loginForm) {
    loginForm.addEventListener("submit", async (e) => {
        e.preventDefault();

        const username = document.getElementById("username").value.trim().toLowerCase();
        const password = document.getElementById("password").value.trim();

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