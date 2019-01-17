$(document).ready(function () {
    countItem();
    $("#checkAll").click(function () {
        //全选
        var status = $("#checkAll").prop("checked")

        $("[name=check]").prop("checked", status)
        countItem();
    })
    // 反选
    $("[name=check]").change(function () {
        var uncheck = $("[name=check]").not("input:checked").length


        if (uncheck == 0) {
            $("#checkAll").prop("checked", true)

        } else {

            $("#checkAll").prop("checked", false)
        }

        countItem();


    })

    //数量增减
    $(".add").click(function () {
        var value = $(this).prev().val()

        $(this).prev().val(parseInt(value) + 1)

        qty = parseInt(value) + 1

        //价格联动 单价*数量
        var pricestr = $(this).parent().prev().html()
        var price = parseFloat(pricestr.substring(1))//从第一截止末尾 去人民币标志

        var sum = price * qty
        //修改小计
        $(this).parent().next().html("<b>&yen;" + sum + "</b>")
        countItem();

    })

    $(".minus").click(function () {
        var value = $(this).next().val()
        if (value > 1) {
            $(this).next().val(parseInt(value) - 1)
            qty = parseInt(value) - 1

            //价格联动 单价*数量
            var pricestr = $(this).parent().prev().html()
            var price = parseFloat(pricestr.substring(1))//从第一截止末尾 去人民币标志
            var sum = price * qty
            //修改小计
            $(this).parent().next().html("<b>&yen;" + sum + "</b>")
            countItem();

        } else {
            var res = confirm("确定要移除？")
            if (res) {
                $(this).parents(".g-item").remove()
            }
        }

    })

    $(".count input").blur(function () {
        var value = $(this).val()
        var priceStr = $(this).parent().prev().html()
        var price = priceStr.substring(1)/*去掉人民币符号*/
        var sum = price * value
        $(this).parent().next().html("<b>&yen;" + sum + "</b>")/*加回人民币符号*/
        countItem();

    })

    //移除操作
    $(".g-item .action").click(function () {
        //获取父元素g.item 移除
        $(this).parent().remove()
        countItem();

    })

    //做工具栏价格和数量的统计
    function countItem() {

        var count = 0;//保存总数量
        var price = 0;//保存总价格
        //获取被选中的商品/价格 做累加
        $("[name=check]:checked").each(function () {
            //each 用于遍历数组或集合，没取到一个元素 自动调用相关函数
            count += parseInt($(this).parents(".g-item").find(".count input").val())
            //获取价格字符串
            var priceStr = $(this).parents(".g-item").find(".sum b").html()
            //截取和转换
            var priceNum = parseFloat(priceStr.substr(1))
            price += priceNum



        })

        //显示在工具栏
        $(".submit-count span").html(count)
        $(".submit-price span").html("&yen;" + price)
    }


})