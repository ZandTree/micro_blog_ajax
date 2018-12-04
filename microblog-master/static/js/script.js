// set csrf token
// Установка csrf_token
(function () {
    let csrftoken = Cookies.get('csrftoken');
    $.ajaxSetup({
        headers: {"X-CSRFToken": csrftoken}
    });
})();

// Показать форму комментария
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

        }
    })
};

// var  $button = $('#need_login');
//
//      $button.on('click',function(){
//
//         var data = {
      // "csrfmiddlewaretoken" : document.getElementsByName('csrfmiddlewaretoken')[0].value,
       // "login": $('#id_login').val(),
       // "password": $('#id_password').val(),
       // "remember": $('#id_remember').val()
       //  }

        // var temp = {'X-CSRFToken': document.getElementsByName('csrfmiddlewaretoken'[0].value };

//         $.post({
//           url : "/accounts/login/",
//           // headers: temp,
//           type: "POST",
//           data : data,
//           contentType: "application/x-www-form-urlencoded",
//           dataType: "text",
//           success: function(response){
//         // redirect to the required url
//         window.location = response;
//         },
//         error: function(xhr, ajaxOptions, thrownError){
//         alert('login failed - please try again');
//         },
//     });
// });
