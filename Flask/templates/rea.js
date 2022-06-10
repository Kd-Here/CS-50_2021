
/***********************************************
 JQuery function to toggle the navigation menu
***********************************************/

$(function() { 
    $('.menu-button').on('click', function(){
        $('.off-canvas-menu').toggleClass('open');
        $('.menu-bar1').toggleClass('active');
        $('.menu-bar2').toggleClass('active');
        $('.menu-bar3').toggleClass('active');
    });
});