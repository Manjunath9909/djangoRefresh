import json
#handler function
def handler(type, listofnumbers):
    if type == 1:
        return bubbleSort(listofnumbers)


#bubble sort
def bubbleSort(listofnums):
    
    listLen = listofnums.__len__()
    indextoIgnore = listLen - 1
    for i in range(0, listLen):
        for j in range(0, indextoIgnore):
            if(listofnums[j] > listofnums[j+1]):
                temp = listofnums[j]
                listofnums[j] = listofnums[j+1]
                listofnums[j+1] = temp
        indextoIgnore -=1

    jsonObject = json.dumps({'sortedList' : listofnums, 'algo' : 'Bubble Sort', 'time' : '1s'}, indent=2)
    return jsonObject

#selection sort
def selectionSort(listofnums):
    return True

#quick sort 
def quickSort(listofnums):
    return True 

#insertion sort 
def insertionSort(listofnums):
    return True

#merge sort 
def mergeSort(listofnums):
    return True

#heap sort
def heapSort(listofnums):
    return True
