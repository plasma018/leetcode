/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {number[]} preorder
 * @return {TreeNode}
 */
var bstFromPreorder = function(preorder) {
  let dummy = new TreeNode(Number.MAX_VALUE)
  let queue = []
  queue.push(dummy)
  let root = new TreeNode(preorder[0])
  dummy.left = root
  queue.push(root)
  for (let i = 1; i < preorder.length; i++) {
    let node = new TreeNode(preorder[i])
    let prev = queue.pop()
    let flag = prev
    if (node.val < flag.val) {
      flag.left = node
      queue.push(flag)
      queue.push(node)
      continue
    }

    while (node.val > flag.val) {
      prev = flag
      flag = queue.pop()
    }

    prev.right = node
    queue.push(flag)
    queue.push(node)
  }

  return root
};
