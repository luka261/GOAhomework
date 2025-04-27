// Level 86:
// 1) შექმენით form სადაც მომხმარებელი შემოიტანს სახელს, მეილს და ასაკს,
// პროგრამამ ყველა დაsubmit'ებაზე localstorage'ში შეინახოს ახალი ობიექტი, სადაც იქნება შენახული იმ ადამიანის შესახებ ინფორმაცია

// ანუ localstorage უნდა გამოიყურებოდეს ასე:
// key       value
// person1   {...}
// person2   {...}


form.addEventListener('submit', (event) => {
    event.preventDefault(); 

    const name = document.querySelector('#name').value;
    const email = document.querySelector('#email').value;
    const age = document.querySelector('#age').value;

    const userInfo = {
        name,
        email,
        age
    };


});