$(function () {
    $("#btnShow").click(function () {
        //1.创建xhr
        var xhr = createXhr();
        //2.创建请求 - get
        xhr.open('get', '/02-query', true);
        //3.设置回调函数
        xhr.onreadystatechange = function () {
            if (xhr.readyState == 4 && xhr.status == 200) {
                var users = xhr.responseText.split('|');
                var html = "";
                for (var i = 0; i < users.length; i++) {
                    var u = users[i].split('-');

                    html += "<tr>";
                    html += "<td>" + u[0] + "</td>";
                    html += "<td>" + u[1] + "</td>";
                    html += "<td>" + u[2] + "</td>";
                    html += "<td>" + u[3] + "</td>";
                    html += "</tr>";

                    // console.log("ID:"+u[0]);
                    // console.log("用户名称:"+u[1]);
                    // console.log("用户密码:"+u[2]);
                    // console.log("邮箱:"+u[3]);
                }
                console.log(html);
                $("#content").html(html);
            }
        }
        //4.发送请求
        xhr.send(null);
    });
});