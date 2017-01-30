function numOnly(arr) {
  var newarr = [];
  for (var i=0; i<arr.length; i++) {
    if (typeof arr[i] === "number") {
      newarr.push(arr[i]);
    }
  }
  return newarr;
}
var test = numOnly([1,"apple",-3,"orange",0.51]);
console.log(test);
