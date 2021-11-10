from api_doc_common import *

misc = Module("misc", "Sonstiges", "", Version.ANY, [
    Func("version", FuncType.STATE, Elem.OBJECT("Version der Wallbox-Firmware.", members={
            "firmware": Elem.STRING("Die Firmware-Version, die aktuell ausgeführt wird."),
            "spiffs": Elem.STRING("Die Version der Konfiguration, die aktuell verwendet wird."),
        })
    ),

    Func("modules", FuncType.STATE, Elem.OPAQUE("Initialisierungszustand der Firmware-Module.")),
    Func("reboot", FuncType.COMMAND, Elem.NULL("Startet den ESP neu, um beispielsweise Konfigurationsänderungen anzuwenden."), command_is_action=True),

    Func("uptime", FuncType.HTTP_ONLY, Elem.OPAQUE("Die Laufzeit des ESPs seit dem letzten Neustart in Millisekunden.<br/><br/>Achtung: Diese Zeit wird direkt über den Takt des Prozessors gemessen. Die Genauigkeit ist damit nur ausreichend für Zeitmessungen im Bereich Minuten bis wenige Stunden. Die Zeitmessung läuft nach ungefähr 50 Tagen über und beginnt wieder bei 0.")),

    Func("debug_report", FuncType.HTTP_ONLY, Elem.OPAQUE("Generiert einen Debug-Report. Dieser besteht aus allen Zuständen und Konfigurationen, sowie den letzten empfangenen Kommandos und Konfigurationsupdates. Passwörter werden, genau wie bei Konfigurationsabfragen, zensiert.")),

    Func("force_reboot", FuncType.HTTP_ONLY, Elem.OPAQUE("Erzwingt einen sofortigen Neustart des ESPs. Nützlich, falls {{{ref:reboot}}} aus irgendwelchen Gründen hängt.")),

    Func("update", FuncType.HTTP_ONLY, Elem.OPAQUE("Notfall-Update-Seite mit der eine Firmware-Aktualisierung eingespielt werden kann, auch wenn das normale Webinterface nicht funktioniert.")),
    Func("flash_firmware", FuncType.HTTP_ONLY, Elem.OPAQUE("Nimmt ein Firmware-Update als POST entgegen, dass dann geflasht wird.")),
    Func("flash_spiffs", FuncType.HTTP_ONLY, Elem.OPAQUE("Nimmt ein Update der Konfigurationspartition als POST entgegen, dass dann geflasht wird.")),
], hide_prefix=True)
