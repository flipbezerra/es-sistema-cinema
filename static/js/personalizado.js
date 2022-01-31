/* Instruções javascript - funcionamento do video embutido no modal */
const Play = document.querySelector('#play'),
Close = document.querySelector('#close'),
Modal = document.querySelector('.modal');

Play.addEventListener('click',()=>{
    Modal.classList.add('show');
});

Close.addEventListener('click',()=>{
    Modal.classList.remove('show');
    var iframes = Modal.getElementsByTagName('iframe');
    if (iframes != null) {
        for (let i = 0; i < iframes.length; i++) {
            const iframe = iframes[i];
            iframe.src = iframe.src;
        }
    }
});

window.setTimeout(function() {
    /* Instruções javascript - limite de tempo para os alertas serem exibidos */
    $(".messages").fadeTo(400, 0).slideUp(400, function(){
      $(this).remove();
   });
}, 3000);
