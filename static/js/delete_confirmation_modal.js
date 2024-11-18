var deleteModal = document.getElementById("deleteModal");

// When the modal is shown, set the product name and form action
deleteModal.addEventListener("show.bs.modal", function (event) {
  var button = event.relatedTarget; // Button that triggered the modal
  var productId = button.getAttribute("data-product-id"); // Extract product ID from data-* attributes
  var productName = button.getAttribute("data-product-name"); // Extract product name
  var url = button.getAttribute("data-url-name"); // Extract product delete URL

  // Update the modal content
  var productNameElement = document.getElementById("product-name");
  productNameElement.textContent = productName;

  // Update the form action to point to the correct delete URL
  var form = document.getElementById("delete-form");
  form.action = url; // Set the action URL directly from the data attribute
});
