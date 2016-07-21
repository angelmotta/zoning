$(document).ready(function(){
var copyTextareaBtns = document.getElementsByTagName('button');
var copyTextareas = document.getElementsByTagName('textarea');

for(i=0; i<copyTextareaBtns.length; i++) {
copyTextareaBtns[i].addEventListener('click', function(event) {
    
    copyTextareas[i].select();

    try {
        var successful = document.execCommand('copy');
        var msg = successful ? 'successful' : 'unsuccessful';
        console.log('Copying text command was ' + msg);
    }
    catch (err) {
        console.log('Oops, unable to copy');
    }
});
}
});
