function addMessage(text, sender) {
    let chatBox = document.getElementById("chat-box");

    let msg = document.createElement("div");
    msg.classList.add("message", sender);
    msg.innerText = text;

    chatBox.appendChild(msg);
    chatBox.scrollTop = chatBox.scrollHeight;
}

function sendMessage() {
    let input = document.getElementById("user-input");
    let message = input.value.trim();
    let algo = document.getElementById("algorithm").value;

    if (message === "") return;

    addMessage(message, "user");

    fetch("/chat", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({message: message, algorithm: algo})
    })
    .then(res => res.json())
    .then(data => {
        addMessage(data.response, "bot");
    });

    input.value = "";
}

function clearChat() {
    document.getElementById("chat-box").innerHTML = "";
}

// ✅ ENTER KEY SUPPORT
document.getElementById("user-input").addEventListener("keypress", function(e) {
    if (e.key === "Enter") {
        e.preventDefault();
        sendMessage();
    }
});