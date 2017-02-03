$(document).ready(function(){

 for(var i=1; i<152; i++){
    $('#pokemon').append('<img id='+i+' src="http://pokeapi.co/media/img/'+i+'.png">');
  }

 $(document).on("click", "img", function() {
     var idnum = $(this).attr("id");
     var imgurl= "http://pokeapi.co/media/img/" + idnum + ".png";
     var url = "http://pokeapi.co/api/v1/pokemon/" + idnum;
     var data = $.get(url);
     console.log(data);

   $.get(url, function(res) {
      var name = res.name;
      var type = "<h4>Types</h4>" + "<ul>";
      for (var i=0; i<res.types.length; i++) {
        type += "<li>" + res.types[i].name +"</li>";
      }
      type += "</ul>";
      var height = "<h4>Height</h4>" + res.height;
      var weight = "<h4>Weight</h4>" + res.weight;

     $('#pokedex h1').html(name);
      $('#pokedex img').attr('src',imgurl);
      $('#types').html(type);
      $('#height').html(height);
      $('#weight').html(weight);

   }, "json");

   });
 });
