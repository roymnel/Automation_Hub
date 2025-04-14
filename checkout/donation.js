function updatePercent(val) {
  document.getElementById("donationDisplay").innerText = val + "%";
}

function completeCheckout() {
  const method = document.getElementById("paymentMethod").value;
  const charity = document.getElementById("charitySelect").value;
  const percent = document.getElementById("donationPercent").value;

  alert(`✅ Order confirmed!
Payment method: ${method}
Charity: ${charity}
Donated: ${percent}%
Thank you for your purchase and generosity!`);

  // Placeholder – real payment/donation logic goes here
}
