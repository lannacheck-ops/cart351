window.onload = function () {
    console.log("loaded script_get.js");
    // Convention to get the form id then get the button
    document
        .querySelector("#insertPlantFormFetch")
        .addEventListener("submit", async function (event) {
            // Prevent the submit button from submitting the data(data in the url) and have full control over what happens to the data
            event.preventDefault();
            console.log("button clicked");
            const htmlForm = document.querySelector("#insertPlantFormFetch");
            const formData = new FormData(htmlForm);
            // console.log(htmlForm);

            //doing a get request
            const queryParams = new URLSearchParams(formData).toString();
            // The question mark at the end of the base url is to make a query
            const url = `/getDataFromForm?${queryParams}`;

            try {
                // Fetch goes to that url that is defined in main.py
                let res = await fetch(url)
                let resJSON = await res.json()
                console.log(resJSON)
                document.querySelector("#result-container").innerHTML +=
                    ` THE NEW RESULT: ${resJSON.data_received}
        OWNER NAME : ${resJSON.owner}
        PLANT NAME : ${resJSON.plantname}`

            }
            catch (err) {
                console.log(err)
            }

        });
};