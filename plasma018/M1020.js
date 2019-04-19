/**
 * @param {number[][]} A
 * @return {number}
 */
var numEnclaves = function (A) {
  const row = A.length - 1
  const column = A[0].length - 1
  const status = []
  for (let i = 0; i <= row; i++) {
    let c = []
    for (let j = 0; j <= column; j++) {
      c[j] = false
    }
    status[i] = c
  }

  function help (A, status, i, j) {
    if (status[i][j]) {
      return 0
    }

    if (A[i][j] !== 1) {
      return A[i][j]
    }
    status[i][j] = true
    let up = help(A, status, i - 1, j)
    let left = help(A, status, i, j - 1)
    let right = help(A, status, i, j + 1)
    let down = help(A, status, i + 1, j)

    if (right === -1 || down === -1 || up === -1 || left === -1) {
      A[i][j] = -1
      return A[i][j]
    }
    return right + down + 1 + up + left
  }

  let sum = 0

  for (let i = 0; i <= row; i++) {
    if (A[i][0] === 1) {
      A[i][0] = -1
    }

    if (A[i][column] === 1) {
      A[i][column] = -1
    }
  }

  for (let i = 0; i <= column; i++) {
    if (A[0][i] === 1) {
      A[0][i] = -1
    }

    if (A[row][i] === 1) {
      A[row][i] = -1
    }
  }

  for (let i = 1; i < row; i++) {
    for (let j = 1; j < column; j++) {
      if (A[i][j] === 1) {
        let area = help(A, status, i, j)
        if (area < 1) {
          continue
        }
        sum += area
      }
    }
  }
  return sum
}

const A = [
  [0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1],
  [1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0],
  [0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0],
  [1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1],
  [0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0],
  [1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1],
  [0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0],
  [0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0],
  [1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0],
  [1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1]]

console.log(numEnclaves(A))
