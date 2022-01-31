from spike import PrimeHub, MotorPair, DistanceSensor
from spike.control import wait_for_seconds
import time

hub = PrimeHub()
mp = MotorPair('C', 'D')
ds = DistanceSensor('F')
go = True


# create a beep function
def beep(nums):
    for x in range(nums):
        hub.speaker.beep()

    """
    Functon that waits until there is an object less than
    distance cm away then starts moving backwards
    very quickly for duration seconds.
    After it stops moving, it beeps once.
    """


def forcePush(distance=30, duration=1.5):
    startRun = time.time()
    while True:
        ds.wait_for_distance_closer_than(distance)
        mp.move(duration, 'seconds', 0, -100)
        beep(1)
        endRun = time.time() - startRun
        if (endRun > duration):
            mp.stop()
            beep(1)
            break

    """
    Function to move forward until the sensor detects
    an object with the set distance and backward until 
    an object is at least set distance
    """


def hoverOne(distance=30, duration=15):
    startRun = time.time()
    while True:
        currDist = ds.get_distance_cm()
        if (currDist == None) or (currDist > distance):
            mp.set_default_speed(10)
            mp.start()
        elif (currDist <= distance):
            mp.set_default_speed(-10)
            mp.start()
        endRun = time.time() - startRun
        if endRun >= duration:
            mp.stop()
            beep(2)
            break


def hoverTwo(distance=30, duration=15):
    startRun = time.time()
    while True:
        currDist = ds.get_distance_cm()
        if (currDist == None) or (currDist >= distance * 1.05):
            mp.set_default_speed(20)
            mp.start()
        elif currDist <= distance * 0.9:
            mp.set_default_speed(-20)
            mp.start()
        endRun = time.time() - startRun
        if endRun >= duration:
            mp.stop()
            beep(3)
            break


def demoPA03():
    # Wait 5 sec and beep so you can get ready for video
    wait_for_seconds(5)
    for i in range(5):
        beep(1)
        wait_for_seconds(1)
    forcePush()
    hoverOne(duration=10)
    hoverTwo(duration=10)


demoPA03()
