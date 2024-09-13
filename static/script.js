$(document).ready(function () {
    $("#popup").html("Login Successfull.")
    $("#popup").show()
    setTimeout(hidePopup, 2500);
})

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

function hidePopup() {
    $("#popup").hide()
}