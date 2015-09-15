import { init, reverse, concat, takeWhile, pipe, converge, gte, join, flip, curry, identity } from 'ramda'

const alphabet = 'abcdefghijklmnopqrstuvwxyz'.split('')

// Simple version ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

function diamond(char) {
  const letters = takeWhile(c => char >= c, alphabet)

  const pyramid = letters.map(
    (c, index) => c.repeat(index + 1)
  )

  return concat(init(pyramid), reverse(pyramid)).join('\n')
}

// Ramda only version ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

function pyramid(letters) {
  return letters.map(
    (c, index) => c.repeat(index + 1)
  )
}

const diamondr = pipe(
  identity,
  gte,
  flip(takeWhile)(alphabet),
  pyramid,
  converge(
    concat,
    init,
    reverse
  ),
  join('\n')
)

// Tests ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

const testLetters = ['a', 'c', 'n']

testLetters.forEach(letter => {
  console.log(diamondr(letter))
  console.log('\n')
})
