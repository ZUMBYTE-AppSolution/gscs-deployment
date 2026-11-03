# GSCS Deployment-Katalog

230 GSCS-Profile mit 9.626 Konfigurationsfeldern. Installation, Startparameter, TCP-/UDP-Ports und Zugangsdaten sind je Spiel hinterlegt. Die Konfiguration erscheint in passenden Bereichen im GSCS-Webinterface. Native Ausführung, Docker und die benötigten Kompatibilitätslaufzeiten richten sich nach dem gewählten Profil und Node.

Die vollständige Liste steht in [SPIELE.md](SPIELE.md). Die Profile enthalten keine Spielserver-Binaries oder Zugangsdaten. Spielabhängige Konten, Tokens und Originaldateien müssen bereitgestellt werden. Die enthaltenen Profile sind strukturell geprüft; nicht alle Spiele wurden installiert und im Spielbetrieb getestet.

`catalog.json` enthält die SHA-256-Prüfsummen. Neue oder geänderte Profile werden bei der Übernahme im Webinterface angezeigt. Eigene Startskripte und Konfigurationswerte bleiben bei Updates erhalten. Im Deployment-Editor kannst du zwischen Assistent und freiem JSON-Editor wählen.

- [Eigenes Repository erstellen](https://github.com/ZUMBYTE-AppSolution/gscs-deployment/wiki/Eigenes-Repository)
- [Profilformat mit Konfigurationsfeldern](PROFILFORMAT.md)
- [Profil-Wiki](https://github.com/ZUMBYTE-AppSolution/gscs-deployment/wiki)
- [GSCS Alpha herunterladen](https://github.com/ZUMBYTE-AppSolution/gscs-release/releases/tag/v0.1.0-alpha.3)

Hytale besitzt getrennte geführte Anmeldungen für den Downloader und den Serveranbieter. GSCS erneuert laufende Serversitzungen über die hinterlegte Kontoverbindung. Für einen eigenen Anbieterzugang die [Anleitung](https://github.com/ZUMBYTE-AppSolution/gscs-deployment/wiki/Hytale-Anmeldung) beachten.

Spielnamen, Logos und Spielserver gehören ihren jeweiligen Rechteinhabern. Für übernommene Vorlagendefinitionen gilt zusätzlich [LICENSE.third-party.txt](LICENSE.third-party.txt).
