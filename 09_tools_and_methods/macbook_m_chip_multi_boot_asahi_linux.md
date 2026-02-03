# 🖥️ Multi-Boot Setup: Macbook M Chip mit Asahi Linux

## 📋 Inhaltsverzeichnis

1. [Einleitung](#einleitung)
2. [Was ist Asahi Linux?](#was-ist-asahi-linux)
3. [Voraussetzungen](#voraussetzungen)
4. [Wichtige Hinweise & Warnungen](#wichtige-hinweise--warnungen)
5. [Dual-Boot: macOS + Asahi Linux](#dual-boot-macos--asahi-linux)
6. [Triple-Boot: macOS + Asahi Linux + weitere Distribution](#triple-boot-macos--asahi-linux--weitere-distribution)
7. [Partitionsverwaltung](#partitionsverwaltung)
8. [Bootloader-Konfiguration](#bootloader-konfiguration)
9. [Post-Installation](#post-installation)
10. [Troubleshooting](#troubleshooting)
11. [Nützliche Befehle](#nützliche-befehle)
12. [Ressourcen & Links](#ressourcen--links)

---

## Einleitung

Dieser Guide erklärt, wie man einen **Multi-Boot** bzw. **Triple-Boot** auf einem **MacBook mit Apple Silicon (M1/M2/M3/M4)** einrichtet, um neben **macOS** auch **Asahi Linux** und optional weitere Betriebssysteme zu nutzen.

### Zielgruppe

- Enterprise Architects und System Architects
- Entwickler, die native Linux-Performance auf Apple Silicon benötigen
- IT-Professionals, die Multi-OS-Umgebungen für Tests/Entwicklung nutzen

### Was du lernen wirst

- ✅ Asahi Linux neben macOS installieren (Dual-Boot)
- ✅ Mehrere Linux-Distributionen parallel betreiben (Triple-Boot)
- ✅ Sichere Partitionierung ohne macOS-Datenverlust
- ✅ Boot-Management zwischen Betriebssystemen
- ✅ Troubleshooting häufiger Probleme

---

## Was ist Asahi Linux?

**Asahi Linux** ist ein Community-Projekt, das Linux nativ auf Apple Silicon Macs (M1/M2/M3/M4) zum Laufen bringt.

### Besonderheiten

- **Native ARM64-Architektur** - Keine Emulation, volle Performance
- **Reverse-Engineering** - Apple stellt keine offiziellen Treiber bereit
- **Aktive Entwicklung** - Hardware-Support verbessert sich kontinuierlich
- **Basiert auf Arch Linux ARM** - Rolling-Release-Modell

### Hardware-Support (Stand: Februar 2026)

| Komponente | M1 | M2 | M3 | M4 | Status |
|------------|-----|-----|-----|-----|---------|
| CPU | ✅ | ✅ | ✅ | ⚠️ | Voll/Beta |
| GPU (OpenGL) | ✅ | ✅ | ⚠️ | ⚠️ | Experimentell |
| GPU (Vulkan) | 🔄 | 🔄 | ❌ | ❌ | In Arbeit |
| Wi-Fi | ✅ | ✅ | ✅ | ⚠️ | Voll/Beta |
| Bluetooth | ✅ | ✅ | ⚠️ | ⚠️ | Voll/Beta |
| USB-C | ✅ | ✅ | ✅ | ✅ | Voll |
| Thunderbolt | ⚠️ | ⚠️ | ❌ | ❌ | Teilweise |
| Touch ID | ❌ | ❌ | ❌ | ❌ | Nicht verfügbar |
| Webcam | ✅ | ✅ | ⚠️ | ⚠️ | Voll/Beta |
| Audio | ✅ | ✅ | ⚠️ | ⚠️ | Voll/Beta |
| HDMI | ✅ | ✅ | ✅ | ⚠️ | Voll/Beta |

**Legende:**
- ✅ Voll funktionsfähig
- 🔄 In aktiver Entwicklung
- ⚠️ Beta/Experimentell
- ❌ Nicht unterstützt

> **Tipp:** Prüfe den aktuellen Stand auf [asahilinux.org](https://asahilinux.org) vor der Installation!

---

## Voraussetzungen

### Hardware

- **MacBook, Mac Mini oder Mac Studio** mit Apple Silicon (M1/M2/M3/M4)
- **Mindestens 100 GB freier Speicherplatz** (empfohlen: 150-200 GB)
- **Empfohlen:** 16 GB RAM oder mehr für optimale Performance

### Software

- **macOS 12.3 (Monterey) oder neuer** - Aktuelle Updates installiert
- **Internetverbindung** - Für den Download der Asahi-Installer
- **Backup-Lösung** - Time Machine oder alternative Backup-Software

### Kenntnisse

- ✅ Grundlegende Terminal-Kenntnisse (macOS/Linux)
- ✅ Verständnis von Partitionierung und Bootloadern
- ✅ Bereitschaft, experimentelle Software zu nutzen
- ⚠️ **Nicht empfohlen für Produktivsysteme ohne Backup!**

---

## Wichtige Hinweise & Warnungen

### ⚠️ Vor der Installation

1. **Vollständiges Backup erstellen**
   ```bash
   # Time Machine Backup über GUI starten
   # Oder: Carbon Copy Cloner / SuperDuper verwenden
   ```

2. **System-Updates installieren**
   ```bash
   # macOS auf neueste Version aktualisieren
   # System Settings → Software Update
   ```

3. **FileVault temporär deaktivieren** (optional, aber empfohlen)
   ```bash
   # System Settings → Privacy & Security → FileVault
   # Nach Installation wieder aktivieren
   ```

4. **Sicherheitshinweise**
   - ❌ **Touch ID funktioniert in Asahi Linux NICHT**
   - ❌ **Secure Enclave ist unter Linux nicht zugänglich**
   - ⚠️ **GPU-Performance ist noch nicht auf macOS-Niveau**
   - ⚠️ **Akku-Laufzeit kann kürzer sein als unter macOS**

### 🔒 Rechtliche Hinweise

- ✅ Asahi Linux ist legal und verstößt nicht gegen Apples EULA
- ✅ Garantie bleibt erhalten (reine Software-Installation)
- ⚠️ Bei Problemen: macOS neu installieren entfernt Asahi Linux

---

## Dual-Boot: macOS + Asahi Linux

### Schritt 1: Speicherplatz freigeben

```bash
# Freien Speicherplatz prüfen
df -h /

# Empfehlung: Mindestens 100 GB frei
# Falls nötig: Daten aufräumen oder externe Festplatte verwenden
```

### Schritt 2: Asahi-Installer starten

```bash
# Terminal öffnen (⌘ + Space → "Terminal")

# Installer herunterladen und ausführen
curl https://alx.sh | sh
```

**Hinweis:** Der Installer ist ein offizieller Bash-Script von asahilinux.org

### Schritt 3: Installer-Optionen wählen

Der Installer fragt nach folgenden Optionen:

1. **Sprache auswählen**
   - `1` für Englisch
   - `2` für Deutsch (falls verfügbar)

2. **Speicherplatz zuweisen**
   ```
   Wie viel Speicherplatz für Asahi Linux?
   Empfehlung: 80-150 GB
   
   Beispiel: 120 GB eingeben
   ```

3. **Distribution wählen**
   ```
   Verfügbare Optionen:
   1) Asahi Linux Desktop (Fedora Remix) - EMPFOHLEN
   2) Asahi Linux Minimal (nur CLI)
   3) ALARM (Arch Linux ARM) - Für Fortgeschrittene
   
   Empfehlung für Einsteiger: Option 1
   ```

4. **Desktop Environment wählen** (bei Desktop-Installation)
   ```
   1) KDE Plasma - Ähnlich zu Windows
   2) GNOME - Ähnlich zu macOS
   
   Empfehlung: KDE Plasma (bessere Performance auf M-Chips)
   ```

### Schritt 4: Installation abschließen

```bash
# Der Installer erstellt automatisch:
# - Neue APFS-Container für Linux
# - Bootloader (m1n1 + U-Boot + GRUB)
# - Partitionen für /boot, /, /home

# Nach Abschluss:
# System herunterfahren und neu starten
```

### Schritt 5: Erster Boot in Asahi Linux

1. **Mac ausschalten** (nicht Neustart!)
2. **Power-Button gedrückt halten** (ca. 5-10 Sekunden)
3. **Boot-Optionen erscheinen**
   - `Macintosh HD` → macOS starten
   - `Asahi Linux` → Linux starten

4. **Asahi Linux auswählen**
   - GRUB-Bootloader erscheint
   - Standard-Kernel wird automatisch gestartet

### Schritt 6: Erste Anmeldung

```bash
# Standard-Credentials (je nach Distribution):
# Fedora Remix:
Username: alarm
Passwort: alarm

# Nach Login: Passwort ändern!
passwd

# System aktualisieren
sudo dnf update -y  # Fedora
sudo pacman -Syu    # Arch Linux ARM
```

---

## Triple-Boot: macOS + Asahi Linux + weitere Distribution

### Übersicht Triple-Boot-Szenarien

1. **macOS + Asahi Linux + Ubuntu ARM**
2. **macOS + Asahi Linux + Arch Linux ARM**
3. **macOS + Asahi Fedora + Asahi Arch** (beide Asahi-Varianten)

### Methode 1: Asahi-Installer für mehrere Instanzen nutzen

Der Asahi-Installer kann **mehrmals** ausgeführt werden, um zusätzliche Linux-Installationen zu erstellen.

#### Schritt-für-Schritt

```bash
# 1. Erste Installation (z.B. Asahi Fedora)
curl https://alx.sh | sh
# Speicherplatz zuweisen: z.B. 80 GB
# Fedora Remix wählen

# 2. Nach erfolgreichem Boot in macOS zurückkehren

# 3. Zweite Installation (z.B. Asahi Arch)
curl https://alx.sh | sh
# Speicherplatz zuweisen: z.B. 60 GB
# Arch Linux ARM wählen

# Resultat:
# - macOS (Original)
# - Asahi Linux 1 (Fedora)
# - Asahi Linux 2 (Arch)
```

### Methode 2: Manuelle Partitionierung (Fortgeschritten)

Für erfahrene Nutzer: Eigene Partitionen erstellen und andere ARM64-Distributionen installieren.

#### Voraussetzungen

- Verständnis von APFS, GPT-Partitionen
- Erfahrung mit `diskutil` (macOS) oder `parted` (Linux)
- Bereitschaft, bei Problemen macOS neu zu installieren

#### Warnung

> ⚠️ **Diese Methode ist experimentell!** Nur für fortgeschrittene Nutzer.  
> Falsches Partitionieren kann zu **Datenverlust** führen!

#### Schritte

```bash
# 1. In macOS: Zusätzlichen APFS-Container erstellen
diskutil apfs addVolume disk0 APFS "Linux2" -size 60g

# 2. In Asahi Linux booten

# 3. Neue Partition für zweite Distribution vorbereiten
sudo parted /dev/nvme0n1
(parted) print  # Partitionstabelle anzeigen
(parted) mkpart primary ext4 XGB YGB  # Neue Partition erstellen
(parted) quit

# 4. Dateisystem erstellen
sudo mkfs.ext4 /dev/nvme0n1pX

# 5. Distribution installieren (z.B. Ubuntu ARM)
# - Ubuntu ARM ISO herunterladen
# - Mit dd auf USB-Stick schreiben
# - Von USB booten und auf /dev/nvme0n1pX installieren
```

### Methode 3: GRUB für mehrere Distributionen konfigurieren

Nach Installation mehrerer Linux-Systeme: GRUB anpassen, um alle zu erkennen.

```bash
# In der primären Asahi-Installation:

# 1. GRUB-Konfiguration aktualisieren
sudo grub-mkconfig -o /boot/grub/grub.cfg

# 2. os-prober aktivieren (erkennt andere Betriebssysteme)
sudo nano /etc/default/grub
# Zeile hinzufügen:
GRUB_DISABLE_OS_PROBER=false

# 3. GRUB neu generieren
sudo grub-mkconfig -o /boot/grub/grub.cfg

# 4. System neu starten
sudo reboot
```

### Boot-Reihenfolge beim Triple-Boot

1. **Power-Button gedrückt halten** → Boot-Menü (macOS Recovery)
2. **Asahi Linux wählen** → GRUB-Bootloader startet
3. **Im GRUB:**
   - Asahi Linux 1 (Fedora)
   - Asahi Linux 2 (Arch/Ubuntu)
   - macOS (über GRUB's macOS-Chain-Loader)

---

## Partitionsverwaltung

### Partition-Layout nach Asahi-Installation

```
/dev/nvme0n1 (Interne NVMe SSD)
├── /dev/nvme0n1p1  - EFI System Partition (macOS)
├── /dev/nvme0n1p2  - macOS System (APFS)
├── /dev/nvme0n1p3  - macOS Data (APFS)
├── /dev/nvme0n1p4  - Asahi Linux /boot (FAT32)
├── /dev/nvme0n1p5  - Asahi Linux / (ext4)
└── /dev/nvme0n1p6  - Asahi Linux /home (ext4) [optional]
```

### Partitionen in macOS anzeigen

```bash
diskutil list

# Erwartete Ausgabe:
/dev/disk0 (internal, physical):
   #:                       TYPE NAME                    SIZE       IDENTIFIER
   0:      GUID_partition_scheme                        *500.3 GB   disk0
   1:                        EFI EFI                     524.3 MB   disk0s1
   2:                 Apple_APFS Container disk1         400.0 GB   disk0s2
   3:                 Apple_APFS Container disk2         100.0 GB   disk0s3
```

### Partitionen in Asahi Linux anzeigen

```bash
# Alle Partitionen anzeigen
lsblk

# Detaillierte Informationen
sudo fdisk -l /dev/nvme0n1

# Dateisystem-Informationen
df -h
```

### Partitionsgröße ändern

#### In macOS (vor Asahi-Installation)

```bash
# Verfügbaren Platz prüfen
diskutil apfs list

# Container-Größe ändern
diskutil apfs resizeContainer disk0s2 350g
# Gibt 150 GB für Linux frei
```

#### In Asahi Linux (nach Installation)

```bash
# ⚠️ Vorsicht: Kann zu Datenverlust führen!
# Nur wenn du weißt, was du tust!

# Mit GParted (GUI)
sudo pacman -S gparted
sudo gparted

# Oder mit parted (CLI)
sudo parted /dev/nvme0n1
(parted) resizepart 5 120GB
(parted) quit

# Dateisystem anpassen
sudo resize2fs /dev/nvme0n1p5
```

---

## Bootloader-Konfiguration

### Boot-Prozess auf Apple Silicon mit Asahi

```
Power-Button → iBoot (Apple) → m1n1 (Asahi) → U-Boot → GRUB → Linux Kernel
```

**Komponenten:**

1. **iBoot** - Apples Firmware (nicht modifizierbar)
2. **m1n1** - Asahi's Stage-1-Bootloader (lädt U-Boot)
3. **U-Boot** - Stage-2-Bootloader (ARM-Standard)
4. **GRUB** - Standard-Linux-Bootloader

### GRUB-Konfiguration anpassen

```bash
# Konfigurationsdatei bearbeiten
sudo nano /etc/default/grub

# Wichtige Optionen:
GRUB_DEFAULT=0                    # Standard-Boot-Eintrag (0 = erster)
GRUB_TIMEOUT=10                   # Wartezeit in Sekunden
GRUB_CMDLINE_LINUX_DEFAULT="quiet splash"  # Kernel-Parameter
GRUB_DISABLE_OS_PROBER=false      # Andere OS erkennen

# Änderungen speichern und GRUB neu generieren
sudo grub-mkconfig -o /boot/grub/grub.cfg
```

### Standard-Betriebssystem ändern

#### Methode 1: In macOS (Startup Disk)

```
System Settings → General → Startup Disk
→ macOS oder Asahi Linux wählen
→ Restart
```

#### Methode 2: In GRUB (Linux)

```bash
# Standard-Eintrag ändern
sudo nano /etc/default/grub
GRUB_DEFAULT=0  # Ändern zu gewünschtem Index

# Liste der Einträge anzeigen:
awk -F\' '/menuentry / {print $2}' /boot/grub/grub.cfg

# GRUB aktualisieren
sudo grub-mkconfig -o /boot/grub/grub.cfg
```

### Boot-Optionen temporär ändern

```bash
# Beim GRUB-Bootmenü:
# 1. Gewünschten Eintrag mit Pfeiltasten wählen
# 2. "e" drücken zum Editieren
# 3. Kernel-Parameter anpassen (z.B. "nomodeset" hinzufügen)
# 4. Strg+X oder F10 drücken zum Booten
```

---

## Post-Installation

### Erste Schritte nach der Installation

```bash
# 1. System aktualisieren
# Fedora:
sudo dnf update -y && sudo dnf upgrade -y

# Arch Linux:
sudo pacman -Syu

# 2. Wichtige Tools installieren
sudo dnf install -y git vim curl wget htop  # Fedora
sudo pacman -S git vim curl wget htop       # Arch

# 3. Firmware-Updates prüfen
sudo asahi-fwupdate
# Oder manuell:
curl -sL https://alx.sh/fw | sudo sh

# 4. GPU-Treiber installieren (experimentell)
# Für M1/M2:
sudo pacman -S mesa-asahi-edge
```

### Desktop-Optimierungen

```bash
# 1. HiDPI-Skalierung aktivieren (für Retina-Displays)
# KDE Plasma:
System Settings → Display → Scale: 200%

# GNOME:
gsettings set org.gnome.desktop.interface scaling-factor 2

# 2. Touchpad-Gestures aktivieren
sudo dnf install libinput-gestures  # Fedora
sudo pacman -S libinput-gestures    # Arch

libinput-gestures-setup autostart
libinput-gestures-setup start

# 3. Batterie-Optimierung
sudo pacman -S tlp
sudo systemctl enable tlp.service
sudo systemctl start tlp.service
```

### macOS-Integration

```bash
# 1. Gemeinsamen Ordner zwischen macOS und Linux erstellen
# In macOS: ExFAT-Partition erstellen (beide OS können lesen/schreiben)
diskutil eraseDisk ExFAT SHARED disk0s7

# In Linux: Mounten
sudo mkdir /mnt/shared
sudo mount -t exfat /dev/nvme0n1p7 /mnt/shared

# Automatisches Mounten bei Boot:
sudo nano /etc/fstab
# Zeile hinzufügen:
/dev/nvme0n1p7  /mnt/shared  exfat  defaults  0  0

# 2. macOS-Partition lesen (read-only)
sudo pacman -S apfsprogs
sudo mkdir /mnt/macos
sudo mount -t apfs -o ro /dev/nvme0n1p2 /mnt/macos
```

### Performance-Tuning

```bash
# 1. CPU-Governor auf Performance setzen
echo performance | sudo tee /sys/devices/system/cpu/cpu*/cpufreq/scaling_governor

# Permanent:
sudo nano /etc/default/cpupower
# GOVERNOR="performance"
sudo systemctl enable cpupower.service

# 2. GPU-Performance (M1/M2)
# DRM-Debugging deaktivieren:
sudo nano /etc/modprobe.d/asahi.conf
# Zeile hinzufügen:
options asahi drm.debug=0

# 3. Swap-Nutzung optimieren
sudo sysctl vm.swappiness=10
# Permanent:
echo "vm.swappiness=10" | sudo tee -a /etc/sysctl.conf
```

---

## Troubleshooting

### Problem: Boot-Menü erscheint nicht

**Symptom:** Nach Installation bootet Mac direkt in macOS, kein Asahi-Option sichtbar.

**Lösung:**

```bash
# 1. In macOS: Startup Security Utility öffnen
# Neustart mit ⌘+R gedrückt halten
# → Startup Security Utility → Security Policy
# → "Reduced Security" wählen
# → "Allow booting from external media" aktivieren

# 2. NVRAM zurücksetzen
# Mac ausschalten, dann einschalten mit:
# ⌘+Option+P+R gedrückt halten (ca. 20 Sekunden)

# 3. Asahi neu installieren (worst case)
curl https://alx.sh | sh
```

### Problem: Wi-Fi funktioniert nicht

**Symptom:** Keine Wi-Fi-Netzwerke sichtbar in Asahi Linux.

**Lösung:**

```bash
# 1. Firmware-Status prüfen
dmesg | grep -i firmware

# 2. Wi-Fi-Firmware neu installieren
sudo asahi-fwupdate
# Oder:
curl -sL https://alx.sh/fw | sudo sh

# 3. NetworkManager neu starten
sudo systemctl restart NetworkManager

# 4. Falls Problem weiterhin besteht:
# Modul neu laden
sudo modprobe -r brcmfmac
sudo modprobe brcmfmac
```

### Problem: Schwarzer Bildschirm nach GRUB

**Symptom:** GRUB erscheint, aber nach Kernel-Auswahl: schwarzer Bildschirm.

**Lösung:**

```bash
# Im GRUB-Menü:
# 1. Eintrag wählen
# 2. "e" drücken
# 3. Zeile mit "linux" suchen
# 4. Am Ende hinzufügen: nomodeset
# Beispiel:
linux /vmlinuz-6.x.x root=/dev/nvme0n1p5 ro quiet splash nomodeset

# 5. Strg+X drücken zum Booten

# Nach erfolgreichem Boot:
# Permanent machen:
sudo nano /etc/default/grub
# Zeile ändern:
GRUB_CMDLINE_LINUX_DEFAULT="quiet splash nomodeset"

sudo grub-mkconfig -o /boot/grub/grub.cfg
```

### Problem: Audio funktioniert nicht

**Symptom:** Kein Sound über Speaker oder Kopfhörer.

**Lösung:**

```bash
# 1. ALSA prüfen
aplay -l

# 2. PulseAudio neu starten
pulseaudio -k
pulseaudio --start

# 3. Lautstärke prüfen (manchmal auf 0%)
alsamixer
# Mit Pfeiltasten Lautstärke erhöhen, "M" zum Unmuten

# 4. Firmware-Update
sudo asahi-fwupdate

# 5. Experimentelle Audio-Treiber installieren (M1/M2)
# (Prüfe asahilinux.org für aktuelle Anleitung)
```

### Problem: Bluetooth funktioniert nicht

**Symptom:** Keine Bluetooth-Geräte erkennbar.

**Lösung:**

```bash
# 1. Bluetooth-Service prüfen
sudo systemctl status bluetooth

# 2. Falls nicht aktiv: Starten
sudo systemctl enable bluetooth
sudo systemctl start bluetooth

# 3. Firmware neu laden
sudo asahi-fwupdate

# 4. Bluetooth-Modul neu laden
sudo modprobe -r hci_bcm4377
sudo modprobe hci_bcm4377

# 5. Bluetooth-Geräte scannen
bluetoothctl
[bluetooth]# power on
[bluetooth]# agent on
[bluetooth]# default-agent
[bluetooth]# scan on
```

### Problem: Suspend/Resume funktioniert nicht

**Symptom:** Nach Suspend (Schlafmodus) wacht Mac nicht auf oder friert ein.

**Lösung:**

```bash
# 1. Suspend temporär deaktivieren
sudo systemctl mask sleep.target suspend.target hibernate.target

# 2. Oder: Kernel-Parameter anpassen
sudo nano /etc/default/grub
# Hinzufügen:
GRUB_CMDLINE_LINUX_DEFAULT="quiet splash mem_sleep_default=s2idle"

sudo grub-mkconfig -o /boot/grub/grub.cfg

# Hinweis: Suspend-Support ist noch experimentell auf Apple Silicon
```

### Problem: Kann nicht mehr in macOS booten

**Symptom:** Boot-Menü zeigt nur Asahi, macOS-Option fehlt.

**Lösung:**

```bash
# Methode 1: NVRAM-Reset
# Mac ausschalten, dann einschalten mit:
# ⌘+Option+P+R gedrückt halten (20 Sekunden)

# Methode 2: macOS Recovery
# Mac ausschalten, Power-Button gedrückt halten
# → Optionen → Disk Utility → First Aid auf macOS-Partition

# Methode 3: Boot-Option erzwingen
# Power-Button gedrückt halten → "Macintosh HD" wählen

# Methode 4: In Asahi Linux GRUB anpassen
sudo grub-mkconfig -o /boot/grub/grub.cfg
# Sollte macOS automatisch erkennen
```

### Problem: GRUB zeigt nur schwarzen Bildschirm

**Symptom:** Kein GRUB-Menü, nur schwarzer Bildschirm nach Asahi-Auswahl.

**Lösung:**

```bash
# In macOS Terminal:

# 1. Asahi neu installieren (behält Daten)
curl https://alx.sh | sh
# Option wählen: "Repair/Reinstall"

# 2. Falls nicht verfügbar: Bootloader manuell reparieren
# Von Asahi USB-Stick booten, dann:
sudo mount /dev/nvme0n1p5 /mnt
sudo mount /dev/nvme0n1p4 /mnt/boot
sudo arch-chroot /mnt
grub-install --target=arm64-efi --efi-directory=/boot
grub-mkconfig -o /boot/grub/grub.cfg
exit
sudo reboot
```

### Problem: Externe Monitore werden nicht erkannt

**Symptom:** HDMI/USB-C Monitor funktioniert nicht.

**Lösung:**

```bash
# 1. Kernel-Log prüfen
dmesg | grep -i hdmi
dmesg | grep -i display

# 2. Xrandr prüfen (unter X11)
xrandr --query

# 3. DRM-Treiber prüfen
ls /sys/class/drm/

# 4. Firmware-Update
sudo asahi-fwupdate

# 5. Falls weiterhin Probleme:
# Experimentelle DRM-Optionen aktivieren
sudo nano /etc/modprobe.d/asahi.conf
options asahi drm_kms_helper.edid_firmware=edid/1920x1080.bin

# Hinweis: Multi-Monitor-Support ist noch in Entwicklung
```

---

## Nützliche Befehle

### System-Information

```bash
# Hardware-Info
neofetch                    # Übersicht
lscpu                       # CPU-Details
lspci                       # PCI-Geräte
lsusb                       # USB-Geräte
free -h                     # RAM-Auslastung

# Asahi-spezifisch
cat /proc/device-tree/model # Mac-Modell anzeigen
uname -r                    # Kernel-Version
asahi-version               # Asahi-Version (falls installiert)
```

### Disk & Partition

```bash
# Disk-Nutzung
df -h                       # Partitions-Nutzung
du -sh /home/*              # Ordner-Größen
lsblk                       # Block-Devices

# Partitions-Details
sudo fdisk -l /dev/nvme0n1
sudo parted /dev/nvme0n1 print
```

### Performance-Monitoring

```bash
# Echtzeit-Monitoring
htop                        # Prozess-Monitor
iotop                       # I/O-Monitor (sudo)
nethogs                     # Netzwerk-Monitor (sudo)

# CPU-Frequenz
watch -n 1 cat /sys/devices/system/cpu/cpu0/cpufreq/scaling_cur_freq

# GPU-Status (wenn verfügbar)
cat /sys/class/drm/card0/device/gpu_busy_percent
```

### Netzwerk

```bash
# Verbindung prüfen
ip addr                     # IP-Adressen
ip route                    # Routing-Tabelle
ping -c 4 8.8.8.8          # Internet-Test

# Wi-Fi
nmcli device wifi list      # SSID scannen
nmcli device wifi connect "SSID" password "PASSWORD"

# Firewall
sudo firewall-cmd --state   # Fedora
sudo ufw status             # Arch (falls installiert)
```

### Logs & Debugging

```bash
# System-Logs
journalctl -xe              # Systemd-Logs (letzte Fehler)
dmesg | tail -50            # Kernel-Logs
journalctl -b               # Logs seit Boot

# Boot-Probleme
journalctl -p err           # Nur Fehler
systemctl --failed          # Fehlgeschlagene Services
```

---

## Ressourcen & Links

### Offizielle Asahi Linux Ressourcen

- **Hauptseite:** https://asahilinux.org
- **Installation Guide:** https://asahilinux.org/install/
- **Hardware Support:** https://github.com/AsahiLinux/docs/wiki/Feature-Support
- **Blog & Updates:** https://asahilinux.org/blog/

### Community & Support

- **Discord:** https://discord.gg/asahi-linux
- **Reddit:** https://reddit.com/r/AsahiLinux
- **GitHub:** https://github.com/AsahiLinux
- **Forum:** https://discussion.fedoraproject.org/tag/asahi

### Dokumentation

- **Arch Wiki:** https://wiki.archlinux.org/title/Apple_Silicon
- **Asahi Wiki:** https://github.com/AsahiLinux/docs/wiki
- **GPU-Treiber:** https://asahilinux.org/2022/12/gpu-drivers-now-in-asahi-linux/

### Tools & Software

- **Asahi Installer:** https://github.com/AsahiLinux/asahi-installer
- **m1n1 (Bootloader):** https://github.com/AsahiLinux/m1n1
- **U-Boot:** https://github.com/AsahiLinux/u-boot
- **Linux Kernel:** https://github.com/AsahiLinux/linux

### Alternativen zu Asahi

- **UTM (Virtualisierung):** https://mac.getutm.app/ - Linux in VM statt Native Boot
- **Parallels Desktop:** https://www.parallels.com/ - Kommerzielle VM-Lösung
- **VMware Fusion:** https://www.vmware.com/products/fusion.html - VM für macOS

---

## Hinweise für Enterprise Architects

### Relevanz für EA-Arbeit

Als **Enterprise Architect** ist Multi-Boot mit Asahi Linux relevant für:

1. **Native Performance-Tests** - Vergleich ARM64 vs. x86_64 Architekturen
2. **Cloud-Entwicklung** - AWS Graviton, Azure ARM-VMs lokal testen
3. **Container-Workloads** - Docker/Kubernetes auf ARM64 entwickeln
4. **Security-Testing** - Unterschiedliche OS-Umgebungen für Pentesting
5. **Architektur-Dokumentation** - Multi-Plattform-Szenarien verstehen

### Best Practices

- ✅ **Immer Backup** vor Experimenten
- ✅ **Dokumentiere** deine Partition-Layouts und Boot-Konfigurationen
- ✅ **Verwende VMs** für kritische Produktionsumgebungen
- ✅ **Native Boot** nur für Entwicklung/Testing
- ⚠️ **Nicht für Unternehmens-Laptops** ohne IT-Freigabe

### Integration in Enterprise-Umgebungen

```bash
# Beispiel: CI/CD-Pipeline für ARM64 testen

# 1. Docker-Container auf ARM64 bauen
docker buildx build --platform linux/arm64 -t myapp:arm64 .

# 2. Kubernetes-Manifeste für ARM-Nodes testen
kubectl apply -f deployment-arm64.yaml
kubectl get pods -o wide  # Node-Architektur prüfen

# 3. Performance-Metriken sammeln
kubectl top nodes
kubectl top pods
```

---

## Zusammenfassung

### Was du gelernt hast

- ✅ Asahi Linux neben macOS installieren (Dual-Boot)
- ✅ Triple-Boot mit mehreren Linux-Distributionen
- ✅ Partitionsverwaltung auf Apple Silicon
- ✅ Bootloader-Konfiguration (GRUB, m1n1, U-Boot)
- ✅ Troubleshooting häufiger Probleme
- ✅ Performance-Optimierung und Post-Installation

### Nächste Schritte

1. **Ausprobieren:** Backup erstellen und Asahi installieren
2. **Optimieren:** Desktop-Umgebung und Performance-Tuning
3. **Dokumentieren:** Eigene Erfahrungen als ADR festhalten
4. **Teilen:** Feedback im Asahi-Forum oder Community

### Empfohlene Hardware

- **Ideal:** MacBook Pro 14"/16" M1/M2 mit 16+ GB RAM
- **Akzeptabel:** MacBook Air M1/M2 mit 8+ GB RAM
- **Experimentell:** Mac Studio M1/M2 (bester Hardware-Support)
- **Nicht empfohlen:** M3/M4 (Support noch Beta, Stand Feb 2026)

---

## Changelog

| Datum | Version | Änderung |
|-------|---------|----------|
| 2026-02-03 | 1.0 | Initiale Version erstellt |

---

**Autor:** Enterprise Architect Roadmap Community  
**Lizenz:** MIT License  
**Repository:** [github.com/Artifex-Vision-ICT-R-D/enterprise_architect](https://github.com/Artifex-Vision-ICT-R-D/enterprise_architect)

---

*Dieser Guide ist Teil der Enterprise Architect Roadmap. Für weitere Tools und Methoden siehe: [09_tools_and_methods/](../09_tools_and_methods/)*
