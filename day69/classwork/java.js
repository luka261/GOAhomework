// 1) შექმენით ცვლადი სადაც შეინახავთ ახლანდელ Date'ს

let date = new Date();


// 2) ჯერ გამოიტანეთ ეს ცვლადი, შემდეგ კი გამოიყენეთ და გამოიტანეთ ყველა მეთოდი რომელიც რესურსებშია ჩაგდებული

console.log(date.getFullYear());
console.log(date.getMonth());
console.log(date.getDate());
console.log(date.getDay());
console.log(date.getHours());
console.log(date.getMinutes());
console.log(date.getSeconds());
console.log(date.getMilliseconds());


// 3) გააკეთეთ დროის ამთვლელი პროგრამა, html + js'ით, ისეთი როგორიც მე გავაკეთე

setInterval(() => {
    const date = new Date();
    myp.textContent = '${date.getHours()}:${date.getMinutes()}:${date.getSeconds()}';
}, 1000)


