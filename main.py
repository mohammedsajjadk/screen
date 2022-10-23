import cv2
import numpy as np
import pyautogui
import keyboard
import time
import datetime

SCREEN_SIZE = (1920, 1080)
FPS = 20
time_stamp = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
file_name = f'{time_stamp}.mp4'

fourcc = cv2.VideoWriter_fourcc(*"XVID")
out = cv2.VideoWriter(file_name, fourcc, FPS, (SCREEN_SIZE))

prev = 0
snapshot = False

while True:
	time_elapsed = time.time() - prev
	# print("time elapsed: ", time_elapsed)
	if not snapshot:
		img = pyautogui.screenshot()
		snapshot = True

	if time_elapsed > 1.0/FPS:
		prev = time.time()
		frame = np.array(img)
		frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
		out.write(frame)
		snapshot = False

	if keyboard.is_pressed("esc"):
		break

out.release()