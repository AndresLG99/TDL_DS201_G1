# To-Do List

A console-based To-Do List application built with Python that allows users to manage tasks interactively. 
It includes functionality to add, delete, and view tasks, as well as a basic AI logic that suggests tasks based on priority and deadline.

## 📂 Table of Contents

- [About](#about)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [Contact](#contact)

## 📌 About

This project was created as a simple yet functional task management tool that runs in the terminal. The goal is to help users keep track of their daily responsibilities through a clean, menu-driven interface.

A basic AI logic is integrated to suggest tasks based on common routines, which adds a helpful touch for users who may need inspiration or reminders.

The project is written in **Python** and focuses on building logic, user input handling, and menu design — making it a great exercise for learning and practicing console applications in programming.

Tasks are stored with a user-defined **priority** and **deadline**, which the AI suggestion module uses to recommend the most urgent or important task.

The application is written in **Python**, and makes use of the following libraries:
- `art` – for styled text banners
- `datetime` – for handling task deadlines

## ✨ Features

- 📌 **Add tasks** with priority and deadline
- 🗑️ **Delete tasks** by ID
- 📋 **View all added tasks**
- 🤖 **Suggest tasks** using a basic AI logic based on urgency
- ❌ **Exit the application** via the menu

## ⚙️ Installation

Clone the repository and run the main script:

```bash
git clone https://github.com/AndresLG99/TDL_DS201_G1.git
```
```bash
cd TDL_DS201_G1
```
```bash
python index.py
```

Ensure you have Python 3 installed.

Required libraries: ```art```, ```datetime```. Install missing packages via:
```bash
pip install art
```

## 🚀 Usage

When you run index.py, you will be presented with a menu:

1. Add task
2. Remove task
3. View tasks
4. Suggest tasks
5. Exit

Select an option by typing the number and pressing Enter. The program will guide you through each interaction.

## 👥 Team
This project was developed collaboratively by:

- Akiko Keira
- Andres Lopez
- Daniel Carranza
- Melissa Osorio

## 🤝 Contributing
We welcome contributions! To contribute:

1. Fork this repository.
2. Create a new branch. 
``` bash
git checkout -b feature/YourFeature
```
3. Commit your changes. 
``` bash
git commit -m 'Add new feature'
```
4. Push to the branch. 
``` bash
git push origin feature/YourFeature
```
5. Open a Pull Request.

## 📬 Contact
For questions or suggestions, feel free to reach out through GitHub Issues or contact one of the team members directly.

Project Repository: https://github.com/AndresLG99/TDL_DS201_G1