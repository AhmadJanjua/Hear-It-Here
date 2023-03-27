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

function navBar() {
  let searchBtn = document.querySelector('.searchBtn');
  let closeBtn = document.querySelector('.closeBtn');
  let searchBox = document.querySelector('.searchBox')
  let menuToggle = document.querySelector('.menuToggle');
  let header = document.querySelector('header');

  searchBtn.onclick = function () {
    searchBox.classList.add('active');
    closeBtn.classList.add('active');
    searchBtn.classList.add('active');
    menuToggle.classList.add('hide');
    header.classList.remove('open');
  }

  closeBtn.onclick = function () {
    searchBox.classList.remove('active');
    closeBtn.classList.remove('active');
    searchBtn.classList.remove('active');
    menuToggle.classList.remove('hide');
  }

  menuToggle.onclick = function () {
    header.classList.toggle('open');
    searchBox.classList.remove('active');
    closeBtn.classList.remove('active');
    searchBtn.classList.remove('active');
  }
}

