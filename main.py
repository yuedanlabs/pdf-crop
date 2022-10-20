"""
thanks to https://github.com/py-pdf/PyPDF2
refer to https://pypdf2.readthedocs.io/en/latest/user/cropping-and-transforming.html

refer:
    page.mediabox RectangleObject [left, bottom, right, top]
"""

from copy import deepcopy
from itertools import product
from PyPDF2 import PdfWriter, PdfReader

reader = PdfReader("input.pdf")
writer = PdfWriter()

page0 = reader.pages[0]

# split horizontally into 3 equal parts
# divide vertically into 4 equal parts
x, y = (3, 4)

# for j in range(y, 0, -1):
#     for i in range(1, x+1):
#         pagex = deepcopy(reader.pages[0])
#         pagex.mediabox.lower_left = (
#             (page0.mediabox.right / x) * (i - 1),
#             (page0.mediabox.top / y) * (j - 1),
#         )
#         pagex.mediabox.upper_right = (
#             (page0.mediabox.right / x) * i,
#             (page0.mediabox.top / y) * j,
#         )
#         writer.add_page(pagex)

for j, i in product(range(y, 0, -1), range(1, x + 1)):
    # print(i, j)
    pagex = deepcopy(reader.pages[0])
    # lower_left = (left, bottom)
    pagex.mediabox.lower_left = (
        (page0.mediabox.right / x) * (i - 1),
        (page0.mediabox.top / y) * (j - 1),
    )
    # upper_right = (right, top)
    pagex.mediabox.upper_right = (
        (page0.mediabox.right / x) * i,
        (page0.mediabox.top / y) * j,
    )
    writer.add_page(pagex)

with open("output.pdf", "wb") as fp:
    writer.write(fp)
