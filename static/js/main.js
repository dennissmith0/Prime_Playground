console.log('JavaScript file loaded.')

document.getElementById('patternForm').addEventListener('submit', function(e) {
    e.preventDefault();  // Prevent the form from being submitted in the default way
    createPattern();
  }); 
document.getElementById('multiplesForm').addEventListener('submit', function(e) {
    e.preventDefault(); // Prevent form submission
    highlightMultiples();
  });

const gridContainer = document.getElementById('grid-container');
  let isMultiplesOfSixOn = false;
  let isColumnToLeftOn = false;
  let isMultiplesOfFiveOn = false;
  let isColumnToRightOn = false;
  let isMultiplesOfSevenOn = false;
  let ishighlightMultiplesOn = false;

function createPattern() {
    // Clear grid before creating a new pattern
    gridContainer.innerHTML = "";
  
    const rangeInput = document.getElementById('rangeInput');
    let range = parseInt(rangeInput.value) || 211;  // Use input value or default to 211 if input is empty
   
    // Adjust range so that the final row is full
    const remainder = range % 6;
    if (remainder === 0) {
        range = range; // since we start at 2, we dont need to add one to the multiples of 6 to complete the row
    } else if (remainder === 1) {
        range = range - 1; // have to subtract 1 b/c we start at 2. otherwise input 25 (remainder=1) gives 26, etc.
    } else if (remainder <= 5){
        range += (6 - remainder) // 5 - remainder would work if we start at 1, but starting at 2 requires 6 - remainder
    }
    
    for (let i = 0; i < range; i++) {
      const gridItem = document.createElement('div');
      gridItem.classList.add('grid-item');
      gridItem.textContent = i + 2;
      gridContainer.appendChild(gridItem);
    }
    
    // Reset the range input field after creating the pattern
    rangeInput.value = "";
}
  
function checkPrime(num) {
  if (num <= 1) {
    return false;
  }
  for (let i = 2; i <= Math.sqrt(num); i++) {
    if (num % i === 0) {
      return false;
    }
  }
  return true;
}

function toggleMultiplesOfSix() {
    const gridItems = document.querySelectorAll('.grid-item');
    isMultiplesOfSixOn = !isMultiplesOfSixOn;
    
    gridItems.forEach(item => {
      const value = parseInt(item.textContent);
      item.classList.toggle('highlight', isMultiplesOfSixOn && value % 6 === 0);
    });
}
  
function toggleColumnToLeft() {
    const gridItems = document.querySelectorAll('.grid-item');
    isColumnToLeftOn = !isColumnToLeftOn;
    
    gridItems.forEach((item, itemIndex) => {
      const columnIndex = itemIndex % 6;
      const value = parseInt(item.textContent);
      const isPrime = checkPrime(value);
      item.classList.toggle('highlight-column-left', isColumnToLeftOn && columnIndex === 3 && isPrime);
    });
}

function toggleColumnToRight() {
    const gridItems = document.querySelectorAll('.grid-item');
    isColumnToRightOn = !isColumnToRightOn;
    
    gridItems.forEach((item, itemIndex) => {
      const columnIndex = itemIndex % 6;
      const value = parseInt(item.textContent);
      const isPrime = checkPrime(value);
      item.classList.toggle('highlight-column-right', isColumnToRightOn && columnIndex === 5 && isPrime);
    });
}
  
function toggleMultiplesOfFive() {
    const gridItems = document.querySelectorAll('.grid-item');
    isMultiplesOfFiveOn = !isMultiplesOfFiveOn;
    
    gridItems.forEach((item, itemIndex) => {
      const rowIndex = Math.floor(itemIndex / 6);
      const columnIndex = itemIndex % 6;
      const isMultipleOfFive = (rowIndex % 5 === 3 && (columnIndex === 0 || columnIndex === 5)) || (rowIndex % 5 === 0 && columnIndex === 3) || (rowIndex % 5 === 1 && columnIndex === 2) || (rowIndex % 5 === 2 && columnIndex === 1) || (rowIndex % 5 === 4 && columnIndex === 4);
      item.classList.toggle('highlight-multiples-five', isMultiplesOfFiveOn && isMultipleOfFive);
    });
}

function toggleMultiplesOfSeven() {
    const gridItems = document.querySelectorAll('.grid-item');
    isMultiplesOfSevenOn = !isMultiplesOfSevenOn;
    
    gridItems.forEach((item, itemIndex) => {
      const rowIndex = Math.floor(itemIndex / 6);
      const columnIndex = itemIndex % 6;
      const isMultipleOfSeven = (rowIndex % 7 === 0 && columnIndex === 5) || ((rowIndex) % 7 === 2 && columnIndex === 0) || (rowIndex % 7 === 3 && columnIndex === 1) || (rowIndex % 7 === 4 && columnIndex === 2) || ((rowIndex) % 7 === 5 && columnIndex === 3) || (rowIndex % 7 === 6 && columnIndex === 4);
      item.classList.toggle('highlight-multiples-seven', isMultiplesOfSevenOn && isMultipleOfSeven);
    });
}

function highlightMultiples() {
    const multiplesInput = document.getElementById('multiplesInput');
    ishighlightMultiplesOn = !ishighlightMultiplesOn;

    let multiple = parseInt(multiplesInput.value) || 0; // Use the input value, default to 1 if input is empty
    
    const gridItems = document.querySelectorAll('.grid-item');
    
    gridItems.forEach(item => {
      const value = parseInt(item.textContent);
      item.classList.toggle('highlight', value % multiple === 0);
    });
  
    // Reset the multiples input field after highlighting
    multiplesInput.value = "";
}

function clearHighlights() {
    const gridItems = document.querySelectorAll('.grid-item');
  
    gridItems.forEach(item => {
      // Remove all highlight classes
      item.classList.remove('highlight');
      item.classList.remove('highlight-column-left');
      item.classList.remove('highlight-column-right');
      item.classList.remove('highlight-multiples-five');
      item.classList.remove('highlight-multiples-seven');
    });
}
//   createPattern();