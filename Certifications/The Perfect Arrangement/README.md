# The Perfect Arrangement

Write a query to print the id, first name and last name. To filter the names, concatenate the first and last names to create a combined name. Return the names of customers whose combined names are less than 12 letters long. Sort the results by their combined name lengths, then alphabetically, case insensitive, by combined name, then by id. All sorts are ascending.

## Input Format

CUSTOMER
 
Name                  Type                Description
ID                         Integer            unique id, primary key.
FIRST_NAME     String
LAST_NAME      String
COUNTRY           String
CREDIT_LIMIT    Float

## Output Format
```bash
CUSTOMER. ID CUSTOMER. FIRST NAME CUSTOMER.  LAST NAME
```

## Sample Input




## Sample Output
```bash
1 Alex White
9 Riley Garza
5 Blake Fuller
4 Drew Bradley
2 Tyler Hanson
```

## Explanation
AlexWhite is 9 letters, so it is included in the results. JordanFernandez is 15 letters, so it is omitted.  The last 3 names are the same length, so they are sorted alphabetically ascending.

Names that are excluded and their lengths
```bash
MorganThomas  12
PeytonHarris  12
EllisGutierrez  14
JordanFernandez 15
SpencerJohnston 15
```