if __name__ == '__main__':
    N = int(input())
    
    temp=[] # make an empty list
    for _ in range(N):
        
        commands = input().strip().split() 
        # separate input immediately -> ex) command / value / value
        command = commands[0] # command
        args = commands[1:] # one or more
        
        
        if command == "insert":
            p, value = map(int, args)
            temp.insert(p, value) # insert value at position at p
        
        elif command == "print":
            print(temp) 
             
        elif command == "remove":
            value = int(args[0])
            temp.remove(value) # remove first occurence of value
            
        elif command == "append":
            value = int(args[0])
            temp.append(value) # add value at the end of list
        
        elif command == "sort":
            temp.sort() # sort the list
        
        elif command == "pop":
            temp.pop() # pop the last element from the list
            
        elif command == "reverse":
            temp.reverse() # reverse the list
