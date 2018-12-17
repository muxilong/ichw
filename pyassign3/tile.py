def main():
#思路是这样的
#按照 0，1，2，....的顺序将每个方格扫描一遍
#如果将一个方格作为一块砖最左下角的方格，可以放下一块砖（这时可能有横向和纵向两种铺法），就铺进去
#如果这个方格已经被前面的砖覆盖，就跳过这个方格
#如果这个方格能铺的两种形式的砖都会与前面的砖有重合的方格，程序就会往回走，去判断其他的铺砖方式
#方法的合理性：
#每一种铺法下的所有砖，都有它最左下角的那个方格
#这个程序的目的，就是通过遍历每一个方格，找到所有左下角方格
    def change(x):
    # x代表每个格子的位置，这个函数的作用是求出x的横坐标和纵坐标
        t = []
        t.append(x%m)
        t.append(x//m)
        return t

    def brick(u,v,x):
    # 这个函数的作用是创建一个列表，列表里面是一块砖占的方格
    # u，v是砖的长、宽或宽、长
        brick = []
        for i in range(u):
            for j in range(v):
                brick.append(x + i + m * j)
        return brick

    def judgebrick(u,v,x,p):
    # 这个函数的作用是判断能不能放的下一块砖
    # 其中，p表示已经放入的砖的数目
        if (change(x)[0]+u-1) >= m or (change(x,)[1]+v-1) >= n:
            return False
    #判断这个砖是否超出了墙的边界
        for i in brick(u,v,x):
            for j in range(p):
                if i in solution[j]:
                    return False
    #solution表示一种铺砖方法，判断这块新的砖中的方格是否与前面的砖重合
        return True
   
    def conflict(x,p,solution):
    # 这个函数的作用是判断这个方格是不是已经被前面铺过的砖覆盖了    
        for i in range(p):
            if x in solution[i]:
                return True
        return False



    def solve(x,p):
        if p == m*n//(a*b):
            print(solution)
            allsolution.append(solution[:])
        else:
        
            if conflict(x,p,solution):
        #如果这个方格已经被铺过，就看下一个方格
                solve(x+1,p)
            if not conflict(x,p,solution):
                if judgebrick(a,b,x,p):
        #如果能铺的下一块砖，就铺进去
                    solution[p] = brick(a,b,x)
                    solve(x+1,p+1)
                if judgebrick(b,a,x,p):
                    solution[p] = brick(b,a,x)
                    solve(x+1,p+1)
    m = int(input('write down the lenth of the tile: '))
    n = int(input('write down the wedth of the tile: '))
    a = int(input('write down one lenth of the brick: '))
    b = int(input('write down another lenth of the brick: '))
    solution = [0 for i in range(m*n//(a*b))]
    allsolution = []
    solve(0,0)  
    
            
    import turtle as mxl
    print('总方法数='+str(len(allsolution)))
    num = mxl.numinput('decide on which filling approach you wanna see',\
        'ranging from 1-'+str(len(allsolution)),1,minval=1,maxval=len(allsolution))
    k = int(num)
    #下面首先画出边界
    mxl.speed(0)
    mxl.penup()
    mxl.goto(-m*30,-n*30)
    mxl.pendown()
    mxl.pensize(6)
    for i in range(2):
        mxl.fd(m*60)
        mxl.lt(90)
        mxl.fd(n*60)
        mxl.lt(90)
    #画出横线和竖线
    mxl.lt(90)
    mxl.pensize(0)
    mxl.color('blue')
    for i in range(1,m):
        mxl.penup()
        mxl.goto(-m*30+60*i,-n*30)
        mxl.pendown()
        mxl.fd(n*60)
    mxl.rt(90)
    for i in range(1,n):
        mxl.penup()
        mxl.goto(-m*30,-n*30+60*i)
        mxl.pendown()
        mxl.fd(m*60)
    # 画出数字
    mxl.pensize(2)
    for i in range(m):
        for j in range(n):
            mxl.penup()
            mxl.goto(i*60+30-m*30,j*60+30-n*30)
            mxl.pendown()
            mxl.write(i+m*j)
    # 画砖
    mxl.color('black')
    mxl.pensize(4)
    for element in allsolution[k-1]:
        element.sort()
    
        x1 = change(element[0])[0]
        y1 = change(element[0])[1]
        x2 = change(element[-1])[0]
        y2 = change(element[-1])[1]
        mxl.penup()
    #依次走到砖的四个顶点
        mxl.goto(x1*60-m*30,y1*60-n*30)
        mxl.pendown()
        mxl.goto(x2*60+60-m*30,y1*60-n*30)
        mxl.goto(x2*60+60-m*30,y2*60+60-n*30)
        mxl.goto(x1*60-m*30,y2*60+60-n*30)
        mxl.goto(x1*60-m*30,y1*60-n*30)
    
    turtle.done()        
if __name__ == '__main__':
    main()
        
        
