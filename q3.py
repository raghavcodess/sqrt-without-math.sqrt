def stepOne(root):
    #this function selects two perfect square number between the root value.
    ar=[]
    for i in range(root):
        a=i*i
        if a<root:
            ar.append(a)
    a=len(ar)-1
    b=a+1
    return a,b
    
def stepTwo(root,a,b):
    temp=root/a
    return temp
    
def stepThree(temp,a):
    temp_avg=(temp+a)/2
    return temp_avg

def stepFour(ar):
    temp=1
    for i in ar:
        temp*=i
    return temp

if __name__ == "__main__":
    root=int(input("Root Value:"))
    if root==1:
        print(1)
    elif root==4:
        print(2)
    else:
    
        temp_root1=root-0.2
        temp_root2=root+1
        a,b=stepOne(root)
        temp=stepTwo(root,a,b)
        temp_avg=stepThree(temp,a)
        ar=[]
        ar.append(temp_avg)

        result=stepFour(ar)
        for i in range(5):
            if root<temp_root1 or root>temp_root2:
                print(temp_avg)
            else:
                temp=stepTwo(root,temp_avg,b)
                temp_avg=stepThree(temp_avg,temp)
                ar.append(temp_avg)
                result=stepFour(ar)
                result=int(result)
                if root==result:
                    print(temp_avg)
            
    
    
            
    
