const {expect} = require("chai")
const calc = require("../src")

describe("string calculator", () => {
  it("should return 0 for an empty string", () => {
    expect(calc("")).to.eql(0)
  })

  it("should return the value of a number", () => {
    expect(calc("5")).to.eql(5)
  })

  it("should return the sum of two comma separated numbers", () => {
    expect(calc("3,6")).to.eql(9)
  })

  it("should return the sum of more than two numbers", () => {
    expect(calc("1,2,3,4,5,6")).to.eql(21)
  })

  it("should work for new lines too", () => {
    expect(calc("3\n6")).to.eql(9)
  })

  it("should work for a mix of new lines and commas", () => {
    expect(calc("4\n2,1")).to.eql(7)
  })

  it("should allow customizable delimiters", () => {
    expect(calc("//x\n1x2")).to.eql(3)
    expect(calc("//;\n1;2;3")).to.eql(6)
  })

  it("should allow customizable delimiters with no numbers", () => {
    expect(calc("//;\n")).to.eql(0)
  })

  it("should throw an error for negative numbers", () => {
    expect(() => calc("-1,4,6,-2")).to.throw("Negatives not allowed: -1, -2")
  })
})
