d3.csv("static/data/creases.csv", function(data) {
	var count = 0;
    data.forEach(function(thing){
    	console.log(count)
        $("#demoCon .container").append("<div class='col-sm-4 portfolio-item'><a href='#port" + count + "' class='portfolio-link artport' data-toggle='modal'><div class='caption'><div class='caption-content'><h4>"+ thing["thing"]+ "</h4></div></div><img src='static/img/creases/" + thing["thing"] + ".jpg' class='img-responsive'></img></a></div>");
    	//$("#demoCon .container").append("<div class='portfolio-modal modal fade' id='port" + count + "' tabindex='-1' role='dialog' aria-hidden='true'><div class='modal-content'><div class='close-modal' data-dismiss='modal'><div class='lr'><div class='rl'></div></div></div><div class='container'><div class='row'><div class='col-lg-8 col-lg-offset-2'><div class='modal-body projectinfo'><h2 class='project-title'>"+ thing["thing"]+ "</h2><img src='static/img/creases/"+ thing["thing"]+ ".jpg class='img-responsive img-centered'><p align='left'>print me</p><button type='button' class='btn btn-default' data-dismiss='modal'><i class=fa fa-times'></i> Close</button></div></div></div></div></div></div>");
    	count++;
    });
});