$(document).ready(function () {
    $('#cin').hide();
    $("#add-task").hover(function () {
            $('#cin-message').hide();
            $('#cin').show();
        },
        function () {
            $('#cin').hide();
            $('#cin-message').show();
        });
    $("#cin").keypress(function (event) {
        if (event.keyCode === 13) {
            $("#todo-list").append($('#todo-list').html("< li class ='list-group-item'>< input type='checkbox ' name = ''  id = '' class = 'mr-2' > " + $('#cin').val() + "</li>"));
        }
    });
});




$(document).ready(function () {
    /* Progress Bar animation */
    $(".progress-bar").animate({
        width: "100%"
    }, 250); // start in under a sec
});