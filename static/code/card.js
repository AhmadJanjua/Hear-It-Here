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

      
      createPopup();

      // create a popup to show the user that there are no more cards left
      popup.style.opacity = '1';
      //add transition to the popup
      popup.style.transition = 'opacity 4s ease-in-out';
      return false;
    }
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
  if (likedCards.length == 4) {
    popup.querySelector('h2').innerHTML = 'You swept right on all the cards??';
    popup.querySelector('h3').innerHTML = ' I think you should retry, click the reset button in the middle!';
    // popup.querySelector('img').src = can add image
    popup.querySelector('p').textContent = 'Maybe you like all types of music!';
  }
  else if (likedCards.length == 0) {
    popup.querySelector('h2').innerHTML = 'You didnt swipe right on any cards??';
    popup.querySelector('h3').innerHTML = ' I think you should retry, click the reset button in the middle!';
    // popup.querySelector('img').src = can add image
    popup.querySelector('p').textContent = "Maybe you don't like music?";
  }
  else if (likedCards.includes('nas') && likedCards.includes('kdot') && likedCards.includes('duke') ) {
    popup.querySelector('h2').innerHTML = 'Your Genre is: Jazz / Hip-Hop';
    popup.querySelector('h3').innerHTML = ' You got this because you swiped right on Kendrick Lamar-To Pimp a Butterfly, and Duke Ellington-Duke Ellington & John Coltrane';
    // popup.querySelector('img').src = can add image
    popup.querySelector('p').textContent = 'Jazz rap is a fusion of jazz and hip hop music that developed in the late 1980s and early 1990s. It is an alternative hip hop subgenre that combines the rhythm of hip hop with jazz instrumentation. Duke Ellington was an American jazz pianist, and ra from 1923 through the rest of his life. He is acknowledged as one of the greatest composers in jazz and his innovative arrangements featured his piano playing against a rich, deep sound. In 2015, rap superstar Kendrick Lamar brought new light to this hybrid with his second major-label album, To Pimp a Butterfly, which was an expansive collage of hip-hop, funk and soul, with jazz firmly affixed to the center.';
  }
  else if (likedCards.includes('nas') && likedCards.includes('kdot')) {
    popup.querySelector('h2').innerHTML = 'Your Genre is: Rap';
    popup.querySelector('h3').innerHTML = ' You got this because you swiped right on Kendrick Lamar-To Pimp a Butterfly, and Nas-Illmatic';
    // popup.querySelector('img').src = can add image
    popup.querySelector('p').textContent = 'Rap is a genre of popular music that originated in African American communities in the United States in the 1970s. Nas and Kendrick Lamar are two prominent figures in rap music. Nas’ debut album, Illmatic, released in 1994, is widely regarded as one of the greatest hip-hop albums of all time. Kendrick Lamar’s second major-label album, To Pimp a Butterfly, released in 2015, was an expansive collage of hip-hop, funk and soul, with jazz firmly affixed to the center. Both albums have had a profound impact on the rap genre and continue to be celebrated for their artistry and influence.';
  }
  //Quran genre
  else if (likedCards.includes('quran')  ) {
    popup.querySelector('h2').innerHTML = 'Your Genre is: Quran';
    popup.querySelector('h3').innerHTML = ' You got this because you swiped right on the Quran';
    // popup.querySelector('img').src = can add image
    popup.querySelector('p').textContent = 'MashAllah brother! The Quran is the central religious text of Islam, which Muslims believe to be a revelation from God. It is widely regarded as the finest piece of literature in the Arabic language.';
  }
  

 

}
