$(document).ready(function () {
    $("#username").val("");
    $("#password").val("");

    $('#login-btn').click(function (event) {
        event.preventDefault();

        var username = $('#username').val();
        var password = $('#password').val();

        if (!username || !password) {
            alert('Please enter both username and password.');
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
                console.log('Success:', response);
                window.location.href = '/';
            },
            error: function (xhr, status, error) {
                console.error('Error:', error);
                alert('Login failed. Please try again.');
                $("#username").val("");
                $("#password").val("");
            }
        });
    });
});
