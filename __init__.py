from constraint import *


less_than = lambda x, y: x < y
greater_than = lambda x, y: x > y


if __name__ == '__main__':
    # Dependency scheduler
    problem = Problem()
    tasks = list('ABCD')

    problem.addVariables(tasks, range(len(tasks)))
    problem.addConstraint(AllDifferentConstraint())

    # Schedule B before A
    problem.addConstraint(FunctionConstraint(less_than), ['B', 'A'])
    problem.addConstraint(FunctionConstraint(greater_than), ['A', 'B'])

    solutions = sorted(sorted(x.items()) for x in problem.getSolutions())
    if not solutions:
        print 'Could not meet constraints'
    else:
        print [task for task, position in sorted(list(solutions[0]), key=lambda x: x[1])]
