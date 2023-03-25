//NAVIGATION

function hideIconBar(){
    const iconBar = document.getElementById("iconBar");
    const navigation = document.getElementById("navigation");
    iconBar.setAttribute("style", "display:none;"); 
    navigation.classList.remove("hide");
}

function showIconBar(){
    var iconBar = document.getElementById("iconBar");
    var navigation = document.getElementById("navigation");
    iconBar.setAttribute("style", "display:block;");
    navigation.classList.add("hide");
}

//Comment

function showComment(){
    var commentArea = document.getElementById("comment-area");
    commentArea.setAttribute("style", "display:block;");
}


function showReply(){
    var commentArea = document.getElementById("reply-area");
    commentArea.setAttribute("style", "display:block;");
}





function doSubmit() {
  var button = document.getElementById('js-btn'),
      timer = document.getElementById('js-timer'),
      reset = document.getElementById('js-reset');
  
  
  button.addEventListener('click', doSubmit);
  reset.addEventListener('click', resetButton);
  
  if (button.classList.contains('do-submit')) { return; }

  // do clicked animation
  button.classList.add('do-submit');
  
  // TODO handle submit, should return amountLoaded
  
  // manually feed amountLoaded as if receiving 0-100% values
  setTimeout(function() {
    doTimer(0);
  }, 1200);
  
  setTimeout(function() {
    doTimer(15);
  }, 1200);

  setTimeout(function() {
    doTimer(75); 
  }, 2000);

  setTimeout(function() {
    doTimer(100);
  }, 2800);
}


function doTimer(amountLoaded) { 
  
  timer.style.strokeDashoffset = 3.83 * (100 - amountLoaded) + 'px';

  if (amountLoaded === 100) {
    setTimeout(function() {
      button.classList.add('success');
    }, 500);
  }
}