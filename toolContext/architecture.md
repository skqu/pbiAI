# Online Bookstore

## Purpose

The system allows customers to browse books, place orders, and track deliveries.

## Components

### Web Frontend

Responsibilities:
- Display products
- Handle user interaction
- Call backend APIs

Technology:
- React

### API Gateway

Responsibilities:
- Route requests
- Authentication
- Rate limiting

Technology:
- ASP.NET Core

### Product Service

Responsibilities:
- Manage book catalog
- Search products
- Product information

Technology:
- ASP.NET Core
- PostgreSQL

### Order Service

Responsibilities:
- Create orders
- Update order status
- Validate purchases

Technology:
- ASP.NET Core
- PostgreSQL

### Payment Service

Responsibilities:
- Process payments
- Communicate with payment provider

Technology:
- ASP.NET Core

### Notification Service

Responsibilities:
- Send order confirmations
- Send shipping notifications

Technology:
- ASP.NET Core
- RabbitMQ

## Data Flow

Customer
-> Web Frontend
-> API Gateway
-> Product Service

Customer
-> Web Frontend
-> API Gateway
-> Order Service
-> Payment Service

Order Service
-> Notification Service

## Non-Functional Requirements

- Support 10,000 users
- 99.9% availability
- GDPR compliant
- Secure customer data
`