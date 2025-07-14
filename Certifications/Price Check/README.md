# Price Check

There is a shop with old-fashioned cash registers where prices are entered manually, leading to potential errors. Given a list of items and their correct prices, compare them to the prices entered a time of sale and determine the number of errors.

## Example
* products        = ['eggs', 'milk', 'cheese']
* productPrices   = [2.89, 3.29, 5.79]
* productSold     = ['eggs', 'eggs', 'cheese', 'milk']
* soldPrice       = [2.89, 2.99, 5.97, 3.29].

## Price
Product     Actual      Expected        Error
eggs        2.89        2.89
eggs        2.99        2.89            1
cheese      5.97        5.79            1
milk        3.29        3.29

The second sale of eggs has the wrong price, as does the sale of cheese. There are 2 errors in pricing.

## Function Description

Complete the function priceCheck in the editor with the following parameter(s):
* string products[n]: each products[i] is the name of an item for sale
* float productPrices[n]; each productPrices[i] is the price of products[i]
* string productSold[m]: each productSold[j] is the name of a product sold
* float soldPrice[m]: each soldPrice[j] contains the sale price recorded for productSold[j].

## Returns

* int the number of sale prices that were entered incorrectly

## Constraints

* 1 ≤ n ≤ 10^5
* 1 ≤ m ≤ n
* 1.00 ≤ product Prices[i], soldPrice[j] < 100000.00, where O<i<n, and O<j<m

## Input Format for Custom Testing

* The first line contains an integer n, the size of the products array.
* The next n lines each contain an element products[i].
* The next line contains an integer n, the size of the productPrices array.
* The next n lines each contain an element productPrices[i].
* The next line contains an integer m, the size of the productSold array.
* The next mlines each contain an element, productSold[j]..
* The next line contains an integer, m, the size of the soldPrice array.
* The next mlines each contain an element soldPrice[j].


The sales of rice and cheese were at the wrong prices. So, the number of sale prices that were entered incorrectly is 2.