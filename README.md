# spfwalk.py

`spfwalk.py` is a Python script that queries and retrieves SPF (Sender Policy Framework) records for a given domain. It recursively fetches included records.

## Requirements

- Python 3.x
- dnspython library (install using `pip install dnspython`)

## Usage

```
python spfwalk.py [-v] domain
```


### Options

- `-v` or `--verbose`: Enable verbose mode to display query and recursion steps

## Example

```
$ python3 spfwalk.py -v microsoft.com

Querying TXT records for microsoft.com...
Recursively querying included domain: _spf-c.microsoft.com...
Querying TXT records for _spf-c.microsoft.com...
Recursively querying included domain: _spf-a.microsoft.com...
Querying TXT records for _spf-a.microsoft.com...
Recursively querying included domain: spf.protection.outlook.com...
Querying TXT records for spf.protection.outlook.com...
Recursively querying included domain: spf-a.hotmail.com...
Querying TXT records for spf-a.hotmail.com...
Recursively querying included domain: _spf-ssg-a.msft.net...
Querying TXT records for _spf-ssg-a.msft.net...
Recursively querying included domain: _spf1-meo.microsoft.com...
Querying TXT records for _spf1-meo.microsoft.com...
Recursively querying included domain: _spf-b.microsoft.com...
Querying TXT records for _spf-b.microsoft.com...
Recursively querying included domain: _spf-mdm.microsoft.com...
Querying TXT records for _spf-mdm.microsoft.com...

IP Records:
ip4:65.55.111.0/24
ip4:65.54.51.64/26
ip4:131.253.30.0/24
ip6:2a01:111:f403:8000::/50
ip4:52.100.0.0/14
ip4:65.54.241.0/24
ip4:65.55.90.0/24
ip4:65.52.80.137/32
ip4:65.54.190.0/24
ip4:104.47.0.0/17
ip4:65.55.116.0/25
ip4:157.58.196.96/29
ip4:66.119.150.192/26
ip4:207.46.22.98/29
ip4:52.234.172.96/28
ip4:206.191.224.0/19
ip4:23.103.224.0/19
ip4:65.55.34.0/24
ip4:20.63.210.192/28
ip4:104.44.112.128/25
ip6:2a01:111:f403::/49
ip6:2a01:111:f400::/48
ip4:134.170.174.0/24
ip4:134.170.113.0/26
ip4:40.107.0.0/16
ip4:157.58.30.128/25
ip6:2a01:111:f403:f000::/52
ip4:157.56.120.128/26
ip4:207.46.117.0/24
ip4:131.253.121.0/26
ip4:134.170.141.64/26
ip4:157.55.0.192/26
ip6:2a01:111:f403:c000::/51
ip4:20.94.180.64/28
ip4:167.220.67.232/29
ip4:134.170.143.0/24
ip4:40.92.0.0/15
ip4:52.236.28.240/28
ip4:65.54.61.64/26
ip4:65.55.42.224/28
ip4:157.55.2.0/25
ip4:157.55.1.128/26
ip4:52.185.106.240/28

Include Records:
spf-a.hotmail.com
_spf-c.microsoft.com
_spf-ssg-a.msft.net
_spf-a.microsoft.com
_spf1-meo.microsoft.com
_spf-b.microsoft.com

Fail Type: -all
```

# greetz

Sup [swarley](https://github.com/swarley7/)