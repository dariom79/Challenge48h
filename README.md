# Challenge48h
Scrapy Decision Tree

by Dario Mastroeni
---------------------

Here the scrapy spider that scraps of all options in the dropdowns, recursively.
To run it:

cd dario_challenge/dario_challenge/spiders
scrapy crawl DecisionTree

For each element will be log in output (as "DEBUG") the element itself and its parent.
For example: {'element': 'B', 'parent': 'A'}

For a better experience, I suggest you to put the output in a JSON file:

scrapy crawl DecisionTree -t json -o outputfile.json


and treat it with the script "print_tree.py" at the begin of the repository. It requires "anytree 2.6.0".

python print_tree.py <outputfile.json>

This will be the output:

![Screenshot](screenshot.png)


Best Regards,
 Dario Mastroeni
   
   
Ps: be aware to delete "outputfile.json" before of a rerun: it will append the new output instead of overwrite.
