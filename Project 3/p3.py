

class Object:
    def __init__(self, idNum, weight, value):
        self.id = idNum
        self.weight = int(weight)
        self.value = int(value)
        self.ratio = 0
    def __str__(self):
        return "(object {}, weight {}, value {})".format(self.id, self.weight, self.value)
    def __repr__(self):
        return str(self)

def readInputFile(fileName):
    with open(fileName, "r") as f:
        totalWeight = int(f.readline().rstrip('\n'))
        weights = f.readline().rstrip('\n').split(",")
        values = f.readline().rstrip('\n').split(",")
        objects = []
        for i in range(0,len(weights)):
            objects.append(Object(i + 1, weights[i], values[i]))
    f.close()
    return(totalWeight, objects)

def dynamic_programming(totalWeight, objects):
    memorytable = []
    for obj in range(0,len(objects)+1):
        memorytable.append([])
        for weight in range(0, totalWeight+1):
            if(obj == 0 or weight == 0):
                memorytable[obj].append(0)
            else:
                if(weight<objects[obj-1].weight):
                    memorytable[obj].append(memorytable[obj-1][weight])
                else:
                    no_change = memorytable[obj-1][weight]
                    no_add_from_above = memorytable[obj-1][weight-objects[obj-1].weight]
                    value_of_this = objects[obj-1].value
                    memorytable[obj].append(max(no_change,no_add_from_above+value_of_this))
    knapsack = []
    length = len(objects)
    weight = totalWeight
    for obj in range(length-1, -1, -1):
        if memorytable[obj+1][weight] != memorytable[obj][weight]:
            knapsack.append(objects[obj])
            weight = weight - objects[obj].weight
    return(memorytable[len(objects)][totalWeight], knapsack)

def brute_force(totalWeight, objects):
    memorytable = []
    memorytable.append("x")
    memorytable.append("o")
    for i in range(1,len(objects)):
        a = memorytable
        memorytable = []
        for str in a:
            memorytable.append(str + "x")
            memorytable.append(str + "o")
    maxVal = 0
    knapsack = []
    for str in memorytable:
        tempVal = 0
        tempKnapsack = [];
        tempWeight = 0
        for i in range(0,len(str)):
            if(str[i] == "x"):
                tempVal = tempVal + objects[i].value
                tempKnapsack.append(objects[i])
                tempWeight = tempWeight + objects[i].weight
        if (tempVal > maxVal) and (tempWeight <= totalWeight):
            maxVal = tempVal
            knapsack = tempKnapsack
    return(maxVal, knapsack)

def greedy(totalWeight, objects):
    knapsackWeight = 0
    knapsack = []
    knapsackValue = 0
    for obj in objects:
        obj.ratio = obj.value/obj.weight
    objects = reversed(sorted(objects, key = lambda x: x.ratio))
    for obj in objects:
        if(knapsackWeight + obj.weight <= totalWeight):
            knapsackWeight = knapsackWeight + obj.weight
            knapsack.append(obj)
            knapsackValue = knapsackValue + obj.value
    return(knapsackValue, knapsack)

again = 1
while again ==1:
    try:
        fileName = input("Enter the file name of the knapsack you want to solve: ")
        print()
        totalWeight, objects = readInputFile(fileName)
        print("Total Weight of the Knapsack: ", totalWeight)
        print("All the Objects in the Knapsack: ", objects)
        print()
        print("-----Dynamic Programming-----")
        max_value, knapsack = dynamic_programming(totalWeight,objects)
        print("Calculated Maximum Value of the Knapsack: ", max_value)
        print("Items in Max Value Knapsack: ", sorted(knapsack, key = lambda x: x.id))
        print()
        print("-----Brute Force-----")
        max_value, knapsack = brute_force(totalWeight,objects)
        print("Calculated Maximum Value of the Knapsack: ", max_value)
        print("Items in Max Value Knapsack: ", sorted(knapsack, key = lambda x: x.id))
        print()
        print("-----Greedy-----")
        max_value, knapsack = greedy(totalWeight,objects)
        print("Calculated Maximum Value of the Knapsack: ", max_value)
        print("Items in Max Value Knapsack: ", sorted(knapsack, key = lambda x: x.id))
    except OSError:
        print("That file does not exist in your current directory")
    print()
    again = int(input("Do you want to try another knapsack? (enter 1 for yes and 0 for no)"))

