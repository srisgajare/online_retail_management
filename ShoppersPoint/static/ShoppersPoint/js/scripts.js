$(function() {
	$('pre').on('click', function(event) {
		event.preventDefault();
		$(this).selText().addClass("selected");
	});

});
jQuery.fn.selText = function() {
    var obj = this[0];
    if ((/msie|trident/i).test(navigator.userAgent)) {
        var range = obj.offsetParent.createTextRange();
        range.moveToElementText(obj);
        range.select();
    } else if ((/opera|firefox/i).test(navigator.userAgent)) {
        var selection = obj.ownerDocument.defaultView.getSelection();
        var range = obj.ownerDocument.createRange();
        range.selectNodeContents(obj);
        selection.removeAllRanges();
        selection.addRange(range);
    } else if ((/chrome|safari/i).test(navigator.userAgent)) {
        var selection = obj.ownerDocument.defaultView.getSelection();
        selection.setBaseAndExtent(obj, 0, obj, 1);
    }
    return this;
}



$("#add_cart").on('click', function(event) {
    $.ajax({
        type: "POST",
        url: '{% url "user:add_item" %}}',
        data: {
            'csrfmiddlewaretoken': '{{ csrf_token }}',
            'q': '{{ product_id }}',
        },
        success: function(results) {
            json = JSON.stringify(json);
            var json_response = JSON.parse(json);
            $("#cart-size").text(json_response.cart_count);
            toastr.success('Success!');
        }
    })
});