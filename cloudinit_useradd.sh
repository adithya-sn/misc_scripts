#!/bin/bash

useradd myuser -m -s /bin/bash
usermod -aG sudo myuser
/bin/bash -c 'echo myuser:"mypasswd" | chpasswd'
