class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        if p is None and q is None:
            return True
        if q is None: return None
        if p is None: return None
        if p is not None and q is not None:
            queue_p, queue_q = [], []
            queue_p.append(p)
            queue_q.append(q)
            res_p, res_q = [], []
            while len(queue_p) > 0 and len(queue_q) > 0:
                node_p = queue_p.pop(0)
                node_q = queue_q.pop(0)
                if node_p is not None:
                    res_p.append(node_p.val)
                    if node_p.left:
                        queue_p.append(node_p.left)
                    else:
                        queue_p.append(None)
                    if node_p.right:
                        queue_p.append(node_p.right)
                    else:
                        queue_p.append(None)
                else:
                    res_p.append(None)
                if node_q is not None:
                    res_q.append(node_q.val)
                    if node_q.left:
                        queue_q.append(node_q.left)
                    else:
                        queue_q.append(None)
                    if node_q.right:
                        queue_q.append(node_q.right)
                    else:
                        queue_q.append(None)
                else:
                    res_q.append(None)
            print(res_p, res_q)
            if res_p == res_q:
                return True
            else:
                return False
