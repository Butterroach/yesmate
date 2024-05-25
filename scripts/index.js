setTimeout(() => {
    document
        .getElementById("downloadbutton")
        .addEventListener("click", function (event) {
            console.log("hai");
            let aElement = document.createElement("a");
            resp = fetch("/api/download", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    Accept: "application/json",
                },
                body: JSON.stringify({
                    url: document.getElementById("url").value,
                }),
            })
                .then((resp) => {
                    return resp.json();
                })
                .then((data) => {
                    aElement.href = data["url"];
                    aElement.download = true;
                    aElement.click();
                });
        });
}, 1);
