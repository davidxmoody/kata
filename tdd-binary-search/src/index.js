function defaultCompare(a, b) {
  return b - a
}

function search(array, item, start, end, compare) {
  if (end < start) {
    return -1
  }

  const mid = Math.floor((start + end) / 2)
  const midNum = array[mid]

  const comparisonValue = compare(midNum, item)

  if (comparisonValue === 0) {
    return mid
  }

  if (comparisonValue < 0) {
    return search(array, item, start, mid - 1, compare)
  }

  return search(array, item, mid + 1, end, compare)
}

module.exports = (array, item, compare = defaultCompare) => {
  return search(array, item, 0, array.length - 1, compare)
}
