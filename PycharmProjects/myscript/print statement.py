print("Usage examples: CheckVncSession.sh -clear \n  -clear     Clear stuck VNC sessions and files \n  -refresh   Refresh xpid sessions if killed \n  -abort     abort specific Display ID  \n  -v         Script version   ")



match argument:
            case "clear":
                Clear_stuck_session()
            case "abort":
                Forcekillsession_id()
            case "refresh":
                Display_ps_ef_VNC_session()
            case "default":
                    print("Usage examples: CheckVncSession.sh -clear \n  -clear     Clear stuck VNC sessions and files \n  -refresh   Refresh xpid sessions if killed \n  -abort     abort specific Display ID  \n  -v         Script version   ")
