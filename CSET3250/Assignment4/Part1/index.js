function calculateNumbers() {
  console.log("Calculating numbers");
  let items = [];
  items.push(document.getElementsByClassName("input"));
  console.log(items);
  let total = 0;
  let i = 0;
  items.forEach(element => {
    console.log("i is: " + i);
    console.log(element[i].value);
    total += element[i].value;
    i++;
  });
  console.log(total);
}
