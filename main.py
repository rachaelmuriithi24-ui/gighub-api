from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Optional

app = FastAPI(
    title="GigHub API - C027-01-0895/2024",
    description="API for managing freelance gigs",
    version="1.0.0"
)

# In-memory database
gigs_db = [
    {
        "id": 1,
        "title": "Social Media Manager",
        "description": "Manage social media pages and create engaging weekly content for a local business.",
        "category": "Marketing",
        "budget": 15000.0,
        "currency": "KES",
        "status": "Open",
        "client_name": "Jane Mwangi"
    },
    {
        "id": 2,
        "title": "Data Entry Specialist",
        "description": "Enter customer records into a company database with high accuracy and speed.",
        "category": "Data",
        "budget": 10000.0,
        "currency": "KES",
        "status": "Open",
        "client_name": "Peter Otieno"
    },
    {
        "id": 3,
        "title": "Business Consultant",
        "description": "Provide business strategy advice for a growing retail company in Nairobi.",
        "category": "Consulting",
        "budget": 30000.0,
        "currency": "KES",
        "status": "Open",
        "client_name": "Mercy Wanjiku"
    },
    {
        "id": 4,
        "title": "SEO Marketing Campaign",
        "description": "Improve website ranking using modern SEO techniques and keyword research.",
        "category": "Marketing",
        "budget": 18000.0,
        "currency": "KES",
        "status": "Open",
        "client_name": "David Kariuki"
    },
    {
        "id": 5,
        "title": "Excel Data Analysis",
        "description": "Analyze sales records and prepare monthly performance reports using Excel.",
        "category": "Data",
        "budget": 12000.0,
        "currency": "KES",
        "status": "In Progress",
        "client_name": "Ann Njeri"
    },
    {
        "id": 6,
        "title": "Financial Consultant",
        "description": "Advise a startup on budgeting, financial planning and investment strategies.",
        "category": "Consulting",
        "budget": 40000.0,
        "currency": "KES",
        "status": "Open",
        "client_name": "Kevin Mutiso"
    },
    {
        "id": 7,
        "title": "Email Marketing",
        "description": "Create weekly email campaigns and manage subscriber engagement.",
        "category": "Marketing",
        "budget": 14000.0,
        "currency": "KES",
        "status": "Closed",
        "client_name": "Sarah Achieng"
    },
    {
        "id": 8,
        "title": "Database Cleanup",
        "description": "Clean duplicate customer records and improve database accuracy.",
        "category": "Data",
        "budget": 9000.0,
        "currency": "KES",
        "status": "Open",
        "client_name": "Brian Ouma"
    },
    {
        "id": 9,
        "title": "HR Policy Consultant",
        "description": "Review company HR policies and recommend improvements for compliance.",
        "category": "Consulting",
        "budget": 35000.0,
        "currency": "KES",
        "status": "In Progress",
        "client_name": "Grace Wairimu"
    },
    {
        "id": 10,
        "title": "Digital Marketing Strategy",
        "description": "Develop a digital marketing strategy to increase online brand visibility.",
        "category": "Marketing",
        "budget": 22000.0,
        "currency": "KES",
        "status": "Open",
        "client_name": "John Kamau"
    }
]


class GigCreate(BaseModel):
    title: str = Field(min_length=5, max_length=100)
    description: str = Field(min_length=20, max_length=500)
    category: str = Field(pattern="^(Marketing|Data|Consulting)$")
    budget: float = Field(gt=0)
    client_name: str = Field(min_length=2, max_length=50)


class GigUpdate(BaseModel):
    budget: Optional[float] = Field(None, gt=0)
    status: Optional[str] = Field(
        None,
        pattern="^(Open|In Progress|Closed)$"
    )


@app.get("/")
def root():
    return {
        "message": "Welcome to the GigHub API!"
    }


@app.get("/gigs")
def get_gigs(
    category: Optional[str] = None,
    min_budget: Optional[float] = None,
    max_budget: Optional[float] = None
):
    """
    Return all gigs with optional filtering.
    """

    results = gigs_db

    if category:
        results = [
            gig for gig in results
            if gig["category"].lower() == category.lower()
        ]

    if min_budget is not None:
        results = [
            gig for gig in results
            if gig["budget"] >= min_budget
        ]

    if max_budget is not None:
        results = [
            gig for gig in results
            if gig["budget"] <= max_budget
        ]

    return results


@app.get("/gigs/search")
def search_gigs(q: str):
    """
    Search gigs by title.
    """

    results = []

    for gig in gigs_db:
        if q.lower() in gig["title"].lower():
            results.append(gig)

    return results


@app.get("/gigs/{gig_id}")
def get_gig(gig_id: int):
    """
    Return a single gig by its ID.
    """

    for gig in gigs_db:
        if gig["id"] == gig_id:
            return gig

    raise HTTPException(status_code=404, detail="Gig not found")


@app.post("/gigs")
def create_gig(gig: GigCreate):
    """
    Create a new gig.
    """

    for existing_gig in gigs_db:
        if existing_gig["title"].lower() == gig.title.lower():
            raise HTTPException(
                status_code=400,
                detail="A gig with this title already exists."
            )

    new_id = max(g["id"] for g in gigs_db) + 1

    new_gig = {
        "id": new_id,
        "title": gig.title,
        "description": gig.description,
        "category": gig.category,
        "budget": gig.budget,
        "currency": "KES",
        "status": "Open",
        "client_name": gig.client_name
    }

    gigs_db.append(new_gig)

    return {
        "message": "Gig created successfully",
        "gig": new_gig
    }


@app.put("/gigs/{gig_id}")
def update_gig(gig_id: int, gig_update: GigUpdate):
    """
    Update a gig's budget or status.
    """

    for index, gig in enumerate(gigs_db):

        if gig["id"] == gig_id:

            if gig_update.budget is not None:
                gigs_db[index]["budget"] = gig_update.budget

            if gig_update.status is not None:
                gigs_db[index]["status"] = gig_update.status

            return {
                "message": "Gig updated successfully",
                "gig": gigs_db[index]
            }

    raise HTTPException(status_code=404, detail="Gig not found")


@app.delete("/gigs/{gig_id}")
def delete_gig(gig_id: int):
    """
    Delete a gig.
    """

    for index, gig in enumerate(gigs_db):

        if gig["id"] == gig_id:
            deleted_gig = gigs_db.pop(index)

            return {
                "message": "Gig deleted successfully",
                "gig": deleted_gig
            }

    raise HTTPException(status_code=404, detail="Gig not found")