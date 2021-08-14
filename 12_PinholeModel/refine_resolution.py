import os
import cv2

# fps = [os.path.join('chessboard', f) for f in os.listdir('chessboard')]
# for fp in fps:
#     X = cv2.imread(fp)
#     h, w = X.shape[:2]
#     print(h, w, h/4, w/4)
#     X = cv2.resize(X, (int(h/4), int(w/4)))
#     cv2.imwrite(fp.replace('.png', '_resize.png'), X)