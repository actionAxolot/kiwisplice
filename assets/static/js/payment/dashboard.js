// Just show windows and stuff
$(".render_table").on("click", function (e) {
    e.preventDefault();
    $('#payment-info').modal({"backdrop":true, "show":true});

    // Now fetch data and whatever
    var link = $(e.currentTarget);
    var data = {
        "date":$(e.currentTarget).data("month"),
        "status":$(e.currentTarget).data("income"),
    }

    // Send request
    $.get(
        link.attr("href"),
        data,
        function (data) {
            $("#payment-info-table").html(data.template);
        },
        "json"
    );
});

$("#payment-info").on("hidden", function (e) {
    $(e.currentTarget).find("#payment-info-table").html(
        '<div class="progress progress-striped progress-danger active"><div style="width: 100%;" class="bar"></div></div>'
    );
});