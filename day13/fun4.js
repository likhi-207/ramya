const greet=(name,callback)=>{
    console.log(name)
    callback();
}
greet("enzo",()=>console.log("hello"))