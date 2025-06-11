console.log('Hello, world!');
console.log('div');
const doc = document.getElementsByTagName("div")
let div = doc[2];
div.textContent = 'morght';


const headings = document.getElementsByTagName("h2")
for(i = 0 ; i<headings.length ; i++)
headings[i].style.fontStyle = "italic"
console.log(headings)


