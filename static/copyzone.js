$(document).ready(function(){
var copyTextareaBtns = document.getElementsByTagName('button');


for(i=0; i<copyTextareaBtns.length; i++) {
copyTextareaBtns[i].addEventListener('click', function(event) {
   
    $(this).parent().prev().find("textarea").select();

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
