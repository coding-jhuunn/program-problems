function sym(...args) {
  const diff = (arr1, arr2) => [
    ...arr1.filter((e) => !arr2.includes(e)),
    ...arr2.filter((e) => !arr1.includes(e)),
  ];
  // reduce function = all the elements of the array to a single value by repeated applying a function

  return [...new Set(args.reduce(diff))];
}

console.log(
  sym([3, 3, 3, 2, 5], [2, 1, 5, 7], [3, 4, 6, 6], [1, 2, 3], [5, 3, 9, 8], [1])
);

// use .... when

// spread operator : expands elements of an iterable
// rest parameter: represents and indefinity number of arguments as an array
