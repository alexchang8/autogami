
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

$(document).ready(function() {
  $(".typed").typed({
    strings: ["CS major at Cornell University","software engineer + designer", "Cornell University Unmanned Air Systems"],
    startDelay: 1200,
    backDelay: 1000,
    loop: true,
    loopCount: 5,
    showCursor: true
  });
});

function VerticalTimeline( element ) {
   this.element = element;
   this.blocks = this.element.getElementsByClassName("js-cd-block");
   this.images = this.element.getElementsByClassName("js-cd-img");
   this.contents = this.element.getElementsByClassName("js-cd-content");
   // ...
};

VerticalTimeline.prototype.showBlocks = function() {
   var self = this;
   for( var i = 0; i < this.blocks.length; i++) {
      (function(i){
         if( self.contents[i].classList.contains("cd-is-hidden") && self.blocks[i].getBoundingClientRect().top <= window.innerHeight*self.offset ) {
            // add bounce-in animation
            self.images[i].classList.add("cd-timeline__img--bounce-in");
            self.contents[i].classList.add("cd-timeline__content--bounce-in");
            self.images[i].classList.remove("cd-is-hidden");
            self.contents[i].classList.remove("cd-is-hidden");
         }
      })(i);
   }
};

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



