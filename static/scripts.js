const ws = new WebSocket("ws://localhost:8000/ws")

ws.onmessage = function (event) {
    let msg_list = document.getElementById('msg_list')
    let li = document.createElement('li')
    let result = JSON.parse(event.data)
    let content = document.createTextNode(result.count + ". " + result.text)
    li.appendChild(content)
    msg_list.appendChild(li)
}

function sendMessage(event) {
    let input = document.getElementById("messageText")
    let data = JSON.stringify(
        {
            data: input.value
        }
        )
    ws.send(data)
    input.value = ''
    event.preventDefault()
}