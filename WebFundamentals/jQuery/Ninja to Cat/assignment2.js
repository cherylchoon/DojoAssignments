$(document).ready(function(){

  $('img').hover(function() {
    var currentImage = $(this).attr('src');
    console.log('data-alt-src value is', $(this).attr('data-alt-src'));
    $(this).attr('src',$(this).attr('data-alt-src'));
    $(this).attr('data-alt-src', currentImage);
  });
})
