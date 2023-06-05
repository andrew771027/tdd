$(document).ready(function () {
    $('input').on('keypress', function () {
        console.log("Handler for `keypress` called.");
        $('.has-error').hide();
    });
});