# GSCS Deployment-Katalog

61 eigene, auf GSCS abgestimmte Profile. 35 sind freigegeben; 26 benötigen zusätzliche Konfiguration und anschließende Administratorfreigabe. Enthalten sind unter anderem Minecraft, Hytale, Rust, Project Zomboid, Valheim, Satisfactory, 7 Days to Die, ARK, DayZ, Core Keeper, Palworld, V Rising sowie Source-/GoldSource-Spiele.

Die vollständige Liste steht in [SPIELE.md](SPIELE.md). Steam-Server-App-IDs und Startmetadaten wurden mit Valve SteamCMD abgeglichen. Spielgrafiken werden anhand der Client-App-ID bzw. der offiziellen Website ermittelt.

`catalog.json` enthält die SHA-256-Prüfsumme jeder Definition. Neue oder geänderte GitHub-Definitionen werden im Webinterface zur Prüfung vorgemerkt. Die Definitionen enthalten keine Spielserver-Binaries und keine Zugangsdaten. Eine Prüfung der Metadaten ist kein Nachweis eines erfolgreichen Starts auf allen Betriebssystemen. Space Engineers erfordert zunächst die manuelle Welt-/Serverkonfiguration. Containerimages und GSCS-Installpakete werden getrennt veröffentlicht.

- [Eigenes Repository erstellen](https://github.com/ZUMBYTE-AppSolution/gscs-deployment/wiki/Eigenes-Repository)
- [Profilformat und Beispiele](https://github.com/ZUMBYTE-AppSolution/gscs-deployment/wiki/Profilformat)
- [Prüfen und aktualisieren](https://github.com/ZUMBYTE-AppSolution/gscs-deployment/wiki/Pruefen-und-Aktualisieren)
- [Unabhängiges Beispiel](examples/mein-spiel.json)

Spielnamen und Logos gehören den jeweiligen Rechteinhabern. Die Spielbedingungen und gegebenenfalls erforderlichen Accounts/Token bleiben maßgeblich. GSCS ermittelt Spielgrafiken aus der Client-App-ID beziehungsweise der offiziellen Website.
