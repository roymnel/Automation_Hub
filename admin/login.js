function adminLogin() {
  const username = document.getElementById("adminUser").value.trim();
  const password = document.getElementById("adminPass").value.trim();

  // 💡 Hardcoded credentials (replace or hook into back-end later)
  const validUsername = "admin";
  const validPassword = "letmein";

  if (username === validUsername && password === validPassword) {
    document.getElementById("loginSection").classList.add("d-none");
    document.getElementById("adminPanel").classList.remove("d-none");
  } else {
    alert("❌ Invalid credentials. Please try again.");
  }
}
