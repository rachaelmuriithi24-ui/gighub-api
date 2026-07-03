GigHub API

Project Description

GigHub API is a RESTful API developed using FastAPI to manage freelance gig listings. The API enables clients to post freelance jobs and allows users to view, search, update, and delete gig records. It uses an in-memory database to store gig information, making it suitable for learning and demonstrating backend API development concepts.

# Features

The API provides the following functionality:
* View all available gigs.
* Filter gigs by category and budget range.
* Search for gigs by title.
* View the details of a specific gig using its ID.
* Create a new gig listing.
* Update the budget or status of an existing gig.
* Delete a gig that is no longer available.

# Technologies Used

This project was developed using the following technologies:

   * Python 3
   * FastAPI
   * Pydantic
   * Uvicorn

# API Endpoints

The API implements the following endpoints:

 * GET /  – Displays a welcome message.
 * GET /gigs – Returns all gigs, with optional filtering by category and budget.
 * GET /gigs/search  – Searches for gigs by title using a query parameter.
 * GET /gigs/{gig_id} – Returns details of a specific gig based on its ID.
 * POST /gigs – Creates a new gig after validating the input data.
 * PUT /gigs/{gig_id}  – Updates the budget or status of an existing gig.
 * DELETE /gigs/{gig_id} – Deletes a gig from the database.

# How to Run the Project

 *To run the application:

   1. Install Python 3 on your computer.

   2. Install the required packages:

    * FastAPI
    * Uvicorn

  3. Open the project folder in the terminal.

  4. Run the command:

    `uvicorn main:app --reload`

  5. Open your web browser and visit:

   * Swagger UI: http://127.0.0.1:8000/docs
   * ReDoc Documentation: http://127.0.0.1:8000/redoc

# Admission Number

   C027-01-0895/2024

# Author

  Rachael Muriithi Njeri

# Conclusion

  The GigHub API demonstrates the implementation of a RESTful web service using FastAPI. It provides complete CRUD operations, input validation through Pydantic models, search and filtering functionality, and proper error handling. The project meets the requirements for managing freelance gig listings and serves as a practical example of backend API development.

