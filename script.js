// Script for index.html (for now)
let input = "test";


function buttonFunction() {
  // let addStuffDiv = document.querySelector('#addStuffHere');
  // for (let x = 0; x < testNum; x++) {
  //   addStuffDiv.appendChild(document.createElement('p')).textContent='Test Added!';
  // }
  testFunc();
}

function callbackFunc(response) {
  console.log(response);
}

function testFunc() {
  $.ajax({
      type: "POST",
      url: "Quiz.py",
      data: { param: input },
      success: callbackFunc
    });
}
