# Gray Hat Hacking: The Ethical Hacker's Handbook (6th Edition) – Companion Repository

[![Book Cover](https://www.mheducation.com/cover-images/Webp_400-wide/1264268947.webp)](https://www.mheducation.com/highered/mhp/product/gray-hat-hacking-ethical-hacker-s-handbook-sixth-edition.html)

**Up-to-date offensive security and ethical hacking resources**  
Companion code, labs, scripts, and community materials for the industry-standard book:

**Gray Hat Hacking: The Ethical Hacker's Handbook, Sixth Edition**  
Authors: Allen Harper, Ryan Linn, Stephen Sims, Michael Baucom, Huascar Tejeda, Daniel Fernandez, Moses Frost  
Publisher: McGraw-Hill Education  
Publication: 2022  
ISBN: 9781264268948 (print), 9781264268955 (eBook)

This repository contains:

- Proof-of-concept (PoC) code referenced in the book
- Virtual lab build scripts and configurations
- Updated exploits / tools (where legal and safe to share)
- Community-submitted fixes, errata, and modern adaptations
- Additional learning resources and cheat sheets

> **Important Legal Notice**  
> All code and materials here are provided strictly for **educational purposes** in controlled lab environments.  
> Unauthorized use against systems you do **not** own or have explicit written permission to test is illegal.  
> Always follow ethical guidelines, laws (such as the CFAA in the US), and get proper authorization before any security testing.

## 📖 About the Book

The Sixth Edition delivers field-tested techniques to understand and defend against modern threats:

- Modern exploit development (including Ghidra, binary analysis)
- Web application, cloud, and IoT attacks
- Ransomware, living-off-the-land, and advanced persistence
- Reverse engineering, fuzzing, and vulnerability research
- 7 new chapters compared to previous editions covering the latest attacker tactics

Authors are active trainers at Black Hat, DEF CON, RSA Conference, and many BSides events.

## 📂 What's Inside

| Directory              | Description           |
| --------------------   | --------------------  |
| `/chapter-code/`       | PoC scripts & snippets organized by book chapter (Python, C, Bash, PowerShell) |
| `/labs/`               | Vagrant / Docker / VMware / VirtualBox lab build files (Kali, vulnerable VMs) |
| `/tools/`              | Helper scripts, custom tools, updated wrappers for book tools              |
| `/errata/`             | Community-reported errors, fixes, and platform updates                      |
| `/cheatsheets/`        | Quick reference cards (nmap, Metasploit, Ghidra, gdb, etc.)                |
| `/resources/`          | Recommended further reading, CTF write-ups, legal templates, updated links |
|        |          |

### 🚀 Quick Start – Building the Labs

Most chapters assume you have a safe testing environment. Recommended setup:

1. Install **VirtualBox** + **Vagrant** (or use Docker/Podman)
2. Clone this repo:

   ```bash
   git clone https://github.com/your-username/cybersecurity_labs/gray-hat-hacking.git
   cd gray-hat-hacking

    ```

### 🛠 Requirements

- Kali Linux / Parrot OS / other pentest distro (2024+ rolling release recommended)
- Python 3.9+, gcc, make, nasm, gdb, ghidra, radare2, cutter, etc.
- VirtualBox / VMware / Docker
- **(Optional)** Windows VMs for exploit development (Windows 10/11 debugging setup)

### ⚠️ Responsible Use

- **Only** run exploits against lab machines you control.
- Do **not** use this code in production environments without explicit written authorization.
- Report newly discovered 0-days responsibly (follow coordinated vulnerability disclosure policies — see resources like CERT/CC or the project's own VDP if applicable).

#### 🙌 Contributing

We welcome contributions in the following areas:

- Fixes to outdated code (tools, APIs, and exploits change quickly)
- Improved lab automation (Docker Compose, Ansible playbooks, etc.)
- Modernized exploits that still teach the original concepts from the book
- New write-ups, blog links, or references that align with chapter topics

**Please open an issue first** to discuss major changes or new additions before submitting a pull request.

#### 📜 License

- **Code**: MIT License (see [LICENSE](LICENSE) file)
- **Documentation & markdown files**: Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)
- **Book content**: Remains © McGraw Hill Education — this repository contains only companion materials, PoC code, labs, and community contributions.

##### 🔗 Official & Useful Links

- [Publisher page (McGraw Hill)](https://www.mheducation.com/highered/product/gray-hat-hacking-ethical-hacker-s-handbook-sixth-edition-harper/M9781264268948.html)
- [Amazon (Sixth Edition)](https://www.amazon.com/Gray-Hat-Hacking-Ethical-Handbook/dp/1264268947)
- [O'Reilly platform (eBook access)](https://www.oreilly.com/library/view/gray-hat-hacking/9781264268955/)

- **Passionately Written By: Ikwuka Okoye (ikwukao)**

- **Happy (and ethical) hacking! 🛡️**

- *Last updated: May 2026*

###### To Be Continued

---
