class GoalBasedAgent:
    def __init__(self):
        self.goals = []

    def add_goal(self, goal):
        self.goals.append(goal)

    def select_action(self, percept):
        if self.goals:
            current_goal = self.goals[0]  
            if self.is_goal_achieved(current_goal, percept):
                self.goals.pop(0)
            else:
                return self.plan_for_goal(current_goal, percept)
        return self.default_action()  

    def is_goal_achieved(self, goal, percept):
        pass

    def plan_for_goal(self, goal, percept):
        pass

    def default_action(self):
        pass

class Goal:
    def __init__(self, condition):
        self.condition = condition

# Instantiate the agent
agent = GoalBasedAgent()

# Define conditions
condition1 = "Some condition for goal 1"
condition2 = "Some condition for goal 2"

# Add goals
agent.add_goal(Goal(condition1))
agent.add_goal(Goal(condition2))

# Define percept
percept = "Perceptual input"

# Select action based on percept
action = agent.select_action(percept)