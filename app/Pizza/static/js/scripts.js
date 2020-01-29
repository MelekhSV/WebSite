$(document).ready(function () {
    var form = $('#form_buying product');
    console.log(form);
    form.on('submit', function (e) {

        e.preventDefault();
        console.log('123');
        var nmb = $('number').val();
        console.log(nmb);
        var submit_btn=$('$submin_btn');
        var products_name = submin_btn.data("post.title");

        console.log(submit_btn);
        console.log(products_name);
        //
        // $('.basket-items ul').append('<li> '+products_name+','+nmb'</li>');
        $('.basket-items ul').append('<li> dsgf</li>');

    });


    function showingBasket(){
        $('.basket-items').toggleClass('hidden');
    }




    $('.basket-container').on('click ',function (e) {
        e.preventDefault();
        showingBasket();

    })
    $('.basket-container').mouseover(function () {
        showingBasket()

    })
    $('.basket-container').mouseout(function () {
        showingBasket();
        $('.basket-items').addClass('hidden');

    })



});