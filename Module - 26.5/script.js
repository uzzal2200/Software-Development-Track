document.addEventListener('DOMContentLoaded', function() {
    const productList = document.getElementById('productList');
    const categoryFilter = document.getElementById('categoryFilter');

    // Fetch categories
    fetch('https://fakestoreapi.com/products/categories')
        .then(response => response.json())
        .then(categories => {
            categories.forEach(category => {
                const option = document.createElement('option');
                option.value = category;
                option.textContent = category;
                categoryFilter.appendChild(option);
            });
        });

    // Fetch products
    function fetchProducts(category = 'all') {
        let url = 'https://fakestoreapi.com/products';
        if (category !== 'all') {
            url += `/category/${category}`;
        }

        fetch(url)
            .then(response => response.json())
            .then(products => {
                productList.innerHTML = '';
                products.forEach(product => {
                    const productDiv = document.createElement('div');
                    productDiv.classList.add('product');
                    productDiv.innerHTML = `
                        <img src="${product.image}" alt="${product.title}">
                        <h3>${product.title}</h3>
                        <p>Price: $${product.price}</p>
                        <a href="product.html?id=${product.id}">View Details</a>
                    `;
                    productList.appendChild(productDiv);
                });
            });
    }

    categoryFilter.addEventListener('change', function() {
        fetchProducts(categoryFilter.value);
    });

    // Initial fetch of all products
    fetchProducts();
});
