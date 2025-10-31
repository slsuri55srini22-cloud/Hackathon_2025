import csv

# Data
data = [
    {
        "Issue": "Driver Power State Failure",
        "Recommendation": """Root Cause:
This error usually occurs due to incompatible or outdated drivers (especially GPU, WiFi, or chipset), or power management settings that prevent hardware from entering/exiting sleep states properly.

Recommended Fix Steps:
1. Boot Windows into Safe Mode.
2. Open Device Manager (Win + X → Device Manager).
3. Expand 'Display adapters', 'Network adapters', and 'Universal Serial Bus controllers'.
4. Right-click each major device and select “Update driver”.
5. Disable any recently installed or faulty drivers.
6. Run `sfc /scannow` and `DISM /Online /Cleanup-Image /RestoreHealth` in Command Prompt (Admin).
7. Restart your PC.

System Recovery:
- After updating drivers, reboot normally.
- If the system still fails, use “System Restore” to roll back to a stable point.
- You can also uninstall problematic updates using Safe Mode.

Preventive Measures:
- Always install official drivers from your device manufacturer (e.g., HP Support Assistant).
- Avoid forcing sleep/hibernate frequently when heavy processes are running.
- Keep Windows, BIOS, and firmware up to date."""
    },
    {
        "Issue": "Blue Screen of Death (BSOD)",
        "Recommendation": """Root Cause:
Blue Screen of Death (BSOD) errors usually indicate critical hardware or driver failures, memory corruption, or system file damage.

Recommended Fix Steps:
1. Note down the stop code shown on the screen.
2. Run Memory Diagnostic Tool (mdsched.exe).
3. Check Event Viewer → Windows Logs → System for critical events.
4. Run `sfc /scannow` and `DISM /Online /Cleanup-Image /RestoreHealth`.
5. Uninstall any new hardware or drivers recently added.
6. Update BIOS if needed.

System Recovery:
- Boot into Safe Mode and restore previous drivers.
- Use “System Restore” to return to a stable configuration.

Preventive Measures:
- Regularly update all drivers and perform disk checks.
- Avoid overclocking and unsafe power cycles."""
    },
    {
        "Issue": "Network Adapter Missing",
        "Recommendation": """Root Cause:
This issue occurs when the network drivers are corrupted or Windows fails to detect the adapter after sleep or update.

Recommended Fix Steps:
1. Run `netsh winsock reset` and `netsh int ip reset` in CMD (Admin).
2. Restart your PC.
3. Open Device Manager → Network Adapters → Scan for hardware changes.
4. Reinstall the WiFi/Ethernet driver from manufacturer’s website.

System Recovery:
- If missing even in BIOS, enable LAN/WLAN from BIOS settings.
- Use USB Ethernet/WiFi dongle as temporary backup.

Preventive Measures:
- Avoid abrupt shutdowns during Windows Updates.
- Keep drivers and firmware up to date."""
    },
    {
        "Issue": "No Bootable Device Found",
        "Recommendation": """Root Cause:
The system cannot detect a bootable drive (e.g., missing OS, corrupted boot sector, or misconfigured BIOS).

Recommended Fix Steps:
1. Enter BIOS (F2 or Del) and ensure your SSD/HDD is detected.
2. Check boot order — your OS drive should be listed first.
3. If not detected, reseat SSD/HDD or check cables.
4. Run “Automatic Repair” from Windows Recovery (Win + Shift + F8).
5. Use Command Prompt → run `bootrec /fixmbr`, `bootrec /fixboot`, `bootrec /rebuildbcd`.

System Recovery:
- If drive fails hardware test, replace it and reinstall OS.
- Use bootable USB drive for recovery.

Preventive Measures:
- Avoid abrupt shutdowns and frequent forced restarts.
- Regularly back up important data."""
    },
    {
        "Issue": "Improper Storage Protocol in F2",
        "Recommendation": """Root Cause:
This message indicates incorrect storage configuration in BIOS or mismatched controller mode (AHCI vs RAID).

Recommended Fix Steps:
1. Enter BIOS (F2 key).
2. Under Storage → Controller, ensure correct mode (usually AHCI for single drives).
3. Save changes and restart.
4. If error persists, load BIOS defaults and save.

System Recovery:
- Reset BIOS to defaults.
- Update BIOS firmware if issue continues.

Preventive Measures:
- Avoid manual BIOS changes unless necessary.
- Keep BIOS updated."""
    },
    {
        "Issue": "Dust Filter Message",
        "Recommendation": """Root Cause:
This occurs when the system detects dust filter blockage affecting cooling.

Recommended Fix Steps:
1. Power off the system.
2. Open case and clean dust filter using compressed air.
3. Reattach filter and restart the system.

Preventive Measures:
- Clean filters regularly.
- Avoid placing system in dusty environments."""
    },
    {
        "Issue": "BitLocker Recovery",
        "Recommendation": """Root Cause:
Triggered when BitLocker detects hardware or firmware changes and needs the recovery key.

Recommended Fix Steps:
1. Enter recovery key when prompted.
2. Sign in with your Microsoft account to retrieve the key (https://account.microsoft.com/devices/recoverykey).
3. Disable and re-enable BitLocker if the issue repeats.

System Recovery:
- If key unavailable, data may be inaccessible without recovery key.

Preventive Measures:
- Always back up BitLocker key to Microsoft account or external drive."""
    }
]

# Write to CSV (keep real newlines inside quotes)
with open("issue_recommendations.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=["Issue", "Recommendation"], quoting=csv.QUOTE_ALL)
    writer.writeheader()
    writer.writerows(data)

print("✅ CSV file 'issue_recommendations.csv' created successfully!")
