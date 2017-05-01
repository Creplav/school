'''
This program takes an unspecified number of scores and then finds the average.
From there, the program finds how many are above or below the average
'''

class ScoreCalculator:
    def __init__(self):
        self.scores = []
        self.students_average_or_above = 0
        self.students_below_average = 0
        self.get_input()
        average = self.find_average_score(self.scores)

        self.calculate_total(average, lower_scores, higher_scores)

    def get_input(self):
        user_input = input("Please enter a group of numbers: ")
        self.scores.append([int(i) for i in user_input.split()])

    def find_average_score(self, scores):
        class_total = 0
        average = 0
        for score in scores:
            class_total += score
        class_total / len(scores)
        return average

    def find_results(self, scores, average):
        for score in scores:
            scores.count(score >= average)
            scores.count(score < average)


score_calculator = ScoreCalculator()