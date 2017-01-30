function printRange(num1,num2,skipamt) {
  for (var i=num1; i<num2; i=(i+skipamt)) {
    console.log(i);
  }
}

printRange(2,10,2);
