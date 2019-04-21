#nonterminal = ["S'", "S", "C"]
#terminal = ['c','d']
#production = {"S'":  [("S")],"S":   [("C", "C")],"C":   [('c', "C"),('d')]}

from Parser import parser 
#GO to main() kha

class LR1:
    def __init__(self, nt_list, t_list, pd):
        self.nonterminal = nt_list
        self.terminal = t_list
        self.production = pd
        self.first = {}
        self.states = []
        self.table = {}
        self.stack = []
        self.reduction = []

        for i in self.nonterminal:
            self.first[i] = set()
       
        
    def find_first(self, symbol):
        if symbol in self.terminal:
            return {symbol}
        elif symbol in self.nonterminal:
            r = set()
            for prod in self.production[symbol]:
                r = r.union(self.find_first(prod[0]))
            return r
            
    def compute_first(self):
        for sym in self.nonterminal:
            self.first[sym] = self.find_first(sym)

    def inittialize_states(self):

        element = ("S'", tuple(), ("S",) , "$")
        self.stack.append(self.closure(element))
        self.states.append(self.closure(element))
        

    def closure(self, element):
      
        elements = set()
        production_set = set()
        production_set.add(element)
        
        while len(production_set) > 0:
            element = production_set.pop()
            elements.add(element)
            
            if len(element[2]) > 0:
                next_symbol = element[2][0]
                
                if next_symbol in self.nonterminal:
                    if len(element[2]) == 1:
                        lookahead = [element[3]] 
                    else:
                        lookahead = self.first[element[2][1]]

                    for p in self.production[next_symbol]:
                
                        for l in lookahead:
                            new_element = (next_symbol,tuple(), p, l)
                            
                            if new_element not in elements:
                                production_set.add(new_element)
                                
        return elements

    

    def action(self,state):
        states = self.stack.pop(0)
        
        check = False
        
        for symbol in self.terminal:
            found = False
            rules = set()
            for element in states:
 
                if len(element[2]) == 0:
                    check2 = False
                    if(state not in self.table.keys()):
                        self.table[state]={}
                    if(element[3] not in self.table[state].keys()):
                        self.table[state][element[3]] = set()
                    self.table[state][element[3]] = ('r', (element[0],element[1]))
                    if(('r', (element[0],[element[1]])) in self.reduction):
                        check = False
                    else:
                        self.reduction.append(('r', (element[0],element[1])))

                elif element[2][0] == symbol:
                 
                    check = True
                    found = True
                    new_item = (element[0], element[1]+tuple(element[2][0]), element[2][1:], element[3])

                    new_state = self.closure(new_item)

                    rules = rules.union(new_state)
            

                    if(state not in self.table.keys()):
                        self.table[state]={}
                    if(symbol not in self.table[state].keys()):
                        self.table[state][symbol] = ()
                  
            if(found):
                if(rules in self.states):
                   
                    check = False
                    self.table[state][symbol] = ('s', self.states.index(rules))
                else:
                    self.states.append(rules)
                    self.table[state][symbol] = ('s', self.states.index(rules))

            if(check):
                self.stack.append(rules)
                
                
                    

        for symbol in self.nonterminal:

            rules = set()
            check = False
            found = False
            
            for element in states:
                
                if len(element[2]) > 0 and element[2][0] == symbol:
                    #print(element[2],symbol)
                    check = True
                    found = True
                    new_item = (element[0], element[1]+tuple(element[2][0]), element[2][1:], element[3])
                    new_state = self.closure(new_item)
                    #print(new_state)
                    rules = rules.union(new_state)
                    
                    if(state not in self.table.keys()):
                        self.table[state]={}
                    if(symbol not in self.table[state].keys()):
                        self.table[state][symbol] = ()
            if(found):
                   
                if(rules in self.states):
                    self.table[state][symbol] = ('', self.states.index(rules))
                else:
                    self.states.append(rules)
                    self.table[state][symbol] = ('s', self.states.index(rules))

                   
            if(check):
                self.stack.append(rules)
             

        #print(state,"Stack = ", len(self.stack))

    

    def construct(self):
        self.compute_first()
        self.inittialize_states()
        state = 0
        #stack =
        while(True):
            if(len(self.stack) == 0):
                break
            self.action(state)
            state += 1
        self.table[0]["S'"] = ('','accept')
        return self.table
    
#when the main function is running, type down the string kha
def main():
    f= open("input.txt","r")
    lines = []
    counter = 0
    nonterminal = []
    terminal = []
    production = {}
    for line in f:
        line = line.split()
        if(counter == 0):
            nonterminal += line
        elif(counter == 1):
            terminal += line
        else:
            index = line.pop(0)
            if(index not in production.keys()):
                production[index] = []
            production[index].append(tuple())
            for i in line:
                production[index][len(production[index])-1] += tuple(i)
        counter += 1

    string = input()
    lr = LR1(nonterminal, terminal, production)
    parser(lr.construct(), string)
    
   
main()
