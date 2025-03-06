def print_msg(message):
    greeting = "Hello "

    def printer():
        # print(greeting, message)
        return greeting+message

    return printer

#print(print_msg("Mu"))
# x = print_msg("My world")
# x.printer()
func = print_msg("My world is beautiful")
print(func())

# #decorators wo function hote hai jo du dusre functions ko change karke return karte hai.

# TOLL BOOTH

# ek function lete hai usko hum ek box me se ya ek pipe me se pass on kar dete hai, waha par hame uspe kuch aur extra work
# karna ho toh kar lete ehai warna jane dete hai