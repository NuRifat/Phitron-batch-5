// Load all cocktails
const allCocktail = () => {
    fetch('https://www.thecocktaildb.com/api/json/v1/1/search.php?f=a')
        .then(response => response.json())
        .then(data => displayProduct(data.drinks))
        .catch(err => console.log(err));
};

//Search cocktail by name
const searchItem = (searchText) => {
    fetch(`https://www.thecocktaildb.com/api/json/v1/1/search.php?s=${searchText}`)
        .then(response => response.json())
        .then(data => {
            if (data.drinks) {
                displayProduct(data.drinks);
            } else {
                displayNotFound();
            }
        })
        .catch(err => console.log(err));
};

//display Item
const displayProduct = (products) => {
    const productContainer = document.getElementById("meal-container");
    productContainer.innerHTML = ""; // clear previous result

    products.forEach(product => {
        console.log(product);
        const div = document.createElement("div");
        div.classList.add("col-lg-4", "col-md-6", "col-sm-12");
        div.innerHTML = `
        <div class="card text-center h-100">
            <img class = "card-img-top" src="${product.strDrinkThumb}" />
            <div class = "card-body">
                <h5 class="card-title">Name: ${product.strGlass} </h5>
                <h6 class="card-subtitle mb-2 text-muted">Category: ${product.strCategory.slice(0, 20)}</h6>
                <p class="card-text">${product.strInstructions.slice(0, 15)}...</p>
                <button class="btn btn-outline-primary" onClick="handleAddToCart('${product.strDrinkThumb}','${product.strGlass}')">Add to Cart</button>
                <button class="btn btn-outline-success" onClick="showDetails('${product.strGlass}','${product.strDrinkThumb}','${product.strCategory}','${product.strAlcoholic}','${product.strInstructions}')">Details</button>
            </div>
       </div>
       `;
        productContainer.appendChild(div);
    });
}

//show not found message
const displayNotFound = () => {
    const productContainer = document.getElementById("meal-container");
    productContainer.innerHTML = `
        <div class="col-12 text-center">
            <h3>Your searched drink is not found</h3>
        </div>
    `;
}

// Cart function 
const handleAddToCart = (img, name) => {
    const table = document.getElementById("cart-body");

    const cartCount = document.getElementById("cart-count").innerText;
    let convertedCount = parseInt(cartCount);
    if (convertedCount >= 7) {
        alert("You can not add more than 7 items.");
        return;
    }
    convertedCount += 1;
    document.getElementById("cart-count").innerText = convertedCount;

    const row = document.createElement("tr");
    row.innerHTML = `
        <td>${convertedCount}</td>
        <td><img src="${img}" style="width:40px;" class="rounded-circle"></td>
        <td>${name}</td>
    `;

    table.appendChild(row);
}

// Modal details function
const showDetails = (name, img, category, alcohol, instruction) => {
    const title = document.getElementById("modal-title");
    title.innerText = name;

    const body = document.querySelector(".modal-body");
    body.innerHTML = `
        <div style="height:370px; display: flex; flex-direction: column;">
            <div style="height: 220px; overflow: hidden; text-align: center;">
                <img src="${img}" style="width: 100%; height: 100%; object-fit: cover;" class="rounded">
            </div>
            <div>
                <p>Details</p>
                <p>Category: <strong>${category}</strong></p>
                <p>Alcoholic: <strong>${alcohol}</strong></p>
                <p>${instruction}</p>
            </div>
        </div>
    `;

    const modalElement = document.getElementById("staticBackdrop");
    const modal = new bootstrap.Modal(modalElement);
    modal.show();
}

// Handle search submit
document.querySelector("form").addEventListener("submit", (event) => {
    event.preventDefault(); // stops page reload
    const searchText = event.target.querySelector("input").value.trim();
    if (searchText) {
        searchItem(searchText);
    } else {
        allCocktail(); // load default again if empty search
    }
});

allCocktail();
