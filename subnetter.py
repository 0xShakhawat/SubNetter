#!/usr/bin/env python3

import ipaddress
import argparse

# tabulate package import condition
try:
    from tabulate import tabulate
    TABULATE_AVAILABLE = True
except ImportError:
    TABULATE_AVAILABLE = False

def calculate_vlsm(network, subnets):
    network = ipaddress.IPv4Network(network)
    subnets = sorted(subnets, reverse=True)  # sort
    allocated_subnets = []
    current_address = network.network_address

    for host_count in subnets:
        needed_subnet = find_appropriate_subnet(current_address, host_count)

        # fitting subnets in available spaces
        if needed_subnet['network'] <= network.broadcast_address:
            allocated_subnets.append(needed_subnet)
            current_address = needed_subnet['broadcast'] + 1
        else: 
            print(f"Insufficient address space for the host requirement of {host_count}.")

    display_subnets(allocated_subnets, subnets)

    return allocated_subnets # list of allocated subnets

def calculate_subnet(network):
    network = ipaddress.IPv4Network(network)
    subnet_info = {
        'IP Address': str(network),
        'Subnet Mask': str(network.netmask),
        'Wildcard Mask': str(network.hostmask),
        'Network Bits': network.prefixlen,
        'Host Bits': 32 - network.prefixlen,
        'Usable Hosts': network.num_addresses - 2,
        'Network Address': str(network.network_address),
        'First IP': str(network.network_address + 1),
        'Last IP': str(network.broadcast_address - 1),
        'Broadcast Address': str(network.broadcast_address)
    }
    return subnet_info



def find_appropriate_subnet(start_address, hosts_required):

    # prefix_length adjustment
    if hosts_required > 2:
        prefix_length = 32 - (hosts_required + 2 - 1).bit_length()
    else:
        # minimum subnet size for small subnets needing only 2 hosts
        prefix_length = 30  
    subnet = ipaddress.IPv4Network((start_address, prefix_length), strict=False)

    return {
        'network': subnet.network_address,
        'mask': subnet.netmask,
        'first_address': subnet.network_address + 1,
        'last_address': subnet.broadcast_address - 1,
        'broadcast': subnet.broadcast_address,
        'available_hosts': (subnet.num_addresses - 2),
        'cidr': subnet
    }

def display_subnet(subnet_info):
    for key, value in subnet_info.items():
        print(f"{key}: {value}")


def display_subnets(subnets, required_hosts):
    for i, subnet in enumerate(subnets):
        print(f"Subnet {i + 1}:")
        print(f"  Network IP: {subnet['network']}")
        print(f"  Broadcast IP: {subnet['broadcast']}")
        print(f"  First Host IP: {subnet['first_address']}")
        print(f"  Last Host IP: {subnet['last_address']}")
        print(f"  Subnet Mask: {subnet['mask']}")
        print(f"  Subnet IP: {subnet['cidr']}")
        print(f"  Available Hosts: {subnet['available_hosts']}")
        print(f"  Needed Hosts: {required_hosts[i]}")
        print("")

def display_subnets_table(subnets, required_hosts):
    headers = ["Subnet", "Network IP", "Broadcast IP", "First Host IP", "Last Host IP", 
               "Subnet Mask", "Subnet IP", "Available Hosts", "Needed Hosts"]
    table_data = []
    for i, subnet in enumerate(subnets):
        table_data.append([
            i+1,
            subnet['network'], 
            subnet['broadcast'],
            subnet['first_address'],
            subnet['last_address'],
            subnet['mask'],
            subnet['cidr'],
            subnet['available_hosts'],
            required_hosts[i]
        ])

    print(tabulate(table_data, headers=headers, tablefmt="grid"))

def display_banner():
    # ascii art banner

    banner = """

       _____ _    _ ____  _   _ ______ _______ _______ ______ _____  
      / ____| |  | |  _ \| \ | |  ____|__   __|__   __|  ____|  __ \ 
     | (___ | |  | | |_) |  \| | |__     | |     | |  | |__  | |__) |
      \___ \| |  | |  _ <| . ` |  __|    | |     | |  |  __| |  _  / 
      ____) | |__| | |_) | |\  | |____   | |     | |  | |____| | \ \ 
     |_____/ \____/|____/|_| \_|______|  |_|     |_|  |______|_|  \_\


           Created by @0xShakhawat         
    """
    print(banner)

    print("-" * 50) 
    print(" A powerful tool for subnet and VLSM calculations.")
    print("-" * 50) 
    print("\n Also check out the SubNetter app on the Play Store:")
    print(" https://play.google.com/store/apps/details?id=me.shakhawat.subnetter")
    print("   - A user-friendly subnet calculator with additional tools and an Academy!\n")



def main():
    display_banner()
    parser = argparse.ArgumentParser(description="SubNetter - Subnetting Calculator Tool")
    parser.add_argument('network', help="Network address in CIDR format (e.g., 192.168.1.0/24)")
    parser.add_argument('-s', '--subnets', type=str, help="Comma-separated list of required subnets or host counts (for VLSM)")
    parser.add_argument('-t', '--table', action='store_true', help="Display results in a table (requires 'tabulate' package)")

    args = parser.parse_args()

    if args.subnets:
        subnets = [int(h) for h in args.subnets.split(',')] 
        calculated_subnets = calculate_vlsm(args.network, subnets) # storing calculated subnet info

        # view table format if -t is used and tabulate is available
        if args.table:
            if TABULATE_AVAILABLE:
                display_subnets_table(calculated_subnets, args.subnets) # passing calculated subnets 
            else:
                print("Error: The 'tabulate' package is required for table output. "
                      "Please install it using 'pip install tabulate'.")
    else:
        subnet_info = calculate_subnet(args.network)
        display_subnet(subnet_info)


if __name__ == "__main__":
    main()