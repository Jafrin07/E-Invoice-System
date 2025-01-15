# E-Invoice-System

## Introduction

The E-Invoice System is a Python-based desktop application designed to simplify the process of creating and managing invoices. Using `tkinter` for the graphical user interface and `docxtpl` for document generation, this system provides a seamless experience for users to input customer information, add products, and generate professional invoices.

## Features

- **Intuitive User Interface**: A clean and easy-to-use interface created with `tkinter`.
- **Customer Information**: Fields for entering customer name, address, and phone number.
- **Product Addition**: Dropdown menus for selecting products and quantities, along with input for the price per unit.
- **Invoice Generation**: Generates `.docx` format invoices with `docxtpl`.
- **Total Cost Calculation**: Automatically calculates the total cost of added products.
- **Reset Functionality**: Clear the form and start a new invoice with ease.

## Requirements

- Python 3.x
- `tkinter` (comes pre-installed with Python)
- `docxtpl`

To install `docxtpl`, use the following command:
```bash
pip install docxtpl
```

## Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/yourusername/e-invoice-system.git
    ```
2. Change to the project directory:
    ```bash
    cd e-invoice-system
    ```
3. Run the application:
    ```bash
    python main.py
    ```

## Usage

1. Enter customer details including name, address, and phone number.
2. Select the product, quantity, and enter the price per unit.
3. Click "Add Product" to add the item to the invoice list.
4. Once all products are added, click "Generate Invoice" to create the invoice document.
5. Use the "New Invoice" button to reset the form and start a new invoice.

## Future Enhancements

- **Validation**: Add input validation for customer details and product prices.
- **Enhanced UI**: Improve the visual appearance of the user interface.
- **Error Handling**: Implement error handling for better robustness.
- **Additional Features**: Incorporate features like saving and loading previous invoices.

## Contributing

Contributions are welcome! Please fork this repository and submit a pull request with your improvements or bug fixes.

## License

This project is licensed under the MIT License.

