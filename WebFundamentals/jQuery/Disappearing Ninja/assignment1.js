$(document).ready(function() {

  $('img').click(function() {
    $(this).fadeOut();
  })

  $('#restore').click(function(){
    $('img').show();
  })

})
