from constraint import *


less_than = lambda x, y: x < y
greater_than = lambda x, y: x > y


LessThanConstraint = FunctionConstraint(less_than)
GreaterThanConstraint = FunctionConstraint(greater_than)


class TaskScheduler(object):
    def __init__(self, task_names):
        self.task_names = task_names[:]
        self.problem = Problem()
        self.reset()

    def reset(self):
        self.problem.reset()
        self.problem.addVariables(self.task_names, range(len(self.task_names)))
        # Require that only one task is scheduled for each step
        self.problem.addConstraint(AllDifferentConstraint())

    def request_order(self, before, after):
        assert(before in self.task_names)
        assert(after in self.task_names)
        self.problem.addConstraint(LessThanConstraint, [before, after])

    def get_schedule(self):
        solutions = sorted(sorted(x.items())
                        for x in self.problem.getSolutions())
        if solutions:
            return [task for task, position in sorted(list(solutions[0]),
                    key=lambda x: x[1])]
        return []


if __name__ == '__main__':
    tasks = list('ABCD')

    scheduler = TaskScheduler(tasks)

    # Schedule B before A
    scheduler.request_order('B', 'A')
    # Schedule D before A
    scheduler.request_order('D', 'A')

    schedule = scheduler.get_schedule()
    if not schedule:
        print 'Could not meet constraints'
    else:
        print schedule

    scheduler.reset()

    # Schedule B before A
    scheduler.request_order('B', 'A')
    # Schedule A before B
    scheduler.request_order('A', 'B')

    schedule = scheduler.get_schedule()
    if not schedule:
        print 'Could not meet constraints'
    else:
        print schedule
