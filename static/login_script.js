$("#popup").hide()

$(document).ready(function () {
    $("#username").val("");
    $("#password").val("");
});

function hidePopup() {
    $("#popup").hide()
}

$('#login-btn').click(function (event) {
    event.preventDefault();

    var username = $('#username').val();
    var password = $('#password').val();

    if (!username || !password) {
        $("#popup").html("Please input both username and password.")
        $("#popup").show()
        setTimeout(hidePopup, 4000);

        $("#username").val("");
        $("#password").val("");
        $("#username").focus();

        return;
    }

    $.ajax({
        url: '/login-user',
        type: 'POST',
        contentType: 'application/json',
        data: JSON.stringify({
            username: username,
            password: password
        }),
        success: function (response) {
            window.location.href = '/';
        },
        error: function (xhr, status, error) {
            console.error('Error:', error);

            $("#popup").html("Incorrect credentials inserted. Please try again.")
            $("#popup").show()
            setTimeout(hidePopup, 4000);

            $("#username").val("");
            $("#password").val("");

            $("#username").focus();
        }
    });
});