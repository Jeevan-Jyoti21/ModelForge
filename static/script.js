async function fetchMessage() {
    const response = await fetch('/get_message');
    const data = await response.json();
    document.getElementById('PRT').innerText = data.message;
}