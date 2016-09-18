class Company(object):

		def __init__(self, name, title, start_date):
				self.name = name
				self.title = title
				self.start_date = start_date

		def getName(self):
				return self.name

		def getTitle(self):
				return self.title

		def getStartDate(self):
				return self.start_date
		# Add the remaining methods to fill the requirements above

		def __str__(self):
				return  "{} is a {} and began working {}".format(self.name, self.title, self.start_date)

myCompany = Company("Acme", "Hello", "June")
print(myCompany.getName())
print(myCompany.getTitle())
print(myCompany.getStartDate())
print(myCompany.__str__())




# >>> from pets import Pet
# >>> polly = Pet("Polly", "Parrot")
# >>> print "Polly is a %s" % polly.getSpecies()
# Polly is a Parrot
# >>> print "Polly is a %s" % Pet.getSpecies(polly)
# Polly is a Parrot
# >>> print "Polly is a %s" % Pet.getSpecies()
# Traceback (most recent call last):
#   File "", line 1, in
# TypeError: unbound method getSpecies() must be called with Pet instance as first
# argument (got nothing instead)

# john = Company("john")





