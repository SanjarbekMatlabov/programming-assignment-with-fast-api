// fetch("http://localhost:8000/news")
//   .then(response => response.json())
//   .then(data => console.log(data))
//   .catch(error => console.error("Error:", error));
// fetch("http://localhost:8000/admin/login", {
//   method: "POST",
//   headers: { "Content-Type": "application/x-www-form-urlencoded" },
//   body: new URLSearchParams({ username: "admin", password: "admin123" })
// })
//   .then(response => response.json())
//   .then(data => localStorage.setItem("token", data.access_token)) // Tokenni saqlash
//   .catch(error => console.error("Error:", error));
// fetch("http://localhost:8000/admin/news", {
//   method: "POST",
//   headers: {
//     "Content-Type": "application/json",
//     "Authorization": "Bearer " + localStorage.getItem("token"),
//   },
//   body: JSON.stringify({ title: "Yangi yangilik", content: "Bu yangilik mazmuni" })
// })
//   .then(response => response.json())
//   .then(data => console.log("Yangilik qo‘shildi:", data))
//   .catch(error => console.error("Error:", error));
