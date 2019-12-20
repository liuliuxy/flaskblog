var login_url = " {{url_for('user.login')}}";


$(document).ready(function () {
    $(".loginkey").click(function () {
        $(".popBox-content").slideDown("fast")
    });

    $(".loginclose").click(function () {
        $(".popBox-content").slideUp("fast")
    });
});

// $(window).on("hashchange", function () {
//     var hash = window.location.hash.replace('#', '');
//     var url = null;
//     if (hash = "login") {
//         url = login_url
//     }
//     S.ajax({
//         type: post,
//         url: 'url'
//     })
// });
//
// $(window).trigger("hashchange");
