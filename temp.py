import ctypes

# 定义函数
def chpaper(image):
	image_path = image
	ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path, 3)

if __name__ == '__main__':
	pass
