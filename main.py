import numpy
import random
import moviepy.editor as mpy

SURFACEWIDTH = 1920
SURFACEHEIGHT = 1280

# returns a numpy array which represents a single frame
def make_np_array(t):
  frame = []
  for i in range(SURFACEHEIGHT):
    currentRow = []
    for j in range(SURFACEWIDTH):
      currentPixel = []
      for k in range(3):
        currentPixel += [random.randint(0, 255)]
      currentRow += [currentPixel]
    frame += [currentRow]

  array = numpy.array(frame)
  return array

if __name__ == '__main__':
  video = mpy.VideoClip(make_np_array, duration = 5)
  video.write_videofile("test.mp4", fps = 15, audio = False, preset = "ultrafast", logger = "bar")

