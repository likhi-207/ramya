console.log('Hello, world!');
console.log('div');
const doc = document.getElementsByTagName("div")
let div = doc[2];
div.textContent = 'morght';


const headings = document.getElementsByTagName("h2")
for(i = 0 ; i<headings.length ; i++)
headings[i].style.fontStyle = "italic"
console.log(headings)


const bye = document.createElement("h1");
 bye.textContent = "Bye! Bye!";

 document.body.appendChild(bye);


const button = document.querySelector("#button1")

button.addEventListener("mouseover" , ()=>{
    button.style.backgroundColor = "red"
    button.style.scale = 1.2
})

button.addEventListener("mouseout" , ()=>{
    button.style.backgroundColor = "white"
    button.style.scale = 0.9
})

button.addEventListener("dblclick" , ()=>{
    console.log("double clicked bro")
})

button.addEventListener("click" , ()=>{
    const newh2 = document.createElement("h2")
    console.log()
    newh2.textContent = document.getElementById("input").value
    document.getElementById("container").appendChild(newh2)
})

