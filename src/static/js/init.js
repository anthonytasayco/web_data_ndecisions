
/*########################
# fullScreen
########################*/


function fullScreen(){
		var $header= $('.header').outerHeight();
		var vHeight = $(window).height() - $header; 
		

		var vWidth = $(window).width();
		//console.log(vHeight);
		if(vWidth>740){
			$('.wrapper-table, .center-inner').height(vHeight);
		}else{
			$('.wrapper-table').css('height', 'auto');
			$('.center-inner').css('height', '100%');
		}
	}
fullScreen();
$(window).resize(function(event) {
	fullScreen();
});	