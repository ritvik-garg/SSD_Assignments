function myFunction() {
    window.open(
        'resources/SSD_Assignment_2.pdf'
    );
}

// function blink_text() {
//     $('.blink').fadeOut(100);
//     $('.blink').fadeIn(100);
// }
// setInterval(blink_text, 500);

var blink = document.getElementById('blink');
setInterval(function() {
    blink.style.opacity = (blink.style.opacity == 0 ? 1 : 0);
}, 100);