$(".action-commission").on("click", function(e){
    e.preventDefault();
    var appLabel = $(e.currentTarget).data("app-label");
    var model = $(e.currentTarget).data("model");
    var id = $(e.currentTarget).data("id");
    var isTabbed = $(e.currentTarget).data("is-tabbed");
    
    // Form the query string to send to the URL before rendering
    var q = "?app_label="+ appLabel + "&id=" + id + "&model=" + model + "&is_tabbed=" + isTabbed;
    var url = "/comisiones/ajax/" + q;

    // Now trigger the pop-up 
    $("#commission-info").modal({"backdrop": true, "show": true});

    // Now load the necessary info into the popup
    $("#commission-info-table").load(url);
});

$("#commission-info").on("hidden", function(e){
    $(e.currentTarget).find("#commission-info-table").html(
        '<div class="progress progress-striped progress-danger active"><div style="width: 100%;" class="bar"></div></div>'
    );
});
