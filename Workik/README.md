# Discord Bot with MySQL Authorization

## Introduction
This Discord bot is designed to authenticate servers using a MySQL database. It utilizes Discord.py for interaction and MySQL for server authorization.

## Prerequisites
- Python 3.7 or higher
- Discord.py library
- MySQL Connector library

## Installation
1. Install the required Python libraries:
    ```bash
    pip install discord.py mysql-connector-python
    ```

2. Set up a MySQL database with the following structure:
    ```sql
    CREATE TABLE discord_servers (
        id VARCHAR(255) PRIMARY KEY,
        auth_token VARCHAR(255) NOT NULL
    );
    ```

## Features
- **Authentication Command:** Use `!authenticate <auth_token>` to authenticate the server.
- **Hello Command:** Use `!hello` to check if the server is authenticated.

## How to Use
1. Clone or download the bot code from the repository.
2. Replace `"BOT-TOKEN"`, `"your-hostname"`, `"username"`, `"password"`, and `"your-database-name"` with your Discord bot token, MySQL database credentials, and database name in the last lines of the code.
3. Run the bot using the following command:
    ```bash
    python discord.py
    ```

## Commands
- `!authenticate <auth_token>`: Authenticate the server using the provided authentication token.
- `!hello`: Check if the server is authenticated and respond with a greeting.

## Example Usage
- To authenticate the server: `!authenticate YOUR_AUTH_TOKEN`
- To check if the server is authenticated: `!hello`

## Note
This bot requires a MySQL database for server authentication.

Feel free to contribute or report issues on [GitHub](https://github.com/yourusername/your-repository).
