function getIngredList() {
    $.ajax({
        url: "http://127.0.0.1:8000/sushi_rinjin/ingred/",
        success: function (result) {
            var ingreds = {"ingreds": result};
            var template = "<ul>" +
                "{{#ingreds}}" +
                "<li> {{ingredient}}</li>" +
                "{{/ingreds}}" +
                "</ul>";
            var html = Mustache.to_html(template, ingreds);
            $("#ingred_list").html(html);
        }
    });
}

(function () {
    document.getElementById("get_ingred_rest")
        .addEventListener("click", function () {
            getIngredList();
            //document.getElementById("demo").innerHTML = "Hello World";
        });
})();
