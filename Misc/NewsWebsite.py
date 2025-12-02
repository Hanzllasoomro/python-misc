import os
import zipfile

# Create project directory
project_name = "dynamic-news-website"
os.makedirs(project_name, exist_ok=True)

# index.html
index_html = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Dynamic News Website</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <h1>Latest News</h1>
  <div id="news" class="news-container"></div>
  <script src="app.js"></script>
</body>
</html>
"""

# style.css
style_css = """body {
  font-family: Arial, sans-serif;
  background: #f4f4f4;
  margin: 0;
  padding: 20px;
}
h1 {
  text-align: center;
}
.news-container {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 20px;
  margin-top: 20px;
}
.news-card {
  background: #fff;
  padding: 15px;
  border-radius: 10px;
  box-shadow: 0 2px 5px rgba(0,0,0,0.1);
  display: flex;
  flex-direction: column;
}
.news-card img {
  width: 100%;
  border-radius: 10px;
  max-height: 180px;
  object-fit: cover;
}
.news-card h2 {
  font-size: 18px;
  margin: 10px 0;
}
.news-card p {
  font-size: 14px;
  color: #555;
  flex-grow: 1;
}
.news-card small {
  color: #777;
  display: block;
  margin: 8px 0;
}
.news-card a {
  text-decoration: none;
  color: white;
  background: #007BFF;
  padding: 8px 12px;
  border-radius: 5px;
  text-align: center;
  transition: background 0.3s;
}
.news-card a:hover {
  background: #0056b3;
}
"""

# app.js
app_js = """const newsContainer = document.getElementById("news");
const url = "https://api.spaceflightnewsapi.net/v4/articles/?limit=12";

// Show loading
newsContainer.innerHTML = "<p>Loading latest news...</p>";

fetch(url)
  .then(response => response.json())
  .then(data => {
    newsContainer.innerHTML = ""; // clear loading message
    data.results.forEach(article => {
      const newsCard = document.createElement("div");
      newsCard.classList.add("news-card");
      newsCard.innerHTML = `
        <img src="${article.image_url || 'https://via.placeholder.com/300x180'}" alt="News Image"/>
        <h2>${article.title}</h2>
        <p>${article.summary || ''}</p>
        <small>Published: ${new Date(article.published_at).toLocaleString()}</small>
        <a href="${article.url}" target="_blank">Read More</a>
      `;
      newsContainer.appendChild(newsCard);
    });
  })
  .catch(error => {
    console.error("Error fetching news:", error);
    newsContainer.innerHTML = "<p>Failed to load news. Please try again later.</p>";
  });
"""

# Save files
with open(os.path.join(project_name, "index.html"), "w") as f:
    f.write(index_html)

with open(os.path.join(project_name, "style.css"), "w") as f:
    f.write(style_css)

with open(os.path.join(project_name, "app.js"), "w") as f:
    f.write(app_js)

# Create zip file
zip_filename = f"{project_name}.zip"
with zipfile.ZipFile(zip_filename, 'w') as zipf:
    for root, dirs, files in os.walk(project_name):
        for file in files:
            file_path = os.path.join(root, file)
            zipf.write(file_path, os.path.relpath(file_path, project_name))

zip_filename
