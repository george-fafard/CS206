from solution import SOLUTION
import constants as c
import copy
import os

class PARALLEL_HILL_CLIMBER:
    def __init__(self):
        os.system("del brain*.nndf")
        os.system("del fitness*.txt")
        self.parents = {}
        self.nextAvailableID = 0
        for i in range(0, c.populationSize):
            self.parents.update({i: SOLUTION(self.nextAvailableID)})
            self.nextAvailableID+=1

    def Evolve(self):
        self.Evaluate(self.parents)
        for currentGeneration in range(0, c.numberOfGenerations):
            self.Evolve_For_One_Generation()

    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.Evaluate(self.children)
        self.Print()
        self.Select()

    def Print(self):
        print("\n")
        for i in self.parents:
            print("Best individual Swarm member fitness: " + str(self.parents[i].fitness) + " best child swarm memmber fitness: " + str(self.children[i].fitness))
            print("Overall swarm fitness: " + str(self.parents[i].swarmFitness) + " child overall swarm fitness: " + str(self.children[i].swarmFitness))
        print("\n")

    def Spawn(self):
        self.children = {}
        for i in self.parents:
            self.children.update({i: copy.deepcopy(self.parents[i])})
            self.children[i].Set_ID(self.nextAvailableID)
            self.nextAvailableID+=1

    def Evaluate(self, solutions):
        for bot in solutions:
            solutions[bot].Start_Simulation("DIRECT")
        for bot in solutions:
            solutions[bot].Wait_For_Simulation_To_End()

    def Mutate(self):
        for i in self.children:
            self.children[i].Mutate()

    def Select(self):
        for i in self.parents:
            if self.parents[i].fitness > self.children[i].fitness:
                self.parents[i] = self.children[i]

    def Show_Best(self):
        lowest = None
        myKey = None
        for speeddemon in self.parents:
            if lowest != None:
                if self.parents[speeddemon].fitness < lowest:
                    lowest = self.parents[speeddemon].fitness
                    myKey = speeddemon
            else:
                lowest = self.parents[speeddemon].fitness
                myKey = speeddemon
        self.parents[myKey].Start_Simulation("GUI")
        print("Most Effective Swarm Fitness: " + str(self.parents[myKey].fitness))

