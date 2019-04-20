import cv2
import numpy as np


def drawMatchesKnn_cv2_1(img1_gray, kp1, img2_gray, kp2, goodMatch):
    # print goodMatch
    h1, w1 = img1_gray.shape[:2]
    h2, w2 = img2_gray.shape[:2]

    # vis = np.zeros((max(h1, h2), w1 + w2, 3), np.uint8)
    # vis[:h1, :w1] = img1_gray
    # vis[:h2, w1:w1 + w2] = img2_gray
    vis = np.zeros((h1+h2, max(w1 , w2), 3), np.uint8)
    vis[:h1, :w1] = img1_gray
    vis[h1:h1+h2,:w2] = img2_gray

    p1 = [kpp.queryIdx for kpp in goodMatch]
    p2 = [kpp.trainIdx for kpp in goodMatch]
    # print p1
    # print p2

    # post1 = np.int32([kp1[pp].pt for pp in p1])
    # post2 = np.int32([kp2[pp].pt for pp in p2]) + (w1, 0)

    post1 = np.int32([kp1[pp].pt for pp in p1])
    post2 = np.int32([kp2[pp].pt for pp in p2]) + (0, h1)

    for (x1, y1), (x2, y2) in zip(post1, post2):
        cv2.line(vis, (x1, y1), (x2, y2), (0, 0, 255))

    # res = cv2.resize(vis, (600, 2000), interpolation=cv2.INTER_AREA)
    # cv2.namedWindow("match", cv2.WINDOW_NORMAL)
    # cv2.imshow("match", vis)
    cv2.imwrite("/Users/zrain/Desktop/scshot/unsame/picCCCC.png",vis)

def drawMatchesKnn_cv2(img1_gray, kp1, img2_gray, kp2, goodMatch):
    # print goodMatch
    h1, w1 = img1_gray.shape[:2]
    h2, w2 = img2_gray.shape[:2]

    vis = np.zeros((max(h1, h2), w1 + w2, 3), np.uint8)
    vis[:h1, :w1] = img1_gray
    vis[:h2, w1:w1 + w2] = img2_gray
    # vis = np.zeros((h1+h2, max(w1 , w2), 3), np.uint8)
    # vis[:h1, :w1] = img1_gray
    # vis[h1:h1+h2,:w2] = img2_gray

    p1 = [kpp.queryIdx for kpp in goodMatch]
    p2 = [kpp.trainIdx for kpp in goodMatch]
    # print p1
    # print p2

    post1 = np.int32([kp1[pp].pt for pp in p1])
    post2 = np.int32([kp2[pp].pt for pp in p2]) + (w1, 0)

    # post1 = np.int32([kp1[pp].pt for pp in p1])
    # post2 = np.int32([kp2[pp].pt for pp in p2]) + (h1, 0)

    for (x1, y1), (x2, y2) in zip(post1, post2):
        cv2.line(vis, (x1, y1), (x2, y2), (0, 0, 255))

    # res = cv2.resize(vis, (600, 2000), interpolation=cv2.INTER_AREA)
    # cv2.namedWindow("match", cv2.WINDOW_NORMAL)
    # cv2.imshow("match", vis)
    cv2.imwrite("/Users/zrain/Desktop/scshot/same/picAAAA.png",vis)


img1_gray = cv2.imread("/Users/zrain/Desktop/scshot/unsame/picC.png")
img2_gray = cv2.imread("/Users/zrain/Desktop/scshot/unsame/picD.png")

# img1_gray=cv2.resize(img1_gray,(400,800),interpolation=cv2.INTER_AREA)
# img2_gray=cv2.resize(img2_gray,(400,800),interpolation=cv2.INTER_AREA)

sift = cv2.SIFT()
# sift = cv2.SURF()

kp1, des1 = sift.detectAndCompute(img1_gray, None)
kp2, des2 = sift.detectAndCompute(img2_gray, None)

# BFmatcher with default parms
bf = cv2.BFMatcher(cv2.NORM_L2)
matches = bf.knnMatch(des1, des2, k=2)

goodMatch = []
for m, n in matches:
    if m.distance < 0.50 * n.distance:
        goodMatch.append(m)

drawMatchesKnn_cv2_1(img1_gray, kp1, img2_gray, kp2, goodMatch[:])
# drawMatchesKnn_cv2(img1_gray, kp1, img2_gray, kp2, matches[:])

# cv2.waitKey(0)
# cv2.destroyAllWindows()