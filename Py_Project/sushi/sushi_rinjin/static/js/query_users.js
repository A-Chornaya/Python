function getUsersOrders() {
    var select_user = document.getElementById("id_user");
    var user_id = select_user.options[select_user.selectedIndex].value;

    $.ajax({
        url: "http://127.0.0.1:8000/sushi_rinjin/queries_rest/user_orders/" +
                user_id.toString(),
        success: function (result) {
            var orders = {"orders": result};

            var template = "<ul>"+
                "{{#orders}}" +
                "<li>Order №  {{id}}, used {{pay_method}}</li>" +
                "{{/orders}}" +
                "</ul>";
            var html = Mustache.to_html(template, orders);
            $("#query_user_orders").html(html);
        }
    });
}

function paid(pay_bool) {
    if (pay_bool) {return 'paid'}
    else { return 'not paid'}
}

function getDishByPrice() {
    var element_price = document.getElementById("id_price");
    var price = element_price.value;

    $.ajax({
        url: "http://127.0.0.1:8000/sushi_rinjin/queries_rest/price/" +
                price.toString(),
        success: function (result) {
            var dishes = {"dishes": result};

            var template = "<ul>"+
                "{{#dishes}}" +
                "<li>{{dish_name}}: {{price}} grn</li>" +
                "{{/dishes}}" +
                "</ul>";
            var html = Mustache.to_html(template, dishes);
            $("#query_price").html(html);
        }
    });
}

(function () {
    document.getElementById("button_user_order")
        .addEventListener("click", function () {
            getUsersOrders();
        });
    document.getElementById("button_price")
        .addEventListener("click", function () {
            getDishByPrice();
        });
})();
