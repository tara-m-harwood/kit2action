# kit2action
ActionKit -> Action Network

Excercise in migrating data from the ActionKit sandbox account to my developer account at Action Network, because why not?

2025-04-27: Very basic version of the program is successful.  It uses the ActionKit API to GET an array of user records, filtered by source. Then a script interates over the array, transmogifies each record into AN format, and individually POSTs each record to the Action Network API.
