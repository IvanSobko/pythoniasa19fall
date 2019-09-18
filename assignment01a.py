"""
Assignment 1-A
==============

Update the Python script below to make it more compact and readable; use at least variables and f-strings.
For those who are already familiar with Python – write the best code you can to conform to the Zen of Python.

"""

poem = '''
This is the house that Jack built.

This is the malt 
That lay in the house that Jack built.

This is the rat, 
That ate the malt 
That lay in the house that Jack built.

This is the cat, 
That kill'd the rat, 
That ate the malt 
That lay in the house that Jack built.

This is the dog, 
That worried the cat, 
That kill'd the rat, 
That ate the malt 
That lay in the house that Jack built.

This is the cow with the crumpled horn, 
That toss'd the dog, 
That worried the cat, 
That kill'd the rat, 
That ate the malt 
That lay in the house that Jack built.

This is the maiden all forlorn, 
That milk'd the cow with the crumpled horn, 
That tossed the dog, 
That worried the cat, 
That kill'd the rat, 
That ate the malt 
That lay in the house that Jack built.

This is the man all tatter'd and torn, 
That kissed the maiden all forlorn, 
That milk'd the cow with the crumpled horn,
That tossed the dog, 
That worried the cat, 
That kill'd the rat, 
That ate the malt 
That lay in the house that Jack built.

This is the priest all shaven and shorn, 
That married the man all tatter'd and torn, 
That kissed the maiden all forlorn, 
That milked the cow with the crumpled horn,
That tossed the dog, 
That worried the cat, 
That kill'd the rat, 
That ate the malt 
That lay in the house that Jack built.

This is the cock that crow'd in the morn, 
That waked the priest all shaven and shorn, 
That married the man all tatter'd and torn, 
That kissed the maiden all forlorn, 
That milk'd the cow with the crumpled horn, 
That tossed the dog, 
That worried the cat, 
That kill'd the rat, 
That ate the malt 
That lay in the house that Jack built.

This is the farmer sowing his corn, 
That kept the cock that crow'd in the morn, 
That waked the priest all shaven and shorn,
That married the man all tatter'd and torn, 
That kissed the maiden all forlorn, 
That milk'd the cow with the crumpled horn,
That tossed the dog, 
That worried the cat, 
That killed the rat, 
That ate the malt 
That lay in the house that Jack built.
'''


entities = (("house","", "that Jack built"),("malt", "lay in"),("rat","ate"),("cat","kill'd"),("dog","worried"),
            ("cow","toss'd"," with the crumpled horn"), ("maiden","milk'd"," all forlorn"),
            ("man","kissed","all tatter'd and torn"), ("priest","married","all shaven and shorn"),
            ("cock","waked","that crow'd in the morn"), ("farmer","kept","sowing his corn"), ("",""))

result_str = ""
for i in range(len(entities)-1):
    print(f"This is the {entities[i][0]}{entities[i][2] if len(entities[i]) == 3 else ''}, \n{result_str}")
    result_str = f"That {entities[i+1][1]} the {entities[i][0]}{entities[i][2] if len(entities[i]) == 3 else ''}, \n{result_str}"
