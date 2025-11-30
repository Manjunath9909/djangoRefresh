async function sortnumbers1()
{
    const APIurl = "http://127.0.0.1:8000/api?numbers="
    var numbers = document.getElementById("numlist").value;
    var requestURL = APIurl + numbers;
    console.log("we are going to sort : " + numbers);
    try 
    {
        var response1 = await fetch(requestURL);
    } 
    
    catch (error) 
    {
        console.log(error);
    }

    data = response1.json();
    console.log(data['sortedList']);
}

function sortnumbers()
{
    const APIurl = "http://127.0.0.1:8000/api?numbers="
    var numbers = document.getElementById("numlist").value;
    var requestURL = APIurl + numbers;
    fetch(requestURL) 
    .then(response => {
    if (!response.ok) {
      throw new Error(`HTTP error! Status: ${response.status}`);
    }
    return response.json();
    })
    .then(data => {
    //console.log(data.sortedList); 
    //console.log(data.algo);
    //console.log(data.time); 
    var resultdiv = document.getElementById("resultdiv");
    resultdiv.innerHTML = data.sortedList + " sorted with " + data.algo + " in " + data.time;
    })
    .catch(error => {
    console.error('Error fetching or parsing JSON:', error);
    });
}