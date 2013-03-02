#!/usr/bin/python

import os

outputFile = None
folder = None

# Input fields
toPhone = 38
tofName = 21
tolName = 22
toAddress1 = 27
toCity = 25
toState = 24
toZIP = 28
toCountry = 23
toEmail = 32

# The converting method 
def convert(fname):
	# Open the file and skip the header line
	inputFile = open(os.path.join(folder,fname),'r')
	inputFile.readline()
	# Parse each order line and write to the output file
	for line in inputFile:
		order = Order(line)
		outputFile.write(order.printout())
	inputFile.close()

def splitter(info):
	uniterated = info.split(',')
	iterated = []
	curpiece = ""
	for piece in uniterated:
		if curpiece.count('"')%2 == 0:
			curpiece = piece
		else:
			curpiece+=piece
		curpiece.replace(',',' ')
		curpiece.replace('"',' ')
		if curpiece.count('"')%2 == 0:
			iterated.append(curpiece)
	return iterated


class Order:
	def __init__(self, info):
		# Create the two dictionaries.
		self.organized = []
		self.unorganized = splitter(info)
		# OrderID
		self.organized.append("")
		# ShipmentInformation_ServiceType
		self.organized.append("")
		# ShipmentInformation_BillingOption
		self.organized.append("")
		# ShipmentInformation_QvnOption
		self.organized.append("")
		# ShipmentInformation_QvnShipNotification1Option
		self.organized.append("")
		# ShipmentInformation_NotificationRecipient1Type
		self.organized.append("")
		# ShipmentInformation_NotificationRecipient1FaxorEmail
		self.organized.append(self.unorganized[toEmail].lower())
		# ShipTo_CompanyOrName
		self.organized.append(self.unorganized[tofName].upper() + " " + self.unorganized[tolName].upper())
		# ShipTo_StreetAddress
		self.organized.append(self.unorganized[toAddress1].upper())
		# ShipTo_RoomFloorAddress2
		self.organized.append("")
		# ShipTo_City
		self.organized.append(self.unorganized[toCity].upper())
		# ShipTo_State
		self.organized.append(self.unorganized[toState].upper())
		# ShipTo_Country
		self.organized.append(self.unorganized[toCountry].upper())
		# ShipTo_ZipCode
		self.organized.append(self.unorganized[toZIP])
		# ShipTo_Telephone
		self.organized.append(self.unorganized[toPhone])
		# ShipTo_ResidentialIndicator
		self.organized.append("")
		# Package_PackageType
		self.organized.append("")
		# Package_Weight
		self.organized.append("")
		# Package_Reference1,2,3,4,5
		self.organized.append("")
		self.organized.append("")
		self.organized.append("")
		self.organized.append("")
		self.organized.append("")
		# Package_DeclaredValueOption
		self.organized.append("")
		# Package_DeclaredValueAmount
		self.organized.append("")
		# ShipTo_LocationID
		self.organized.append("")

	def printout(self):
		strToWrite = ""
		for piece in self.organized:
			strToWrite+= str(piece) + ","
		strToWrite = strToWrite[0:(len(strToWrite)-1)] + '\n'
		return strToWrite

# The main python script
folder= r"\\SERVER\Shipping\StoreManager-UPS_Converter\Data"
outputFile = open(r"C:\UPS\WSTD\ImpExp\AcctPkgs\Sample Order Import 1\worldship.csv",'w')

#folder = "C:\Users\Alex\Desktop\StoreManager-UPS_Integration\Data"
#outputFile = open(r"C:\Users\Alex\Desktop\worldship.csv",'w')

header = "OrderId,ShipmentInformation_ServiceType,ShipmentInformation_BillingOption,ShipmentInformation_QvnOption,ShipmentInformation_QvnShipNotification1Option,ShipmentInformation_NotificationRecipient1Type,ShipmentInformation_NotificationRecipient1FaxorEmail,ShipTo_CompanyOrName,ShipTo_StreetAddress,ShipTo_RoomFloorAddress2,ShipTo_City,ShipTo_State,ShipTo_Country,ShipTo_ZipCode,ShipTo_Telephone,ShipTo_ResidentialIndicator,Package_PackageType,Package_Weight,Package_Reference1,Package_Reference2,Package_Reference3,Package_Reference4,Package_Reference5,Package_DeclaredValueOption,Package_DeclaredValueAmount,ShipTo_LocationID\n"
outputFile.write(header)

# For every file in the current directory, convert the X-Cart orders
for fname in os.listdir(folder):
	if fname.endswith(".csv"):
		convert(fname)
		# Delete the source file
		os.remove(os.path.join(folder,fname))
	elif fname.endswith(".xls"):
		os.remove(os.path.join(folder,fname))
print("Files successfully converted.")


    