'use strict';


var tinderContainer = document.querySelector('.tinder');
var allCards = document.querySelectorAll('.tinder--card');
var nope = document.getElementById('nope');
var love = document.getElementById('love');
let likedCards = [];
var sum = 0;



function initCards(card, index) {
  var newCards = document.querySelectorAll('.tinder--card:not(.removed)');

  newCards.forEach(function (card, index) {
    card.style.zIndex = allCards.length - index;
    card.style.transform = 'scale(' + (20 - index) / 20 + ') translateY(-' + 30 * index + 'px)';
    card.style.opacity = (10 - index) / 10;
  });
  
  tinderContainer.classList.add('loaded');
}

initCards();

allCards.forEach(function (el) {
  var hammertime = new Hammer(el);

  hammertime.on('pan', function (event) {
    el.classList.add('moving');
  });

  hammertime.on('pan', function (event) {
    if (event.deltaX === 0) return;
    if (event.center.x === 0 && event.center.y === 0) return;

    tinderContainer.classList.toggle('tinder_love', event.deltaX > 0);
    tinderContainer.classList.toggle('tinder_nope', event.deltaX < 0);

    var xMulti = event.deltaX * 0.03;
    var yMulti = event.deltaY / 80;
    var rotate = xMulti * yMulti;

    event.target.style.transform = 'translate(' + event.deltaX + 'px, ' + event.deltaY + 'px) rotate(' + rotate + 'deg)';
  });
const popup = document.getElementById('popup');
  hammertime.on('panend', function (event) {
    el.classList.remove('moving');
    tinderContainer.classList.remove('tinder_love');
    tinderContainer.classList.remove('tinder_nope');

    var moveOutWidth = document.body.clientWidth;
    var keep = Math.abs(event.deltaX) < 80 || Math.abs(event.velocityX) < 0.5;

    event.target.classList.toggle('removed', !keep);

    if (keep) {
      event.target.style.transform = '';
    } else {
      var endX = Math.max(Math.abs(event.velocityX) * moveOutWidth, moveOutWidth);
      var toX = event.deltaX > 0 ? endX : -endX;
      var endY = Math.abs(event.velocityY) * moveOutWidth;
      var toY = event.deltaY > 0 ? endY : -endY;
      var xMulti = event.deltaX * 0.03;
      var yMulti = event.deltaY / 80;
      var rotate = xMulti * yMulti;

      event.target.style.transform = 'translate(' + toX + 'px, ' + (toY + event.deltaY) + 'px) rotate(' + rotate + 'deg)';
      if (event.deltaX > 0) {
      // The card was swiped to the right
        console.log('Liked');
        likedCards.push(event.target.id);
    } else {
      // The card was swiped to the left
      console.log('Disliked');
    }
      initCards();
      var cards = document.querySelectorAll('.tinder--card:not(.removed)');
      // popup.style.opacity = '0';
      // if (cards.length == 0) {
      //   // alert('There are no more cards left!');
      //   // create a popup to show the user that there are no more cards left
      //   popup.style.opacity = '1';
      //   //add transition to the popup
      //   popup.style.transition = 'opacity 5s ease-in-out';
      //   return false;
      // }
      
    }
  });
});
function createButtonListener(love) {
  return function (event) {
    var cards = document.querySelectorAll('.tinder--card:not(.removed)');
    var moveOutWidth = document.body.clientWidth * 1.5;

    popup.style.opacity = '0';
    if (cards.length == 0) {
      // alert('There are no more cards left!');
      //if the last element of liked cards is empty, remove it
      if (likedCards[likedCards.length - 1] == "") {
        likedCards.pop();
      }

      console.log(likedCards);
      console.log("There are no more cards left!");
      //get ascii sum of liked cards

      console.log("the sum is:" + sum);
      
      createPopup();

      // create a popup to show the user that there are no more cards left
      popup.style.opacity = '1';
      //add transition to the popup
      popup.style.transition = 'opacity 3s ease-in-out';
      return false;
    }
    for (var i = 0; i < likedCards.length; i++) {
      for (var j = 0; j < likedCards[i].length; j++) {
        sum += likedCards[i].charCodeAt(j);
      }
    }
    console.log(sum);
    var card = cards[0];

    card.classList.add('removed');

    if (love) {
      card.style.transform = 'translate(' + moveOutWidth + 'px, -100px) rotate(-30deg)';
      likedCards.push(card.id);
      console.log('Liked');
    } else {
      card.style.transform = 'translate(-' + moveOutWidth + 'px, -100px) rotate(30deg)';
      console.log('Disiked');
    }

    initCards();

    event.preventDefault();
  };
}


var nopeListener = createButtonListener(false);
var loveListener = createButtonListener(true);

nope.addEventListener('click', nopeListener);
love.addEventListener('click', loveListener);

function createPopup(){
  //create a popup with the ascii sum
  const popup = document.getElementById('popup');
  //Rap genre
  if (likedCards.includes('nas') && likedCards.includes('kdot')) {
    popup.querySelector('h2').innerHTML = 'Your Genre is: Rap';
    // popup.querySelector('img').src = can add image
    popup.querySelector('p').textContent = 'Rap music is a genre of popular music that originated in the United States in the 1970s. It consists of a stylized rhythmic music that commonly accompanies rapping, which is a rhythmic and rhyming speech that is chanted. You got this because you swiped right on Nas-illmatic and Kendrick Lamar-To Pimp a Butterfly';
  }
  //Quran genre
  else if (likedCards.includes('quran')  ) {
    popup.querySelector('h2').innerHTML = 'Your Genre is: Quran';
    // popup.querySelector('img').src = can add image
    popup.querySelector('p').textContent = 'MashAllah brother! The Quran is the central religious text of Islam, which Muslims believe to be a revelation from God. It is widely regarded as the finest piece of literature in the Arabic language. You got this because you swiped right on the Quran';
  }
  
  if (sum == 1732) {
    popup.querySelector('h2').innerHTML = 'You swept right on all the cards??';
    // popup.querySelector('img').src = can add image
    popup.querySelector('p').textContent = 'Guess you like all types of music!';
  }
 

}
