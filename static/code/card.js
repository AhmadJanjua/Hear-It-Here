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
      popup.style.transition = 'opacity 2s ease-in-out';
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
  if (likedCards.length == (allCards.length - 1)) {
    popup.querySelector('h2').innerHTML = 'You swept right on all the cards??';
    popup.querySelector('h3').innerHTML = ' I think you should retry, click the reset button in the middle!';
    // popup.querySelector('img').src = can add image
    popup.querySelector('p').textContent = 'Maybe you like all types of music?';
  }
  else if (likedCards.length == 0) {
    popup.querySelector('h2').innerHTML = 'You didnt swipe right on any cards??';
    popup.querySelector('h3').innerHTML = ' I think you should retry, click the reset button in the middle!';
    // popup.querySelector('img').src = can add image
    popup.querySelector('p').textContent = "Maybe you don't like music?";
  }
  else if (likedCards.includes('week') && likedCards.includes('duke') ) {
    popup.querySelector('h2').innerHTML = 'Your Genre is: R&B / Jazz';
    popup.querySelector('h3').innerHTML = ' You got this because you swiped right on The Weeknd-Kiss Land and Duke Ellington-Duke Ellington & John Coltrane';
    // popup.querySelector('img').src = can add image
    popup.querySelector('p').textContent = 'R&B is a genre of popular music that originated in African-American communities in the 1940s. Jazz is a music genre that originated in African American communities of New Orleans. Kiss Land is The Weeknd’s first studio album, released on September 10, 2013. Duke Ellington was an American composer, pianist, and leader of a jazz orchestra. Some of his most famous albums include Masterpieces by Ellington (1950), Duke Ellington & John Coltrane (1963), and Such Sweet Thunder (1957).';
  }
  else if (likedCards.includes('week') && likedCards.includes('kdot') ) {
    popup.querySelector('h2').innerHTML = 'Your Genre is: R&B / Hip Hop';
    popup.querySelector('h3').innerHTML = ' You got this because you swiped right on The Weeknd-Kiss Land and Kendrick Lamar-To Pimp a Butterfly';
    // popup.querySelector('img').src = can add image
    popup.querySelector('p').textContent = 'R&B/Hip-Hop is a genre of popular music that combines elements of rhythm and blues and hip hop. R&B/Hip-Hop often incorporates smooth melodies and soulful vocals with the rhythmic beats and rap verses of hip hop. Two notable albums in this genre are Kiss Land by The Weeknd and To Pimp a Butterfly by Kendrick Lamar. Kiss Land, released in 2013, explores themes of love, sex, and fear through a blend of R&B and dark wave. To Pimp a Butterfly, released in 2015, is an expansive collage of hip-hop, funk and soul, with jazz firmly affixed to the center.';
  }
  else if (likedCards.includes('week') && likedCards.includes('mj') ) {
    popup.querySelector('h2').innerHTML = 'Your Genre is: R&B / Pop';
    popup.querySelector('h3').innerHTML = ' You got this because you swiped right on The Weeknd-Kiss Land and  Michael Jackson-Thriller';
    // popup.querySelector('img').src = can add image
    popup.querySelector('p').textContent = 'R&B, or rhythm and blues, is a genre of popular music that combines elements of soul, gospel, jazz, and blues. R&B has evolved over time and now often incorporates elements of pop, funk, hip hop, and electronic music. The terms popular music and pop music are often used interchangeably, . Examples of pop music include Michael Jackson’s Thriller, released in 1982, and The Weeknd’s Kiss Land, released in 2013.';
  }
  else if (likedCards.includes('kdot') && likedCards.includes('duke') ) {
    popup.querySelector('h2').innerHTML = 'Your Genre is: Jazz / Hip-Hop';
    popup.querySelector('h3').innerHTML = ' You got this because you swiped right on Kendrick Lamar-To Pimp a Butterfly, and Duke Ellington-Duke Ellington & John Coltrane';
    // popup.querySelector('img').src = can add image
    popup.querySelector('p').textContent = 'Jazz rap is a fusion of jazz and hip hop music that developed in the late 1980s and early 1990s. It is an alternative hip hop subgenre that combines the rhythm of hip hop with jazz instrumentation. Duke Ellington was an American jazz pianist, and ra from 1923 through the rest of his life. He is acknowledged as one of the greatest composers in jazz and his innovative arrangements featured his piano playing against a rich, deep sound. In 2015, rap superstar Kendrick Lamar brought new light to this hybrid with his second major-label album, To Pimp a Butterfly, which was an expansive collage of hip-hop, funk and soul, with jazz firmly affixed to the center.';
  }
  else if (likedCards.includes('mj') && likedCards.includes('duke') ) {
    popup.querySelector('h2').innerHTML = 'Your Genre is: Pop / Jazz';
    popup.querySelector('h3').innerHTML = ' You got this because you swiped right on Micheal Jackson-Thriller and Duke Ellington-Duke Ellington & John Coltrane';
    // popup.querySelector('img').src = can add image
    popup.querySelector('p').textContent = 'Pop is a genre of popular music that originated in the 1950s. It is characterized by its catchy melodies, simple chord progressions, and relatable lyrics. It often incorporates elements from other styles such as rock, dance, hip hop, and country. Jazz is known for its improvisation, swing and blue notes, call and response vocals, polyrhythms, and syncopation. Jazz has roots in blues and ragtime. Two notable albums in this genre are Thriller by Micheal Jackson and Duke Ellington & John Coltrane by Duke Ellington. Pop music is characterized by its catchy melodies, simple chord progressions, and relatable lyrics. It often incorporates elements from other styles such as rock, dance, hip hop, and country.';
  }
  else if (likedCards.includes('sound') && likedCards.includes('duke') ) {
    popup.querySelector('h2').innerHTML = 'Your Genre is: Soundtrack / Jazz';
    popup.querySelector('h3').innerHTML = ' You got this because you swiped right on the Soundtracks and Jazz cards';
    // popup.querySelector('img').src = can add image
    popup.querySelector('p').textContent = 'Soundtrack is a term used for a selection of songs that are featured in a film or other visual media. These songs have become a category of their own, with increasingly high-quality music being composed. Notable soundtracks include "God of War Ragnorok", "Inception", "LA Noire" and "The Road to Perdition". Jazz is a music genre that originated in African American communities of New Orleans. Jazz is known for its improvisation, swing and blue notes, call and response vocals, polyrhythms, and syncopation. Jazz has roots in blues and ragtime.';
  }
  else if (likedCards.includes('mj')  ) {
    popup.querySelector('h2').innerHTML = 'Your Genre is: Pop';
    popup.querySelector('h3').innerHTML = ' You got this because you swiped right on Micheal Jackson-Thriller';
    // popup.querySelector('img').src = can add image
    popup.querySelector('p').textContent = 'The terms “popular music” and “pop music” are often used interchangeably, although the former describes all music that is popular and includes many diverse styles. Pop music is characterized by its catchy melodies, simple chord progressions, and relatable lyrics. It often incorporates elements from other styles such as rock, dance, hip hop, and country.';
  }
  else if (likedCards.includes('nas') || likedCards.includes('kdot')) {
    popup.querySelector('h2').innerHTML = 'Your Genre is: Rap';
    popup.querySelector('h3').innerHTML = ' You got this because you swiped right on Kendrick Lamar-To Pimp a Butterfly, Nas-Illmatic or both!';
    // popup.querySelector('img').src = can add image
    popup.querySelector('p').textContent = 'Rap is a genre of popular music that originated in African American communities in the United States in the 1970s. Nas and Kendrick Lamar are two prominent figures in rap music. Nas’ debut album, Illmatic, released in 1994, is widely regarded as one of the greatest hip-hop albums of all time. Kendrick Lamar’s second major-label album, To Pimp a Butterfly, released in 2015, was an expansive collage of hip-hop, funk and soul, with jazz firmly affixed to the center. Both albums have had a profound impact on the rap genre and continue to be celebrated for their artistry and influence.';
  }
  else if (likedCards.includes('week')  ) {
    popup.querySelector('h2').innerHTML = 'Your Genre is: R & B';
    popup.querySelector('h3').innerHTML = ' You got this because you swiped right on The Weeknd-Kiss Land';
    // popup.querySelector('img').src = can add image
    popup.querySelector('p').textContent = 'R&B, or rhythm and blues, is a genre of popular music that combines elements of soul, gospel, jazz, and blues. R&B has evolved over time and now often incorporates elements of pop, funk, hip hop, and electronic music. R&B lyrical themes often encapsulate the experience of pain and the quest for freedom and joy, as well as triumphs and failures in terms of relationships, economics, and aspirations. The genre is known for its smooth melodies and soulful vocals.';
  }
  else if (likedCards.includes('duke')  ) {
    popup.querySelector('h2').innerHTML = 'Your Genre is: Jazz';
    popup.querySelector('h3').innerHTML = ' You got this because you swiped right on Duke Ellington-Duke Ellington & John Coltrane';
    // popup.querySelector('img').src = can add image
    popup.querySelector('p').textContent = 'Jazz is a music genre that makes heavy use of improvisation, polyrhythms, syncopation, and the swung note.  Jazz makes heavy use of improvisation, polyrhythms, syncopation, and the swung note. Jazz has evolved to incorporate elements from many other genres and has a rich history of innovation and experimentation.';
  }
  else if (likedCards.includes('sound')  ) {
    popup.querySelector('h2').innerHTML = 'Your Genre is: Soundtracks';
    popup.querySelector('h3').innerHTML = ' You got this because you swiped right on the Soundtracks card';
    // popup.querySelector('img').src = can add image
    popup.querySelector('p').textContent = 'Soundtrack is a term used for a selection of songs that are featured in a film or other visual media. These songs have become a category of their own, with increasingly high-quality music being composed. Notable soundtracks include "God of War Ragnorok", "Inception", "LA Noire" and "The Road to Perdition".';
  }

  

 

}
