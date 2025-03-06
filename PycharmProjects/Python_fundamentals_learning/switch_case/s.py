# This code runs only in python 3.10 or above versions
def number_to_string(argument):
	match argument:
		case "v":
			return "zero"
		case "l":
			return "one"
		case "m":
			return "two"
		case default:
			return "something"


head = number_to_string("v")
print(head)
