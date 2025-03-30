// 1) გაიხსენეთ როდის გამოვიდა ES6 და მოიყვანეთ მაგალითები თუ რა updateბი შემოიტანა, ასევე ახსენეთ რაში გამოგვადგა ეს updateები
// 2) ახსენით რატომ ჯობია let და const, var Keyword'ს
// 3) გამოიყენეთ for...of loop
// 4) გამოიყენეთ for...in loop/
// 5) გამოიყენეთ Object.assign() მეთოდი და ახსენით როგორ მუშაობს
// 6) შექმენით ფუნქცია arrow function'ის გამოყენებით

for (let i = 0; i < 10; 1++) {
    console.log(i);
}

let arr = [1, 2, 3, 4, 5];
for (let i of arr) {
    console.log(i);
}


let sum = (a, b) => a + b;
console.log(sum(5, 5));


