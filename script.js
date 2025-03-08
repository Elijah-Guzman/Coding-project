// Script for index.html (for now)
let testNum = 1;

function buttonFunction() {
  for (let x = 0; x < testNum; x++) {
    let addStuffDiv = document.querySelector('#addStuffHere');
    addStuffDiv.appendChild(document.createElement('p')).textContent='Test Added!';
  }
}
