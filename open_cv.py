import numpy as np
import cv2
a=np.array([[1,2,3,4],[5,67,8,9]])
min_val,max_val,min_indx,max_indx=cv2.minMaxLoc(a)

def cal_loc(filePath_bg, filePath_qk):
    '''
    bg: 背景图片
    qk: 缺口图片
    '''
    # 读取背景图片和缺口图片
    bg_img = cv2.imread(filePath_bg)  # 背景图片
    qk_img = cv2.imread(filePath_qk)  # 缺口图片

    # 识别图片边缘
    bg_edge = cv2.Canny(bg_img, 100, 200)
    qk_edge = cv2.Canny(qk_img, 100, 200)

    # 转换图片格式
    bg_pic = cv2.cvtColor(bg_edge, cv2.COLOR_GRAY2RGB)
    qk_pic = cv2.cvtColor(qk_edge, cv2.COLOR_GRAY2RGB)

    # 缺口匹配
    res = cv2.matchTemplate(bg_pic, qk_pic, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)  # 寻找最优匹配
    # 返回缺口的X坐标
    return max_loc[0]


a = int(cal_loc('bigimage.jpg', 'smallimage.jpg')/2.08)
print(a)
