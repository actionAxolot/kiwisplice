// Just show windows and stuff
$(".render_table").on("click", function(e){
    e.preventDefault();
    $("#inventory-info").modal({"backdrop": true, "show": true});

    // Now fetch data and whatever
    var link = $(e.currentTarget);
    var data = {
	"section": $(e.currentTarget).data("section"),
	"prototype": $(e.currentTarget).data("prototype"),
	"block": $(e.currentTarget).data("block"),
	"date-const": $(e.currentTarget).data("date-const"),
	"status": $(e.currentTarget).data("status")
    }

    // Send request
    $.get(
	link.attr("href"),
	data,
	function(data){
	    $("#inventory-info-table").html(data.template);
	},
	"json"
    );
});

$("#inventory-info").on("hidden", function(e){
    $(e.currentTarget).find("#inventory-info-table").html(
	'<div class="progress progress-striped progress-danger active"><div style="width: 100%;" class="bar"></div></div>'
    );
});
