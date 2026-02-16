function sum(...numbers) {
  return numbers;
}

console.log(sum(1, 2, 3, 4));

let [...rest] = [10, 20, 30, 40, 50];

console.log(rest);