var numQuarters = 60;
function randomChance (numQuarters) {
  while (numQuarters >= 0) {
    var bonus = Math.floor(Math.random() * 51 + 50);
    numQuarters--;
    var win = numQuarters + bonus;
    if (Math.trunc(Math.random()*100) === Math.trunc(Math.random()*100)) {
      return win;
    }
    if (numQuarters === 0) {
      return 0;
    }
  }
}

var winnings = randomChance(numQuarters);
console.log(winnings);
