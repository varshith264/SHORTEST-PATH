import turtle
from collections import deque

grid = [
"+++++++++++++++++++++++++++++s+++++++++++++++++++++",
"+               +                                 +",
"+  ++++++++++  +++++++++++++   +++++++  +++++++++++",
"+          +             +    +               ++  +",
"+  +++++++  +++++++++++++  +++++++++++++++++++++  +",
"+  +     +  +           +  +                 +++  +",
"+  +  +  +  +  +  ++++  +  +  +++++++++++++  +++  +",
"+  +  +  +  +  +  +        +  +  +        +       +",
"+  +  ++++  +  ++++++++++  +  +  ++++  +  +  ++   +",
"+  +     +  +          +   +           +  +  ++  ++",
"+  ++++  +  +++++++ ++++++++  +++++++++++++  ++  ++",
"+     +  +     +              +              ++   +",
"++++  +  ++++++++++ +++++++++++  ++++++++++  +++  +",
"+  +  +                    +     +     +  +  +++  +",
"+  +  ++++  +++++++++++++  +  ++++  +  +  +  ++   +",
"+  +  +     +     +     +  +  +     +     +  ++  ++",
"+  +  +  +++++++  ++++  +  +  +  ++++++++++  ++  ++",
"+                       +  +  +              ++  ++",
"+ ++++++             +  +  +  +  +++        +++  ++",
"+ ++++++ ++++++ +++++++++    ++ ++   ++++++++++  ++",
"+ +    +    +++ +     +++++++++ ++  +++++++    + ++",
"+ ++++ ++++ +++ + +++ +++    ++    ++    ++ ++ + ++",
"+ ++++    +     + +++ +++ ++ ++++++++ ++ ++ ++   ++",
"+      ++ +++++++e+++     ++          ++    +++++++",
"+++++++++++++++++++++++++++++++++++++++++++++++++++",
 ]
#you can change the starting and ending point of the route in grid but dont forget to remove the previous locations 
start=[0,29]                  
for x in range(25):
    for y in range(51):
        if(grid[x][y]=='s'):
            start[0]=x
            start[1]=y

def drawsquare(b,a,col):
    b=b*(-1)
    t.speed(100000)
    t.up()
    t.goto(a,b)
    t.down()
    t.begin_fill()
    t.fillcolor(col)
    for i in range(4):
        t.forward(10) 
        t.left(90)
    t.end_fill()

def clickstart(x,y):
    start[0]=x
    start[1]=y

def valid(st):
    i=start[0]
    j=start[1]
    for t in st:
        if(t=='L'):
            j-=1
        elif(t=='U'):
            i-=1
        elif(t=='D'):
            i+=1
        else :
            j+=1
    if(( i>=0 and j>=0) and (i<25 and j<51)):
        
        if(grid[i][j]=='e'):
            return [1,i,j]
        elif(grid[i][j]==' '):
            return [0,i,j]
    return [2,i,j]
    
    

visited=[[0 for i in range(51)] for j in range(25) ]
flag=1
possible_dir_right_now=['U','D','L','R']
x=deque()
for i in possible_dir_right_now:
    cur=valid(i)
    if(cur[0]==0):
        x.append(i)

end=[0,0]
answer=""
while(len(x)!=0 and flag==1):
    latest=x.popleft()
    for i in possible_dir_right_now :
        current=latest+i
        cur_list=valid(current)
        if(cur_list[0]==1):
            visited[cur_list[1]][cur_list[2]]=1
            answer=current
            flag=0
            break
        elif (cur_list[0]==0 and visited[cur_list[1]][cur_list[2]]==0):
            x.append(current)
            visited[cur_list[1]][cur_list[2]]=1

p=start[0]
q=start[1]
gridd=[[0 for i in range(51)] for j in range(25) ]
for i in range (25):
    for j in range(51):
        if(grid[i][j]=='+'):
            gridd[i][j]='+'
        else :
            gridd[i][j]=' '
for i in answer:
    if(i=='L'):
        gridd[p][q-1]='_'
        q=q-1
    elif(i=='R'):
        gridd[p][q+1]='_'
        q=q+1
    elif(i=='D'):
       gridd[p+1][q]='_'
       p=p+1
    elif(i=='U'):
       gridd[p-1][q]='_'
       p=p-1

t=turtle.Turtle()
#draws initial grid on the screen and black colour square represents a wall
#orange represents starting point
#red represents ending point
for xc in range(25):
    for yc in range(51):
        if(grid[xc][yc]=='+'):
            drawsquare((xc-12)*10,(yc-25)*10,"black")
        elif(grid[xc][yc]=='s'):
            drawsquare((xc-12)*10,(yc-25)*10,"orange")
            continue
        elif(grid[xc][yc]=='e'):
            drawsquare((xc-12)*10,(yc-25)*10,"red")

            
#drawing the shortest path using green

p=start[0]
q=start[1]
for i in answer:
    if(i=='L'):
        drawsquare((p-12)*10,(q-1-25)*10,"green")
        q=q-1
    elif(i=='R'):
        drawsquare((p-12)*10,(q+1-25)*10,"green")
        q=q+1
    elif(i=='D'):
       drawsquare((p+1-12)*10,(q-25)*10,"green")
       p=p+1
    elif(i=='U'):
       drawsquare((p-1-12)*10,(q-25)*10,"green")
       p=p-1
    
  
