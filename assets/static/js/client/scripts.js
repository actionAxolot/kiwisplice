$(".date-picker").datepicker({
	"format": "dd/mm/yyyy",
});


// Map position capture
$("#map-container").on("click", function(e){
    var x = e.pageX - $("#map-container").offset().left;
    var y = e.pageY - $("#map-container").offset().top;

    // Now set them to be stored
    $("#id_x").val(x.toFixed(5));
    $("#id_y").val(y.toFixed(5));

    // Load and display pointer image
    var img = "<img id='pointer-thing' src='/static/img/map/pointer_red.png' />";
    $("#map-container").html(img);
    $("#pointer-thing").css({
        position: 'absolute',
        top: y + 5,
        left: x - 8,
        zIndex: 3500
    });

    return false;
});

$(document).ready(function(){
  if($("#id_x").val()){
    var x = parseFloat($("#id_x").val());
    var y = parseFloat($("#id_y").val());

    var img = "<img id='pointer-thing' src='/static/img/map/pointer_red.png' />";
    $("#map-container").html(img);
    $("#pointer-thing").css({
      position: 'absolute',
      top: y + 5,
      left: x - 8,
      zIndex: 3500
    });

    return false;
  }
})
