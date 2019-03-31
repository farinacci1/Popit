
function jqUpdateSize(){
    // Get the dimensions of the viewport
    var width = $(window).width();
    var height = $(window).height();

    if (width < 740){
      $(".Home").html("");
      $(".Notifications").html("");
      $(".Messages").html("");
      $(".header_content_right").width('60%');
    }
    else if (width >- 740){
      $(".Home").html("Home");
      $(".Notifications").html("Notifications");
      $(".Messages").html("Messages");
      $(".header_content_right").width('50%');
    }
    if(width < 390){
        $(".header_content_right").width('70%');

    }


};
$(document).ready(jqUpdateSize);    // When the page first loads
$(window).resize(jqUpdateSize);     // When the browser changes size
