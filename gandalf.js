document.getElementById("fetch-quote").addEventListener("click", function (){
    fetch("http://127.0.0.1:5000/quote")
    .then(response => response.json())
    .then(data => {
        // Update the quote in the paragraph
        document.getElementById("quote").innerText = data.quote;

        // Update the Gandal image
        const gandalfImageElement = document.getElementById("gandalf-image");
        gandalfImageElement.src = data.image;
        gandalfImageElement.style.display = "block";
   
    })
    .catch(error =>{
        console.error("Error fetching the quote", error);
        document.getElementById("quote").innerText = "Could not load quote. Try again later";
    });

});
