import cv2

# 读取图片
image = cv2.imread('/home/nagisa/opencv/egg')

# 检查图片是否读取成功
if image is None:
    print("Error: Could not read image.")
else:
    # 显示图片
    cv2.imshow('Image', image)

    # 等待用户按键，之后关闭窗口
    cv2.waitKey(0)
    cv2.destroyAllWindows()

