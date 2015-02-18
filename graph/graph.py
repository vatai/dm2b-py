from graphics import *
from math import *
from time import sleep

win_width = 400
win_height = 400
r=100
dotr = 10

def main():
    global win
    win = GraphWin("My Graph", win_width, win_height)

    g = [
        [0,1],   # 0
        [1,2],   # 1
        [0],     # 2
        [1,2],   # 3
        [4,3,0], # 4
        [5],     # 5
        [5]      # 6
    ]
    n = len(g)
    draw_graph(g)

    p1 = get_vertex_point(3,n)
    p2 = get_vertex_point(4,n)
    line = Line(p1,p2)
    line.setOutline("red")
    line.draw(win)
    draw_vertices([1,2,3],n,"green")

    sleep(2)
    #win.getMouse()
    win.close()

def get_vertex_coords(i,n,c):
    arg=2.*pi*i/n
    x=win_width/2+r*c*cos(arg)
    y=win_height/2+r*c*sin(arg)
    return (x,y)

def get_vertex_point(i,n):
    return Point(*get_vertex_coords(i,n,1))

def get_loop_point(i,n):
    return Point(*get_vertex_coords(i,n,1.2))

def draw_vertices(v,n,color='white'):
    for i in v:
        p = get_vertex_point(i,n)
        c= Circle(p,dotr)
        c.setFill(color)
        c.draw(win)
        Text(p,str(i)).draw(win)
        
def draw_edges(g):
    n = len(g)
    loopr = 20
    for i in range(n):
        for j in g[i]:
            if i != j:
                p1=get_vertex_point(i,n)
                p2=get_vertex_point(j,n)
                Line(p1,p2).draw(win)
            else:
                c = Circle(get_loop_point(i,n),loopr)
                c.draw(win)


def draw_graph(g):
    n = len(g)
    draw_edges(g)
    draw_vertices(range(n),n,'white')

main()

