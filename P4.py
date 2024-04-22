class Birds:
    def _init_(self):
         self.members = ['Sparrow', 'Robin', 'Duck']

    def printMembers(self):
         print('Printing members of the Birds class')
         for member in self.members:
             print('\t%s ' % member)