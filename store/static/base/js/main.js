function displayProducts(products) {
    const productListDiv = document.getElementById('productList');
    productListDiv.innerHTML = ''; // Clear previous content
    products.forEach(product => {
        const productDiv = document.createElement('div');
        productDiv.textContent = `${product.name} - $${product.price}`;
        productListDiv.appendChild(productDiv);
    });
}

function getProducts() {
    const xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function () {
        if (xhr.readyState === XMLHttpRequest.DONE) {
            if (xhr.status === 200) {
                const data = JSON.parse(xhr.responseText);
                displayProducts(data);
            } else {
                console.error('Error fetching products:', xhr.status);
            }
        }
    };

    xhr.open('GET', '/list_product', true); // Replace with your API endpoint
    xhr.send();
}

// Call the getProducts function when the page finishes loading
window.onload = function () {
    getProducts();
};