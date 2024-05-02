import time

input1 = input("Enter a noun: ")
input2 = input("Enter a verb: ")
input3 = input("Enter a noun: ")
input4 = input("Enter a verb: ")

story = f"""
    Once upon a time,there was {input1} who loved to {input2} all day long
    One day, Bob walked into room and caught the {input3} in act.

    {input1}: "What are you doing?"
    {input3}: "I am just {input2}ing, what the big deal"
    {input1}: "Well, it's not everyday you see a {input3} {input2} in the middle of the day"
    {input3}: "I guess you are right. Maybe i should take a break." 
    {input1}: "That's a probably a good idea. Why we don't we go {input4} instead"
    {input3}: "Sure,that sounds like fun!"

    And so, Bob and the bannana went off to {input4} and had a great time.
    The end
"""

for char in story:
    print(char, end="", flush=True)
    time.sleep(0.02)