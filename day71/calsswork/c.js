// 1) წამოიღეთ ელემენტები getElementsByClassName'ის საშუალებით
// 2) წამოიღეთ ელემენტი querySelector'ის მეშვეობით (ჯერ id, შემდეგ class)
// 3) წამოიღეთ js'ში img და შეუცვალეთ: src და width
// 4) წამოიღეთ js'ში p და შეუცვალეთ: color, backgroundColor და fontSize
// 5) js'ის გამოყენებით, შექმენით ახალი p და textNode, შემდეგ textNode ჩასვით პარაგრაფში და პარაგრაფი ჩასვით html'ში მოცემულ div'ში

let div = document.querySelector('.container');
let img = document.querySelector('img');
img.src = 'https://www.w3schools.com/js/pic_bulbon.gif';
img.width = '100';
let p = document.querySelector('p');
p.style.color = 'red';
p.style.backgroundColor = 'black';
p.style.fontSize = '20px';
let newP = document.createElement('p');
let textNode = document.createTextNode('Hello World');
newP.appendChild(textNode);
div.appendChild(newP);