import cv2

img = cv2.imread("image.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

x = 70
s = (x / gray.shape[1]) / 2
y = int(s * gray.shape[0])
gray = cv2.resize(gray, (x,y))

mode = input("0- темный фон, 1- светлый фон:")

if mode == "1":
    for i in range(len(gray)):
        for j in range(len(gray[i])):
            if 0 <= gray[i][j] < 25:
                print('◙', end="")
            elif 25 <= gray[i][j] < 50:
                print('◘', end="")
            elif 50 <= gray[i][j] < 75:
                print('▲', end="")
            elif 75 <= gray[i][j] < 100:
                print('♦', end="")
            elif 100 <= gray[i][j] < 125:
                print('#', end="")
            elif 125 <= gray[i][j] < 150:
                print('%', end="")
            elif 150 <= gray[i][j] < 175:
                print('!', end="")
            elif 175 <= gray[i][j] < 200:
                print('•', end="")
            elif 200 <= gray[i][j] < 225:
                print('.', end="")
            elif 225 <= gray[i][j] <= 255:
                print(' ', end="")
        print()
else:
    for i in range(len(gray)):
        for j in range(len(gray[i])):
            if 0 <= gray[i][j] < 25:
                print(' ', end="")
            elif 25 <= gray[i][j] < 50:
                print('.', end="")
            elif 50 <= gray[i][j] < 75:
                print('•', end="")
            elif 75 <= gray[i][j] < 100:
                print('!', end="")
            elif 100 <= gray[i][j] < 125:
                print('%', end="")
            elif 125 <= gray[i][j] < 150:
                print('#', end="")
            elif 150 <= gray[i][j] < 175:
                print('♦', end="")
            elif 175 <= gray[i][j] < 200:
                print('▲', end="")
            elif 200 <= gray[i][j] < 225:
                print('◘', end="")
            elif 225 <= gray[i][j] <= 255:
                print('◙', end="")
        print()
