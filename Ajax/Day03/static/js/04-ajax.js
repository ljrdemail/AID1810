$(function () {
    $("#btnReg").click(function () {
        var params = {
            "uname": $("#uname").val(),
            "upwd": $("#upwd").val(),
            "uemail": $("#uemail").val()
        };
        $.ajax({
            "url": "/02-post", "type": "post", "data": params, "async": true, "success": function (data) {
                alert(data)
            }, "error": function () {
                alert("程序内部错误！")
            }
        });


    })

});