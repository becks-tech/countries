print("Random country quiz")

class Countries:

    def __init__(self, name, capital, pop):
        self.name = name
        self.capital = capital
        self.pop = pop


    def country(self):
        return "The country is: {} and it has a population of {}. The capital is: {} million".format(self.name, self.pop, self.capital)
        
country = str(input("Choose a number between 1 and 10:

france = Countries("France",67, "Paris")

print(france.country())


#do the input as numbers using an if statement, such as number 1 is france, 2 germany etc.. begin with the program just listing some facts about the country

#then, for more of a challenge, incorporate a quiz element, where the user has to guess the capital for the country that is listed. the listed countries
#could appear as part of a random loop so the order is different each time, see maths quiz. for example, if input == answer then print correct. 



 
