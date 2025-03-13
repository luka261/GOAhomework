// 1) პირველი ვერსიით გააკეთეთ იგივენაირი ანიმაცია, 
// მაგრამ საათის ისრის მიმართულების მაგივრად ყუთმა იმოძრაოს საათის ისრის მიმართულების საწინააღმდეგოდ
// first version

// const child = document.getElementById('child');

// let x = 0;
// let y = 0;

// const moveDown = setInterval(() => {
//    y += 1; 
//    child.style.top = `${y}px`;
//    if (y == 450){
//       clearInterval(moveDown);
//       const moveRight = setInterval(() => {
//          x += 1; 
//          child.style.left = `${x}px`;
//          if (x == 450){
//             clearInterval(moveRight);
//             const moveUp = setInterval(() => {
//                y -= 1; 
//                child.style.top = `${y}px`;
//                if (y == 0){
//                   clearInterval(moveUp);
//                   const moveLeft = setInterval(() => {
//                      x -= 1; 
//                      child.style.left = `${x}px`;
//                      if (x == 0){
//                         clearInterval(moveLeft);
//                      }
//                   }, 5)
//                }
//             }, 5)
//          }
//       }, 5)
//    }
// }, 5)



// 1) მეორე ვერსიით გააკეთეთ იგივენაირი ანიმაცია, 
// მაგრამ საათის ისრის მიმართულების მაგივრად ყუთმა იმოძრაოს საათის ისრის მიმართულების საწინააღმდეგოდ
// second version

// const child = document.getElementById("child");

// let left = 0;
// let y = 0;
// let direction = "down";

// const move = setInterval(function(){
//     if(direction == "down"){
//         y++;
//         if(y == 450){
//             direction = "right";
//         }
//     } else if(direction == "right"){
//         left++;
//         if(left == 450){
//             direction = "up";
//         }
//     } else if(direction == "up"){
//         y--;
//         if(y == 0){
//             direction = "left";
//         }
//     } else if(direction == "left"){
//         left--;
//         if(left == 0 && y == 0){
//             direction = "down";
//         }
//     }

//     child.style.left = left + 'px';
//     child.style.top = y + 'px';
// }, 5);