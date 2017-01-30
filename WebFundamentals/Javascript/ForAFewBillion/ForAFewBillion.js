var penny = 0.01;

function doubleSum (penny) {
  for (var i=1; i<31; i++) {
    penny = penny * 2;
  }
  return penny;
}

doubleSum(penny);
console.log(doubleSum(penny));
