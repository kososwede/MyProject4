function flashMessage() {
    $("#flash_message").addClass("show");
    setTimeout(function () {
        $("#flash_message").removeClass("show");
    }, 3000);
}
flashMessage();