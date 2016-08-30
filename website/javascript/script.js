$(document).ready(function(){
	console.log("heyyyy guys");
	 $('.button-collapse').sideNav({
      menuWidth: 200, // Default is 240
      edge: 'left', // Choose the horizontal origin
      closeOnClick: true // Closes side-nav on <a> clicks, useful for Angular/Meteor
    }
  );
//cheating and using a transition jquery plugin 
var $body    = $('html, body'); // Define jQuery collection 
var content  = $('#main').smoothState({
    onStart : {
      duration: 250,
      render: function () {
        content.toggleAnimationClass('is-exiting');
        
        // Scroll user to the top
        $body.animate({ 'scrollTop': 0 });

      }
    }
  }).data('smoothState');

//smoothState = $('#main').smoothState(options).data('smoothState');
})