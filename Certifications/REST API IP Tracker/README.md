# REST API: IP Tracker

A REST API contains information about IP addresses. Given an IP address, make a fetch call to the REST API to fetch its information and find its country of origin.

Perform an HTTP GET request to: https://jsonmock.hackerrank.com/api/ip?ip=<ip>
where <ip> is the IP address to query.

For example, a GET request to: https://jsonmock.hackerrank.com/api/ip?ip=172.217.20.46 will return the information for the IP address 172.217.20.46

The response is a JSON object with the following 5 fields:
* page: the current page of the results (1)
* per_page: the maximum number of results returned per page
* total: the total number of results (1 or 0)
* total_pages: the total number of pages with results (1)
* data: Either an empty array or an array with a single IP record object in the following form:
    * ip: IP address [STRING]
    * country: associated country code [STRING]

Below is an example of an IP record:

```bash
{
    "ip": "172.217.28.46", 
    "country": "US"
}
```

Please note that you will get the data from page 1 as any given IP just has a single record (if any). Page 1 is the default page returned on an API hit. No further page hits are required.

Given an IP, the goal is to get the country associated with this IP.

## Function Description
Complete the function ipTracker in the editor below.

ipTracker has the following parameter:
* ip: IP address which we want to track [STRING]

## Returns
* If no record is returned, return the string No Result Found.
* If an IP record is received, return the country code (String)

## Constraints
* There will be only one page per query.
* There will be 0 or 1 record in the response.


## Input Format For Custom Testing
In the first and only line, there is an IP address.

## ▼ Sample Case 0

### Sample Input For Custom Testing
```bash
172.217.20.46
```

### Sample Output
```bash
US
```

### Explanation
The IP address is queried and the country is returned.

## ▼ Sample Case 1

### Sample Input For Custom Testing
```bash
172.217.20.50
```

### Sample Output
```bash
No Result Found
```

### Explanation
The IP address is queried and no record is returned, i.e. "total":0. The function returns 'No Result Found'.