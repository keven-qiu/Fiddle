breakableTasks = {}  # (taskName, duration)
unbreakableTasks = {}  # (taskName, duration)
events = {}  # (eventName, (startTime, endTime)) / idk how time is stored, but we would convert to min
# wake =  int time (in min) that the user should wake up at / start their day
# sleep = int time (in min) the the user should sleep at / end their day

unavailableTime = events.values()


def getFreeTime(unavailableTime, wake, sleep):
    freeChunks = []
    unavailableTime.insert(0, (0, wake))
    unavailableTime.append((sleep, 1440))

    for i in range(0, len(freeChunks) - 1):
        freeChunks[i] = unavailableTime[i + 1][0] - unavailableTime[i][1]

    return freeChunks


def splitTasks(breakableTasks):
    for task, time in breakableTasks.items():
        if time % 50 > 10:
            numDivisions = time // 50 + 1
            timeChunk = time // numDivisions
        else:
            timeChunk = 50
            numDivisions = time // 50
        totalTime = timeChunk * numDivisions
        breakableTasks[task] = (totalTime, timeChunk, numDivisions)

    return breakableTasks


def allTimeChunks(unbreakableTasks, breakableTasks):
    taskChunks = unbreakableTasks.values()

    for time in breakableTasks.values():
        totalTime, timeChunk, numDivisions = time
        for i in range(numDivisions):
            taskChunks.append(timeChunk)

    return taskChunks


def matchTime(unavailableTime, wake, sleep):
    freeTime = getFreeTime(unavailableTime, wake, sleep).sort()
