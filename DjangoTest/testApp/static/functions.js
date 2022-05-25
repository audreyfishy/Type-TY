function test(token){
    var xhr = new XMLHttpRequest();
    xhr.open('POST', 'form', true);
    xhr.setRequestHeader('X-CSRFToken', token);
    xhr.send();
}