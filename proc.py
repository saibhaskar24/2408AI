import win32con
import win32gui
import win32process

def get_hwnds_for_pid (pid):
  def callback (hwnd, hwnds):
    if win32gui.IsWindowVisible (hwnd) and win32gui.IsWindowEnabled (hwnd):
      _, found_pid = win32process.GetWindowThreadProcessId (hwnd)
      if found_pid == pid:
        hwnds.append (hwnd)
    return True
    
  hwnds = []
  win32gui.EnumWindows (callback, hwnds)
  return hwnds

if __name__ == '__main__':
  import subprocess
  import time
  notepad = subprocess.Popen ([r"notepad.exe"])
  #
  # sleep to give the window time to appear
  #
  time.sleep (2.0)
  
  for hwnd in get_hwnds_for_pid (notepad.pid):
    print( hwnd, "=>", win32gui.GetWindowText (hwnd))
    win32gui.SendMessage (hwnd, win32con.WM_CLOSE, 0, 0)