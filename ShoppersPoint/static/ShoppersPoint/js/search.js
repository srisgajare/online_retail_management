$("#search-id").on('click', function(event) {
    var search_query = ($("#search-input").val());
    if (search_query !== '' || search_query !== ' ') {
        $.ajax({
            type: 'GET',
            url: '/home/search/' + search_query,
            success: function (data) {
                console.log("data:");
                $('#main-results-search').html(data);
            },
            error: function (data) {
                console.log("data:");
                console.log(data);
            }
        });
    }
});

$(document).click(function (event) {
    var $is_inside = $(event.target).closest('#main-results-search').length;

    if (event.target.id === 'search-input' || $is_inside) {
        return 0;
    } else {
        $('#results-search').remove();
    }
});