# django_learn_better

Learning Django, take two.

The use case this time is a database of poets, their poems, and when/where they were published.

This time my policy for structuring the project is one app per domain object. So I have an app for person, an app for person names, and an app for poets. A poet is a type of person, and persons have names. The person and person names apps could be used in any other project that deals with some (any) type of person.
