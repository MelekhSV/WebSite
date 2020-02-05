$(document).ready(function () {
    var form = $('#form_buying_product');
    console.log(form);


    function basketUpdating(products_name, nmb, products_price, is_delete){
        var data = {};
        data.products_name = products_name;
        data.nmb = nmb;
        data.products_price = products_price;

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


        basketUpdating(products_name, nmb, products_price,is_delete=false)



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
        basketUpdating(products_name, nmb, is_delete = true)

    })
    
    
    
    function calculatingBasketAmount(){
        var total_order_amount = 0
        $('.total-product-in-basket-amount').each(function () {
            total_product_in_basket_amount += parseFloat($(this).text();

        })
        console.log(total_order_amount);
        $('#total_order_amount').text(total_order_amount);
    };

    $(document).on('change',".product-in-basket-nmb", function(){
        var current_nmb = $(this).val()
        var curent_tr = $(this).closest('tr');

        var current_price = parseFloat(curent_tr.find('.prosuct-price').text());
        var total_amount = current_nmb*current_price;
        current_tr.find('.total-product-in-basket-amount').text(total_amount);
        calculatingBasketAmount();
    })



    calculatingBasketAmount();

});