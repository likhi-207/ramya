const arr=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
arr.filter((element,index)=>{
    console.log(element, index)
    return true
})







console.log('Hello, world!');
console.log('div');
const doc = document.getElementsByTagName("div")
let div = doc[1];
div.textContent = 'Australia';


const headings = document.getElementsByTagName("h2")
for(i = 0 ; i<headings.length ; i++)
headings[i].style.fontStyle = "italic"
console.log(headings)











const addDiv = (name)=>{
    const ramya = document.createElement("div");
    
    ramya.classList.add("my-class");
    ramya.textContent = name;
    const parent = 
    document.getElementById("container");
    if (parent){
      parent.appendChild(ramya);
}
};