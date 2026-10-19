# GitHub Portfolio Analyzer

A command-line Python application that analyzes a public GitHub profile and displays useful information about the user and their repositories.

The application uses the **GitHub REST API** to retrieve profile data and repository statistics from a GitHub username entered by the user.

## 🚀 Features

- Validate whether a GitHub username exists
- Display GitHub profile information
- Show username, name, and bio
- Display followers and following count
- Show number of public repositories
- Display account creation date
- Display GitHub profile URL
- List repositories returned by GitHub
- Show repository language and description
- Show stars and forks
- Display open issues
- Display repository topics
- Show repository last-updated time
- Interactive terminal menu

## 🛠️ Tech Stack

- Python 3
- Requests
- GitHub REST API

## 📁 Project Structure

```text
GitHub-Portfolio-Analyzer/
├── main.py
├── exp.py
└── README.md
```

### `main.py`

Main command-line application used to fetch and display GitHub profile and repository information.

### `exp.py`

Experimental/development version of the application.

## 📋 Requirements

Make sure Python 3 is installed.

Install the required Python package:

```bash
pip install requests
```

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/qxet456/GitHub-Portfolio-Analyzer.git
```

Move into the project directory:

```bash
cd GitHub-Portfolio-Analyzer
```

Install the dependency:

```bash
pip install requests
```

## ▶️ Usage

Run the application:

```bash
python main.py
```

The program displays:

```text
--------------------
OPTIONS
--------------------
A. CONTINUE
B. EXIT
--------------------
```

Choose:

```text
A
```

Then enter the GitHub username you want to analyze.

For example:

```text
Type username: qxet456
```

The program retrieves the user's public GitHub information and displays it in the terminal.

Choose:

```text
B
```

to exit the application.

## 👤 Profile Information

The analyzer can display:

- Username
- Name
- Bio
- Followers
- Following
- Public repository count
- Account creation date
- GitHub profile URL

## 📊 Repository Information

For each repository returned by the GitHub API, the application displays:

- Repository name
- Primary programming language
- Description
- Stars
- Forks
- Open issues
- Last updated date
- Repository URL
- Topics

## 🔍 How It Works

The application sends HTTP `GET` requests to GitHub's API.

Profile endpoint:

```text
https://api.github.com/users/{username}
```

Repository endpoint:

```text
https://api.github.com/users/{username}/repos
```

The JSON responses are parsed using Python and the relevant information is displayed in the terminal.

## ⚠️ Current Limitations

- The application currently uses unauthenticated GitHub API requests, so GitHub API rate limits apply.
- GitHub's repository API uses pagination, so users with many repositories may not have every repository returned by a single request.
- The project currently runs entirely through the command line.
- Network and API errors could use additional handling.

## 🔮 Future Improvements

Possible improvements include:

- GitHub API authentication
- Pagination for retrieving all repositories
- Portfolio scoring
- Repository ranking
- Programming-language statistics
- Better exception handling
- GitHub API rate-limit handling
- JSON export
- CSV export
- Automated tests
- Web interface
- Graphical statistics and charts

## 🎯 Purpose

This project was created to practice:

- Working with REST APIs
- HTTP requests
- JSON parsing
- Python loops and conditionals
- Command-line applications
- Processing GitHub repository data

It can also serve as the foundation for a more advanced **GitHub developer portfolio analyzer**.

## 👨‍💻 Author

Created by [qxet456](https://github.com/qxet456).

---

If you find this project useful, consider giving it a ⭐.