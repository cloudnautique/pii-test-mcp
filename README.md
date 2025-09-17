# FastMCP PII Filter Demo Server

A FastMCP server demonstrating PII filtering capabilities with customer data lookup tools.

## Features

- **Customer Lookup Tools:**
  - `lookup_customer(customer_id)` - Get full customer information by ID
  - `lookup_customer_by_name(name)` - Get full customer information by name
  - `lookup_customer_drivers_license(customer_id)` - Get driver's license info by ID
  - `list_customers()` - List all customers with names and IDs only

- **Built-in Prompts:**
  - `list_customers_prompt` - Prompt to list customers safely

## Quick Start

### Run directly from git repo:
```bash
uvx --from git+https://github.com/YOUR_USERNAME/YOUR_REPO.git fastmcp-server
```

### Run locally:
```bash
uv run main.py
```

### Docker:
```bash
docker build -t fastmcp-server .
docker run -p 8000:8000 fastmcp-server
```

## Sample Data

The server includes sample customer data with PII for testing:
- John Smith (ID: 001)
- Jane Doe (ID: 002)
- Bob Johnson (ID: 003)

Each customer record includes name, email, phone, SSN, driver's license, and address.