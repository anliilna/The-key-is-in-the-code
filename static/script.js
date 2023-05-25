function redirect() {
    var textValue = document.getElementById("textBox").value;
    if(textValue == Admin)
    {
        location.href = "sun.html";
    }
    else if(textValue == 456)
    {
        location.href = "www.yoursite.com/chris.html";
    }
    else
    {
        alert("Invalid Input");
    }
}