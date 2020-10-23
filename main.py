import numpy as np
from PIL import Image


def evklid(x, y):
    x = np.transpose(x)
    y = np.transpose(y)
    a = np.transpose(x - y)
    b = np.dot(a, np.eye(10))
    c = x - y
    return np.sqrt(np.dot(b, c))


res = []

im = Image.open("3.bmp")
im = np.asarray(im, dtype=np.float64)

ima = Image.open("3a.bmp")
ima = np.asarray(ima, dtype=np.float64)

imb = Image.open("3b.bmp")
imb = np.asarray(imb, dtype=np.float64)

imc = Image.open("3c.bmp")
imc = np.asarray(imc, dtype=np.float64)

core_three = (ima + imb + imc) / 3
print(core_three)

rez_1 = 0

for l1, l2 in zip(im, core_three):
    rez_1 += evklid(l1, l2)
res.append(rez_1)

#########################################

ima = Image.open("4a.bmp")
ima = np.asarray(ima, dtype=np.float64)

imb = Image.open("4b.bmp")
imb = np.asarray(imb, dtype=np.float64)

imc = Image.open("4c.bmp")
imc = np.asarray(imc, dtype=np.float64)

core_four = (ima + imb + imc) / 3
print(core_four)

rez_2 = 0

for l1, l2 in zip(im, core_four):
    rez_2 += evklid(l1, l2)
res.append(rez_2)

#########################################

ima = Image.open("5a.bmp")
ima = np.asarray(ima, dtype=np.float64)

imb = Image.open("5b.bmp")
imb = np.asarray(imb, dtype=np.float64)

imc = Image.open("5c.bmp")
imc = np.asarray(imc, dtype=np.float64)

core_five = (ima + imb + imc) / 3
print(core_five)

rez_3 = 0

for l1, l2 in zip(im, core_five):
    rez_3 += evklid(l1, l2)
res.append(rez_3)

#########################################

ima = Image.open("9a.bmp")
ima = np.asarray(ima, dtype=np.float64)

imb = Image.open("9b.bmp")
imb = np.asarray(imb, dtype=np.float64)

imc = Image.open("9c.bmp")
imc = np.asarray(imc, dtype=np.float64)

core_nine = (ima + imb + imc) / 3
print(core_nine)

rez_4 = 0

for l1, l2 in zip(im, core_nine):
    rez_4 += evklid(l1, l2)
res.append(rez_4)
det = min(res)
idn = res.index(det)

det_dict = {
    0: '3',
    1: '4',
    2: '5',
    3: '9'
}
print(det_dict[idn])
