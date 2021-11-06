import random


class ExerciseLogic:
    lowExercises = []
    moderateExercises = []
    highExercises = []
    exercises = {
        {"Low": lowExercises},
        {"Moderate": moderateExercises},
        {"High": highExercises}
    }

    suggestedExercise = ""
    exerciseLevel = ""

    def __init__(self, exerciseLevel):
        self.exerciseLevel = exerciseLevel

    def assignExercise(self):
        self.suggestedExercise = random.choice(self.exercises[self.exerciseLevel])
