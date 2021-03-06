# Docker

Docker is an open source software platform to create, deploy and manage virtualized application containers on a common operating system (OS).
Docker is a tool that packages, provisions and runs containers independent of the OS.Docker was created to work on the Linux platform, but has extended to offer greater support for non-Linux operating systems, including Microsoft Windows and Apple OS X. Versions of Docker for Amazon Web Services (AWS) and Microsoft Azure are available.

## How to Install Docker for windows 10

Docker Desktop for Windows requires Microsoft Hyper-V to run. The Docker Desktop for Windows installer enables Hyper-V for you, if needed, and restarts your machine. After Hyper-V is enabled, VirtualBox no longer works, but any VirtualBox VM images remain. VirtualBox VMs created with docker-machine (including the default one typically created during Toolbox install) no longer start. These VMs cannot be used side-by-side with Docker Desktop for Windows. However, you can still use docker-machine to manage remote VMs.

### System Requirements:

- Windows 10 64bit.

- Virtualization is enabled in BIOS. Typically, virtualization is enabled by default. This is different from having Hyper-V enabled. 

- CPU SLAT-capable feature.

- At least 4GB of RAM.

### Install Docker Desktop for Windows desktop app

- Double-click Docker Desktop for Windows Installer.exe to run the installer.

- If you haven’t already downloaded the installer (Docker Desktop Installer.exe), you can get it from download.docker.com. It typically downloads to your Downloads folder, or you can run it from the recent downloads bar at the bottom of your web browser.

- Follow the install wizard to accept the license, authorize the installer, and proceed with the install.

- You are asked to authorize Docker.app with your system password during the install process. Privileged access is needed to install networking components, links to the Docker apps, and manage the Hyper-V VMs.

- Click Finish on the setup complete dialog to launch Docker.


### Docker Advantages 

- Docker has emerged as a de facto standard platform that allows users to quickly compose, create, deploy, scale and oversee containers across Docker hosts. 

- Docker allows a high degree of portability so that users can register and share containers over various hosts in private and public environments. 

- Docker benefits include efficient application development, lower resource use and faster deployment compared to VMs.

### Docker DisAdvantages

- There are also potential challenges with Docker. The sheer number of containers possible in an enterprise can be difficult to manage efficiently.

- Security can also pose a problem. Despite excellent logical isolation, containers share the host's operating system. 

- An attack or flaw in the underlying operating system can potentially compromise all of the containers running atop the OS. 
Some organizations run containers within a VM, although containers do not require virtual machines.
