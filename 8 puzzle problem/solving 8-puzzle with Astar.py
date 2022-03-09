import copy

def poscheck(initial):
    for i in range(0,3):
         for j in range(0,3):
                if initial[i][j]==0:
                    pos = (i,j)
    return pos

def heuristic(initial, final):
                h = 0 #heuristic initial value
                for i in range(0,3):
                    for j in range(0,3):
                        if initial[i][j] != final[i][j]:
                            h = h+1
                return h

class Pattern():
    
    def __init__(self, parent=None, matrix = None, previous=None):
        self.parent = parent
        self.matrix  = matrix    
        self.zero_pos = poscheck(self.matrix)
        self.g = 0
        self.h = 0
        self.f = 0
        
    def __eq__(self, other):
        return self.matrix == other.matrix
    
def astar(start, end):
    start_pattern = Pattern(None, start)
    start_pattern.parent = start_pattern
    start_pattern.g = start_pattern.h = start_pattern.f = 0
    end_pattern = Pattern(None, end)
    end_pattern.g = end_pattern.h = end_pattern.f = 0
    
    open_list = []
    closed_list = []
    
    open_list.append(start_pattern)
    
    while len(open_list)>0:
        
        current_pattern = open_list[0]
        current_index = 0
        
        for index, item in enumerate(open_list):
            if item.f < current_pattern.f:
                current_pattern = item
                current_index = index

        open_list.pop(current_index)    
        closed_list.append(current_pattern)

        #print(current_pattern.matrix)
        #print("current pattern\n")
        #for line in current_pattern.matrix:
        #    print ('  '.join(map(str, line)))               #for debugging
        #print("\n")
        
        if current_pattern == end_pattern:
            path = []
            current = current_pattern
            while current is not start_pattern:
                path.append(current.matrix)
                current = current.parent
            return path[::-1]
        
        
        children = []
        for new_position in [(0,-1),(0,1),(-1,0),(1,0)]:
            
            node_position = (current_pattern.zero_pos[0] + new_position[0], current_pattern.zero_pos[1] + new_position[1])
            
            if node_position[0] > 2 or node_position[0] < 0 or node_position[1] > 2 or node_position[1] < 0:
                continue
            
            #f current_pattern.parent != None:
            if node_position[0] == current_pattern.parent.zero_pos[0] and node_position[1] == current_pattern.parent.zero_pos[1]:
                continue
                                                                                 
            new_matrix = copy.deepcopy(current_pattern.matrix)
            new_matrix[node_position[0]][node_position[1]] = 0
            new_matrix[current_pattern.zero_pos[0]][current_pattern.zero_pos[1]] = current_pattern.matrix[node_position[0]][node_position[1]]
                
            new_pattern = Pattern(current_pattern, new_matrix)
            #print(new_pattern.matrix)
            #print("child")
            #for line in new_pattern.matrix:
            #    print ('  '.join(map(str, line)))               #for debugging
            #print("\n")
            
            children.append(new_pattern)
            
        for child in children:
            
            child.g = current_pattern.g +1   
            child.h = heuristic(child.matrix, end_pattern.matrix)           
            #child.h = ((child.position[0] - end_node.position[0])**2) + ((child.position[1] - end_node.position[1])**2)
            child.f = child.g + child.h
            
            
        for child in children:                     #remove all child nodes which are already visited i.e. closed_list
            flag = False
            for item in closed_list:
                if (item == child):
                    flag = True
                    break
            if flag == True:
                continue 
        
            for item in open_list:
                if item == child and item.g <= child.g:
                    flag = True
                    break
            if flag == False:
                open_list.append(child)
        

def main():
    
    start = [[6, 2, 8],
               [3, 7, 1],
               [5, 4, 0]]      
    
    end = [[1,2,3],
        [4,5,6],
        [7,8,0]]
    
    path = astar(start, end)
    for i in range(0,len(path)):
        print(i,"\n")
        for line in path[i]:
            print ('  '.join(map(str, line)))
        print("\n\n")
    
if __name__ == '__main__':
    main()