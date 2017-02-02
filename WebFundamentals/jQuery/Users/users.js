
$(document).ready(function(){
  $('#submit').click(function() {
    $row = $('<tr/>');
      for(i=1; i<=4; i++){
        if (i<5) {
          cellVal = $("#test"+i).val();
          $row.append($("<td/>").text(cellVal));
        }
          //cellVal = i < 5 ? $("#test"+i).val() : $("input").val();

      }
      $('table').append($row);
  })
});
