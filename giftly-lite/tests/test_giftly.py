import os
os.environ["DISPLAY"] = ""
from src.main import AleniaGiftlyLite
import time

app = AleniaGiftlyLite()
app.path = "test_dir"
os.makedirs("test_dir", exist_ok=True)
with open("test_dir/test.jpg", "wb") as f:
    f.write(b"")
app.width_entry.insert(0, "32")
app.height_entry.insert(0, "32")
app.scale_entry.insert(0, "1")
app.fps_entry.insert(0, "10")
app.on_run()

for i in range(10):
    app.update()
    time.sleep(0.1)
print("Finished test")
