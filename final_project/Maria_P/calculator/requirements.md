--- Beer Calculator App ---

-- Business problem --

Homebrweing - brewing beer in small batches at home - is an expensive hobby, especially due to the cost of the ingredients.
To optimize their costs, homebrewers need to carefully track their ingredients and to plan their recipes and the needed ingredients.
In addition, they need to know the cost of an ingredient in a recipe, so they can plan and use the best ingredient in the optimal quantity.


--- Requirements ---

Create an application to help homebrewers calculate the cost of using an ingredient and track their ingredients and recipes. 

Requirements overview

1. The application will have 3 main functionalities: Costs, Ingredients, Recipes
2. Users will be able to access a 'Home' page.
3. Users will be able to calculate the cost of using an ingredient in a recipe.
4. Users will be able to see a list of calculate costs
5. Users will be able to add an ingredient
6. Users will be able to see a list of added ingredients
7. Users will be able to add a recipe
8. Users will be able to see a list of added recipes

Requirements description

1. Pages overview
As a user I want to a see consistent design with identifiable elements across all pages so that I can easily recognize the application

Acceptance criteria:
- Have a descriptive title for each page
- Have on each page a navigation bar with 4 elements: 'Home, 'Costs', 'Ingredients', 'Recipes'
- Have on each page social media buttons for Facebook, Instagram, Twitter, LinkedIn and Pinterest
- Have on each page a footer with basic copyright information
- Have a relevant favicon

2. 'Home' page
As a user I want to have a Home page so that I can understand the purpose of the application and navigate to each main section/functionality of the application

Acceptance criteria:
- Have a carousel with a relevant image and the stated purpose for main section/functionality of the application
- Have a button leading to each main section under the carousel

3. 'Costs' page
As a user I want to see all calculated costs so that I can plan my ingredients for each recipe

Acceptance criteria:
- Have table displaying for each cost: 'Recipe', 'Ingredient', 'Quantity (g)', 'Cost (RON)' (calculated cost) and 'Date & Time' (of cost calculation)
    - Show newest costs at the top of the table
- Have a buton to open the 'Calculate Cost' page
- If there are no calculated costs, the text 'No costs are available' will be displayed instead of the table

4. 'Calculate Cost' page
As a user I want to calculate the cost of using an ingredient in a specific quantity so that I can better plane my recipes

Acceptance criteria:
- Have a form with the following fields: 'Recipe' - drop-down with all recipes; 'Ingredient' - drop-down with all ingredients; 'Quantity (g) - numeric field; 'Date & Time' - DateTime field pre-filled with curent date and time
- Have 2 buttons: 'Submit' and 'Cancel'
- User will be able to calculate a cost by filling all fields with correct data and clicking on 'Calculate' button
- The cost will be computed using the price of the ingredient and the quntity entered by the user for the cost
- User will be able to cancel the calculation by clicking on 'Cancel' button
- Both 'Calculate' and 'Cancel' actions will take the user to the 'Costs' page


5. 'Ingredients' page
As a user I want to see all ingredients so that I can track my ingredients

Acceptance criteria:
- Have table displaying for each ingredient: 'Name', 'Type', 'Quantity (g)', 'Price (RON/100g)' and 'Update Date & Time'
    - Show ingredients in alphabetical order
- Have a buton to open the 'Add Ingredient' page
- If there are no ingredients, the text 'No ingredients are available' will be displayed instead of the table

6. 'Add Ingredient' page
As a user I want to add an ingredient so that I can better track my ingredients

Acceptance criteria:
- Have a form with the following fields: 'Name' - text field; 'Ingredient Type' - drop-down with pre-defined ingredient types; 'Quantity (g) - numeric field; 'Price for 100 g (RON)' - numeric field; 'Update Date & Time' - DateTime field pre-filled with curent date and time
- Have 2 buttons: 'Add' and 'Cancel'
- User will be able to add an ingredient by filling all fields with correct data and clicking on 'Add' button
- User will be able to cancel by clicking on 'Cancel' button
- Both 'Add' and 'Cancel' actions will take the user to the 'Ingredients' page

7. 'Recipes' page
As a user I want to see all recipes so that I can track my recipes and plan the needed ingredients

Acceptance criteria:
- Have table displaying for each recipe: 'Name', 'Type', 'Ingredients' and 'Update Date & Time'
    - Show recipes in alphabetical order
- Have a buton to open the 'Add Recipe' page
- If there are no recipes, the text 'No recipes are available' will be displayed instead of the table

8. 'Add Recipe' page
As a user I want to add a recipe so that I can better track my recipes and the ingredients I need for each of them

Acceptance criteria:
- Have a form with the following fields: 'Name' - text field; 'Recipe Type' - drop-down with pre-defined recipe types; 'Ingredients' - multiple-choice field with all available ingredients; 'Update Date & Time' - DateTime field pre-filled with curent date and time
- Have 2 buttons: 'Add' and 'Cancel'
- User will be able to add an recipe by filling all fields with correct data and clicking on 'Add' button
- User will be able to cancel by clicking on 'Cancel' button
- Both 'Add' and 'Cancel' actions will take the user to the 'Recipe' page

9. 'Admin' functionality
As an Admin user I want to have access to the 'Admin' interface so that I can manage the entities in the application

Acceptance criteria:
- Enable the Admin interface available for Costs, Ingredients, Ingredient Types, Recipes and Recipe Types
- Customize Admin interface to show available fields for each model
- Enable 'Search' functionality for 'Name' field (Ingredients, Ingredient Types, Recipes and Recipe Types) and 'Ingredient' and 'Recipe' fields (Costs)
- Enable links on 'Name' field (Ingredients, Ingredient Types, Recipes and Recipe Types)





The user will be able see all ingredients
The user will be able to add a new ingredient with a dedicated form.
Each ingredient will have a name, a type, a quantity in grames, a price in RON for 100 grames and a date of update.
The list of ingredient types will be pre-defined.

--Recipes--
The user will be able to see all recipes and to add a new recipe.
The user will be able to add a new recipe with a dedicated form.
Each recipe will have a name, a type, one or more ingredients and a date of update.
The list of recipe types will be pre-defined.


--Costs--
The user will be able to select a recipe, input the quantity of each ingredient needed in the recipes and calculate the recipe costs based on the price for 100 g.


The Admin view will be activated for Ingredients, Ingredient Types, Recipes, Recipe Types and Recipe Costs.