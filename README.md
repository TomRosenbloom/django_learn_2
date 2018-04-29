# django_poetry

Learning Django, take two.

The use case this time is a database of poets, their poems, and when/where they were published.

This time my policy for structuring the project is one app per domain object. So I have an app for person, an app for person names, and an app for poets. A poet is a type of person, and persons have names. The person and person names apps could be used in any other project that deals with some (any) type of person.

NB the naming of persons is an interesting topic, if you need a structure with maximum flexibility. This is someting that wouldn't matter too much in a commercial context, but could be very important in say Digital Humanities. I found this interesting post:
https://stackoverflow.com/questions/20958/list-of-standard-lengths-for-database-fields/19845397#19845397
and also this:
https://softwareengineering.stackexchange.com/questions/233778/how-to-model-more-than-one-last-name
...and created my person_name model accordingly. There is a stem class which is extended by classes for Polynym, Mononym and Pictonym. These each have a foreign key rel to Person. The name stem has a 'role'  of 'preferred', 'legal',  'pseudonym' etc.


There's also some interesting business with partial dates, in this case for dates of birth which may not be known exactly. There is a django package for handling partial dates but in the end I went with my own crude solution. There are text fields for year, month, and month day, and a date field for date of birth. According to how these are entered, the date field may be generated from one or more of the text fields e.g. year '1850' with no month or day would yield 18500101. The point of this is simply to allow partial dates to be used in date ordering. 
