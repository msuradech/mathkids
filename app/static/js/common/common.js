import { loadUser } from "../utils/utils.js";

export function initNavbar() {
    const userInfo = document.getElementById("user-info");
    if (userInfo) {
        loadUser();
    }
    
    const logoutBtn = document.getElementById("logout-btn");
    if (logoutBtn) {
        logoutBtn.addEventListener("click", async () => {
            await fetch("/logout", { credentials: "include" });
            window.location.reload();
        });
    }
}