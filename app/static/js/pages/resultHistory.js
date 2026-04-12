import { initNavbar } from "../common/common.js";

initNavbar();

const dropdown = document.getElementById("username");

if (dropdown) {
    dropdown.addEventListener("change", async () => {
        const username = dropdown.value;

        if (!username) return;

        const res = await fetch(`/result-history/${username}`);
        const data = await res.json();

        console.log(data);
    });
}