Information Security
===

## [Information Security: Context and Introduction (Coursera)](https://www.coursera.org/learn/information-security-data)

### 1 - Introduction to Information Security 

Information Security: the preservation of the confidentiality, availability and integrity of information.

* Confidentiality - unauthorized people don't have access to information
* Availability - authorized people have access to information in a timely manner
* Integrity - the information accessed is complete and accurate, void of unauthorized modification

aka the "[CIA triad](https://upload.wikimedia.org/wikipedia/commons/9/9a/CIAJMK1209.png)"

Integrity mechanisms include logging of access and authentication, change tracking, authorization checks on view, modify, delete operations, possibility to share authentication, authorisation and audit across components of a system.

Availability is concerned to build reliable systems that remain accessible even if under attack (Denial of Service - DoS) or when heavily used. A compromised system might be at risk of providing incorrect information or access to information for unautorized users - failures of integrity and confidentiality.

[RMIAS Model](https://upload.wikimedia.org/wikipedia/commons/d/da/A_Reference_Model_of_Information_Assurance_and_Security_%28RMIAS%29.png) - we consider
* Information Taxonomy: describes the information being protected - form of information (paper, electronic, verbal), state (creation, storage, transmission, ..., destruction), sensitivity (normal, confidential), location.
* Security Goals: set of goals and concepts to strive for, prioritized by risk analysis, IAS octet - CIA (confidentiality, integrity, availability), accountability (can hold users responsible for their actions), auditability (can monitor actions by machines and humans), nonrepudation (con proove occurence / non-occurence of an event), authenticity & trustworthiness (can verify identity and establish trust in 3rd party), privacy (allow users to control their personal information).
* Security Countermeasures: techniques or processes to achieve security goals, takes cost effectiveness into account - Technical (Authentication, Authorisation, Cryptograpy, Firewalls, intrusion detection devices), Legal (Law, Contracts, Agreements, compliance to regulations), Human-Oriented (Training, Ethics, Awareness, Security Culture), Organisation (procedural, policies, determine complience through audits)
* Security Development Life Cycle: application and temporal process of development from Requirements -> Design -> Security Countermeasures Implementation -> Management and Monitoring (-> Retirement), often iterativ)    

Key knowledge areas (as drafted by ACM JTF)
* Cyper Defence - how can we protect a system (Cryptography, Data Security, Computer Security, Network Security, Information Assurance)
* Cyper Operations - what can be done to a system (Cyber Attack, Penetration Testing, Reverse Engineering of malware, Cryptanalysis)
* Digital Forensics - identify intrusions into our systems, gather and investigate data from systems (hardware and software foreniscs, incident response, cypbercrime, cyber law enforcement)
* Cyber physical systems - what's the influence from the factory, in embedded systems (supervisory control and data acquisition, Internet of Things, Industrial Control Systems) 
* Secure Software Development - building secure and usable systems (Secure Sytems Design, Secure Coding, Secure Deployment, Maintainablity, Usability of Secure Systems)
* Cyber Ethics - how do we use information systems ethically (Privacy, Anonymity, Intellectual Property Rights)
* Cyber Policy, Governance and Law - what do we need to conform to (Laws, Regulations, Act, Government and Institutional Policies and Practices)
* Cyber Risk Management - how can we stay online when we are attacked (Disaster Recovery, Business Continuity, Security Evaluation, Cyber Economics)
* Human Behaviour - what do people do that make them/us vulnerable (Social Engineering, Social Networks, User Experience, Organizational Behaviour)

### Glossary

* ACM - Association of Computer Machinery (has a joint task force to define cyper security key areas et al)
* Authenticated - a mechanism by which a user is identified and uses some token to prove who they are.
* Authorized - a user who has ben authenicated, and has some level of authorisation identified and checked by the system.
* [CIA triad](https://upload.wikimedia.org/wikipedia/commons/9/9a/CIAJMK1209.png) - Confidentiality, Integrity, Availability
* data at rest vs. data in motion - data stored in a computer or on disk vs. data being transmitted.
* IFIP - International Federation for Information Processing (has a working group on information security education)
* ISMI - Information Security Management System
* Nonrepudiation - the assurance that someone cannot deny something, like a signature on a contract.
* [RMIAS](https://upload.wikimedia.org/wikipedia/commons/d/da/A_Reference_Model_of_Information_Assurance_and_Security_%28RMIAS%29.png) - Reference Model of Information Assurance and Security


### Further Reading


