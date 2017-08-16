const {expect} = require("chai")
const search = require("../src/index")

describe("binary search", () => {
  it("return -1 for empty array", () => {
    expect(search([], 1)).to.eql(-1)
  })

  it("should return 0 for single item", () => {
    expect(search([1], 1)).to.eql(0)
  })

  it("should find an index in a longer array", () => {
    const arr = [1, 4, 6, 9, 10, 11, 12]

    expect(search(arr, 6)).to.eql(2)
    expect(search(arr, 12)).to.eql(6)
  })
})
