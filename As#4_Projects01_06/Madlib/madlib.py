def mad_libs():
    print("Let\'s play Mad Libs! Fill in the blanks with the words I ask for.")

    name=input("Enter a name: ")
    place=input("Enter a place: ")
    funny_adjective=input("Enter a funny adjective: ")
    random_object=input("Enter a random object: ")
    animal=input("Enter an animal: ")
    action_verb=input("Enter an action verb: ")
    funny_exclamation=input("Enter a funny exclamation: ")

    story = f'''Once upon a time, {name} went to {place}. There, they saw a {funny_adjective} {random_object} that was {action_verb} like a {animal}. \"{funny_exclamation}!\" they exclaimed.'''
    print(story) 


    print("\nHere is your Mad Libs story:")
if __name__ == "__main__":
    print(mad_libs())
     