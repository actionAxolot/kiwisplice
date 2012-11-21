// Just show windows and stuff
$(".render_table").on("click", function(e){
    e.preventDefault();
    $("#client-info").modal({"backdrop": true, "show": true});

    // Now fetch data and whatever
    var link = $(e.currentTarget);
    var data = {
	"month": $(e.currentTarget).data("month"),
	"status": $(e.currentTarget).data("status"),
    }

    // Send request
    $.get(
	link.attr("href"),
	data,
	function(data){
	    $("#client-info-table").html(data.template);
	},
	"json"
    );
});

$("#client-info").on("hidden", function(e){
    $(e.currentTarget).find("#client-info-table").html(
	'<div class="progress progress-striped progress-danger active"><div style="width: 100%;" class="bar"></div></div>'
    );
});
