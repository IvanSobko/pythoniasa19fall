"""
Assignment 2-A
==============

Wrap Assignment 1-A in function `poem()` that satisfies the doctest:

>>> from pathlib import Path
>>> poem() == Path('data/poem-en.txt').read_text()
True
"""
entities = (("house","", " that Jack built"),("malt", "lay in"),("rat","ate"),("cat","kill'd"),("dog","worried"),
            ("cow","toss'd"," with the crumpled horn"), ("maiden","milk'd"," all forlorn"),
            ("man","kissed"," all tatter'd and torn"), ("priest","married"," all shaven and shorn"),
            ("cock","waked"," that crow'd in the morn"), ("farmer","kept"," sowing his corn"), ("",""))





def poem():
    result_str = ""
    for i in range(len(entities) - 1):
        #print(f"This is the {entities[i][0]}{entities[i][2] if len(entities[i]) == 3 else ''}, \n{result_str}")
        result_str = f"That {entities[i + 1][1]} the {entities[i][0]}{entities[i][2] if len(entities[i]) == 3 else ''}, \n{result_str}"

    return result_str


if __name__ == '__main__':
    print(poem())
    # import doctest
    # doctest.testmod()

#test assignment02 branch change