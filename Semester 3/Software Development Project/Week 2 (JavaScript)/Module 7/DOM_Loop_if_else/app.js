const allBox = document.getElementsByClassName("box");
for(let i=0;i<allBox.length;i++){
    const element = allBox[i];
    element.style.backgroundColor = "green";
    if(element.innerText == "box-5"){
        element.style.backgroundColor = "red";
    }
}