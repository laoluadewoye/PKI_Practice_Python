# Table of Contents

1) ### [Goals](#Goals)
2) ### [Utilities Structure](#Utilities-Structure)
3) ### [Defining a Holder](#Defining-a-Holder)
4) ### [Final Class Designs](#Final-Class-Designs)
5) ### [File Design](#File-Design)
6) ### [Process](#Process)
7) ### [Requirements List](#Requirements-List)

# Goals

* Play with default class functions
* Play with Enums
* Play with decorative functions (@)
  * A logging decorator
  * Using class decorators (classmethod, staticmethod, attribute, setter)
  * Using dataclass decorator for simple data structures
* Play with creating environments through JSON/YAML files
* Play with passing filepaths as arguments
* Play with hash tables
* Play with "updating" terminal outputs
* Play with load balancing CAs
* Play with auto-generating environments
* Play with testing
* Play with package files
* Play with documentation
* Play with using dataclasses for messages
* Play with AsciiDoc
* Play with TLA+?
* Play with git pushes and signed commits

# Utilities Structure

## Functionality should exist for-

* The Certificate Authority
  * Both Root and Intermediate
* The Certificate Subject and Relying Party
* Certificate Signing Requests
* Certificate Chains
* The Registration Authority
* Renewing and Revoking Certificates
* Certificate Revocation Lists, OCSP, and real-time validation
* Temporary Certificate Local Caching
* General Communication supported by above PKI functionality

The Certificate Authority should be able to keep a database of certificates

## A certificate object should have-

* My own custom certificate object.
* A certificate object from the Cryptography library. - May not be needed anymore
* The holder's unique ID.
* The certificate authority's unique ID.

## Info on certificate content and signing-

* https://www.ssl.com/faqs/what-is-an-x-509-certificate/
* https://learn.microsoft.com/en-us/azure/iot-hub/reference-x509-certificates
* https://medium.com/@kennch/introduction-to-pki-public-key-infrastructure-e7863c9232f9
* https://www.nist.gov/identity-access-management/personal-identity-verification-piv
* https://www.youtube.com/watch?v=5OqgYSXWYQM

## The certificate itself includes-

* The name of the certificate
* Subject Information
  * Country
  * State/Province
  * Locality
  * Organization
  * Organization Unit
  * Common name of the Subject's URL
  * Contact email address
* Issuer Information
  * Country
  * State/Province
  * Locality
  * Organization
  * Common name of Issuing CA certificate
* Certificate Information
  * Unique Serial Number
  * X.509 Version
  * Signature (Hash) Algorithm
  * Validity Range (Exclusive Edges)
* Public Key Information
  * Encryption Algorithm
  * Public Key
  * Key Size
  * Key Usage Cases
* Certificate Signature

# Defining a Holder

## Possible Holders

A holder can be anything that holds a certificate. This includes-

1) Accounts
   1) user
      1) guest
      2) personal
      3) enterprise
   2) admin
      1) domain_admin
      2) schema_admin
      3) server_admin
      4) network_admin
      5) cloud_admin
      6) database_admin
      7) auditor
   3) system
2) Operating Systems
   1) microsoft
      1) windows
         1) windows_2000
            1) professional
            2) server
            3) advanced_server
            4) datacenter_server
         2) windows_xp
            1) home
            2) professional
         3) windows_vista
            1) starter
            2) home_basic
            3) home_premium
            4) business
            5) enterprise
            6) ultimate
         4) windows_7
            1) starter
            2) home_basic
            3) home_premium
            4) business
            5) enterprise
            6) ultimate
         5) windows_8
            1) home
            2) pro
            3) enterprise
         6) windows_10
            1) home
            2) pro
            3) educational
            4) enterprise
         7) windows_11
            1) home
            2) pro
            3) educational
            4) enterprise
      2) windows_server
         1) windows_server_2003
            1) web
            2) standard
            3) enterprise
            4) datacenter
         2) windows_server_2008
            1) web
            2) standard
            3) enterprise
            4) datacenter
            5) itanium
            6) foundation
            7) hpc
         3) windows_server_2012
            1) foundation
            2) essentials
            3) standard
            4) datacenter
         4) windows_server_2016
            1) standard
            2) datacenter
         5) windows_server_2019
            1) standard
            2) datacenter
         6) windows_server_2022
            1) standard
            2) datacenter
            3) datacenter_azure
   2) unix
      1) linux
         1) debian
            1) ubuntu
            2) linux_mint
            3) kali_linux
            4) raspberry_pi
            5) mx_linux
            6) debian
         2) red_hat
            1) red_hat
            2) fedora
            3) cent_os
         3) arch_linux
         4) gentoo
         5) suse
            1) opensuse
            2) suse_linux_enterprise
         6) alpine
         7) nix_os
         8) qubes_os
         9) ubuntu_server
      2) bsd
         1) freebsd
         2) openbsd
         3) netbsd
      3) solaris
      4) mac_os_x
         1) leopard
         2) snow_leopard
         3) lion
         4) mountain_lion
         5) mavericks
         6) yosemite
         7) el_capitan
         8) sierra
         9) high_sierra
         10) mojave
         11) catalina
         12) big_sur
         13) monterey
         14) ventura
         15) sonoma
         16) sequoia
   3) mobile
      1) ios
      2) android
         1) nougat
         2) oreo
         3) pie
         4) 10
         5) 11
         6) 12
         7) 13
         8) 14
         9) 15
         10) 16
   4) routing
      1) ONIE (Open Network Install Environment)
      2) ONL (Open Network Linux)
      3) OPX (OpenSwitch)
      4) DNOS (Dell Network OS)
      5) Junos OS
      6) FBOSS (Facebook Open Switching System)
      7) SONiC (Software for Open Networking in the Cloud)
      8) ArubaOS
      9) Cisco IOS
      10) NX-OS (Nexus NOS)
      11) OpenWrt
3) Hardware
   1) endpoint
      1) desktop
         1) hewlett_packard
         2) acer
         3) dell
         4) lenovo
         5) toshiba
         6) ibm
         7) fujitsu
         8) nec
         9) apple
      2) laptop
         1) samsung
         2) razer
         3) microsoft
         4) msi
         5) asus
         6) acer
         7) dell
         8) lenovo
         9) hewlett_packard
         10) apple
      3) phone
         1) samsung
         2) apple
         3) huawei
         4) sony
         5) google
         6) microsoft
         7) toshiba
         8) dell
      4) server
         1) dell
         2) hewlett_packard
         3) supermicro
         4) inspur
         5) lenovo
         6) huawei
         7) ibm
         8) fukitsu
         9) cisco
      5) iot
         1) advantech
         2) raspberry_pi
         3) arduino
         4) nvidia
         5) beagleboard
         6) udoo
         7) onlogic
         8) kontron
         9) arbor
         10) axiomtek
   2) network
      1) router
         1) cisco
         2) peplink
         3) advantech
         4) netgear
         5) tp_link
      2) switch
         1) anchor
         2) honeywell
         3) philips
         4) siemens
         5) cisco
         6) hpl
      3) access_point
         1) cisco
         2) fortinet
         3) netgear
         4) zyxel
         5) tp_link
         6) engenius
   3) appliance
      1) firewall
         1) bitdefender
         2) cisco
         3) fortinet
         4) palo_alto
         5) netgate
         6) watchguard
         7) sonicwall
      2) utm (i.e. IDS/IPS, DLP, AC, Proxy)
         1) sonicwall
         2) fortigate
         3) barracuda
         4) juniper
         5) trellix
         6) palo_alto
   4) peripheral
      1) usb_key
         1) samsung
         2) sandisk
         3) corsiar
         4) kingston
         5) pny
      2) smart_card
         1) thales
         2) nxp_semiconductors
         3) cardlogix
         4) infineon
      3) external_storage
         1) seagate
         2) western_digital
         3) sandisk
         4) transcend
         5) lacie

## Holder Identifier

{Hardware Type}.{OS}.{App, Person, or Service}

Short-hand example: Dell.Windows_10.Personal

Long-hand example: Endpoint_Desktop_Dell.Microsoft_Windows_Windows_10.User_Personal

Exceptions include when the OS or Device itself is the Holder, but they still need a unique identifier.

## A Holder Object should have-

* Their Holder type information
* Their Authority information
* Anything required to create a certificate without extensions
* A link that they can be accessed by the simulated network
  * Don't try to use an actual network, just a bunch of fake addresses should work. 
* A hash generated from object content that can used to organize certificates into load balancing CAs.
* Certificates stored on the holder, multiple for CAs.

## Holder CA Status

A holder's device can also be an authority, the status should be attached to the end.

1) Not Authority (Not_Auth)
2) Intermediate Authority (Inter_Auth)
3) Root Authority (Root_Auth)

Short-hand example: Dell.Windows_10.Personal.Not_Auth

Long-hand example: Endpoint_Desktop_Dell.Microsoft_Windows_Windows_10.User_Personal.Not_Auth

## Holder Actions

A holder can perform the following actions-

* All holders
  * Create Key Pairs
  * Create CSRs and send them to registration authorities
  * Request Signing CA's public key and validate certificates
  * Communicate regularly with other entities
* Certificate Authorities Only
  * If Root CA
    * Self-sign own certificate
    * Auto-load own certificate onto all other hardware/software/accounts
  * Return certificates to lower hierarchical respondees
  * Host lower hierarchical certificates on device
  * Registration Duties
    * Accept CSRs
    * Analyze CSRs for basic validity
    * Forward Valid CSRs to corresponding CAs
  * Revocation Duties
    * Routinely check certificates for age

# Final Class Designs

\* = create a requirement to accommodate this

## Certificate Class

### Parameters

* cert_name (str) - Unique Identifier of the certificate

* subject_common_name (str) - Common Domain Name of Subject
* subject_country (str) - Country of Subject
* subject_state (str) - State/Region of Subject
* subject_local (str) - City/Town/Locality of Subject
* subject_org (str) - Organization of Subject
* subject_org_unit (str) - Organizational Unit of Subject
* subject_email (str) - Email of the Subject
* subject_url (str) - Internet Address of the Subject

* issuer_common_name (str) - Common Domain Name of Issuer
* issuer_country (str) - Country of Issuer
* issuer_state (str) - State/Region of Issuer
* issuer_local (str) - City/Town/Locality of Issuer
* issuer_org (str) - Organization of Issuer
* issuer_cert_url (str) - Internet Address of the Issuer

* cert_serial (str) - Unique Serial Number
* cert_x509_ver (int) * - X.509 Version Number
* cert_sig_hash_alg (str) * - Certificate Signature Hashing Algorithm
* cert_not_valid_before (datetime) * - Beginning of Valid Period (Exclusive)
* cert_not_valid_after (datatime) * - End of Valid Period (Exclusive)

* pubkey_encrypt_alg (str) * (Enum, Setup) - Asymmetric Encryption Algorithm
* pubkey_params (dict) * - Asymmetric Encryption Parameters
* pubkey_key (str) * - Asymmetric Encryption Public Key

* cert_signature (str or None) - Digital Signature
* cert_chain (list from top down) - Top Down Certificate Chain

### Methods

* init - creates a certificate
* create_signature - hashes content into a signature

## Holder Class

### Parameters

* holder_name (str) - Unique Identifier of the holder

* holder_env_info (dataclass) - Environment Information
  * holder_level (str) - Holder's Hierarchical Level
  * holder_uid_hash (str) - Holder's UID Hashing Algorithm
  * holder_sig_hash (str) - Holder's Signature Hashing Algorithm
  * holder_encrypt_alg (dict) - Holder's Encryption Algorithm & Params
    * algorithm (str) - Algorithm used
    * params (dict) - Parameters for algorithm
  * revoc_prob (float) - Holder's Revocation Probability
  * cert_valid_dur (datetime or int) - Holder's Certificate Validity Duration
  * cache_dur (datetime or int) - Holder's Regular Cache Duration
  * cooldown_time (datetime or int) - Holder's Cooldown Time
  * timeout_time (datetime or int) - Holder's Wait Time
  * holder_network (HolderNetwork) - Holder's Network

* holder_type_info (dataclass) - Holder's Type Information
  * hardware_type (str) - Holder's Hardware Type
  * hardware_subtype (str) - Holder's Hardware Subtype
  * hardware_brand (str) - Holder's Hardware Brand
  * os_category (str) - Holder's Operating System Category
  * os_subcategory (str) - Holder's Operating System Subcategory
  * os_dist (str) - Holder's Operating System Distribution
  * os_subdist (str) - Holder's Operating System Sub-distribution
  * account_type (str) - Holder's Account Type
  * account_subtype (str) - Holder's Account Subtype
  * ca_status (str) - Holder's Certificate Authority Status
* short_type_name (str) - Holder's Short Type Name
* long_type_name (str) - Holder's Long Type Name

* holder_info (dataclass) - Holder's Information
  * common_name (str) - Holder's Common Domain Name
  * country (str) - Holder's Country
  * state (str) - Holder's State/Region
  * local (str) - Holder's City/Town/Locality
  * org (str) - Holder's Organization
  * org_unit (str) - Holder's Organizational Unit
  * email (str) - Holder's Email
  * url (str) - Holder's Internet Address
* holder_hash (str) - Holder's Hash from Information

* privkey (str) - Holder's Private Key
* pubkey (str) - Holder's Public Key
* holder_certificate (Certificate or None) - Holder's Certificate
* root_certificates (immutable dictionary) - Holder's Root Certificate List
* cached_certificates (mutable dictionary) - Holder's Regular Certificate Cache

* csr_port (queue) - Queue for anything related to Certificate Signing Requests
* message_port (queue) - Queue for anything related to Messages
* oscp_port (queue) - Queue for anything related to OCSP Communications

* has_root_certs (bool) - Holder has root certificates
* has_cert (bool) - Holder has a certificate
* cache_empty (bool) - Holder's regular cache is empty
* waiting_for_csr_response (bool) - Holder is waiting for a CSR response
* waiting_to_send_csr (bool) - Holder's CSR has failed and now is waiting
* waiting_for_response (bool) - Holder is waiting for a response
* waiting_to_send_message (bool) - Holder's response has failed and now is waiting
* waiting_for_revoc_check (bool) - Holder is waiting for a revocation check
* need_new_certificate (bool) - Holder needs a new certificate

### Methods

* init - creates a holder
* hash_identity - hashes all information related to holder identity and returns a hex digest
* send_cert_request - sends a certificate signing request to assigned CA
* receive_csr_response_listener - {may not need this}
* send_data - sends a message to another non-CA holder
* receive_data_listener - {may not need this}
* cache_cert - save a validated cert to cache for a limited amount of time
* check_cache - check if a cert is in the regular cache
* check_root_cache - check if a cert is in the root cache
* check_cert_valid - contact CAs to check if a certificate is valid
* check_csr_port - check if a CSR message is in the queue
* check_message_port - check if a regular message is in the queue
* check_ocsp_port - check if an OCSP message is in the queue
* check_expiration - check if a certificate has expired
* send_self_revoc - send a self revocation message to assigned CA

## CertAuthority Class (Extends Holder)

Needs added functionality for returning certificates, returning certificate responses, checking certificate revocation
statuses, and checking certificate statuses for lower levels.

### Parameters

* valid_cert_list (dict) - Valid Certificate List
* cert_revok_list (dict) - Certificate Revocation List

### Methods

* check_revo_list - checks if a certificate sent is in revocation list
* validate_cert - check if a certificate sent is valid
* send_revoc - send a revocation message to lower level

## HolderNetwork Class

### Parameters

* network_name (str) - Network Name

* network_level_count (str) - Number of Levels in Network Hierarchy
* network_count_by_level (list) - Number of Holders at each level
* network_total_count (int) - Total Number of Holders

* uid_hash (str) - UID Hashing Algorithm
* sig_hash (str) - Signature Hashing Algorithm
* encrypt_alg (dict) - Encryption Algorithm & Params
  * algorithm (str) - Algorithm used
  * params (dict) - Parameters for algorithm
* revoc_probs (list) - Revocation Probabilities for each level
* cert_valid_durs (list) - Certificate Validity Durations for each level
* cache_durs (list) - Regular Cache Duration for each level
* cooldown_durs (list) - Cooldown Time for each level
* timeout_durs (list) - Wait Time for each level

* network (dict) - Network Hierarchy
* network_log (list) - Network Log

### Methods

* init - creates a network
* add_to_network - adds a holder to the network
* contact_holder - bridge between holder
* add_to_log - adds a message to the network log
* save_log - saves the network log to file

# File Design

## Auto

* Number of Root CAs: {enter number here}
* Number of Inter CA levels: {enter number here}
* Number of Inter CAs at each level: {enter list of numbers here}
* Number of Communicating Non-CA devices: {enter number here}

# Process

1) The file contents are read into memory.
   1) If auto, the hierarchical structure is read in first.
      1) The number of root CAs is first.
      2) The number of Inter CA levels is next.
      3) The array of number of Inter CAs at each level is next.
      4) The number of non-CAs is last.
   2) The hashing function used for creating holder hashes is read in.
   3) The hashing function used for creating digital signatures is read in.
   4) The asymmetrical encryption function used throughout the environment is read in.
      1) The parameters needed for the asymmetrical encryption.
   5) The random revocation probabilities for each layer are read in.
   6) The duration of root CA certificates, intermediate CA certificates, and end certificates are read in. 
      1) Formatted in hours, minutes, and seconds for each layer.
   7) The cache duration of intermediate CAs and non-CAs are read in.
      1) Formatted in minutes, and seconds, for each layer.
   8) The CSR cooldown time, or the time to wait if a CSR attempt as failed, is read in.
      1) Formatted in seconds.
   9) The CSR wait time, or the time to wait until a request times out, is read in.
      1) Formatted in seconds.
   10) If manual, the hierarchical structure is read in last.
       1) The number of layers is first.
       2) The list of CAs and non-CAs is next.
2) For each holder read or created-
   1) Phase one
      1) The name of the object is generated as random alphabet characters or loaded in.
      2) The parameters are read through the enums to load the hardware/software/account information.
      3) By default, the extension "Not_Auth" is added as the CA status of the holder
      4) The short and long type names are dynamically created from the information in the above step.
      5) The holder information used for certificates are then loaded in as well.
      6) Everything previously established is then hashed with a hashing function.
      7) The level stated in the file for the holder is read in.
      8) If not root CA-
         1) The holder's hash is then used to determine who they should communicate with on above row.
      9) The encryption key pairs are then generated.
      10) The holder is added to the global network depending on the holder's level.
   2) Phase two
      1) A message cache is created.
      2) If root CA-
         1) A self-signed certificate is created.
      3) If not root CA-
         1) All root certificates are saved to a root cache through the global network.
         2) An empty regular certificate cache is created.
      4) If CA-
         1) An empty certificate revocation list is created.
         2) An empty lower level certificate store is created.
      5) If intermediate CA-
         1) All root certificates are saved to a root cache.
         2) A CSR is submitted to the assigned above CA.
         3) The holder waits for a response and/or certificate from the above CA.
         4) The holder tries again if needed.
      6) If intermediate CA at level 3 or more (meaning they are not directly connected to root CA)-
         1) Add the certificates from the assigned above CA to the regular cache.
   3) Phase three
      1) Non-CA holders communicate random encrypted data with each other.
         1) If the holder does not have a valid certificate, they should first send a CSR to their assigned CA. The 
            holder should then wait for their response and send another if the response fails after a while.
         2) If the holder does have a valid certificate, they are allowed to send the data in a message containing the
            certificate to the recipient's message cache. They must wait for a response to know if the other side
            read the message or not.
         3) If the holder receives a message to their message cache, they shall use the certificate sent inside to
            validate that certificate, using public keys, chains, and other checks. They must send a confirmation or
            rejection message to whoever sent it.
         4) If a holder receives a message rejection response, they must double-check their certificate with their CA
            before trying again.
         5) If a holder receives a message confirmed response, then yippie!
      2) Owners of a certificate (excluding root) can randomly decide whether their certificate is no longer valid and
         request their CA to revoke the status.
         1) This process can be used for renewals with a new coat of paint.
      3) CAs can randomly go through their certificates and randomly decide whether a certificate is no longer valid and
         let their lower-level owner know to make a new one.
         1) This process can be used for renewals with a new coat of paint.
      4) This goes on forever and ever, with all details being logged to file.

# Requirements List

1) Project SHALL simulate an environment where general communication is supported a Public Key Infrastructure to
   provide non-repudiation of encrypted traffic.
2) Project SHALL take JSON or YAML files for designating a hierarchy of root layer CAs, intermediate layer(s) CAs, and
   regular endpoint devices.
   1) Project SHALL pass the desired filepath as a command line argument.
   2) File at filepath SHALL conform to one of two design standards that can be handled by the project.
      1) The first design standard is "auto" and SHALL list how many entities exist at each level of the PKI
         hierarchy.
         1) The auto standard's inputs SHALL be selected in a way that when the numbers of entities per layer are
            arranged from top to bottom in sequential order, all numbers before a given number x are less than x, and
            all numbers after a given number x are greater than x.
         2) The auto standard SHALL automatically generate entities using a predetermined list of values and random
            inputs when names and unique identifiers are needed.
            1) The auto standard SHALL recognize when specific hardware requires specific software and NOT choose
               unrealistic software.
            2) The auto standard SHALL recognize when specific software requires specific accounts and NOT choose
               unrealistic accounts.
            3) The auto standard SHALL recognize when an entity is NOT a non-CA and NOT choose unrealistic hardware,
               software, and accounts.
            4) The auto standard SHALL use enums to conduct this process.
         3) The auto standard SHALL return a timestamped JSON and YAML file of the created hierarchy during the 
            project's runtime.
      2) The second design standard is "manual" and SHALL list out manually created entities, where all relevant 
         fields are present for the entity in question and are either filled or contain an empty string.
      3) There SHALL be default files for both in both JSON and YAML for other users to test. 
      4) Both standards SHALL outline the encryption and hashing algorithms used by the environment.
         1) The chosen encryption algorithm SHALL be an asymmetric encryption algorithm.
         2) Both chosen algorithms SHALL be algorithms recognized as currently viable by NIST or some other valid 
            agency.
      5) Both standards SHALL outline the revocation probability, or the chance that a holder will suddenly decide
         a certificate is no longer valid or usable. This SHALL be used in place of simulating unusual events (i.e.
         compromise of holder in cyberattack).
      6) Both standards SHALL outline the cached time limit, or the amount of time a recently verified certificate
         can stay local to an entity before needing to be reevaluated again.
   3) Any errors that are caused by incorrect files or filepaths being passed into the project SHALL be handled
      gracefully by the project.
   4) In the case where no filepath is passed by the user, the project SHALL have a built-in auto standard setup that
      can run.
      1) The project SHALL inform the user that they must pass the file next time before starting the built-in auto
         standard setup.
   5) All strings used in the configuration file should be lowercase and treated as such explicity.
3) Project SHALL recognize all entities as "holders" that can hold or work with "certificates" to some degree.
   1) Project SHALL have a parsing mechanism to derive the hardware, the operating system (if needed), and the user (if 
      needed) of the holder. 
   2) Project SHALL have a parsing mechanism to assign a holder class or child class depending on the holder's 
      information.
   3) Project SHALL automatically create asymmetric key pairs when creating a holder object.
   4) Project SHALL deem the holder object's name using the syntax shown in the Holder Identifier section if the name
      is NOT already manually established or an empty string.
   5) Project SHALL make any values that are related to identity immutable.
   6) Project SHALL make any functions that do not need to be accessed outside the object private.
4) Project SHALL set up load balancing at all levels, where connections are determined at environment creation.
   1) The load balancing algorithm SHALL use a hash organization method that assigns each CA a hash range. The
      hashes of holder information in the lower level SHALL be used to determine where they will do their PKI 
      communications.
5) Project SHALL have some decorator function method to log the entire runtime, including every distinct action done by 
   the program or the holders.
6) Project SHALL have custom functionality created for the default class methods.
7) Project SHALL satisfy requirements 1-6 above at runtime before even starting the environment simulation.
8) Project SHALL have a test folder that can be used to conduct automatic testing.
9) Project SHALL utilize threading to run all holders at once.
   1) All holders SHALL have mechanisms, flags, and setter functions to facilitate communications.
      1) All holders SHALL be able to "cache" valid certificates and uncache revoked or old-ish certificates.
         1) The parameter to determine how long a certificate can stay cached SHALL be established in environment
            creation.
      2) All holders SHALL have a root cache of certificates from all root CAs.
         1) A holder's root cache SHALL be immutable and without time limit once set up.
      3) All holders SHALL use timestamps set in the future, instead of counters, to determine any sort of expirations.
      4) All holders SHALL check root, then normal caches before checking global index for holders.
   2) All holders that are not CAs SHALL engage in general communication sending random encrypted data from 
      "applications" and "services."
      1) All messages sent between non-CA holders SHALL be signed and endorsed using the PKI architecture.
         1) Non-CA holders SHALL create CSRs to submit before starting communication at all and SHALL have explicit
            measures to prevent such communication.
         2) Non-CA holders who send messages SHALL be responsible for sending a certificate along with it.
         3) Non-CA holders who receive messages SHALL drop any message without a certificate along with it.
      2) The message generation strategy used SHALL recognize when some holders realistically cannot send certain
         types of data and generate accordingly.
   3) All holders that have a certificate SHALL periodically check whether that certificate is valid.
      1) Revoke Decision by holder SHALL have a random chance to take place. This random chance SHALL be established in 
         environment creation.
      2) Holders SHALL communicate this decision with assigned CA and expect a response using a flag and/or other
         measures to help wait safely.
   4) Holders that are CAs SHALL have multiple threads to handle distinct functions.
      1) Holders that are CAs SHALL have a thread for analyzing and responding to CSR requests.
         1) CSR requests that are not being attended to SHALL sit in a dedicated queue for the CA.
         2) Respondees waiting on CA responses SHALL use flags and a dedicated space of their own to handle waiting.
         3) CSR requests SHALL have a small random chance of being rejected. This random chance SHALL be established
            in environment creation.
      2) Holders that are CAs SHALL have a thread for periodically analyzing if certificates need to be revoked.
         1) Certificate revocation analysis SHALL analyze if certificates a) fall outside the expiration date, b) has,
            for some reason, be decided by the CA or the lower-level holder that the certificate no longer works.
            1) Revoke Decision by CA or lower-level holder SHALL have a random chance to take place. This random
               chance SHALL be established in environment creation.
      3) Holders that are CAs SHALL have a thread for responding to certificate revocation checks.
      4) In all threads, Holders that are CAs SHALL always send some response back down to the lower level.
   5) Holders that are root CAs SHALL be excluded from having to communicate outside certain scenarios.
      1) Root CAs SHALL still send public keys when lower levels need to decrypt signatures.
      2) Root CAs SHALL explicitly be excluded from the random chance revoke decision through some measure.

## Depreciated Requirements

* (2.2.X) Both standards SHALL automatically create Registration Authorities for each layer, where RA's would be
   responsible for handling CSRs from lower hierarchical levels.
   1) The top-most root layer SHALL create a RA for each Root CA.
   2) All other layers SHALL have ceil(n / r) RAs, where n is the number of CAs in a given layer, r is the number
      of CAs that SHALL share an RA, and ceil is a function that takes the result and raises the result to the
      nearest whole number that is greater than the result.
   3) The RA ratio factor r SHALL be defined in both standards.

# Development of Interactions

Scenario: All root certificates have been generated and assigned to each device. All Intermediate CAs and regular
devices are going to want to create their own certificates so they can begin to verify communication.

In this interaction, Intermediate CAs should first focus on getting their own certificates before answering lower
devices.

This should include

1) A check to see if they have their own certificate
2) The realization they don't
3) Creation of a CSR
4) Sending the CSR to a higher certificate authority

######################

Holder sub-threads:

* Certificate thread - Handles manging self-certificate and certificate cache checks.
  * Sends to
    * CSR-Request Port
    * OCSP-Request Port
  * Receives from
    * CSR-Answer Port
    * OCSP-Answer Port
* Regular message thread - For just doing normal communications supported by PKI.
  * Sends to
    * Message Port
  * Receives from
    * Message Port
* CA Registry thread - Manages certificate registry and revocation registry.
  * Sends to
    * CSR-Answer Port
    * OCSP-Answer Port
* CA Response thread - Handles answering CSR requests and OCSP requests
  * Sends to
    * CSR-Answer Port
    * OCSP-Answer Port
  * Receives from
    * CSR-Request Port
    * OCSP-Request Port

# Web App API Design and Database Schema

Strategies:

1) Core Python program and frontend will use REST API to interact with SQLite database.
2) Core Python program will directly connect to SQLite database and frontend will use REST API to interact with 
   SQLite database.

Assuming everything will be happening in real time, asyncio would likely have to be used. In addition, option two
may be the better choice as everything will only have to work through the REST API. Having the Python program also
have access may create some sort of weird race condition where the Python program updates the database at the same time
the REST API is trying to access the database. 



* / -> Leads nowhere
  * /api -> Leads to backend API functionality
  * /web -> Leads to frontend web serving functionality

# Database Schema

Database "Metadata" - A database that will contain
