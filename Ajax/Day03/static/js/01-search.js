$(function () {
    $("#uname").keyup(function () {
        var xhr = createXhr()

        xhr.open("get", "/01-search?uname=" + this.value, true)
        xhr.onreadystatechange = function () {
            if (xhr.readyState == 4 && xhr.status == 200) {
                //1 接收想赢数据并转换成JS 对象/数组
                var arr = JSON.parse(xhr.responseText);

                //循环遍历arr 将里面的元素构建成p标记追加到#show里面

                if (arr.length > 0) {
                    $("#show").html("")
                    $("#show").css("display", "block")
                    $.each(arr, function (i, obj) {
                        var $p = $("<p>" + obj + "</p>")
                        $("#show").append($p)
                    })

                } else {
                    $("#show").css("display", "none")
                }
            }

        }
        xhr.send(null);

    })

})