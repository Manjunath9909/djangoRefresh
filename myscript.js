async function sortnumbers()
{
    const APIurl = "http://127.0.0.1:8000/sort/?numbers="
    var numbers = document.getElementById("numlist").value;
    var requestURL = APIurl + '[' + numbers +']';
    console.log("we are going to sort : " + numbers);
    try {
            var response = await fetch(requestURL);
    } catch (error) {
        console.log(error);
    }
    var numbers = await response.text();
    console.log(numbers);
}