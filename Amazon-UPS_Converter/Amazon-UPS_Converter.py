#!/usr/bin/python

import os

outputFile = None

# Input fields
toPhone = 9
toName = 16
toAddress1 = 17
toAddress2 = 18
toCity = 20
toState = 21
toZIP = 22
toCountry = 23

# The converting method 
def convert(fname):
	# Open the file and skip the header line
	inputFile = open(fname,'r')
	inputFile.readline()
	# Parse each order line and write to the output file
	for line in inputFile:
		order = Order(line)
		outputFile.write(order.printout())
	inputFile.close()

# Edit the name to meet internal requirements
def parseName(name):
	components = name.strip().split(" ")
	result = ""
	for piece in components[:(len(components)-1)]:
		result+=(piece + " ")
	result = components[len(components)-1] + " " + result.strip()
	while len(result) < 24:
		result+=" "
	result+=" (AMZ)"
	return result

def splitter(info):
	unchecked = info.split('	')
	checked = []
	for piece in unchecked:
		checked.append(piece.replace(',',' ').strip())
	return checked

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
		self.organized.append("")
		# ShipTo_CompanyOrName
		self.organized.append(parseName(self.unorganized[toName].upper()))
		# ShipTo_StreetAddress
		self.organized.append(self.unorganized[toAddress1].upper())
		# ShipTo_RoomFloorAddress2
		self.organized.append(self.unorganized[toAddress2].upper())
		# ShipTo_City
		self.organized.append(self.unorganized[toCity].upper())
		# ShipTo_State
		self.organized.append(self.unorganized[toState].upper())
		# ShipTo_Country
		self.organized.append(self.unorganized[toCountry].upper())
		#self.organized.append("US")
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
		# Package_Reference1-5
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
outputFile = open(r"C:\UPS\WSTD\ImpExp\AcctPkgs\Sample Order Import 1\worldship.csv",'w')
#outputFile = open(r"C:\Users\Alex\Desktop\Amazon-UPS_Converter\worldship.csv",'w')
# Write the header of the converted file to the output
header = "OrderId,ShipmentInformation_ServiceType,ShipmentInformation_BillingOption,ShipmentInformation_QvnOption,ShipmentInformation_QvnShipNotification1Option,ShipmentInformation_NotificationRecipient1Type,ShipmentInformation_NotificationRecipient1FaxorEmail,ShipTo_CompanyOrName,ShipTo_StreetAddress,ShipTo_RoomFloorAddress2,ShipTo_City,ShipTo_State,ShipTo_Country,ShipTo_ZipCode,ShipTo_Telephone,ShipTo_ResidentialIndicator,Package_PackageType,Package_Weight,Package_Reference1,Package_Reference2,Package_Reference3,Package_Reference4,Package_Reference5,Package_DeclaredValueOption,Package_DeclaredValueAmount,ShipTo_LocationID\n"
outputFile.write(header)
# For every file in the current directory, convert the Amazon orders
for fname in os.listdir(r"\\SERVER\Shipping\Amazon-UPS_Converter"):
#for fname in os.listdir(r"C:\Users\Alex\Desktop\Amazon-UPS_Converter"):
	if fname.endswith(".txt"):
		convert(fname)
		# Delete the source file
		os.remove(fname)
print("Files successfully converted.")


    