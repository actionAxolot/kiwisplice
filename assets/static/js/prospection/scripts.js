if($("#id_visitation_date").get(0)){
    $("#id_visitation_date").datepicker({
        "format": "dd/mm/yyyy"
    });
}

// Get ajax calls and what not. Return and render templates
$(".render_table").on("click", function(e){
    e.preventDefault();
    $("#prospection-info").modal({"backdrop": true, "show": true});
    var link = $(e.currentTarget);
    $.get(
        link.attr("href"),
        {"date": link.data("date"), "status": link.data("status")},
        function(data){
            $("#prospection-info-table").html(data.template);
        },
        "json"
    );
});

// Get ajax calls and what not. Return and render templates
$(".render_table_channel").on("click", function(e){
    e.preventDefault();
    $("#prospection-info").modal({"backdrop": true, "show": true});
    var link = $(e.currentTarget);
    $.get(
        link.attr("href"),
        {"income": link.data("income"), "channel": link.data("channel")},
        function(data){
            $("#prospection-info-table").html(data.template);
        },
        "json"
    );
});

// Get ajax calls and what not. Return and render templates
$(".render_table_status").on("click", function(e){
    e.preventDefault();
    $("#prospection-info").modal({"backdrop": true, "show": true});
    var link = $(e.currentTarget);
    $.get(
        link.attr("href"),
        {"income": link.data("income"), "status": link.data("status")},
        function(data){
            $("#prospection-info-table").html(data.template);
        },
        "json"
    );
});

$("#prospection-info").on("hidden", function(e){
    $(e.currentTarget).find("#prospection-info-table").html(
        '<div class="progress progress-striped progress-danger active"><div style="width: 100%;" class="bar"></div></div>'
    );
});