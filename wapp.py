import constants as c
import pywhatkit as wapp

#number, message, waittime, tabclose?, closetime)
#wapp.sendwhatmsg_instantly(c.TEST_PHONE_NUMBER, c.TEST_MESSAGE, 15, False, 3)

#group id, message, watitime, tabclose?, closetime
wapp.sendwhatmsg_to_group_instantly(c.TEST_GROUP_ID, c.TEST_MESSAGE, 15, True, 3)