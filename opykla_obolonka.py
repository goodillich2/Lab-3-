#для 4 датасету
from PIL import Image, ImageDraw

s = (960,540)

def r(x, y, z):
  return (y[0]-x[0])*(z[1]-y[1])-(y[1]-x[1])*(z[0]-y[0])

# Алгорітм джарвіса для опуклої оболонки
def jarvis_algoritm(points_1):
    counter = len(points_1)
    n_p = list(range(counter))
    for i in range(1,counter):
        if points_1[n_p[i]][0]<points_1[n_p[0]][0]:
            n_p[i], n_p[0] = n_p[0], n_p[i]
    result = [n_p[0]]
    del n_p[0]
    n_p.append(result[0])
    while True:
        right = 0
        for i in range(1, len(n_p)):
            if r(points_1[result[-1]], points_1[n_p[right]], points_1[n_p[i]]) < 0:
                right = i
        if n_p[right] == result[0]:
            break
        else:
            result.append(n_p[right])
            del n_p[right]
    return result


out = Image.new("RGB", s, (255, 255, 255))
f = open('DS4.txt',"r")
points_1 = f.read().split("\n")
for i in range(len(points_1)-1):
    points_1[i] = points_1[i].split(" ")
    points_1[i][0]=int(points_1[i][0])
    points_1[i][1] = int(points_1[i][1])
    out.putpixel((int(points_1[i][1]), 540 - int(points_1[i][0])), (0, 0, 0))
points = jarvis_algoritm(points_1[:-1])
draw = ImageDraw.Draw(out)
for point in points:
    draw.line([points_1[points[points.index(point)-1]][1], 540 - int(points_1[points[points.index(point)-1]][0]),points_1[point][1], 540 - int(points_1[point][0])], fill="blue")
out.show()
out.save('result.jpg')





