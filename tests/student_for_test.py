import sys


class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def get_grade(self):
        if self.score < 0 or self.score > 100:
            raise ValueError('invalid input score')
        if self.score >= 80:
            return 'A'
        if self.score >= 60:
            return 'B'

        return 'C'

if __name__ == '__main__':
    s = Student('Steven', 909)

    #print(s.get_grade())
