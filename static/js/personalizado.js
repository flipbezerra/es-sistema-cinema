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

