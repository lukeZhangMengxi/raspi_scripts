# Apt install `hwinfo` failed due to expired certificate

## Problem

The suggested action from `apt` did not work.

```
pi@raspberrypi:~ $ sudo apt install -y hwinfo
Reading package lists... Done
Building dependency tree       
Reading state information... Done
The following additional packages will be installed:
  libhd21
The following NEW packages will be installed:
  hwinfo libhd21
0 upgraded, 2 newly installed, 0 to remove and 385 not upgraded.
Need to get 658 kB of archives.
After this operation, 2,866 kB of additional disk space will be used.
Err:1 https://mirrors.switch.ca/raspbian/raspbian buster/main armhf libhd21 armhf 21.63-3
  Certificate verification failed: The certificate is NOT trusted. The certificate chain uses expired certificate.  Could not handshake: Error in the certificate verification. [IP: 209.115.181.106 443]
Err:2 https://mirrors.switch.ca/raspbian/raspbian buster/main armhf hwinfo armhf 21.63-3
  Certificate verification failed: The certificate is NOT trusted. The certificate chain uses expired certificate.  Could not handshake: Error in the certificate verification. [IP: 209.115.181.106 443]
E: Failed to fetch https://mirrors.switch.ca/raspbian/raspbian/pool/main/h/hwinfo/libhd21_21.63-3_armhf.deb  Certificate verification failed: The certificate is NOT trusted. The certificate chain uses expired certificate.  Could not handshake: Error in the certificate verification. [IP: 209.115.181.106 443]
E: Failed to fetch https://mirrors.switch.ca/raspbian/raspbian/pool/main/h/hwinfo/hwinfo_21.63-3_armhf.deb  Certificate verification failed: The certificate is NOT trusted. The certificate chain uses expired certificate.  Could not handshake: Error in the certificate verification. [IP: 209.115.181.106 443]
E: Unable to fetch some archives, maybe run apt-get update or try with --fix-missing?
```

<br/>

## Verification
Using `wget` also got the issue.
```
pi@raspberrypi:~/mytmp $ wget https://mirrors.switch.ca/raspbian/raspbian/pool/main/h/hwinfo/libhd21_21.63-3_armhf.deb
--2023-03-19 15:46:44--  https://mirrors.switch.ca/raspbian/raspbian/pool/main/h/hwinfo/libhd21_21.63-3_armhf.deb
Resolving mirrors.switch.ca (mirrors.switch.ca)... 209.115.181.106
Connecting to mirrors.switch.ca (mirrors.switch.ca)|209.115.181.106|:443... connected.
ERROR: The certificate of ‘mirrors.switch.ca’ is not trusted.
ERROR: The certificate of ‘mirrors.switch.ca’ has expired.
```

<br/>

## Fix
However `curl` actually got it working.
I tried `curl` because I wanted to see the verbose log via `-v`; while as it is working, I can simply `apt install` the local deb file.

Note:
There are two deb file required `libhd21_21.63-3_armhf.deb` and `hwinfo_21.63-3_armhf.deb`, I got the URL or the two by:
1. `sudo apt install -y hwinfo` first time reports error for the first URL: https://mirrors.switch.ca/raspbian/raspbian/pool/main/h/hwinfo/libhd21_21.63-3_armhf.deb
2. `curl` download the first URL
3. `sudo apt install ${downloaded}`
4. Now `sudo apt install -y hwinfo` reports error for the second URL: https://mirrors.switch.ca/raspbian/raspbian/pool/main/h/hwinfo/hwinfo_21.63-3_armhf.deb
5. `curl` download the first URL
6. `sudo apt install ${downloaded}`
7. Then `hwinfo` works

```
pi@raspberrypi:~/mytmp $ curl https://mirrors.switch.ca/raspbian/raspbian/pool/main/h/hwinfo/libhd21_21.63-3_armhf.deb --output libhd21_21.63-3_armhf.deb -v
* Expire in 0 ms for 6 (transfer 0x1be2880)
* Expire in 1 ms for 1 (transfer 0x1be2880)
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0* Expire in 0 ms for 1 (transfer 0x1be2880)
* Expire in 2 ms for 1 (transfer 0x1be2880)
* Expire in 0 ms for 1 (transfer 0x1be2880)
* Expire in 0 ms for 1 (transfer 0x1be2880)
* Expire in 2 ms for 1 (transfer 0x1be2880)
* Expire in 0 ms for 1 (transfer 0x1be2880)
* Expire in 0 ms for 1 (transfer 0x1be2880)
* Expire in 2 ms for 1 (transfer 0x1be2880)
* Expire in 0 ms for 1 (transfer 0x1be2880)
* Expire in 0 ms for 1 (transfer 0x1be2880)
* Expire in 2 ms for 1 (transfer 0x1be2880)
* Expire in 0 ms for 1 (transfer 0x1be2880)
* Expire in 0 ms for 1 (transfer 0x1be2880)
* Expire in 2 ms for 1 (transfer 0x1be2880)
* Expire in 1 ms for 1 (transfer 0x1be2880)
* Expire in 1 ms for 1 (transfer 0x1be2880)
* Expire in 2 ms for 1 (transfer 0x1be2880)
* Expire in 1 ms for 1 (transfer 0x1be2880)
* Expire in 1 ms for 1 (transfer 0x1be2880)
* Expire in 2 ms for 1 (transfer 0x1be2880)
* Expire in 1 ms for 1 (transfer 0x1be2880)
* Expire in 1 ms for 1 (transfer 0x1be2880)
* Expire in 2 ms for 1 (transfer 0x1be2880)
* Expire in 2 ms for 1 (transfer 0x1be2880)
* Expire in 2 ms for 1 (transfer 0x1be2880)
* Expire in 4 ms for 1 (transfer 0x1be2880)
* Expire in 2 ms for 1 (transfer 0x1be2880)
* Expire in 2 ms for 1 (transfer 0x1be2880)
* Expire in 4 ms for 1 (transfer 0x1be2880)
* Expire in 3 ms for 1 (transfer 0x1be2880)
* Expire in 3 ms for 1 (transfer 0x1be2880)
* Expire in 4 ms for 1 (transfer 0x1be2880)
* Expire in 3 ms for 1 (transfer 0x1be2880)
* Expire in 3 ms for 1 (transfer 0x1be2880)
* Expire in 4 ms for 1 (transfer 0x1be2880)
* Expire in 4 ms for 1 (transfer 0x1be2880)
* Expire in 4 ms for 1 (transfer 0x1be2880)
* Expire in 8 ms for 1 (transfer 0x1be2880)
* Expire in 5 ms for 1 (transfer 0x1be2880)
* Expire in 5 ms for 1 (transfer 0x1be2880)
* Expire in 8 ms for 1 (transfer 0x1be2880)
* Expire in 5 ms for 1 (transfer 0x1be2880)
* Expire in 5 ms for 1 (transfer 0x1be2880)
* Expire in 7 ms for 1 (transfer 0x1be2880)
*   Trying 209.115.181.106...
* TCP_NODELAY set
* Expire in 200 ms for 4 (transfer 0x1be2880)
  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0* Connected to mirrors.switch.ca (209.115.181.106) port 443 (#0)
* ALPN, offering h2
* ALPN, offering http/1.1
* successfully set certificate verify locations:
*   CAfile: none
  CApath: /etc/ssl/certs
} [5 bytes data]
* TLSv1.3 (OUT), TLS handshake, Client hello (1):
} [512 bytes data]
* TLSv1.3 (IN), TLS handshake, Server hello (2):
{ [122 bytes data]
* TLSv1.3 (IN), TLS handshake, Encrypted Extensions (8):
{ [25 bytes data]
* TLSv1.3 (IN), TLS handshake, Certificate (11):
{ [4034 bytes data]
* TLSv1.3 (IN), TLS handshake, CERT verify (15):
{ [264 bytes data]
* TLSv1.3 (IN), TLS handshake, Finished (20):
{ [52 bytes data]
* TLSv1.3 (OUT), TLS change cipher, Change cipher spec (1):
} [1 bytes data]
* TLSv1.3 (OUT), TLS handshake, Finished (20):
} [52 bytes data]
* SSL connection using TLSv1.3 / TLS_AES_256_GCM_SHA384
* ALPN, server accepted to use http/1.1
* Server certificate:
*  subject: CN=mirrors.switch.ca
*  start date: Feb  6 15:15:31 2023 GMT
*  expire date: May  7 15:15:30 2023 GMT
*  subjectAltName: host "mirrors.switch.ca" matched cert's "mirrors.switch.ca"
*  issuer: C=US; O=Let's Encrypt; CN=R3
*  SSL certificate verify ok.
} [5 bytes data]
> GET /raspbian/raspbian/pool/main/h/hwinfo/libhd21_21.63-3_armhf.deb HTTP/1.1
> Host: mirrors.switch.ca
> User-Agent: curl/7.64.0
> Accept: */*
> 
{ [5 bytes data]
* TLSv1.3 (IN), TLS handshake, Newsession Ticket (4):
{ [57 bytes data]
* TLSv1.3 (IN), TLS handshake, Newsession Ticket (4):
{ [57 bytes data]
* old SSL session ID is stale, removing
{ [5 bytes data]
< HTTP/1.1 200 OK
< Server: nginx/1.18.0 (Ubuntu)
< Date: Sun, 19 Mar 2023 22:47:39 GMT
< Content-Type: application/octet-stream
< Content-Length: 627148
< Last-Modified: Wed, 06 Mar 2019 10:08:07 GMT
< Connection: keep-alive
< ETag: "5c7f9c07-991cc"
< Accept-Ranges: bytes
< 
{ [16117 bytes data]
100  612k  100  612k    0     0  1615k      0 --:--:-- --:--:-- --:--:-- 1615k
* Connection #0 to host mirrors.switch.ca left intact

pi@raspberrypi:~/mytmp $ ls
libhd21_21.63-3_armhf.deb
```
