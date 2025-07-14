# REST API: Patient's Medical Record

A REST API contains patients' medical records. Given a patient id, fetch all the records for the patient and return their average body temperature. The API supports pagination and all pages for a patient must be analyzed.

To access the medical information, perform an HTTP GET request to: https://jsonmock.hackerrank.com/api/medical_records?userid=<userid>&page=<page> 
where <userld is the patient id and <page> is the page number to fetch.

For example, a GET request to https://jsonmock.hackerrank.com/api/medical_records?userid=3&page=3 returns the third page of data for userld 3.

Similarly, a GET request to https://jsonmock.hackerrank.com/api/medical_records?userid=3&page=1 returns the first page of data for userld 3.

The response is a JSON with the following 5 fields:
* page: the current page of the results
* per page: the maximum number of results returned per page
* total: the total number of results
* total pages: the total number of pages with results
* data: Either an empty array or an array of medical records as JSON objects. Each medical record object has multiple properties but below are needed for this question:
    * user Id: user id for which we have queried
    * vitals.bodyTemperature: user's body temperature for this particular record

Below is an example of a medical record:
```bash
{
    id: 11,
    timestamp: 1563846626267,
    diagnosis: {
        id: 2,
        name: "Common Cold",
        severity: 1
    },
    vitals: {
        blood PressureDiastole: 126,
        blood PressureSystole: 75,
        pulse: 99,
        breathingRate: 22,
        body Temperature: 101.9
    },
    userId: 3,
    userName: "Helena Fernandez",
    user Dob: "23-12-1987",
}
```

## Function Description
Complete the function  getAverage Temperature ForUser in the editor below. 
Use the property 'vitals.body Temperature' for each record to calculate the average.

getAverage TemperatureForUser has a single parameter:
    int userld: the patient id to query

## Returns
If the data array of the response does not contain any medical records, return the string "0".
if the data array of the response contains medical records, return the patient's average body Temperature as a string with 1 decimal place.

## Input Format For Custom Testing
In the first and only line, there is a user id.

## Sample Case 0
### Sample Input For Custom Testing
1

### Sample Output
100.7

### Explanation
Given userld as 1, we fetch all medical records for this user by making api calls to https://jsonmock.hackerrank.com/api/medical_records userid=1&page=1, https://jsonmock.hackerrank.com/api/medical_records userid=1&page=2 and https://jsonmock.hackerrank.com/api/medical_records userid=1&page=3 as there are 28 records on 3 pages. For reach record retrieved, we use property 'vitals.body Temperature' and calculate the average for 28 records and return the average value '100.7.


## Sample Case 1
### Sample Input For Custom Testing
10

### Sample Output
8

### Explanation
Given userld as 10, we make an api call to https://jsonmock.hackerrank.com/api/medical_records?userId=10&page=1. The response returns data as an empty array and totalas 0. Hence the function returns "0".