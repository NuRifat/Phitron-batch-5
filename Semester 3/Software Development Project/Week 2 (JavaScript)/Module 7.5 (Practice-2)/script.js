const searchItem = (searchText) => {
    fetch(`https://www.themealdb.com/api/json/v1/1/search.php?s=${searchText}`)
        .then(response => response.json())
        .then(data => {
            if (data.meals) {
                displayMeal(data.meals);
            } else {
                displayNotFound();
            }
        })
        .catch(err => console.log(err));
};

const displayMeal = (products) => {
    const productContainer = document.getElementById("meal-container");
    productContainer.innerHTML = "";

    products.forEach(product => {
        const div = document.createElement("div");
        div.classList.add("col-lg-3", "col-md-4", "col-sm-6");
        div.innerHTML = `
        <div class="card text-center h-100">
            <img class="card-img-top" src="${product.strMealThumb}" />
            <div class="card-body">
                <h5 class="card-title text-primary">${product.strMeal}</h5>
                <button class="btn btn-success mt-2" onclick="loadMealDetails(${product.idMeal})">Details</button>
            </div>
        </div>
        `;
        productContainer.appendChild(div);
    });
};

// load details by ID
const loadMealDetails = (idMeal) => {
    console.log(idMeal);
    fetch(`https://www.themealdb.com/api/json/v1/1/lookup.php?i=${idMeal}`)
        .then(res => res.json())
        .then(data => displayMealDetails(data.meals[0]))
        .catch(err => console.log(err));
};

// display details on top
const displayMealDetails = (meal) => {
    const detailContainer = document.querySelector(".details");
    detailContainer.innerHTML = `
    <div class="card mx-auto my-3 p-3" style="max-width: 400px; ">
        <img class="card-img-top" style="height:250px; " src="${meal.strMealThumb}" />
        <div class="card-body">
            <h2 class="card-title text-primary">${meal.strMeal}</h2>
            <p><strong>Category:</strong> ${meal.strCategory}</p>
            <p><strong>Area:</strong> ${meal.strArea}</p>
            <p>${meal.strInstructions.slice(0, 200)}...</p>
            <a href="${meal.strYoutube}" target="_blank" class="btn btn-danger">Watch Recipe</a>
        </div>
    </div>
    `;
};

// handle search submit
document.querySelector("form").addEventListener("submit", (event) => {
    event.preventDefault();
    const searchText = event.target.querySelector("input").value.trim();
    searchItem(searchText);
});
