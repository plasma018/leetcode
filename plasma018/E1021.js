let removeOuterParentheses = function (S) {
  let flag = 0
  let char
  let answer = ''
  for (let i = 0; i < S.length; i++) {
    char = S.charAt(i)
    if (char === '(') {
      flag += 1
    } else if (char === ')') {
      flag -= 1
    }

    if ((flag === 1 && char === '(') || (flag === 0 && char === ')')) {
      continue
    }
    answer += char
  }
  return answer
}
