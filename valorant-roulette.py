import random

# Define groupings
roles = ["controller", "sentinel", "duelist", "initiator", "allAgents", "male", "female", "unknown", "custom"]

controller = ["brimstone", "viper", "omen", "astra", "harbor", "clove"]
sentinel = ["killjoy", "cypher", "sage", "chamber", "deadlock", "vyse"]
duelist = ["phoenix", "jett", "reyna", "raze", "yoru", "neon", "iso"]
initiator = ["sova", "breach", "skye", "kayo", "fade", "gekko", "tejo"]
allAgents = controller + sentinel + duelist + initiator

male = ["brimstone", "omen", "harbor", "cypher", "chamber", "phoenix", "yoru", "iso", "sova", "breach", "kayo", "gekko", "tejo"]
female = ["viper", "astra", "killjoy", "sage", "deadlock", "vyse", "jett", "reyna", "raze", "neon", "skye", "fade"]
unknown = ["clove"]

custom = []

# Functions

def get_role_choice():
    """
    Prompt the user to choose a role

    Parameters:
        None
    Returns:
        str: The role chosen by the user.
    """
    while True:
        roleChoice = input("Enter the type of role you would like to play (controller, sentinel, duelist, initiator, allAgents, male, female, unknown, custom): ").lower()
        if roleChoice in roles:
            return roleChoice
        else:
            print("Please enter a valid role")

def custom_agent_pool():
    """
    Allows the user to create their own agent pool

    Parameters:
        None
    Returns:
        list: A list of agents added to the custom pool.
    """
    while True:
        customAgentAddition = input("Please enter an agent to enter the agent pool (Type Done to finish): ").lower()
        if customAgentAddition == "Done":
            break
        if customAgentAddition not in allAgents:
            print("Please enter a valid agent.")
        else:
            custom.append(customAgentAddition)
            print(f"Current agent pool: {custom}")
    return custom

def remove_agents(agentPool):
    """ 
    Allows the user to remove agents from the current pool

    Parameters:
        agentPool (list): The current pool of agents.
    Returns:
        list: The updated pool of agents after removals.
    """
    while True:
        print(f"Current agent pool: {agentPool}")
        remove = input("Would you like to remove any agents? (Y/N): ").upper()
        if remove == "Y":
            while True:
                agentToRemove = input("Enter the agent you would like removed: ").lower()
                if agentToRemove in agentPool:
                    agentPool.remove(agentToRemove)
                    
                    # Ensure the pool is not completely emptied
                    if agentPool == []:
                        agentPool.append(agentToRemove) # Re-add the last agent to prevent an empty agent pool
                        print("You cannot remove anymore agents.")

                    break
                else:
                    print(f"Invalid agent name. Try again.")
        elif remove == "N":
            break
        else:
            print("Please enter Y or N.")
    return agentPool

def add_agents(agentPool):
    """
    Allows the user to add agents to the current pool

    Parameters:
        agentPool (list): The current pool of agents.
    Returns:
        list: The updated pool of agents after additions.
    """
    while True:
        print(f"Current agent pool: {agentPool}")
        add = input("Would you like to add any agents? (Y/N): ").upper()
        if add == "Y":
            while True:
                agentToAdd = input("Enter the agent you would like added: ").lower()
                if agentToAdd in allAgents:
                    # Check for duplicates
                    if agentToAdd in agentPool:
                        duplicate = input(f"{agentToAdd} is already in the pool. Add it again? (Y/N): ").upper()
                        if duplicate == "Y":
                            agentPool.append(agentToAdd)
                            print(f"{agentToAdd} added again to the pool.")
                            break
                        elif duplicate == "N":
                            print(f"{agentToAdd} not added.")
                            break
                        else:
                            print("Invalid input. Please enter Y or N.")
                    else:
                        agentPool.append(agentToAdd)
                        print(f"{agentToAdd} added to the pool.")
                        break
                else:
                    print(f"{agentToAdd} is not a valid agent. Please try again.")
        elif add == "N":
            break
        else:
            print("Please enter Y or N.")
    return agentPool

def generate_random_team():
    """
    Generate a random team of a selected number of agents

    Parameters:
        None
    Returns:
        list: A randomly generated team of agents.
    """
    while True:
        try:
            numberInRandomTeam = int(input("How many agents would you like generated?: "))
            if numberInRandomTeam > 5:  # Limits team size to a maximum of 5 agents
                print("Maximum number of agents allowed is 5. Try again.")
            elif numberInRandomTeam <= 0:  # Handle case where the number is zero or negative
                print("Please enter a number greater than 0.")
            else:
                randomTeam = random.sample(allAgents, numberInRandomTeam)  # Randomly samples agents without replacement
                return randomTeam
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def generate_custom_team():
    """
    Generate a custom team based on user input

    Parameters:
        None
    Returns:
        list: A custom team of agents selected by the user.
    """
    customControllers = []
    customSentinels = []
    customDuelists = []
    customInitiators = []

    remainingAgents = 5 # Limits the team size to 5 agents

    # Controllers
    while remainingAgents > 0:
        try:
            print(f"You have {remainingAgents} agents left to select.")
            numberOfControllers = int(input("How many controllers would you like generated?: "))
            if numberOfControllers < 0 or numberOfControllers > remainingAgents:
                print(f"Please enter a number between 0 and {remainingAgents}.")
            else:
                customControllers = random.sample(controller, numberOfControllers) # Randomly select controllers
                remainingAgents -= numberOfControllers # Update remaining agents count
                break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    # Sentinels
    while remainingAgents > 0:
        try:
            print(f"You have {remainingAgents} agents left to select.")
            numberOfSentinels = int(input("How many sentinels would you like generated?: "))
            if numberOfSentinels < 0 or numberOfSentinels > remainingAgents:
                print(f"Please enter a number between 0 and {remainingAgents}.")
            else:
                customSentinels = random.sample(sentinel, numberOfSentinels) # Randomly select sentinels
                remainingAgents -= numberOfSentinels
                break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    # Duelists
    while remainingAgents > 0:
        try:
            print(f"You have {remainingAgents} agents left to select.")
            numberOfDuelists = int(input("How many duelists would you like generated?: "))
            if numberOfDuelists < 0 or numberOfDuelists > remainingAgents:
                print(f"Please enter a number between 0 and {remainingAgents}.")
            else:
                customDuelists = random.sample(duelist, numberOfDuelists) # Randomly select duelists
                remainingAgents -= numberOfDuelists
                break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    # Initiators
    while remainingAgents > 0:
        try:
            print(f"You have {remainingAgents} agents left to select.")
            numberOfInitiators = int(input("How many initiators would you like generated?: "))
            if numberOfInitiators < 0 or numberOfInitiators > remainingAgents:
                print(f"Please enter a number between 0 and {remainingAgents}.")
            else:
                customInitiators = random.sample(initiator, numberOfInitiators) # Randomly select initiators
                remainingAgents -= numberOfInitiators
                break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    randomTeam = customControllers + customSentinels + customDuelists + customInitiators # Combine selected agents
    return randomTeam

def main():
    """
    Main function to manage application of the roulette program, providing user options for generating teams or individual agents.

    Parameters:
        None
    Returns:
        None
    """
    while True:
        menuChoice = input("Welcome! CTRL+C to go back to the menu at any time. Would you like to continue with the Valorant roulette? (Y/N): ").upper()
        if menuChoice == "Y":
            try:
                while True:
                    teamOrIndividual = input("Generate a team (1) or an individual agent (2)? : ")
                    if teamOrIndividual == "1":
                        chooseOrRandom = input("Choose number of agents for each role (1) or generate randomly (2)?: ")
                        if chooseOrRandom == "1":
                            while True:
                                team = generate_custom_team()
                                reroll = input(f"Your random team is: {team}. Would you like to reroll? (Y/N): ").upper()
                                if reroll == "Y":
                                    continue # Allow for rerolling
                                elif reroll == "N":
                                    break
                                else:
                                    print("Please enter Y or N.")
                        elif chooseOrRandom == "2":
                            while True:
                                team = generate_random_team()
                                reroll = input(f"Your random team is: {team}. Would you like to reroll? (Y/N): ").upper()
                                if reroll == "Y":
                                    continue # Allow for rerolling
                                elif reroll == "N":
                                    break
                                else:
                                    print("Please enter Y or N.")
                        else:
                            print("Please enter 1 or 2.")
                    elif teamOrIndividual == "2":
                        roleChoice = get_role_choice()
                        roleToAgentPool = {
                            "controller": controller,
                            "sentinel": sentinel,
                            "duelist": duelist,
                            "initiator": initiator,
                            "allAgents": allAgents,
                            "male": male,
                            "female": female,
                            "unknown": unknown,
                        }
                        if roleChoice == "custom":
                            agentPool = custom_agent_pool()  # Call the function only if "custom" is selected
                        else:
                            agentPool = roleToAgentPool[roleChoice]
                        agentPool = remove_agents(agentPool) # Allow user to remove agents from the pool
                        agentPool = add_agents(agentPool) # Allow user to add agents from the pool
                        while True:
                            chosenAgent = random.choice(agentPool) # Randomly select an agent from the pool
                            reroll = input(f"Your chosen agent is: {chosenAgent}. Would you like to reroll? (Y/N): ").upper()
                            if reroll == "Y":
                                continue # Allow for rerolling
                            elif reroll == "N":
                                break
                            else:
                                print("Please enter Y or N.")
                    else:
                        print("Please enter 1 or 2.")
            except KeyboardInterrupt:
                print("\nReturning to the main menu...")
        elif menuChoice == "N":
            print("Program shutting down...")
            break
        else:
            print("Please enter Y or N.")

if __name__ == "__main__":
    main()