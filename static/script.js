$("#logout-btn").click(function () {
    $.ajax({
        url: "/logout",
        type: "GET",
        success: function (response) {
            window.location.href = "/login";
        },
        error: function (error) {
            console.error("Logout failed", error);
        }
    });
});