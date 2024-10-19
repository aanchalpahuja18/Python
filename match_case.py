# Match Case Statement in Python:

def day_of_week(day):
    match day:
        case 1:
            return "It is a Sunday!"
        case 2:
            return "It's a Monday!"
        case 3:
            return "Its a Tuesday"
        case 4:
            return "Its a Wednesday"
        case 5:
            return "Its a Thursday"
        case 6: 
            return "Its a Friday"
        case 7:
            return "Its a Saturday"
        case _:
            return "Not a valid day!"
        

print(day_of_week("pizza"))


def weekend(day):
    match day:
        case "Sunday" | "Saturday":
            return True
        case "Monday" | "Tuesday" | "Wednesday"  | "Thursday" | "Friday":
            return False
        case _:
            return False
        
print(weekend("pizza"))
