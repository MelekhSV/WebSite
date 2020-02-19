$(document).ready(function () {
    var form = $('#form_buying_product');
    console.log(form);

    function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}


















    function basketUpdating(products_name, nmb, is_delete){
        var data = {};
        data.products_name = products_name;
        data.nmb = nmb;
        // data.products_price = products_price;

            var csrf_token = $('#form_buying_product [name="csrfmiddlewaretoken"]').val();
            data["csrfmiddlewaretoken"] = csrf_token;

        if (is_delete){
            data["is_delete"] = true;
        }


            var url = form.attr("action");
        console.log(data);


            $.ajax({
                url: url,
                type: 'POST',
                data: data,
                cache: true,
                success: function (data) {
                    console.log('OK');
                    console.log(data.products_total_nmb);
                    if (data.products_total_nmb|| data.products_total_nmb == 0) {
                        $('#basket_total_nmb').text("("+data.products_total_nmb+")");
                        console.log(data.products);
                        $('.basket-items ul').html("");
                        $.each[data.products, function (k, v) {
                            $('.basket-items ul').append('<li> '+v.products_name+','+v.nmb+','+v.products_price+'      <a class ="delete-item" href="" data-products_name="'+v.products_name+'"> x </a> </li>');
                        }];
                    }

                },
                error: function  () {
                     console.log('Error');
                },





            //     // $('#likes_list').html();
            //     // $.cach(data, function (key, value) {
            //     //     $('#likes_list').append('<p>' + value.username + ' </p>')
            //     //
            //     // })
            // }

            });



        // $('.basket-items ul').append('<li> '+products_name+','+nmb+'      <a class ="delete-item" href=""> x </a> </li>');

    }



    form.on('submit', function (e) {

        e.preventDefault();
        console.log('123');
        var nmb = $('#number').val();
        console.log(nmb);
        var submit_btn=$('#submit_btn');
        var products_name = submit_btn.data("name");
        var products_price = submit_btn.data("price");


        console.log(products_name);


        basketUpdating(products_name, nmb,is_delete=false)



    });


    function showingBasket(){
        $('.basket-items').removeClass('hidden');
    }




    $('.basket-container').on('click  ',function (e) {
        e.preventDefault();
        showingBasket();

    });
    $('.basket-container').mouseover(function () {
        showingBasket()

    })
    // $('.basket-container').mouseout(function () {
    //     showingBasket();
    //     $('.basket-items').addClass('hidden');


    $(document).on('click', '.delete-item', function (e) {
        e.preventDefault();
        products_name = $(this).data("products_name")
        nmb = 0;
        basketUpdating(products_name, nmb,is_delete = true)

    })
    
    
    
    function calculatingBasketAmount(){
        var total_order_amount = 0
        $('.total-product-in-basket-amount').each(function () {
            console.log($(this).text());
            // total_product_in_basket_amount += parseFloat($(this).text());

        });
        console.log(total_order_amount);
        // var name = $('.name-in-basket-nmb').val();
        // console.log(name);
        // $('.name-in-basket-nmb').each(function () {
        // //     console.log($(this).text());
        // });
        $('#total_order_amount').text(total_order_amount);
    };

    $(document).on('change',".product-in-basket-nmb", function(){
        var current_nmb = $(this).val();
        var curent_tr = $(this).closest('tr');
        // $('.name-in-basket-nmb').each(function () {
        //     console.log($(this).text());
        // });
        // var nmb = $('.name-in-basket-nmb').val();
        // console.log(nmb);
        var current_price = parseFloat(curent_tr.find('.product-price').text());
        var total_amount = current_nmb*current_price;
        current_tr.find('.total-product-in-basket-amount').text(total_amount);
        calculatingBasketAmount();
    })



    calculatingBasketAmount();


// $(document).ready(function () {
//     var form = $('#orders_buying_product');
//     console.log(form);

    $(document).on('click', '.submit_btn_mail', function (e) {
        e.preventDefault();
        var form = $('#orders_buying_product');
        var data1 = {};

        var name = $('.name-in-basket-nmb').val();
        console.log(name);
        data1.name = name;


            // var csrf_token = $('#orders_buying_product [name="csrfmiddlewaretoken"]').val();
            var csrftoken = getCookie('csrftoken');
            data1["csrftoken"] = csrftoken;

            var url = form.attr("action");
            console.log(data1);


            $.ajax({
                url: url,
                type: 'POST',
                data: data1,
                cache: true,
                success: function (data) {
                    console.log('OK');
                    console.log(data.name);
                },
                error: function  () {
                     console.log('Error11111111111111');
                }



            });


    });





    $(document).on('click', '.submit1-btn-mail', function (e) {
            e.preventDefault();
            var form = $('#orders1_buying_product');
            var data = {};
            var name = $('.name1-in-basket-nmb').val();
            var mail = $('.mail1-in-basket-nmb').val();
            var adress = $('.adress1-in-basket-nmb').val();
            console.log(name);
            console.log(mail);
            console.log(adress);
            data.name = name;
            data.mail = mail;
            data.adress = adress;
                // var csrf_token = $('#orders_buying_product [name="csrfmiddlewaretoken"]').val();
                var token = getCookie('csrftoken');
                // data["csrftoken"] = csrftoken;
                var url = form.attr("action");
            console.log(data);
                $.ajax({
                    url: url,
                    headers: { "X-CSRFToken": token },
                    type: 'POST',
                    data: data,
                    cache: true,
                    success: function (data) {
                        console.log('OK');
                        // console.log(data.name);
                    },
                    error: function  () {
                         console.log('Error1223');
                    }
                })
        })
});