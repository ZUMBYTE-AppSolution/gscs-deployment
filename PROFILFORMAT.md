# Deployment-Profile

Eine Vorlage enthält Installation, Start, Ports und die im Webinterface angezeigten Konfigurationsfelder. Im Bereich **Bereitstellung** lassen sich Vorlagen als JSON importieren, mit dem Assistenten bearbeiten oder im freien Editor erstellen. Für eigene Repositories siehe auch das [Deployment-Wiki](https://github.com/ZUMBYTE-AppSolution/gscs-deployment/wiki).

## Eigenes Repository

1. Einen Ordner `templates` anlegen und je Profil eine JSON-Datei speichern. Dateiname und `id` müssen übereinstimmen.
2. `scripts/build-catalog.py` übernehmen und im Repository mit Python ausführen. Die erzeugte `catalog.json` enthält die Prüfsummen der Vorlagen.
3. Repository und Branch oder Tag unter **Bereitstellung → Katalog aktualisieren** eintragen. Ein automatischer Abruf ist optional.
4. Neue Vorlagen freigeben. Geänderte Vorlagen lassen sich vor der Übernahme neben der bisherigen Version ansehen. Eigene Server-Startskripte bleiben bestehen.

Der Abruf unterstützt öffentliche GitHub-Repositories. Für private Quellen die JSON-Datei manuell importieren; Zugangstokens gehören nicht in Katalog-URLs.

## Beispiel

```json
{
  "id": "rust-community",
  "name": "Rust Community",
  "version": "1.0.0",
  "approved": false,
  "steamAppId": 258550,
  "steamGameAppId": 252490,
  "image": "ghcr.io/zumbyte-appsolution/gscs:0.1.0-alpha.3",
  "operatingSystems": ["windows", "linux"],
  "executables": {"windows": "RustDedicated.exe", "linux": "RustDedicated"},
  "arguments": ["-batchmode", "+server.port", "{GAME_PORT}", "+server.hostname", "{SERVER_NAME}", "+server.maxplayers", "{SLOTS}", "+server.seed", "{WORLD_SEED}", "+server.worldsize", "{WORLD_SIZE}"],
  "ports": [{"role": "game", "protocol": "udp", "default": 28015}],
  "configurationTabs": [{"id": "world", "label": "Welt", "icon": "settings", "order": 0}],
  "configurationFields": [
    {"id": "WORLD_SEED", "label": "Welt-Seed", "tab": "world", "type": "integer", "default": "12345", "min": 0},
    {"id": "WORLD_SIZE", "label": "Weltgröße", "tab": "world", "type": "integer", "default": "3500", "min": 1000, "max": 6000}
  ],
  "query": "source",
  "stopCommand": "quit"
}
```

SteamCMD wird durch `steamAppId` automatisch verwendet. Das Spiel-Icon wird über `steamGameAppId` ermittelt. Ohne Steam ist eine offizielle `website` als Quelle für das Spielelogo möglich.

## Felder und Dateien

Unterstützt werden `text`, `textarea`, `integer`, `number`, `checkbox`, `enum`, `password` und `url`. `tab` und `section` gliedern die Einstellungen. `secret` speichert Werte verschlüsselt; `startupPermission` verlangt das Recht zum Bearbeiten des Startskripts. `platform` kann `all`, `windows` oder `linux` sein.

Dateien werden mit `configurationFiles` gebunden:

```json
{
  "configurationFiles": [{
    "path": "settings.ini",
    "format": "ini",
    "bindings": [{"key": "WorldSize", "variable": "{WORLD_SIZE}", "section": "World", "type": "integer"}]
  }]
}
```

Dateiformate sind `ini`, `space`, `json`, `xml` und `template`. JSON-Schlüssel können verschachtelte Pfade wie `world.seed` enthalten. Bei XML sind Property-Namen oder XPath möglich. Unbekannte Einträge bleiben bei gebundenen INI-/JSON-/XML-Dateien erhalten; `template` erzeugt den gesamten Inhalt. Vor Änderungen bleibt eine `.gscs-previous`-Datei bestehen.

`{SERVER_NAME}`, `{SLOTS}`, `{MEMORY}`, `{SERVER_DIR}` und die Portrollen wie `{GAME_PORT}` stehen automatisch bereit. In Textvorlagen sorgen `{JSON_SERVER_NAME}` und `{XML_SERVER_NAME}` für passend maskierte Werte. `{RANDOM_SECRET}`, `{RANDOM_UUID}` und `{RANDOM_DIGITS_8}` erzeugen bei der Serveranlage beständige eigene Werte.

## Installation und Start

`deploymentSteps` unterstützt SteamCMD, Downloads über HTTPS, Archive, GitHub-Releases, JSON-Downloadquellen, Verzeichnisse, Dateien, Kopien, Ausführungsrechte und Befehle. `phase` ist `install` oder `start`. Mit `conditionVariable` und `conditionValue` lassen sich beispielsweise optionale Modloader steuern. Konfigurationsdateien werden standardmäßig erhalten.

Eigene Skripte können unter `installScripts` und `updateScripts` getrennt für `windows` und `linux` hinterlegt werden. Windows verwendet PowerShell, Linux Bash. Für Kundeninstanzen werden Befehle innerhalb des isolierten Spielcontainers ausgeführt. Spielzugangsdaten gehören in als geheim markierte Felder.

Unterschiedliche Startparameter und Arbeitsverzeichnisse werden mit `platformArguments` und `platformWorkingDirectories` beschrieben. Startskripte werden daraus erzeugt. Manuelle Anpassungen erfolgen am eigenen Startskript im Serverdialog und werden bei Updates nicht überschrieben.

## Authentifizierung

`authenticationRequirements` beschreibt benötigte Spielkonten, Tokens und Ersteinrichtung. Steam-Konten verwenden die Felder `STEAM_USER`, `STEAM_PASSWORD` und gegebenenfalls `STEAM_GUARD_CODE`. Hytale verwendet die integrierten geführten Anmeldedialoge; OAuth-Tokens werden nicht in Profile geschrieben.
