function(){
    var elementPosition = $('#sidebar__profile-nav').offset();
    $(window).scroll(function(){
            if($(window).scrollTop() > elementPosition.top){
                  $('#sidebar__profile-nav').addClass("nav-float");
            } else {
                $('#sidebar__profile-nav').removeClass("nav-float");
            }
    });
}();
