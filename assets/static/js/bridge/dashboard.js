// Just show windows and stuff
$(".render_table").on("click", function(e){
    e.preventDefault();
    $("#bridge-info").modal({"backdrop": true, "show": true});

    // Now fetch data and whatever
    var link = $(e.currentTarget);
    var data = {
	"const-status": $(e.currentTarget).data("const-status"),
	"bridge-status": $(e.currentTarget).data("bridge-status"),
    }

    // Send request
    $.get(
	link.attr("href"),
	data,
	function(data){
	    $("#bridge-info-table").html(data.template);
	},
	"json"
    );
});

$("#bridge-info").on("hidden", function(e){
    $(e.currentTarget).find("#bridge-info-table").html(
	'<div class="progress progress-striped progress-danger active"><div style="width: 100%;" class="bar"></div></div>'
    );
});
