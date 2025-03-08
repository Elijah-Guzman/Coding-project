// Script for index.html (for now)
let testNum = 1;

function buttonFunction() {
  let addStuffDiv = document.querySelector('#addStuffHere');
  for (let x = 0; x < testNum; x++) {
    addStuffDiv.appendChild(document.createElement('p')).textContent='Test Added!';
  }
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
