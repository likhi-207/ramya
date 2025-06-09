array = [1, 2, 3, 4, 5];
console.log(array);
console.log(array.length-1);
console.log(array.length);
for(let i in array){
    console.log(i);
}
for(let i of array){
    console.log(i);
}

console.log(array[0]);

array.push(3);
console.log(array);

array.pop();
console.log(array);

array.unshift(0);
console.log(array);

array.shift();
console.log(array);

console.log(array.includes(3));
console.log(array.indexOf(3));

array.slice(0,3);
console.log(array);
array.splice(0,2);
console.log(array);

