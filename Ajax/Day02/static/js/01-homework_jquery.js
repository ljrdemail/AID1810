/**
 * Created by tarena on 19-2-12.
 */
function checkUname() {
    /**
     * 后台地址: /01-checkuname
     * 服务器端:返回1,表示用户名已存在,返回0,表示通过
     * 参数: 要检查的用户名称
     * 请求方式: get
     * 同步or异步: 异步
     * */

        //声明返回值,来表示验证结果,提供给调用者使用
    var ret = true;//表示用户名称不存在
    var uname = $("#uname").val();
    $.get("/01-checkuname", "uname=" + uname, function (data) {
        if (data == 1) {
            $("#uname-show").html("用户名称已存在");
            ret = false;
        } else {
            $("#uname-show").html("用户名称不存在，可以注册！");
        }
    })
    return ret;
}

function registerUser() {
    //验证用户名称在数据库中是否存在
    if (checkUname()) {
        /**
         * 请求地址:/01-register
         * 请求方式:post
         * 请求参数1: uname
         * 请求参数2: upwd
         * 请求参数3: uemail
         * 返回值:插入成功或失败的结果
         * */




        var params =

            {
                "uname": $("#uname").val(),
                "upwd": $("#upwd").val(),
                "uemail": $("#uemail").val()
            }

        $.post('/01-register', params, function (data) {
            alert(data);
        })


    } else {
        alert("用户名称已存在,不能注册");
    }
}

/**
 * 页面加载后要执行的操作
 * */
$(function () {
    //1.为#uname绑定blur事件
    $("#uname").blur(function () {
        checkUname();
    });
    //2.为#btnReg绑定click事件
    $("#btnReg").click(function () {
        registerUser();
    });
});










