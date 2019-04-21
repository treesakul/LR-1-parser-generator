# LR-1-parser-generator
LR(1) parser generator that accepts a context-free grammar. This project consists of a table construcor and a parser.<br>

<b><header> run `LR(1)_Treesakul.py` to start</header></b>

<b><header>1. input.txt format</header></b>
- The first line contains non-terminals, separated by a single space ' '<br>
- The second line contains terminals, separated by a single space ' '<br>
- The rest of the lines contains production rules, each rule is separed by a single new line.

<p align="center">
  <img src="https://github.com/treesakul/LR-1-parser-generator/blob/master/img/input_example.png" width="350" title="input example"><br><br>
</p>

<b><header>2. Table Constructor</header></b><br>
This LR(1) table constructor is constructed using a given contect-free grammar from 1. input.txt 
- To instantiate the contructor, it requires a list of terminals, a list of non-terminals, and a dictionary of production rules.<br>
- `find_first(symbol)` is used to find FIRST() of the symbol<br>
- `compute_first()` is for finding FIRST() of every non-terminals<br>
- `initialize_states()` prepares the first state
- `closure()` computes the rule and gets a set of rules using LR(1) look-ahead method<br>
- `action()` fills in the table on both action and goto<br>
- `construct()` constructs a table from the given grammar<br>


<p align="center">
  <img src="https://github.com/treesakul/LR-1-parser-generator/blob/master/img/table_example.png" width="350" title="derived table example"><br><br>
</p>

<b><header>3. Parser</header></b><br>
The parser takes a string input and table, return the result of 'accept' or 'reject'and displays the stack.<br>
- `parser(table, string)` uses the table to decide whether the input string is accepted or rejected<br>
<p align="center">
  <img src="https://github.com/treesakul/LR-1-parser-generator/blob/master/img/parser_example.png" width="350" title="derived table example"><br><br>
</p>

