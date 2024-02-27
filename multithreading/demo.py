import cv2
import numpy as np
import pyautogui
import pygetwindow as gw

def record_screen(file_path, codec='mp4v', fps=30, duration=10):
    screen = gw.getWindowsWithTitle(gw.getActiveWindow().title)[0]

    screen_width, screen_height = screen.size
    screen_left, screen_top = screen.left, screen.top

    fourcc = cv2.VideoWriter_fourcc(*codec)
    out = cv2.VideoWriter(file_path, fourcc, fps, (screen_width, screen_height))

    start_time = pyautogui.PAUSE  # Set the starting time

    while (pyautogui.PAUSE - start_time) < duration:
        screenshot = pyautogui.screenshot(region=(screen_left, screen_top, screen_width, screen_height))
        frame = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
        out.write(frame)

    out.release()

if __name__ == "__main__":
    video_file_path = "screen_recording.mp4"
    
    # Record screen for 10 seconds (adjust duration as needed)
    record_screen(video_file_path, duration=10)
