import win32gui
import win32con
import ctypes

# Minimize all windows
ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 6)
win32gui.PostMessage(win32con.HWND_BROADCAST,
                     win32con.WM_SYSCOMMAND,
                     win32con.SC_MINIMIZE,
                     0)
