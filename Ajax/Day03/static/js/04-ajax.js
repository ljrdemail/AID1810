//通过 post 请求 发送给 /02-post
$(function () {
    $("#btnReg").click(function () {
        var params = {
            "uname": $("#uname").val(),
            "upwd": $("#upwd").val(),
            "uemail": $("#uemail").val()
        };
        $.ajax({
            "url": "/02-post",
            "type": "post",
            "data": params,
            "async": true,
            "success": function (data) {
                //data表示响应回来的数据
                alert(data)
            },
            "error": function () {
                alert("程序内部错误！")
            }
        });


    })

});