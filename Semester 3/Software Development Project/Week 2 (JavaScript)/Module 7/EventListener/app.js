document.getElementById("add-btn").addEventListener
    ("click", (event) => {
        const inputValue = document.getElementById("input-box").value;

        const container = document.getElementById("comment-container");
        const p = document.createElement("p"); //creating new html p tag inside comment-container
        p.classList.add("child"); // p tag ar class nam deya hosse 'child'
        p.innerText = inputValue;

        container.appendChild(p); //this line adding the comment 
        document.getElementById("input-box").value = ""; // this line making null input's placeholder

        const allComments = document.getElementsByClassName("child");
        // for(let i=0;i<allComments.length;i++){
        //     const element = allComments[i];
        // }
        //shortcut way:
        for(const element of allComments){
            element.addEventListener("click",(event)=>{
                event.target.parentNode.removeChild(element);
            });
        }
    });