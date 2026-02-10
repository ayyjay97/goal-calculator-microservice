# Goal Calculator Microservice

A lightweight microservice that calculates the absolute distance between a "current" value and a "goal" value. This service is designed to be used in the OSU CS361 Term Project.

## Features
* **Universal Calculation:** Works for weight (lbs), money ($), or game XP.
* **Direction Agnostic:** Correctly calculates distance whether the goal is higher or lower than the current value.
* **Decimal Support:** Handles precise float values (e.g., `260.5` to `225.0`).
* **JSON API:** Returns data in a standard format usable by Python, C++, and Node.js.
