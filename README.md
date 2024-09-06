# SubNetter:  A Powerful Subnetting and VLSM Calculator 

[![Python](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)  

Subnetter is a command-line tool written in Python that simplifies subnet calculations and VLSM (Variable Length Subnet Masking) design. Whether you're a network engineer, IT professional, or student learning about networking, SubNetter provides the tools you need to work with IP addresses and subnets efficiently. 

## Features

* **Subnet Calculation:** Calculate subnet mask, network address, broadcast address, usable IP range, and more for a given network address in CIDR notation.
* **VLSM (Variable Length Subnet Masking):** Design and allocate subnets of varying sizes based on specific host requirements. 
* **Table Output:** Display VLSM results in an organized table format using the `tabulate` package (optional).
* **Error Handling:** Provides clear error messages for invalid inputs or insufficient address space. 

## Installation

1. **Prerequisites:** Make sure you have Python 3.6 or higher installed on your system.
2. **Install tabulate (optional):**  If you want to use table output, install the `tabulate` package:
   ```bash
   pip install tabulate
   ```
3. **Clone the Repository:**
   ```bash
   git clone https://github.com/0xShakhawat/subnetter.git
   ```

## Usage

```
python3 subnetter.py <network_address> [-s <subnet_host_counts>] [-t]
```

* **`<network_address>`:** The base network address in CIDR notation (e.g., 192.168.1.0/24).
* **`-s <subnet_host_counts>` (optional):** A comma-separated list of required host counts for each subnet (for VLSM calculations).
* **`-t` (optional):** Display the VLSM results in a table format (requires the `tabulate` package).

**Examples:**

* **Calculate a single subnet:**
   ```bash
   python3 subnetter.py 192.168.1.0/24
   ```

* **Calculate VLSM subnets:**
   ```bash
   python3 subnetter.py 192.168.1.0/24 -s 60,40,20,10,5,2
   ```

* **Calculate VLSM subnets and display results in a table:**
   ```bash
   python3 subnetter.py 192.168.1.0/24 -s 60,40,20,10,5,2 -t
   ```

## Want Even More Features? 

Check out the **Subnetter app on the Play Store!**  

[![SubNetter version](https://img.shields.io/endpoint?color=green&logo=google-play&logoColor=green&url=https%3A%2F%2Fplay.cuzi.workers.dev%2Fplay%3Fi%3Dme.shakhawat.subnetter%26gl%3DUS%26hl%3Den%26l%3DAndroid%26m%3D%24version)](https://play.google.com/store/apps/details?id=me.shakhawat.subnetter)   

[https://play.google.com/store/apps/details?id=me.shakhawat.subnetter](https://play.google.com/store/apps/details?id=me.shakhawat.subnetter)

The SubNetter app offers:

- **User-Friendly Interface:**  A graphical user interface for easier input and calculations.
- **Additional Tools:**  Includes a IP Class Detector, IP to Binary, Base Converter, CIDR Notation Converter, Wildcard Mask Calculator, Ping, and Traceroute tools. 
- **Subnetter Academy:** Interactive lessons and quizzes to help you master networking fundamentals.  

<br/>  
  
[<img src="https://raw.githubusercontent.com/0xShakhawat/0xShakhawat/main/img/play-store.png" alt="get it on play store" width="140"/>](https://play.google.com/store/apps/details?id=me.shakhawat.subnetter)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

- **Shakhawat Hossain (@0xShakhawat)**

**Let me know if you have any questions!** 