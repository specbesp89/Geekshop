
window.onload = function () {
    $('.basket_list').on('click', 'input[type="number"]', function () {
        var t_href = event.target;
        // console.log(t_href.name);  // id корзины
        // console.log(t_href.value); // кол-во
        $.ajax({
            url: "/baskets/edit/" + t_href.name + "/" + t_href.value + "/",
            success: function (data) {
                $('.basket_list').html(data.result);
            }
        });
        event.preventDefault();
    });
}