import { initNavbar } from "../common/common.js";

initNavbar();

const form = document.getElementById("register-form");
const message = document.getElementById("message");

form.addEventListener("submit", async (e) => {
    e.preventDefault();

    const username = document.getElementById("username").value.trim().toLowerCase();
    const password = document.getElementById("password").value.trim();
    const confirmPassword = document.getElementById("confirm_password").value.trim();
    const email = document.getElementById("email").value.trim().toLowerCase();
    const birth_date = document.getElementById("birth_date").value;

    if (password !== confirmPassword) {
        message.innerText = "Password not match";
        message.style.color = "red";
        return;
    }

    if (password.length < 6) {
        message.innerText = "Password must be at least 6 characters";
        message.style.color = "red";
        return;
    }
    
    try {
        const res = await fetch("/register", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ username, password, email, birth_date })
        });

        const data = await res.json();
        console.log(data);

        if (res.ok) {
            message.innerText = "Register success!";
            message.style.color = "green";

            // redirect ไป login หรือ quiz
            setTimeout(() => {
                window.location.href = "/";
            }, 1000);

        } else {
            if (Array.isArray(data.detail)) {
                message.innerText = data.detail[0].msg;
            } else {
                message.innerText = data.detail || "Register failed";
            }
            message.style.color = "red";
        }

    } catch (err) {
        message.innerText = "Network error";
        message.style.color = "red";
    }
});