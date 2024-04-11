class UtilityBasedAgent:
    def __init__(self):
        self.utility_function = None

    def set_utility_function(self, utility_function):
        self.utility_function = utility_function

    def select_action(self, percept):
        possible_actions = self.get_possible_actions(percept)
        best_action = None
        max_utility = float('-inf')
        for action in possible_actions:
            utility = self.utility_function(action, percept)
            if utility > max_utility:
                max_utility = utility
                best_action = action
        return best_action

    def get_possible_actions(self, percept):
        # Return a list of possible actions based on the current percept
        pass

# Instantiate the agent
agent = UtilityBasedAgent()

# Define utility function
def utility_function(action, percept):
    # Calculate the utility of taking the given action based on the current percept
    pass

# Set utility function
agent.set_utility_function(utility_function)

# Select action based on percept
percept = "Perceptual input"
action = agent.select_action(percept)
