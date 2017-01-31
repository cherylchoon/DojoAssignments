var students = [
     {first_name:  'Michael', last_name : 'Jordan'},
     {first_name : 'John', last_name : 'Rosales'},
     {first_name : 'Mark', last_name : 'Guillen'},
     {first_name : 'KB', last_name : 'Tonel'}
]

function name(arr) {
  var count = 1;

  for (var i=0; i<arr.length; i++) {
      var letterCount = (arr[i]['first_name'].length + arr[i]['last_name'].length);
      console.log(count++ + " - " + arr[i]['first_name'],arr[i]['last_name'] + " - "+letterCount);
}
}
name(students);
