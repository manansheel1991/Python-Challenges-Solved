import pickle


def SaveDictionary(dictionary, OutPath):
    with open(OutPath, 'wb') as file:
        pickle.dump(dictionary, file)


def LoadDictionary(InPath):
    with open(InPath, 'rb') as file:
        return pickle.load(file)


dict1 = {'Manan': 30, 'Barkha': 25}

SaveDictionary(
    dict1, r'C:\Users\manan\Documents\Python-Challenges-Solved\test_dict')

LoadDictionary('test_dict')
