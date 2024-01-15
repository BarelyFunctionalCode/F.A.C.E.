import time
import datetime
import threading

from display.display import Display

class Assistant:
  def __init__(self, display):
    self.display = display

    # Start the logic of the assistant in a new thread to not block the Tkinter loop
    new_thread = threading.Thread(target=self.logic)
    new_thread.start()

  def logic(self):
    # self.display.set_face_expression("slow_scan")

    while True:
      self.display.enqueue_update_text(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")

      time.sleep(45)


if __name__ == "__main__":
  # Start the display and assistant
  display = Display()
  assistant = Assistant(display)
  display.start()

