function time(hour, minute, period) {
if (minute < 30) {
  minute = "just after";
}

else {
  minute = "almost";
}

if (period === "AM") {
  period = "morning";
}

else {
  period = "evening";
}
console.log("It's", minute, hour, "in the", period)
}

time(10,35,"PM");
