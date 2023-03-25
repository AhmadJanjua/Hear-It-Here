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