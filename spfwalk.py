import dns.resolver
import argparse

def get_spf_records(domain, seen_domains=None, verbose=False):
    if seen_domains is None:
        seen_domains = set()

    if domain in seen_domains:
        return set(), set(), None

    seen_domains.add(domain)
    spf_records = set()
    fail_type = None

    try:
        if verbose:
            print(f"Querying TXT records for {domain}...")
        answers = dns.resolver.resolve(domain, 'TXT')
        for answer in answers:
            for txt_data in answer.strings:
                if txt_data.startswith(b'v=spf1'):
                    spf_records.update(parse_spf(txt_data.decode('utf-8')))
                    if '-all' in spf_records:
                        fail_type = '-all'
                    elif '~all' in spf_records:
                        fail_type = '~all'
    except dns.resolver.NXDOMAIN:
        print(f"No SPF record found for {domain}")
        return set(), set(), None
    except dns.resolver.NoAnswer:
        print(f"No TXT records found for {domain}")
        return set(), set(), None
    except dns.resolver.Timeout:
        print(f"Timeout while querying {domain}")
        return set(), set(), None

    ip_records = set()
    include_records = set()

    for record in spf_records:
        if record.startswith('include:'):
            included_domain = record.split(':')[1]
            include_records.add(included_domain)
            if verbose:
                print(f"Recursively querying included domain: {included_domain}...")
            included_ip_records, _, included_fail_type = get_spf_records(included_domain, seen_domains, verbose)
            ip_records.update(included_ip_records)

            if included_fail_type == '-all':
                fail_type = '-all'
            elif included_fail_type == '~all' and fail_type != '-all':
                fail_type = '~all'
        elif '/' in record:  # Assume it's an IP address
            ip_records.add(record)

    return ip_records, include_records, fail_type

def parse_spf(spf_record):
    # Simple SPF record parser
    return spf_record.split()

def main():
    parser = argparse.ArgumentParser(description='SPF Record Walker')
    parser.add_argument('domain', help='Domain to query for SPF records')
    parser.add_argument('-v', '--verbose', action='store_true', help='Enable verbose mode')

    args = parser.parse_args()
    
    ip_records, include_records, fail_type = get_spf_records(args.domain, verbose=args.verbose)

    print("\nIP Records:")
    for record in ip_records:
        print(record)

    print("\nInclude Records:")
    for record in include_records:
        print(record)

    if fail_type:
        print(f"\nFail Type: {fail_type}")

if __name__ == "__main__":
    main()
