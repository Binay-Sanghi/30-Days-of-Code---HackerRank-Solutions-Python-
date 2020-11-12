def levelOrder(self,root):
        q = [root]
        for current in q:    
            if current:
                print(current.data,end = " ")
                q.append(current.left)
                q.append(current.right)
