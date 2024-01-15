import time
import datetime
import threading

from display.display import Display

class Assistant:
  def __init__(self, display):
    self.display = display

    self.loop_counter = 0
    self.loop_limit = 45

    # Start the logic of the assistant in a new thread to not block the Tkinter loop
    self.new_thread = threading.Thread(target=self.logic)
    self.new_thread.start()
    # self.new_thread.join()

  def logic(self):
    # self.display.set_face_expression("slow_scan")
    while True:
      self.loop_counter += 1
      if self.display.root == None: break

      if self.loop_counter >= self.loop_limit:
        self.loop_counter = 0
        self.display.enqueue_update_text(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")

      time.sleep(1)

  def stop(self):
    self.new_thread.join()

if __name__ == "__main__":
  # Start the display and assistant
  display = Display()
  assistant = Assistant(display)
  display.start()
  print("Display stopped")
  assistant.stop()

