document.getElementById("generateBtn").addEventListener("click", function() {
    const url = document.getElementById("urlInput").value;

    if (url) {
        document.getElementById("result").innerText = "Generating Sitemap... Please wait.";

        // Here you would integrate the logic to interact with the generated sitemap, for now it's just a placeholder
        // In a real setup, you could make an API call to your Python backend via GitHub Actions
        setTimeout(() => {
            document.getElementById("result").innerHTML = `<a href="sitemap.xml" download>Download your sitemap.xml</a>`;
        }, 2000);
    } else {
        document.getElementById("result").innerText = "Please enter a URL.";
    }
});