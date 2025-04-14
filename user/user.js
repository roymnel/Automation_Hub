// Simulated database structure
const USERS_KEY = "automation_users";
const SESSION_KEY = "automation_session";

// Helper to get all users
function getUsers() {
  return JSON.parse(localStorage.getItem(USERS_KEY)) || [];
}

// Helper to save user
function saveUser(user) {
  const users = getUsers();
  users.push(user);
  localStorage.setItem(USERS_KEY, JSON.stringify(users));
}

// Create session
function loginSession(user) {
  localStorage.setItem(SESSION_KEY, JSON.stringify(user));
  window.location.href = "dashboard.html";
}

// Read session
function getCurrentUser() {
  return JSON.parse(localStorage.getItem(SESSION_KEY));
}

// Logout user
function logout() {
  localStorage.removeItem(SESSION_KEY);
  alert("You have been logged out.");
  window.location.href = "login.html";
}

// Signup logic
function registerUser() {
  const name = document.getElementById("fullname").value.trim();
  const email = document.getElementById("signupEmail").value.trim().toLowerCase();
  const pass = document.getElementById("signupPassword").value;
  const confirm = document.getElementById("confirmPassword").value;

  if (pass !== confirm) {
    alert("Passwords do not match.");
    return;
  }

  const users = getUsers();
  if (users.find(u => u.email === email)) {
    alert("Account already exists with that email.");
    return;
  }

  const newUser = {
    name,
    email,
    password: pass,
    subscriptions: ["AI Contract Generator"],
    orders: ["Order #3015 – $150 – Paid"]
  };

  saveUser(newUser);
  alert("Account created. Logging you in...");
  loginSession(newUser);
}

// Login logic
function loginUser() {
  const email = document.getElementById("email").value.trim().toLowerCase();
  const pass = document.getElementById("password").value;

  const user = getUsers().find(u => u.email === email && u.password === pass);

  if (user) {
    alert("Welcome back!");
    loginSession(user);
  } else {
    alert("Invalid login. Please try again.");
  }
}

// Dashboard logic
function loadDashboard() {
  const user = getCurrentUser();
  if (!user) {
    alert("You must log in first.");
    window.location.href = "login.html";
    return;
  }

  // Welcome message
  document.getElementById("userName").innerText = user.name;

  // Subscriptions
  const subList = document.getElementById("subscriptionList");
  subList.innerHTML = "";
  user.subscriptions.forEach(sub => {
    const li = document.createElement("li");
    li.className = "list-group-item";
    li.innerText = sub;
    subList.appendChild(li);
  });

  // Orders
  const orderList = document.getElementById("orderList");
  orderList.innerHTML = "";
  user.orders.forEach(order => {
    const li = document.createElement("li");
    li.className = "list-group-item";
    li.innerText = order;
    orderList.appendChild(li);
  });
}

// Simulated invoice download
function downloadInvoice() {
  const invoice = "Invoice #3015\\nService: AI Contract Generator\\nAmount: $150\\nStatus: Paid";
  const blob = new Blob([invoice], { type: "text/plain" });
  const link = document.createElement("a");
  link.href = URL.createObjectURL(blob);
  link.download = "invoice.txt";
  link.click();
}

// Auto-load dashboard if on that page
if (window.location.pathname.includes("dashboard.html")) {
  window.addEventListener("DOMContentLoaded", loadDashboard);
}
