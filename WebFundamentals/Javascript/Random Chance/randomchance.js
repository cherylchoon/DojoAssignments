function randomChance (numQuarters, goal) {
  while (numQuarters >= 0) {
    var bonus = Math.floor(Math.random() * 51 + 50);
    numQuarters--;
    console.log(numQuarters);
    var win = numQuarters + bonus;
    if (Math.trunc(Math.random()*100) === Math.trunc(Math.random()*100)) {
       win;
    }
    else if (numQuarters > goal) {
      console.log(numQuarters);
      break;
    }
    else if (numQuarters === 0) {
      return 0;
    }
  }
}

var winnings = randomChance(100, 150);
console.log(winnings);
