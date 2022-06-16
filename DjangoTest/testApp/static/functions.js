function test(token){
    var xhr = new XMLHttpRequest();
    xhr.open('POST', 'form', true);
    xhr.setRequestHeader('X-CSRFToken', token);
    xhr.send(document.getElementById("youtubeID").value);
    xhr.onreadystatechange = () => {
        if (xhr.readyState != 4) return;
        if (xhr.status != 200) {
            console.log(xhr.status + ': ' + xhr.statusText);
        } else {
            let list = JSON.parse(xhr.responseText);
            let embed = document.getElementById("embed");
            embed.innerHTML = list.length;
            for(let e of list){
                let newElement = document.createElement("blockquote");
                newElement.classList.add("twitter-tweet");
                let child = document.createElement("a");
                child.href = e;
                newElement.appendChild(child);
                embed.appendChild(newElement);
            }
            let script = document.createElement("script");
            script.src = "https://platform.twitter.com/widgets.js";
            document.body.appendChild(script);
            document.body.removeChild(script);
        }
    }
}
function add(token){
    var xhr = new XMLHttpRequest();
    xhr.open('POST', 'add', true);
    xhr.setRequestHeader('X-CSRFToken', token);
    xhr.send(document.getElementById("youtubeID").value);
    xhr.onreadystatechange = () => {
        if (xhr.readyState != 4) return;
        if (xhr.status != 200) {
            console.log(xhr.status + ': ' + xhr.statusText);
        } else {
            let list = JSON.parse(xhr.responseText);
            console.log(list);
        }
    }
}