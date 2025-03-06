print("Hello")
import os

def choose_options(argument):
    match argument:
            case "abot":
                    print('abort')
            case "refresh":
                    print('refresh')
            case "default":
                    print('default')

head = choose_options("abot")