# certbot-1cloud
1cloud.ru authenticator plugin for Certbot

An authenticator plugin for [certbot](https://certbot.eff.org/) to support [Let's Encrypt](https://letsencrypt.org/) 
DNS challenges (dns-01) for domains managed by the nameservers of [1cloud.ru](https://1cloud.ru).

## Requirements
* certbot>=0.39.0

## Installation

1. Clone or download this repository
2. Install using pip3
   ```
   sudo pip3 install .
   ```
3. Configure credentials at /etc/letsencrypt/1cloud.ini and set file rights to 0600
   ```
   sudo <your editor> /etc/letsencrypt/1cloud.ini
   sudo chmod 0600 /etc/letsencrypt/1cloud.ini
   ```

## Usage
Use authenticator with certbot:
```
sudo certbot certonly -a certbot-1cloud:dns -d example.com -d *.example.com
```

## Command Line Options
```
 --certbot-1cloud:dns-propagation-seconds PROPAGATION_SECONDS
                        The number of seconds to wait for DNS to propagate
                        before asking the ACME server to verify the DNS record. 
                        (default: 120)
 --certbot-1cloud:dns-credentials PATH_TO_CREDENTIALS
                        Path to 1cloud.ru account credentials INI file 
                        (default: /etc/letsencrypt/1cloud.ini)

```

## Removal
```
sudo pip3 uninstall certbot-1cloud
```
