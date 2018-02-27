
MALE = 'MALE'
FEMALE = 'FEMALE'
GENDER_CHOICES = (
    (MALE, 'Male'),
    (FEMALE, 'Female'),
)

MONTH_CHOICES = (
    (1, 'January'),
    (2, 'February'),
    (3, 'March'),
    (4, 'April'),
    (5, 'May'),
    (6, 'June'),
    (7, 'July'),
    (8, 'August'),
    (9, 'September'),
    (10, 'October'),
    (11, 'November'),
    (12, 'December'),
)

PARTIAL_YEAR='%Y'
PARTIAL_MONTH='%Y-%m'
PARTIAL_DAY='%Y-%m-%d'
PARTIAL_DATE_CHOICES = (
    (PARTIAL_YEAR, 'Year'),
    (PARTIAL_MONTH, 'Month'),
    (PARTIAL_DAY, 'Day'),
)
