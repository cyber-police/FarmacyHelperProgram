class Shelves:
    MINIMUM_AVAILABILITY = 65
    RECOMMENDED_EXP_DATE = 2022
    data = {}
    id = 0

    def setId(self, id):  
        self.id = id

    def setData(self, data):  
        self.data = data

    def isAvailable(self, title):
        j = 0
        for j in range(len(self.data)):
            if self.data[j]["title"].upper() == title.upper():
                return True, j, self.data[j]["price"], self.data[j]["instruction"]
        return False, j

    def sortArray(self, array):
        j = 0
        for j in range(len(self.data)):
            array.append(self.data[j]['title'])
        return array

    def findByDescription(self, value):
        j = 0
        for j in range(len(self.data)):
            if self.data[j]["againstDiseases"].upper() == value.upper():
                return self.data[j]

    def needMore(self):
        j = 0
        array = []
        for j in range(len(self.data)):
            if self.data[j]["count"] <= self.MINIMUM_AVAILABILITY:
                array.append(self.data[j]["title"])
                array.append(self.MINIMUM_AVAILABILITY - self.data[j]["count"])
        if (array != []):
            return True, array
        else:
            return False, j

    def needUtilize(self):
        j = 0
        array = []
        for j in range(len(self.data)):
            if self.data[j]["expiriationDate"] <= self.RECOMMENDED_EXP_DATE:
                array.append(self.data[j]["title"])
        if (array != []):
            return True, array
        else:
            return False, j
