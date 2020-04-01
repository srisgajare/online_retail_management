$(document).ready(function () {
        $("nav a").attr("style", "color: #ffffff; font-size: 20px;");
    });
    $(document).ready(function () {
        $("nav a").hover(
            function () {
                $(this).attr("style", "color: #FFFF00; background-color: #0099FF; font-size: 20px;");
            }, function () {
                $(this).attr("style", "background-color: #0099FF; color: #ffffff;  font-size: 20px;");
            }
        )
    });

    $(".carousel").carousel({
        interval: 5000
    });

     $(document).ready(function () {
        $('#media').carousel({
            pause: true,
            interval: false,
        });
    });

     