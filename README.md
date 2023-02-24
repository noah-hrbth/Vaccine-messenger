# Vaccine-messenger

What's the purpose?

When the first vaccine dates where avaiable in Germany I got one really quick because of a medical condition.
People who didn't have any medical conditions (that would qualify them to get the vaccine early) often had to wait 
for a long time. The problem was that when there were any new vaccine dates you had to be really quick in order to save yourself one 
because there were a lot of people waiting for a date. 
You could get a vaccine date online on Doctolib but they were very rare and there was no notifications for when new dates were avaiable.<br><br>
My gilfriend didn't have any medical condition so I wrote a lil python script which listens for the request on Doctolib when new dates were avaiable. 
I just extracted the JSON file from the request and if there was a new vaccine date I sent a mobile push message with simplepush to my phone.
