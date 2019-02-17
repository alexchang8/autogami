
console.log("hi");

/* Retro Animation */
$(document).ready(function() {
  $(".title").lettering();
  //$(".typed").typed({strings: ["software engineer & designer", "CS Major at Cornell University"]});
});

$(document).ready(function() {
  letteringAnimation();
}, 1000);

function isElementVisible(elem)
{
    var visibleTop = $(window).scrollTop();
    var visibleBottom = visibleTop + $(window).height();

    return ((elem.offset().top + elem.height()) <= visibleBottom);
}
function letteringAnimation() {
  var title1 = new TimelineMax();
  title1.to(".button", 0, {visibility: 'hidden', opacity: 0})
  title1.staggerFromTo(".title span", 0.5, 
  {ease: Back.easeOut.config(1.7), opacity: 0, bottom: -80},
  {ease: Back.easeOut.config(1.7), opacity: 1, bottom: 0}, 0.05);
  title1.to(".button", 0.2, {visibility: 'visible' ,opacity: 1})
}
$('.smooth').on('click', function() {
    $.smoothScroll({
        scrollElement: $('body'),
        scrollTarget: '#' + this.id
    });
    
    return false;
});

/* Scroll Animation */
$(document).ready(function() {
  var options = {
    animateThreshold: 20,
    scrollPollInterval: 5
    }
  $('.aniview').AniView(options);
});


jQuery(document.links) .filter(function() { return this.hostname != window.location.hostname; }) .attr('target', '_blank'); 

/*
jQuery(window).on('load', function(){
  $(".js-masonry").masonry();
}*/
var $grid = $('.js-masonry').masonry({
  // options...
});
// layout Masonry after each image loads
$grid.imagesLoaded().progress( function() {
  $grid.masonry('layout');
});



/*
document.getElementById("down").onclick = function () { 
  alert('hello!'); 
};
*/
document.getElementById("rip").addEventListener("click", function(e) {
  //getdata()
  console.log("hi");
});

