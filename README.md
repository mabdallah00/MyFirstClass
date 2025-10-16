# MyFirstClass

# EventEase - Event Planning System (Python + Flask)

## Overview
EventEase is a simple event planning system that demonstrates class creation, inheritance, interfaces, reflection, and a Flask API.

## Features
- Base class `Event` (5 properties, 2 methods)
- Inherited class `PartyEvent`
- Reflection to print class properties
- Interface using `abc` module
- Flask API that returns JSON
- UML and Wireframe demonstrating MVC architecture

## How to Run
### Run the main app

# EventEase — Functional Requirements

**Project Name:** Party Event 
**Host:** Maysam Abdallah  
**Date:** October 2025  
**Version:** 1.0

## 1. Introduction

### 1.1 Purpose
The purpose of this document is to outline the functional requirements for EventEase, a web-based event management system. The system allows users to create, manage, and track events efficiently. This document provides details about the features, components, and behavior of the system based on the UML design and use cases.

### 1.2 Scope
EventEase is designed to simplify event organization for hosts and attendees. The application will allow users to:
- Create and edit event details (title, date, time, location, theme, and guest list)
- View event summaries and dashboards
- Manage guests and RSVPs
- Send event reminders
- Store and retrieve event data using a database backend

Architecture: **MVC** — Model (data), View (UI), Controller (business logic).

## 2. System Overview

### 2.1 System Architecture
- **Model:** Handles data storage and retrieval of events and users.
- **View:** Displays forms, event summaries, and dashboards.
- **Controller:** Processes user input, validates data, and updates the Model and View.

### 2.2 System Users
1. **Event Host** — create, edit, delete events, invite guests, view reports.  
2. **Guest** — view event details, RSVP, update attendance status.

## 3. Functional Requirements (summary)

| ID    | Requirement Name    | Description                                                                      | Priority |
|-------|---------------------|----------------------------------------------------------------------------------|----------|
| FR-1  | User Registration   | Allow users to create an account with email and password.                       | High     |
| FR-2  | User Login          | Allow registered users to log in securely.                                      | High     |
| FR-3  | Create Event        | Allow users to create events with title, date, time, venue, theme, and guests.  | High     |
| FR-4  | Edit Event          | Allow users to modify event details.                                            | Medium   |
| FR-5  | Delete Event        | Allow users to delete events.                                                    | Medium   |
| FR-6  | View Event Summary  | Display event information in a summary format.                                  | High     |
| FR-7  | Manage Guests       | Allow hosts to add, remove, or edit guest information.                          | High     |
| FR-8  | RSVP Response       | Guests can RSVP "Yes", "No", or "Maybe."                                        | High     |
| FR-9  | Notifications       | Send reminders or updates to hosts and guests.                                  | Low      |
| FR-10 | Data Storage        | Store event and user data in a database.                                        | High     |

## 4. Non-Functional Requirements

- **NFR-1 Performance:** pages should load < 2s.
- **NFR-2 Security:** user credentials must be encrypted; follow best-practice auth.
- **NFR-3 Usability:** responsive and user-friendly UI (mobile + desktop).
- **NFR-4 Reliability:** target 99% uptime.
- **NFR-5 Maintainability:** follow MVC and clean code patterns.

## 5. Use Case Summary

### Use Case: Create Event
- **Actor:** Event Host  
- **Description:** Host creates a new event with title, date, time, venue, theme, and guest list.  
- **Precondition:** User logged in.  
- **Postcondition:** Event saved to DB.

### Use Case: Edit Event
- **Actor:** Event Host  
- **Description:** Host updates event details.  
- **Precondition:** Event exists.  
- **Postcondition:** Event updated.

### Use Case: RSVP to Event
- **Actor:** Guest  
- **Description:** Guest responds to invitation.  
- **Precondition:** Guest received invite.  
- **Postcondition:** RSVP stored.

### Use Case: View Event Summary
- **Actor:** Host or Guest  
- **Description:** Shows event summary on dashboard.  
- **Precondition:** User authenticated.  
- **Postcondition:** Event details displayed.

## 6. Components

- **Event Model:** stores title, date, time, venue, theme, host id, guest list. (UC1–UC4)  
- **User Model:** stores user profile and auth data. (UC1, UC3)  
- **Event Controller:** create / edit / delete events. (UC1–UC2)  
- **RSVP Controller:** manage RSVPs. (UC3)  
- **Dashboard View:** event summaries & analytics. (UC4)

## 7. UML Reference
Include Use Case and Class Diagrams in the repo under `/docs/uml/`.

## 8. Testing Requirements (summary)

| Test ID | Feature            | Test Description                          | Expected Result                       |
|---------|--------------------|-------------------------------------------|---------------------------------------|
| T-1     | User Registration  | Create new account                        | Account created successfully          |
| T-2     | Event Creation     | Create event with valid data              | Event shown on dashboard              |
| T-3     | Event Editing      | Update event details                      | Updated data persisted                |
| T-4     | RSVP               | Guest responds to invitation              | RSVP saved and shown                  |
| T-5     | Data Persistence   | Refresh and revisit event page            | Event data persists in DB             |

## 9. References
- UML diagrams (in `/docs/uml/`)  
- MVC architectural plan  
- EventEase base class code

