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
  let root = new TreeNode(preorder[0])
  let queue = []
  queue.push(root)
  let i
  for (i = 1; i < preorder.length; i++) {
    if (preorder[i] > root.val) {
      break
    }
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

  queue = []
  queue.push(root)

  for (; i < preorder.length; i++) {
    let node = new TreeNode(preorder[i])
    let prev = queue.pop()
    let flag = prev
    if (node.val < flag.val) {
      flag.left = node
      queue.push(flag)
      queue.push(node)
      continue
    }

    while (flag !== root && node.val > flag.val) {
      prev = flag
      flag = queue.pop()
    }

    prev.right = node
    queue.push(flag)
    queue.push(node)
  }

  return root
};
