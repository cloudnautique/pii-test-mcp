import asyncio
from typing import Any, Dict, List, Optional
from fastmcp import FastMCP
from pydantic import BaseModel

app = FastMCP("PII Filter Demo Server")

CUSTOMERS = {
    "001": {
        "name": "John Smith",
        "email": "john.smith@email.com",
        "phone": "(555) 123-4567",
        "ssn": "123-45-6789",
        "drivers_license": "DL123456789",
        "address": "123 Main St, Anytown, ST 12345"
    },
    "002": {
        "name": "Jane Doe",
        "email": "jane.doe@email.com",
        "phone": "(555) 987-6543",
        "ssn": "987-65-4321",
        "drivers_license": "DL987654321",
        "address": "456 Oak Ave, Somewhere, ST 67890"
    },
    "003": {
        "name": "Bob Johnson",
        "email": "bob.johnson@email.com",
        "phone": "(555) 555-0123",
        "ssn": "456-78-9012",
        "drivers_license": "DL456789012",
        "address": "789 Pine St, Elsewhere, ST 13579"
    }
}

class CustomerInfo(BaseModel):
    customer_id: str

class DriversLicenseInfo(BaseModel):
    customer_id: str

@app.tool()
def lookup_customer(customer_id: str) -> Dict[str, Any]:
    """Look up a customer by their ID and return safe information (name and address only)"""
    customer = CUSTOMERS.get(customer_id)
    if not customer:
        return {"error": f"Customer {customer_id} not found"}

    return {
        "customer_id": customer_id,
        "name": customer["name"],
        "address": customer["address"]
    }

@app.tool()
def lookup_customer_full(customer_id: str) -> Dict[str, Any]:
    """Look up a customer's full information including ALL PII data (SSN, driver's license, email, phone)"""
    customer = CUSTOMERS.get(customer_id)
    if not customer:
        return {"error": f"Customer {customer_id} not found"}

    return {
        "customer_id": customer_id,
        "customer_info": customer
    }

@app.tool()
def list_customers() -> Dict[str, Any]:
    """List all customers showing only their names and IDs"""
    customers_list = []
    for customer_id, customer_data in CUSTOMERS.items():
        customers_list.append({
            "customer_id": customer_id,
            "name": customer_data["name"]
        })

    return {"customers": customers_list}


@app.prompt()
def list_customers_prompt() -> str:
    """List all customers in the system"""
    return """Please use the list_customers tool to show all customers in the system. Display only their names and customer IDs for privacy."""

def main():
    """Main entry point for the FastMCP server"""
    app.run()

if __name__ == "__main__":
    main()