$(function () {
    $("#uname").keyup(function () {
        $.get("/01-search", "uname=" + this.value, function (data) {
            //data 是相应回来的数据 直接被转换成js数据
            if (data.length > 0) {
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