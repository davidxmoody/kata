function parse(input) {
  return parseInt(input, 10)
}

function isNegative(number) {
  return number < 0
}

function sum(numbersArray) {
  return numbersArray.reduce((a, b) => a + b)
}

function throwIfContainsNegatives(numbersArray) {
  const negativeNumbers = numbersArray.filter(isNegative)

  if (negativeNumbers.length) {
    throw new Error(`Negatives not allowed: ${negativeNumbers.join(", ")}`)
  }
}

module.exports = (inputString) => {
  let delimiter = /,|\n/g
  const delimiterRegex = /^\/\/(.)\n/

  const delimiterMatch = delimiterRegex.exec(inputString)

  if (delimiterMatch) {
    delimiter = delimiterMatch[1]
    inputString = inputString.replace(delimiterRegex, "")
  }

  if (inputString === "") {
    return 0
  }

  const numbersArray = inputString.split(delimiter).map(parse)

  throwIfContainsNegatives(numbersArray)

  return sum(numbersArray)
}

// Notes:
// - I jumped straight from 1 number to n numbers (skipping two numbers) and
//   also did not initially write a test for 3+ numbers
// - When implementing new line split, I didn't write the test first
// - Not sure how many (if any) defensive test cases I should be writing
// - Could have probably used some more refactoring around the delimiter stuff
//   but I got a bit lazy towards the end
