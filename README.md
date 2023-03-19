# raspi_scripts
Talking is cheap, (understanding and) coding is hard, and keeping code alive (and problem-solving) is harder~

## Projects

Scripts running alive on my Raspberry Pi:
- **jobs_notify** (Check its [README](https://github.com/lukeZhangMengxi/raspi_scripts/tree/master/jobs_notify) for detailed description.)

<br/>

## My Pi Setup
```
pi@raspberrypi:~ $ uname -a
Linux raspberrypi 4.19.97-v7+ #1294 SMP Thu Jan 30 13:15:58 GMT 2020 armv7l GNU/Linux


$ df -BM
Filesystem     1M-blocks  Used Available Use% Mounted on
/dev/root         29210M 3479M    24497M  13% /
devtmpfs            459M    0M      459M   0% /dev
tmpfs               464M    0M      464M   0% /dev/shm
tmpfs               464M    7M      457M   2% /run
tmpfs                 5M    1M        5M   1% /run/lock
tmpfs               464M    0M      464M   0% /sys/fs/cgroup
/dev/mmcblk0p1      253M   53M      200M  21% /boot
tmpfs                93M    0M       93M   0% /run/user/1000
```

- 4 ARM CPU
    ```
    pi@raspberrypi:~/mytmp $ hwinfo --cpu
    01: None 00.0: 10103 CPU                                        
        [Created at cpu.278]
        Unique ID: rdCR.j8NaKXDZtZ6
        Hardware Class: cpu
        Arch: ARM
        Vendor: "ARM Limited"
        Model: 0.4.0 ""
        Platform: "BCM2835"
        Features: half,thumb,fastmult,vfp,edsp,neon,vfpv3,tls,vfpv4,idiva,idivt,vfpd32,lpae,evtstrm,crc32,
        BogoMips: 76.80
        Config Status: cfg=new, avail=yes, need=no, active=unknown

    02: None 01.0: 10103 CPU
        [Created at cpu.278]
        Unique ID: wkFv.j8NaKXDZtZ6
        Hardware Class: cpu
        Arch: ARM
        Vendor: "ARM Limited"
        Model: 0.4.0 ""
        Platform: "BCM2835"
        Features: half
        BogoMips: 76.80
        Config Status: cfg=new, avail=yes, need=no, active=unknown

    03: None 02.0: 10103 CPU
        [Created at cpu.278]
        Unique ID: +rIN.j8NaKXDZtZ6
        Hardware Class: cpu
        Arch: ARM
        Vendor: "ARM Limited"
        Model: 0.4.0 ""
        Platform: "BCM2835"
        Features: half
        BogoMips: 76.80
        Config Status: cfg=new, avail=yes, need=no, active=unknown

    04: None 03.0: 10103 CPU
        [Created at cpu.278]
        Unique ID: 4zLr.j8NaKXDZtZ6
        Hardware Class: cpu
        Arch: ARM
        Vendor: "ARM Limited"
        Model: 0.4.0 ""
        Platform: "BCM2835"
        Features: half
        BogoMips: 76.80
        Config Status: cfg=new, avail=yes, need=no, active=unknown
    ```
- 896MB Memory
    ```
    pi@raspberrypi:~/mytmp $ hwinfo --memory
    01: None 00.0: 10102 Main Memory                                
        [Created at memory.74]
        Unique ID: rdCR.CxwsZFjVASF
        Hardware Class: memory
        Model: "Main Memory"
        Memory Range: 0x00000000-0x39e11fff (rw)
        Memory Size: 896 MB
        Config Status: cfg=new, avail=yes, need=no, active=unknown
    ```
- Network
    ```
    pi@raspberrypi:~/mytmp $ hwinfo --network
    09: None 00.0: 10701 Ethernet                                   
        [Created at net.126]
        Unique ID: usDW.ndpeucax6V1
        Parent ID: lfzD.Sed3PcmdZ23
        SysFS ID: /class/net/eth0
        SysFS Device Link: /devices/platform/soc/3f980000.usb/usb1/1-1/1-1.1/1-1.1:1.0
        Hardware Class: network interface
        Model: "Ethernet network interface"
        Driver: "smsc95xx"
        Driver Modules: "smsc95xx"
        Device File: eth0
        HW Address: b8:27:eb:44:0f:df
        Permanent HW Address: b8:27:eb:44:0f:df
        Link detected: no
        Config Status: cfg=new, avail=yes, need=no, active=unknown
        Attached to: #7 (Ethernet controller)

    10: None 00.0: 1070a WLAN
        [Created at net.126]
        Unique ID: AYEt.QXn1l67RSa1
        Parent ID: 0DfK.dZc7syf8JZ2
        SysFS ID: /class/net/wlan0
        SysFS Device Link: /devices/platform/soc/3f300000.mmcnr/mmc_host/mmc1/mmc1:0001/mmc1:0001:1
        Hardware Class: network interface
        Model: "WLAN network interface"
        Driver: "brcmfmac"
        Driver Modules: "brcmfmac", "brcmfmac"
        Device File: wlan0
        HW Address: b8:27:eb:11:5a:8a
        Permanent HW Address: b8:27:eb:11:5a:8a
        Link detected: yes
        Config Status: cfg=new, avail=yes, need=no, active=unknown
        Attached to: #4 (Network controller)

    11: None 00.0: 10700 Loopback
        [Created at net.126]
        Unique ID: ZsBS.GQNx7L4uPNA
        SysFS ID: /class/net/lo
        Hardware Class: network interface
        Model: "Loopback network interface"
        Device File: lo
        Link detected: yes
        Config Status: cfg=new, avail=yes, need=no, active=unknown
    ```
    and
    ```
    network:
        wlan0                Broadcom BCM43430 WLAN card
        eth0                 Standard Microsystems SMSC9512/9514 Fast Ethernet Adapter
    network interface:
        eth0                 Ethernet network interface
        wlan0                WLAN network interface
        lo                   Loopback network interface
    ```
