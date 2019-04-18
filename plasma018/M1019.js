/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode} head
 * @return {number[]}
 */

let nextLargerNodes = function (head) {
  let answer = []
  let remain = []
  let index = 0
  let next
  while (head !== null) {
    next = head.next
    if (next && next.val > head.val) {
      answer[index] = head.next.val

      for (let i = remain.length - 1; i > -1; i--) {
        if (answer[remain[i]] >= next.val) {
          break
        }
        answer[remain[i]] = next.val
        remain.pop()
      }
    } else {
      answer[index] = head.val
      remain.push(index)
    }

    head = head.next
    index += 1
  }

  for (let i = 0; i < remain.length; i++) {
    answer[remain[i]] = 0
  }
  answer[answer.length - 1] = 0
  return answer
}
