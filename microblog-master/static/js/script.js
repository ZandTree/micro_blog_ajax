// set csrf token
(function () {
    let csrftoken = Cookies.get('csrftoken');
    // console.log(csrftoken);
    $.ajaxSetup({
        headers: {"X-CSRFToken": csrftoken}
    });
})();
//Показать форму комментария
let openForm = function (id) {
    $(`#${id}`).show()
};
// Скрыть форму комментария
let closeForm = function (id) {
    $(`#${id}`).hide()
};

// Поставить лайк
let like = function (id) {
    $.ajax({
        url: "http://127.0.0.1:8000/like/",
        type: "POST",
        data: {
            pk: id,
        },
        success: (response) => {
        window.location = response;
        }
    })

};

$(".need_auth").submit(function(e){
         e.preventDefault();
         var url = $(this).attr('action');
         var data = $(this).serialize();
         $.post(
            url,
            data,
            function(response){
                window.location = response;
            },

        );
     });

 // $("#signup_form").submit(function(e){
 //             e.preventDefault();
 //             var url = $(this).attr('action');
 //             console.log(url);
 //             var data = $(this).serialize();
 //             $.post(
 //                url,
 //                data,
 //                function(response){
 //                    window.location = response;
 //                },

         //    );
         // });



         // error: function(xhr, ajaxOptions, thrownError){
         //        alert('login failed - please try again');
         // },


// "login": $('#id_login').val(),
// "password": $('#id_password').val(),
// "remember": $('#id_remember').val()
