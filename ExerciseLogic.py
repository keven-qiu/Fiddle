import random


class ExerciseLogic:
    lowExercises = ["casual walk", "stretch", "yoga", "Tai-Chi", "biking", "cross trainer"]
    moderateExercises = ["brisk walking", "walking uphill", "strenuous yoga session", "push-ups", "sit-ups",
                         "jump-rope"]
    highExercises = ["weight training", "endurance exercises", "jogging", "cycling", "lap swimming", "circuit training",
                     "sprints", "swimming"]
    exercises = {
        "low": lowExercises,
        "moderate": moderateExercises,
        "high": highExercises
    }

    suggestedExercise = ""
    exerciseLevel = ""

    @staticmethod
    def calculateExerciseLevel(answerTwo, answerThree):
        if answerThree == "no":
            if answerTwo == "poor" or answerTwo == "moderate":
                return "low"
            else:
                return "moderate"
        else:
            if answerTwo == "poor" or answerTwo == "moderate":
                return "moderate"
            else:
                return "high"

    def assignExercise(self):
        return random.choice(self.exercises[self.exerciseLevel])

    def setExerciseLevel(self, level):
        self.exerciseLevel = level
