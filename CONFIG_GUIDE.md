# Configuration Creation Guide

Welcome to the Configuration Creation Guide for PyPkiPractice! This document is intended to guide you through the 
process of creating autoconfiguration and manual configuration files for running the program.

The program is intended to be built in a way where the user's only interaction with the functionality is the initial
runtime of the file, with any other interactions being the viewing of the runtime processes and exploring the state
of each holder.

Because this, the environment that is passed in is the most important part of the process. There are two different
types of files that can be passed, called autoconfiguration and manual configuration. An autoconfiguration is
recognized as any file that has the word "auto" in it, while a manual configuration is any file that has the word 
"manual" in it.

# Autoconfiguration

Autoconfiguration files only set up the environment itself. The actual details of the holders in the network are
randomly generated, but top-level details are specified. You can use the Default_Configs folder to find examples to
guide this reading.

1) The first detail is the amount of levels in the ensuring PKI hierarchy. PKI architecture consists of a number of 
   levels of Certificate Authorities (CAs), with the highest level of CAs being the root CAs. The higher the level,
   the more authority they carry when signing the certificates of lower CAs. The lowest CAs will be the ones that
   directly sign the certificates of regular devices, called "End Certificates". For this reason, I will sometimes
   refer to those regular devices as "end devices". This detail is specified using the `level_count` parameter.
2) The second detail is the amount of holders that will be in each of the **n** levels you specified in `level_count`.
   This detail will be usually be entered in as a list of numbers in the syntax of `[x, y, z]`, where each number
   corresponds to a level going from the top-down. For example, given that `level_count` is equal to 3, the amount `x` 
   is the number of root CAs, the number `y` is the number of second-level intermediate CAs, and the number `z` is the 
   number of end devices. This detail is specified using the `count_by_level` parameter and must be written in a way
   where every next number has to be larger than the last. There is never more top-level CAs than bottom-level CAs. In
   addition, there must be as many settings in the list as there are levels.
3) The third and fourth details are the hashing algorithms used to create the holder's personal hash and sign
   certificates respectively. Both algorithms will enter a string value of one of the hashing algorithms supported by
   the program. The details are specified using the `uid_hash` and `sig_hash` parameters respectively.
   1) The supported algorithms are: SHA224, SHA256, SHA384, SHA512, SHA3_224, SHA3_256, SHA3_384, SHA3_512, BLAKE2b, 
      and BLAKE2s. Please type your chosen algorithm in all lowercase.
4) The fifth detail is the encryption algorithm used to encrypt messages and signatures. How this choice is described
   varies considerably from file format to file format, but commonly an algorithm and parameters are passed together.
   The supported algorithms are RSA and ECC algorithms, each with its own parameters. Use the example files to see how
   to set the detail. This detail is specified using the `encrypt_alg` parameter.
5) The last five details are level-by-level settings that are described in the same way as `count_by_level`.
   1) `revoc_probs` is the detail that sets the probability that a holder in a specific level will revoke a lower
      certificate or their own certificate. This setting must be a decimal value _inclusively_ between 0 and 1.
      Inclusively means that it can also be 0 and 1, but it cannot be outside the range any more than that.
   2) `cert_valid_durs` is the detail that states how long the certificate's validity would last for. It can either
      be a time in the **HH:MM:SS** time format, or the word "none" in all lowercase.
   3) `cache_durs` is the detail that states how long a validated certificate would reside in the local holder's
      certificate cache. It can either be a time in the **MM:SS** time format, or the word "none" in all lowercase.
   4) `cooldown_durs` is the detail that states how long a holder would wait before trying to send another message
      after a rejection or unexpected response. It can either be a number in seconds, or the word "none" in all
      lowercase.
   5) `timeout_durs` is the detail that states how long a holder would wait before timing out a sent message. It can 
      either be a number in seconds, or the word "none" in all lowercase.

These ten details are the only settings needed to run a PKI network simulation. However, if you wish for more detail,
you can also create a manual configuration file.

# Manual Configuration

Manual configuration files do not replace autoconfiguration files. A manual configuration file is more of an add-on to
an autoconfiguration file. It can be used to set the details of specific holders in the hierarchy. The specific format
will vary from file format to file format, but it will generally be organized by the name of the holder, followed by
details about its place in the environment and other details. You can use the Default_Configs folder to find examples to
guide this reading.

The following information describes everything that can be set for a specific holder.

## Holder name

As stated earlier, the name of the holder is the "key" in the key-value organization of the manual configuration file.
This name is a useful way to identify a specific holder in the environment to the user.

## Holder location

The holder location is the first major detail specified in the "values" of the holder. It is specified using the 
`location` parameter and specifies where the holder being set is in the environment. The `level` states the level
in the hierarchy from top to bottom, and the `holder` the position in the level from left to right. This is used to
identify which holder to start setting. If this detail is not specified, the entire key will be ignored.

## Holder environment overrides

The holder environment overrides is the second major detail specified in the "values" of the holder. It is specified
using the `env_overrides` parameter and is used if the default configuration in the autoconfiguration file is not
desired for a specific holder. This detail is optional, meaning if it is not there, the holder will use the
autoconfiguration settings. Much of the parameter names set in here are the same names as the ones in the
autoconfiguration file except for the last five where the 's' is removed. `level_count` and `count_by_level` are not
recognized in `env_overrides` since we only care about where now.

## Holder type info

The hardware, software, and account type of the holder is the third major detail specified in the "values" of the
holder. It is specified using the `holder_type_info` parameter and describes the underlying details of the device
holding the certificate. This detail is optional, meaning if it is not there, the holder will auto generate the
information. If it is there, be sure to spell everything correctly if you want some level of random generation. If the
program does not recognize a value, it may just copy the value over and over to fill in gaps.

### Hardware

* `hardware_type` specifies what type of device it is in general, and is categorized as one of the following:
  * 'endpoint' for an endpoint device
  * 'network' for a networking device
  * 'appliance' for a network appliance
  * 'peripheral' for a miscellaneous peripheral
* `hardware_subtype` specifies what type of device it is specifically, and has its own categories based on the 
  `hardware_type`:
  * 'endpoint' has the following subtypes:
    * 'desktop' for a desktop computer
    * 'laptop' for a laptop
    * 'server' for a server
    * 'phone' for a phone
    * 'iot' for an IoT device
  * 'network' has the following subtypes:
    * 'switch' for a switch
    * 'router' for a router
    * 'access point' for an access point
  * 'appliance' has the following subtypes:
    * 'firewall' for a firewall
    * 'utm' for a unified threat management device
  * 'peripheral' has the following subtypes:
    * 'usb_key' for a USB key
    * 'smart_card' for a smart card
    * 'external_storage' for an external storage device
* `hardware_brand` specifies the brand of the device. Each device can be made by a number of companies, and each 
  subtype has its own list of default companies. They won't be listed here for brevity, but you can check NOTES.md to
  find the information.

### Software

* `os_category` specifies what category of operating system it is in general, and is categorized as one of the
  following:
  * 'microsoft' for a Microsoft operating system
  * 'unix' for a Unix operating system
  * 'mobile' for a mobile operating system
  * 'routing' for a networking operating system
* `os_subcategory` specifies what type of operating system it is specifically, and has its own categories based on
  `os_category`:
  * 'microsoft' has the following subtypes:
    * 'windows' for a Windows operating system
    * 'windows_server' for a Windows Server operating system
  * 'unix' has the following subtypes:
    * 'linux' for a Linux operating system
    * 'bsd' for a BSD operating system
    * 'solaris' for a Solaris operating system
    * 'mac_os_x' for a Mac OS X operating system
  * 'mobile' has the following subtypes:
    * 'android' for an Android operating system
    * 'ios' for an iOS operating system
  * 'routing' has the following subtypes:
    * 'onie' for an ONIE operating system
    * 'onl' for an ONL operating system
    * 'opx' for an OPX operating system
    * 'dnos' for a DNOS operating system
    * 'junos' for a JunOS operating system
    * 'fboss' for a FBOSS operating system
    * 'sonic' for a SONiC operating system
    * 'aruba' for an ArubaOS operating system
    * 'cisco' for a Cisco IOS operating system
    * 'nxos' for a Nexus NOS operating system
    * 'openwrt' for an OpenWrt operating system
* `os_dist` specifies the distribution of the operating system and is based off of `os_subcategory`. As there are a lot
  of distributions, we won't list them here, but you can check NOTES.md to find the information.
* `os_subdist` specifies the sub-distribution or edition of the operating system and is based off of `os_dist`. As 
  there are a lot of these as well, we won't list them here, but you can check NOTES.md to find the information.

Some rules to note that will be expressed in random generation:

* Appliances and peripherals don't really have operating systems, so if they are chosen, they will just be treated as
  hardware devices without a major software.
* Networking devices can only use routing operating systems and Unix operating systems that are not MAC OS X.
* IoT devices can only use Unix operating systems that are not MAC OS X.
* Phones can only use mobile operating systems.
* Servers can only use Windows Server operating systems and Unix operating systems that are not MAC OS X.
* Laptops and Desktops can use anything but mobile operating systems.

### Account

* `account_type` specifies what type of account it is in general, and is categorized as one of the following:
  * 'user' for a user account
  * 'admin' for an admin account
  * 'system' for a system account
* `account_subtype` specifies what type of account it is specifically, and has its own categories based on
  `account_type`:
  * 'user' has the following subtypes:
    * 'guest' for a guest account
    * 'personal' for a personal account
    * 'enterprise' for an enterprise account
  * 'admin' has the following subtypes:
    * 'domain_admin' for a domain admin account
    * 'schema_admin' for a schema admin account
    * 'server_admin' for a server admin account
    * 'network_admin' for a network admin account
    * 'cloud_admin' for a cloud admin account
    * 'database_admin' for a database admin account
    * 'auditor' for an auditor account
* `ca_status` specifies the status of the certificate authority and is categorized as one of the following:
  * 'not_auth' for a certificate authority that is not an authority
  * 'inter_auth' for a certificate authority that is an intermediate authority
  * 'root_auth' for a certificate authority that is a root authority

Some rules to note that will be expressed in random generation:

* Holders that have no operating system type will be treated as a system account.
* Holders that use routing operating system will be treated as a system account.
* Holders that use Windows Server operating system will be treated as either a system or admin account.
* Holders that use Ubuntu Server operating system will be treated as either a system or admin account.

## Holder information

The details about the holder's organization itself is the fourth and last major detail specified in the "values" of the
holder. It is specified using the `holder_info` parameter. This detail is optional, meaning if it is not there, the 
holder will auto generate the information. In addition, if subkeys that are not found within the parameter will be
interpreted as missing and the program will autogenerate.

* `common_name` specifies the common name of the certificate authority or device.
* `country` specifies the country of the certificate authority or device.
* `state` specifies the state or region of the certificate authority or device.
* `locality` specifies the city, town, or locality of the certificate authority or device.
* `org` specifies the organization of the certificate authority or device.
* `org_unit` specifies the organizational unit of the certificate authority or device.
* `email` specifies the email address of the certificate authority or device.
* `url` specifies the URL of the certificate authority or device.

## Closing notes about manual generation

The above parameters are everything that can be manually set for a specific holder. Each default manual configuration
example (except for the JSON one) also has comments that explain everything in depth. Please refer to them for guidance
on how to set up manual configuration.

In addition, it must be emphasized that the manual configuration file is **OPTIONAL**. This means that you can also
decide to not specify some parameters, or only specify the ones you WANT to change. You will see this if looking
the examples, as while some are fully specified, others leave many details up to the random generation and environment
parameters.
