import { initNavbar } from "../common/common.js";

initNavbar();

const form = document.getElementById("change-password-form");
const msg = document.getElementById("msg");

form.addEventListener("submit", async (e) => {
    e.preventDefault();

    const current = document.getElementById("current-password").value;
    const newPass = document.getElementById("new-password").value;
    const confirm = document.getElementById("confirm-password").value;

    if (newPass !== confirm) {
        msg.textContent = "New password and confirm password do not match";
        msg.className = "error";
        return;
    }

    if (newPass.length < 6) {
        msg.textContent = "Password must be at least 6 characters";
        msg.className = "error";
        return;
    }

    try {
        const res = await fetch("/change-password", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                current_password: current,
                new_password: newPass
            })
        });

        const data = await res.json();

        if (res.ok) {
            msg.textContent = "Password updated successfully";
            msg.className = "success";
            form.reset();
        } else {
            msg.textContent = data.detail || "Error updating password";
            msg.className = "error";
        }

    } catch (err) {
        msg.textContent = "Something went wrong";
        msg.className = "error";
    }
});