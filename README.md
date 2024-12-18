Banking System Simulator
This project is a console-based Banking System Simulator implemented in Python, providing a comprehensive framework for managing bank accounts and operations.

Key Features
Account Management: Create, deposit, withdraw, and close accounts. Accounts include attributes such as account number, account holder details, PIN, and balance.
Bank Functionality: Manage up to 100 accounts, add monthly interest, and list all active accounts.
Coin Conversion: Parse coin strings into monetary values using the CoinCollector class.
Utility Functions: Input validation, dollar-to-cents conversion, and random number generation handled by the BankUtility class.
Interactive Menu: The BankManager class provides an easy-to-use interface for managing accounts, transactions, and viewing details.
Classes Overview
Account: Manages individual account data and transactions.
Bank: Stores and handles up to 100 accounts.
CoinCollector: Converts coin strings to monetary values in cents.
BankUtility: Offers utility methods for validations and random number generation.
BankManager: Provides the main menu and handles user interactions.
Program Execution
The program starts by creating a BankManager object and launching the interactive menu for banking operations. Users can manage accounts, perform transactions, view details, and exit the system when finished.
