
console.log("hi");
/*
$(document).ready(function() {
  $(".title").lettering();
});
$(document).ready(function() {
  $('.aniview').AniView();
});*/

/*
$(window).on("scroll",function(){
if($("body").scrollTop() === 500){
    console.log("hi");
    $(window).off("scroll");
    var options = {
    animateThreshold: 100,
    scrollPollInterval: 20
    }
    $('.aniview').AniView(options);
    // Do some stuff here ..
  }
});
function slide(){
    var options = {
    animateThreshold: 100,
    scrollPollInterval: 20
    }
    $('.aniview').AniView(options);
};*/


/*
$(document).ready(function() {
  animation();
}, 1000);

function isElementVisible(elem)
{
    var visibleTop = $(window).scrollTop();
    var visibleBottom = visibleTop + $(window).height();

    return ((elem.offset().top + elem.height()) <= visibleBottom);
}
function animation() {
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
});*/

