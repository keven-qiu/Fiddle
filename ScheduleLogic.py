class ScheduleLogic:
    # okay this will be written as plain code and i'll adapt it/integrate it after

    tasks = {}  # (taskName, duration)
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

    def
