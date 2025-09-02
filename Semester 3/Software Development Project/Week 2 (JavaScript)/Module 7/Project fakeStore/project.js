const loadAllProduct = () => {
    fetch('https://fakestoreapi.com/products')
        .then(response => response.json())
        .then(data => displayProduct(data));
}
const displayProduct = (products) => {
    const productContainer = document.getElementById("product-container");
    products.forEach(product => {
        console.log(product);
        const div = document.createElement("div");
        div.classList.add("card");
        div.innerHTML = `
        <img class="card-img" src="${product.image}" alt="" />
        <h5>${product.title.slice(0, 20)}</h5>
        <h3>Price: ${product.price}</h3>
        <p>${product.description.slice(0, 50)}</p>
        <button onClick="singleProduct('${product.id}')">Details</button>
        <button onClick="handleAddtoCart('${product.title.slice(0, 10)}',${product.price})">Add to Cart</button>
        `;
        productContainer.appendChild(div);
    });
}

const handleAddtoCart = (name, price) => {
    const container = document.getElementById("cart-main-container")

    const div = document.createElement("div");
    div.classList.add("cart-info");
    div.innerHTML = `
    <p>${name}</p>
    <h3 class="price">${price}</h3>
    `;
    container.appendChild(div);
    updateTotal();

    const cartCount = document.getElementById("count").innerText;
    let convertedCount = parseInt(cartCount);
    convertedCount += 1;
    document.getElementById("count").innerText = convertedCount;
};

const updateTotal = () => {
    const allPrice = document.getElementsByClassName("price");
    let sum = 0;
    for (const element of allPrice) {
        sum = sum + parseFloat(element.innerText);
    }
    document.getElementById("total").innerText = sum.toFixed(2);
};

const singleProduct = (id) => {
    console.log(id);
    fetch(`https://fakestoreapi.com/products/${id}`)
        .then(response => response.json())
        .then(data => console.log(data));
};


loadAllProduct();