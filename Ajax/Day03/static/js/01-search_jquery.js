$(function () {
    $("#uname").keyup(function () {
        $.get("/01-search", "uname=" + this.value, function (resText) {

            if (resText.length > 0) {
                $("#show").html("")
                $("#show").css("display", "block")
                $.each(resText, function (i, obj) {
                    var $p = $("<p>" + obj + "</p>")
                    $("#show").append($p)
                })

            } else {
                $("#show").css("display", "none")
            }


        }, "json")


    })

})