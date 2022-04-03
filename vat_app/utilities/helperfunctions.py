from dateutil import  parser

DESCRIPTIONS = {
    'sale':'sale',
    'sele':'sale',
    'purchase':'purchase',
    'parchase':'purchase',
}
# utility functions
# 1 Check if a valid date has been passed
def valid_date(str_date):
    res = True
    try:
        res = bool(parser.parse(str_date))
    except ValueError:
        res = False
    return res
# Clean the description field
# Return value based on dictionary or none
# Format the description column to upper case
def get_description(desc):
    return DESCRIPTIONS.get(desc.lower()).upper()
