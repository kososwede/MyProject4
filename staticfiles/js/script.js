function materializeInit() {
    $('.sidenav').sidenav();
    $('.tabs').tabs();
    $('select').formSelect();
    $('.modal').modal();
    $('.collapsible').collapsible();
    $('.tooltipped').tooltip();
    
    
}
materializeInit();

function flashMessage() {
    $("#flash_message").addClass("show");
    setTimeout(function () {
        $("#flash_message").removeClass("show");
    }, 4000);
}
flashMessage();

