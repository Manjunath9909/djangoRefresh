async function sortnumbers()
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
    console.log(data.name);
}