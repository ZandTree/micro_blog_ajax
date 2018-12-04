// set csrf token
(function(){
    let csrf_token = Cookies.get('csrftoken');
    $.ajaxSetup({
        headers:{"X-XSFRToken":csrftoken}
    });

})();
let openForm = function (id) {
    $(`#${id}`).show()
};

let closeForm = function (id) {
    $(`#${id}`).hide()
};

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
