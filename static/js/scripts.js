$(document).ready(function () {
    $('#theme_switch').on('click', function () {
        alert('asdasd')
        document.body.classList.toggle('xmas_theme')
    })
})
// light number setting start
$(document).ready(function () {
    $(window).on('resize load', function () {
        ww = $(window).width()
        // alert(ww)
        // light_numbber = 0.03197674418 * ww
        light_numbber = 0.0288 * ww
        light_num = parseInt(light_numbber)
        // alert(light_num)
        $('.wire').empty()
        for (var i = 0; i < light_num; i++) {
            $('.wire').append('<li></li>')
        }
    })
})
// light number setting end