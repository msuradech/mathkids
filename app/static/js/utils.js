export function getQuizLevel() {
    const pathParts = window.location.pathname.split("/");
    return pathParts[2]; // index 2 = "01"
}
